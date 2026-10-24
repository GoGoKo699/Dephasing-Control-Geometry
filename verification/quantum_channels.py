"""Small dense channel calculations used by the scientific verification suite.

Column-major vectorization is used for density matrices. Choi matrices are
ordered as output tensor input and use a normalized maximally entangled input.
Rates are incorporated into the supplied jump matrices as square roots.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.linalg import expm, expm_frechet

ComplexMatrix = NDArray[np.complex128]


@dataclass(frozen=True)
class Pulse:
    hamiltonian: ComplexMatrix
    duration: float


def pair_pulse(
    dimension: int,
    source: int,
    target: int,
    omega: float = 1.0,
    *,
    phase_free: bool = True,
) -> Pulse:
    """A selective pair pulse; phase_free also applies the common pair shift."""
    if source == target or omega <= 0:
        raise ValueError("The endpoints must differ and omega must be positive.")
    hamiltonian = np.zeros((dimension, dimension), dtype=complex)
    hamiltonian[source, target] = hamiltonian[target, source] = omega
    if phase_free:
        hamiltonian[source, source] = hamiltonian[target, target] = -omega
    return Pulse(hamiltonian, np.pi / (2 * omega))


def path_pulses(
    dimension: int,
    path: list[int],
    omega: float = 1.0,
    *,
    endpoint_swap: bool = False,
    phase_free: bool = True,
) -> list[Pulse]:
    edges = list(zip(path[:-1], path[1:]))
    if endpoint_swap:
        edges += list(reversed(edges[:-1]))
    return [pair_pulse(dimension, i, j, omega, phase_free=phase_free) for i, j in edges]


def conditioned_pulses(pulses: list[Pulse]) -> list[Pulse]:
    control_one = np.diag([0.0, 1.0])
    return [Pulse(np.kron(control_one, pulse.hamiltonian), pulse.duration) for pulse in pulses]


def halfwidth(hamiltonian: ComplexMatrix) -> float:
    spectrum = np.linalg.eigvalsh(hamiltonian)
    return float((spectrum[-1] - spectrum[0]) / 2)


def dephasing_costs(values: NDArray, rates: NDArray) -> NDArray:
    """values[a, i] is the eigenvalue of Hermitian jump a on level i."""
    differences = values[:, :, None] - values[:, None, :]
    return np.einsum("a,aij->ij", rates, differences**2)


def shortest_distances(costs: NDArray) -> NDArray:
    distances = np.array(costs, dtype=float, copy=True)
    for vertex in range(len(distances)):
        distances = np.minimum(
            distances,
            distances[:, vertex, None] + distances[None, vertex, :],
        )
    return distances


def dissipator(jumps: list[ComplexMatrix]) -> ComplexMatrix:
    dimension = jumps[0].shape[0]
    identity = np.eye(dimension)
    result = np.zeros((dimension**2, dimension**2), dtype=complex)
    for jump in jumps:
        square = jump.conj().T @ jump
        result += (
            np.kron(jump.conj(), jump)
            - np.kron(identity, square) / 2
            - np.kron(square.T, identity) / 2
        )
    return result


def coherent_generator(hamiltonian: ComplexMatrix) -> ComplexMatrix:
    identity = np.eye(len(hamiltonian))
    return -1j * (
        np.kron(identity, hamiltonian) - np.kron(hamiltonian.T, identity)
    )


def sequence_channel(
    pulses: list[Pulse], jumps: list[ComplexMatrix], epsilon: float
) -> ComplexMatrix:
    noise = dissipator(jumps)
    channel = np.eye(len(noise), dtype=complex)
    for pulse in pulses:
        generator = coherent_generator(pulse.hamiltonian) + epsilon * noise
        channel = expm(pulse.duration * generator) @ channel
    return channel


def channel_and_noise_derivative(
    pulses: list[Pulse], jumps: list[ComplexMatrix]
) -> tuple[ComplexMatrix, ComplexMatrix]:
    """Compute E(0) and dE/d epsilon at zero, without finite differences."""
    noise = dissipator(jumps)
    channel = np.eye(len(noise), dtype=complex)
    derivative = np.zeros_like(channel)
    for pulse in pulses:
        ideal, change = expm_frechet(
            pulse.duration * coherent_generator(pulse.hamiltonian),
            pulse.duration * noise,
        )
        derivative = change @ channel + ideal @ derivative
        channel = ideal @ channel
    return channel, derivative


def sequence_unitary(pulses: list[Pulse]) -> ComplexMatrix:
    unitary = np.eye(len(pulses[0].hamiltonian), dtype=complex)
    for pulse in pulses:
        unitary = expm(-1j * pulse.duration * pulse.hamiltonian) @ unitary
    return unitary


def apply_channel(channel: ComplexMatrix, matrix: ComplexMatrix) -> ComplexMatrix:
    return (channel @ matrix.reshape(-1, order="F")).reshape(matrix.shape, order="F")


def basis_probability(
    channel: ComplexMatrix, source: int, target: int, dimension: int
) -> float:
    initial = np.zeros((dimension, dimension), dtype=complex)
    initial[source, source] = 1
    return float(apply_channel(channel, initial)[target, target].real)


def projected_choi(
    channel: ComplexMatrix, dimension: int, code: list[int], ideal_gate: ComplexMatrix
) -> ComplexMatrix:
    """Project, remove the ideal code gate, and form the normalized-input Choi."""
    code_dimension = len(code)
    choi = np.zeros((code_dimension**2, code_dimension**2), dtype=complex)
    for i in range(code_dimension):
        for j in range(code_dimension):
            matrix = np.zeros((dimension, dimension), dtype=complex)
            matrix[code[i], code[j]] = 1
            output = apply_channel(channel, matrix)[np.ix_(code, code)]
            corrected = ideal_gate.conj().T @ output @ ideal_gate
            elementary = np.zeros((code_dimension, code_dimension), dtype=complex)
            elementary[i, j] = 1
            choi += np.kron(corrected, elementary) / code_dimension
    return choi


def pauli_process_matrix(choi: ComplexMatrix) -> ComplexMatrix:
    paulis = [
        np.eye(2),
        np.array([[0, 1], [1, 0]]),
        np.array([[0, -1j], [1j, 0]]),
        np.diag([1, -1]),
    ]
    bell_basis = np.column_stack([p.reshape(-1) / np.sqrt(2) for p in paulis])
    return bell_basis.conj().T @ choi @ bell_basis
