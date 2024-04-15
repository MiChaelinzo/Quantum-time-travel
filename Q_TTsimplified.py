import qiskit
import math
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer

def time_travel_circuit(target_time, num_qubits=6):
    """
    Creates a quantum circuit simulating time travel (fictional).

    This circuit applies Hadamard gates to create a superposition, encodes 
    the target time using phase gates, and entangles qubits in a linear chain.

    Args:
        target_time (int): The target time to encode as a binary string.
        num_qubits (int, optional): The number of qubits in the circuit. Defaults to 6.

    Returns:
        QuantumCircuit: The constructed quantum circuit.
    """

    qc = QuantumCircuit(num_qubits, num_qubits)

    # Apply Hadamard gates to create superposition
    for qubit in range(num_qubits):
        qc.h(qubit)

    # Encode target time using phase gates
    time_binary = bin(target_time)[2:].zfill(num_qubits)
    for qubit, time_bit in enumerate(time_binary):
        if time_bit == '1':
            qc.p(math.pi, qubit)  # Apply phase if the time bit is 1

    # Entangle qubits in a linear chain
    for qubit in range(num_qubits - 1):
        qc.cx(qubit, qubit + 1)

    # Measure all qubits
    qc.measure(range(num_qubits), range(num_qubits))

    return qc

# Example usage:
target_time = 25  # Example target time
num_qubits = 6   # Number of qubits

# Create and run the circuit
ttc = time_travel_circuit(target_time, num_qubits)
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(ttc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
results = job.result()
counts = results.get_counts(ttc)


# Visualize the results
print(plot_histogram(counts))

# Visualize the results
plot_histogram (counts)

