import tkinter as tk
import numpy as np

def capacitance(i,f,v):
    dois_pi=np.multiply(2,np.pi)
    w=np.multiply(dois_pi,f)
    a=np.multiply(w,v)
    return np.divide(i,a)

def distancia_capacitance(x):
    return np.divide(np.multiply(8.854,5.34),x)

def dist_current(i):
    return np.divide(np.multiply(8.854,5.34),i)

def corrente(c,f,v):
    dois_pi=np.multiply(2,np.pi)
    w=np.multiply(dois_pi,f)
    a=np.multiply(w,v)
    return np.multiply(c,a)

def calculate():
    #try:
        #input1_val = float(input1_entry.get()) #cell gap in µm

    input2_val = float(input2_entry.get()) #excitation voltage applied to high plate of the capacitor

    input3_val = float(input3_entry.get()) #excitation frequency applied to high plate of the capacitor

    input4_val = float(input4_entry.get()) #measured current from lock-in in nA
    input4_val = np.multiply(input4_val,1e-9) #convert current to A

    input5_val = input5_entry.get() #float(input5_entry.get()) #desired distance of capacitor plates in µm

    if input5_val == "":
        input5_val = 1
    else:
        input5_val = float(input5_val)

    output1_val = capacitance(input4_val,input3_val,input2_val) #current capacitance in pF
    output1_val = np.multiply(output1_val,1e12) #convert capacitance to pF

    output2_val = distancia_capacitance(output1_val) #current capacitor plates distance in µm

    output4_val = distancia_capacitance(input5_val) #desired goal capacitance in pF

    output3_val = corrente(output4_val,input3_val,input2_val) #desired goal current in nA
    output3_val = np.multiply(output3_val,1e-3) #convert goal current to nA
        

    output1_label.config(text=f"C (pF): {output1_val:.5f}")
    output2_label.config(text=f"d (µm): {output2_val:.2f}")

    if input5_val != 1:
        output3_label.config(text=f"I (nA): {output3_val:.3f}")
        output4_label.config(text=f"C (pF): {output4_val:.5f}")
    else:
        pass
    #except ValueError:
    #    output1_label.config(text="Invalid input, please enter a number")
    #    output2_label.config(text="Invalid input, please enter a number")
    #    output3_label.config(text="Invalid input, please enter a number")
    #    output4_label.config(text="Invalid input, please enter a number")

# Create the main window
root = tk.Tk()
root.title("CS100 strain cell")
root.geometry("550x210")

# Create the input labels and entries
#input1_label = tk.Label(root, text="Gap (µm):")
#input1_label.grid(row=0, column=0)
#input1_entry = tk.Entry(root)
#input1_entry.grid(row=0, column=1)

input2_label = tk.Label(root, text="V (V):")
input2_label.grid(row=0, column=0)
input2_entry = tk.Entry(root)
input2_entry.grid(row=0, column=1)

input3_label = tk.Label(root, text="f (Hz):")
input3_label.grid(row=0, column=2)
input3_entry = tk.Entry(root)
input3_entry.grid(row=0, column=3)

output6_label = tk.Label(root, text=" ")
output6_label.grid(row=1, column=0)

input4_label = tk.Label(root, text="I (nA):")
input4_label.grid(row=2, column=0)
input4_entry = tk.Entry(root)
input4_entry.grid(row=2, column=1)

input5_label = tk.Label(root, text="d (µm):")
input5_label.grid(row=5, column=0)
input5_entry = tk.Entry(root)
input5_entry.grid(row=5, column=1)

# Create the button to trigger the calculation
button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=7, column=0, columnspan=2)

# Create the output labels
output1_label = tk.Label(root, text="C (pF):")
output1_label.grid(row=2, column=2)
output2_label = tk.Label(root, text="d (µm):")
output2_label.grid(row=3, column=2)

output8_label = tk.Label(root, text="Determine current position")
output8_label.grid(row=2, column=3, rowspan=2)

output7_label = tk.Label(root, text=" ")
output7_label.grid(row=4, column=0)

output3_label = tk.Label(root, text="Goal I (nA):")
output3_label.grid(row=5, column=2)
output4_label = tk.Label(root, text="Goal C (pF):")
output4_label.grid(row=6, column=2)

output9_label = tk.Label(root, text="Determine next position")
output9_label.grid(row=5, column=3, rowspan=2)

# Start the main event loop
root.mainloop()
