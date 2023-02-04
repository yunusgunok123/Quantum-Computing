# %% LOAD LIBS
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, IBMQ, execute
import ipywidgets as widgets

# provider = IBMQ.load_account()

# %% QUANTUM COIN GAME

is_flipped = True
def on_flip(b):
    global is_flipped
    is_flipped = True
    on_click()
def on_skip(b):
    global is_flipped
    is_flipped = False
    on_click()

def on_click():
    global is_flipped
    qreg = QuantumRegister(1, 'q')
    creg = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(qreg, creg)
    circuit.h(qreg[0])

    if is_flipped: circuit.x(qreg[0])
    else: circuit.i(qreg[0])

    circuit.h(qreg[0])

    circuit.measure(qreg[0], creg[0])

    backend = Aer.get_backend('aer_simulator')
    job = execute(circuit, backend, shots=2**13)
    res = job.result().get_counts()
    
    if "1" in res: print("You win!")
    else: print("You lose!")

button_x = widgets.Button(description="Flip")
button_i = widgets.Button(description="Skip")
button_x.on_click(on_flip)
button_i.on_click(on_skip)

widgets.HBox([button_x, button_i])

# %% STERN GERLACH EXPERIMENT

qreg = QuantumRegister(1, 'q')
creg = ClassicalRegister(1, 'c')
circuit = QuantumCircuit(qreg, creg)
circuit.h(qreg[0])
# circuit.t(qreg[0])
# circuit.h(qreg[0])
circuit.measure(qreg[0], creg[0])
backend = Aer.get_backend('aer_simulator')
job = execute(circuit, backend, shots=2**13)
job.result().get_counts()

# %% BELL STATES

qreg = QuantumRegister(2, 'q')
creg = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg, creg)

# 00 11
circuit.h(qreg[0])
circuit.cx(qreg[0], qreg[1])

# 00 10
# circuit.h(qreg[0])
# circuit.swap(qreg[0], qreg[1])

circuit.measure(qreg[0], creg[0])
circuit.measure(qreg[1], creg[1])
backend = Aer.get_backend('aer_simulator')
job = execute(circuit, backend, shots=2**13)
job.result().get_counts()

# %%
