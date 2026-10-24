"""Bounded audit of the finite-pulse, one-jump-correcting workspace gadget.

The time-dependent jump conjugation lies in a three-operator trigonometric
span. Testing its coefficient operators checks the whole continuous interval,
not a grid of jump times. Only 16-dimensional unitaries are exponentiated.
"""

from __future__ import annotations

from itertools import product

import numpy as np
from scipy.linalg import expm

from quantum_channels import Pulse, halfwidth, sequence_unitary


PAULIS = [
    np.eye(2, dtype=complex),
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
]


def on_qubit(operator: np.ndarray, qubit: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for position in range(4):
        result = np.kron(result, operator if position == qubit else PAULIS[0])
    return result


def data_kraus_blocks(corrected_isometry: np.ndarray) -> list[np.ndarray]:
    blocks = corrected_isometry.reshape(4, 4, 4)  # output data, work, input data
    return [blocks[:, work, :] for work in range(4)]


def off_diagonal_data_norm(corrected_isometry: np.ndarray) -> float:
    return float(np.sqrt(sum(
        np.linalg.norm(block - np.diag(np.diag(block))) ** 2
        for block in data_kraus_blocks(corrected_isometry)
    )))


def non_z_pauli_weight(corrected_isometry: np.ndarray) -> float:
    blocks = data_kraus_blocks(corrected_isometry)
    weight = 0.0
    for first, second in product(range(4), repeat=2):
        if first in (0, 3) and second in (0, 3):
            continue
        pauli = np.kron(PAULIS[first], PAULIS[second])
        weight += sum(abs(np.trace(pauli.conj().T @ block) / 4) ** 2 for block in blocks)
    return float(weight)


def average_truth_error(corrected_isometry: np.ndarray) -> float:
    success = sum(np.sum(np.abs(np.diag(block)) ** 2) for block in data_kraus_blocks(corrected_isometry)) / 4
    return float(1 - success)


def coherent_workspace() -> dict:
    # Qubit order is C, T, a, b. The data index is the two leading bits.
    control, target, work_a, work_b = 0, 1, 2, 3
    full = np.pi / 2
    half = np.pi / 4
    specifications = [
        (target, work_a, full), (target, work_b, full),
        (control, target, full), (control, work_a, full), (control, work_b, full),
        (target, work_a, full), (target, work_b, full),
        (work_b, target, half), (work_a, work_b, full),
        (work_b, target, -half), (work_a, work_b, full), (work_a, target, half),
    ]
    identity = np.eye(16, dtype=complex)
    x = [on_qubit(PAULIS[1], qubit) for qubit in range(4)]
    y = [on_qubit(PAULIS[2], qubit) for qubit in range(4)]
    z = [on_qubit(PAULIS[3], qubit) for qubit in range(4)]
    one = [(identity - operator) / 2 for operator in z]
    generators = [one[c] @ (identity - x[t]) for c, t, _ in specifications]
    pulses = [
        Pulse(np.sign(angle) * generator, abs(angle))
        for generator, (_, _, angle) in zip(generators, specifications)
    ]
    unitaries = [expm(-1j * pulse.duration * pulse.hamiltonian) for pulse in pulses]
    prefix = [identity]
    for unitary in unitaries:
        prefix.append(unitary @ prefix[-1])
    suffix = [identity for _ in range(len(pulses) + 1)]
    for index in range(len(pulses) - 1, -1, -1):
        suffix[index] = suffix[index + 1] @ unitaries[index]

    cnot = np.eye(4, dtype=complex)
    cnot[2, 2] = cnot[3, 3] = 0
    cnot[2, 3] = cnot[3, 2] = 1
    correct_data = np.kron(cnot.conj().T, np.eye(4))
    input_isometry = np.eye(16, dtype=complex)[:, [0, 4, 8, 12]]
    ideal_error = np.linalg.norm(prefix[-1] @ input_isometry - input_isometry @ cnot)

    toffoli_reference = np.zeros((16, 16), dtype=complex)
    for basis in range(16):
        output = basis ^ 4 if (basis & 2) and (basis & 1) else basis
        toffoli_reference[output, basis] = 1
    toffoli_error = np.linalg.norm(sequence_unitary(pulses[7:]) - toffoli_reference)

    maximum_wrong = 0.0
    maximum_non_z = 0.0
    maximum_rotation_identity_error = 0.0
    coefficient_count = 0
    for index, ((c, t, angle), generator) in enumerate(zip(specifications, generators)):
        # Independently check the signed-angle Pauli conjugation, including CV^-1.
        remainder = angle * (np.sqrt(2) - 1)
        remaining_unitary = expm(-1j * remainder * generator)
        coefficients = [
            (identity - one[c]) @ z[t],
            one[c] @ z[t],
            one[c] @ y[t],
        ]
        conjugated = coefficients[0] + np.cos(2 * remainder) * coefficients[1] + np.sin(2 * remainder) * coefficients[2]
        maximum_rotation_identity_error = max(
            maximum_rotation_identity_error,
            float(np.linalg.norm(remaining_unitary @ z[t] @ remaining_unitary.conj().T - conjugated)),
        )
        # A target jump spans the three operators above. All other Z jumps commute.
        for jump_qubit in range(4):
            error_basis = coefficients if jump_qubit == t else [z[jump_qubit]]
            for error in error_basis:
                coefficient_count += 1
                corrected = correct_data @ suffix[index + 1] @ error @ prefix[index + 1] @ input_isometry
                maximum_wrong = max(maximum_wrong, off_diagonal_data_norm(corrected))
                maximum_non_z = max(maximum_non_z, non_z_pauli_weight(corrected))

    def trajectory_with_midpulse_jumps(locations: dict[int, int]) -> np.ndarray:
        trajectory = identity
        for index, pulse in enumerate(pulses):
            if index in locations:
                half_unitary = expm(-0.5j * pulse.duration * pulse.hamiltonian)
                step = half_unitary @ z[locations[index]] @ half_unitary
            else:
                step = unitaries[index]
            trajectory = step @ trajectory
        return correct_data @ trajectory @ input_isometry

    # A single target jump during the transversal CNOT stores syndrome 11.
    single = trajectory_with_midpulse_jumps({2: target})
    column = single[:, 2].reshape(4, 4)  # input data C=1,T=0, after ideal correction
    single_data_error = 1 - np.sum(np.abs(column[2, :]) ** 2)
    single_work_error = 1 - np.sum(np.abs(column[:, 0]) ** 2)

    # Two encoding jumps supply a nonzero, trace-preserving Pauli-weight witness.
    double = trajectory_with_midpulse_jumps({0: work_a, 1: work_b})
    double_truth = average_truth_error(double)
    double_non_z = non_z_pauli_weight(double)
    target_zero, target_one = (identity + z[target]) / 2, one[target]
    return {
        "dimension": 16,
        "pulse_count": len(pulses),
        "cnot_pulse_count": sum(abs(angle) == full for _, _, angle in specifications),
        "controlled_half_pulse_count": sum(abs(angle) == half for _, _, angle in specifications),
        "duration": float(sum(pulse.duration for pulse in pulses)),
        "maximum_halfwidth": max(halfwidth(pulse.hamiltonian) for pulse in pulses),
        "maximum_target_mixing_block": max(float(np.linalg.norm(target_zero @ pulse.hamiltonian @ target_one, 2)) for pulse in pulses),
        "ideal_data_and_work_error": float(ideal_error),
        "compiled_toffoli_error": float(toffoli_error),
        "one_jump_coefficient_count": coefficient_count,
        "signed_rotation_identity_error": maximum_rotation_identity_error,
        "continuous_one_jump_wrong_amplitude": maximum_wrong,
        "continuous_one_jump_non_z_weight": maximum_non_z,
        "single_jump_witness_data_error": float(single_data_error),
        "single_jump_witness_work_return_error": float(single_work_error),
        "two_jump_witness_truth_error": double_truth,
        "two_jump_witness_non_z_weight": double_non_z,
        "two_jump_pauli_identity_error": abs(double_truth - double_non_z),
    }
