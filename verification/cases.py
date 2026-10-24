"""Focused, deterministic checks of the constructions and conventions."""

from __future__ import annotations

import numpy as np

from quantum_channels import (
    basis_probability,
    channel_and_noise_derivative,
    conditioned_pulses,
    dephasing_costs,
    halfwidth,
    pauli_process_matrix,
    path_pulses,
    projected_choi,
    sequence_channel,
    sequence_unitary,
    shortest_distances,
)
from workspace_case import coherent_workspace


def two_jump_graph() -> dict:
    # Columns are a, b, the useful bridge, and an unhelpful extra level.
    values = np.array([[-1.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.5, 2.0]])
    costs = dephasing_costs(values, np.ones(2))
    distance = float(shortest_distances(costs)[0, 1])
    jumps = [np.diag(row).astype(complex) for row in values]
    sequences = {
        "direct": path_pulses(4, [0, 1]),
        "transfer": path_pulses(4, [0, 2, 1]),
        "swap": path_pulses(4, [0, 2, 1], endpoint_swap=True),
    }
    slopes = {}
    for name, pulses in sequences.items():
        _, derivative = channel_and_noise_derivative(pulses, jumps)
        slopes[name] = -basis_probability(derivative, 0, 1, 4)
        if name == "swap":
            slopes["swap_reverse"] = -basis_probability(derivative, 1, 0, 4)
    finite = []
    for epsilon in [1e-3, 1e-4]:
        channels = {
            name: sequence_channel(pulses, jumps, epsilon)
            for name, pulses in sequences.items()
        }
        row = {"epsilon": epsilon}
        for name, channel in channels.items():
            row[name] = 1 - basis_probability(channel, 0, 1, 4)
        row["swap_reverse"] = 1 - basis_probability(channels["swap"], 1, 0, 4)
        lower = np.pi * epsilon * distance / (16 + 8 * np.pi * epsilon * distance)
        if min(row["transfer"], row["swap"], row["swap_reverse"]) < lower - 1e-12:
            raise AssertionError("The explicit path falls below the finite-noise lower bound.")
        row["finite_lower_bound"] = float(lower)
        finite.append(row)
    return {
        "cost_matrix": costs.tolist(),
        "shortest_distance": distance,
        "first_derivatives": slopes,
        "finite_noise": finite,
    }


def uniform_ladder() -> list[dict]:
    results = []
    logical_x = np.array([[0, 1], [1, 0]], dtype=complex)
    for gaps in [1, 2, 4]:
        dimension = gaps + 1
        values = np.linspace(0.0, 1.0, dimension)
        jumps = [np.diag(values).astype(complex)]
        pulses = path_pulses(dimension, list(range(dimension)), endpoint_swap=True)
        ideal = sequence_unitary(pulses)
        expected_ideal = np.eye(dimension, dtype=complex)
        expected_ideal[0, 0] = expected_ideal[-1, -1] = 0
        expected_ideal[0, -1] = expected_ideal[-1, 0] = 1
        _, derivative = channel_and_noise_derivative(pulses, jumps)
        choi_derivative = projected_choi(derivative, dimension, [0, gaps], logical_x)
        process_derivative = pauli_process_matrix(choi_derivative)
        weights = np.diag(process_derivative).real
        off_diagonal = process_derivative - np.diag(np.diag(process_derivative))
        truth_derivative = -(
            basis_probability(derivative, 0, gaps, dimension)
            + basis_probability(derivative, gaps, 0, dimension)
        ) / 2
        results.append({
            "gaps": gaps,
            "pulse_count": len(pulses),
            "duration": float(sum(pulse.duration for pulse in pulses)),
            "maximum_halfwidth": max(halfwidth(pulse.hamiltonian) for pulse in pulses),
            "ideal_full_gate_error": float(np.linalg.norm(ideal - expected_ideal)),
            "x_derivative": float(weights[1]),
            "y_derivative": float(weights[2]),
            "z_derivative": float(weights[3]),
            "leakage_derivative": float(-np.trace(choi_derivative).real),
            "truth_derivative": float(truth_derivative),
            "off_diagonal_process_derivative": float(np.linalg.norm(off_diagonal)),
        })
    return results


def controlled_gate() -> dict:
    gaps = 3
    target_dimension = gaps + 1
    dimension = 2 * target_dimension
    target_pulses = path_pulses(
        target_dimension, list(range(target_dimension)), endpoint_swap=True
    )
    pulses = conditioned_pulses(target_pulses)
    code = [0, gaps, target_dimension, target_dimension + gaps]
    cnot = np.eye(4, dtype=complex)
    cnot[2, 2] = cnot[3, 3] = 0
    cnot[2, 3] = cnot[3, 2] = 1
    ideal = sequence_unitary(pulses)
    isometry = np.eye(dimension, dtype=complex)[:, code]
    target_noise = np.diag(np.linspace(0.0, 1.0, target_dimension))
    # The extra control-Z channel must not change any truth-table population.
    jumps = [
        np.kron(np.eye(2), target_noise),
        np.sqrt(0.2) * np.kron(np.diag([1.0, -1.0]), np.eye(target_dimension)),
    ]
    epsilon = 0.02
    channel = sequence_channel(pulses, jumps, epsilon)
    _, derivative = channel_and_noise_derivative(pulses, jumps)
    destinations = [code[0], code[1], code[3], code[2]]
    errors = [
        1 - basis_probability(channel, source, target, dimension)
        for source, target in zip(code, destinations)
    ]
    slopes = [
        -basis_probability(derivative, source, target, dimension)
        for source, target in zip(code, destinations)
    ]
    return {
        "gaps": gaps,
        "epsilon": epsilon,
        "control_z_reference_rate": 0.2,
        "pulse_count": len(pulses),
        "maximum_halfwidth": max(halfwidth(pulse.hamiltonian) for pulse in pulses),
        "maximum_operator_norm": max(
            float(np.linalg.norm(pulse.hamiltonian, 2)) for pulse in pulses
        ),
        "ideal_code_gate_error": float(np.linalg.norm(isometry.conj().T @ ideal @ isometry - cnot)),
        "ideal_code_leakage_norm": float(np.linalg.norm(ideal @ isometry - isometry @ cnot)),
        "truth_errors": errors,
        "average_truth_error": float(np.mean(errors)),
        "truth_derivatives": slopes,
        "average_truth_derivative": float(np.mean(slopes)),
    }


def evaluate_all() -> dict:
    return {
        "two_jump_graph": two_jump_graph(),
        "uniform_ladder": uniform_ladder(),
        "controlled_gate": controlled_gate(),
        "coherent_workspace": coherent_workspace(),
    }
