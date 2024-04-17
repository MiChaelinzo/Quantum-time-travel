from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap
from qiskit.ml.datasets import ad_hoc_data
from qiskit.circuit.library import TwoLocal
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QSVM

# Prepare data (example using ad hoc dataset)
feature_dim = 2
sample_total, training_input, test_input, class_labels = ad_hoc_data(
    training_size=20, 
    test_size=10, 
    n=feature_dim, 
    gap=0.3, 
    plot_data=False
)

# Feature map and ansatz
feature_map = ZZFeatureMap(feature_dimension=feature_dim, reps=2)
ansatz = TwoLocal(feature_dim, ['ry', 'rz'], 'cz', reps=2)

# QSVM setup
qsvm = QSVM(feature_map, ansatz, training_input, test_input, class_labels)

# Run QSVM (using a simulator backend)
backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)
result = qsvm.run(quantum_instance)

# Analyze results (example: prediction accuracy)
print(f'Testing accuracy: {result["testing_accuracy"]}')
