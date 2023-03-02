import tkinter as tk
import numpy as np

#constants
#LNLS strain cell model CS100 -> capacitor area = 5.34 mm^2
#LNLS transmission strain cell model CS200T -> capacitor area = 7.42 mm^2
area = 5.34 #capacitor plates area in mm^2
area = np.multiply(area,1e-6) #convert area to m^2

dois_pi=np.multiply(2,np.pi)

e=8.854e-12 #Dielectric constant in F/m

#functions
def capacitance(i,f,v): #returns capacitance in F
    omega=np.multiply(dois_pi,f)
    a=np.multiply(omega,v)
    return np.divide(i,a)

def distancia_capacitance(x):               #If x = 'distance of plates', returns capacitance in F
    return np.divide(np.multiply(e,area),x) #If x = 'capacitance', return distance of plates in m

def dist_current(x,f,v):                    #If x = 'distance of plates', returns current in A
    omega=np.multiply(dois_pi,f)            #If x = 'current', returns distance of plates in m
    a=np.multiply(omega,v)
    return np.multiply(a,np.divide(np.multiply(e,area),x))

def calculate():

    input2_val = float(input2_entry.get()) #excitation voltage applied to high plate of the capacitor in V

    input3_val = float(input3_entry.get()) #excitation frequency applied to high plate of the capacitor in Hz

    input4_val = float(input4_entry.get()) #measured current from lock-in in nA
    input4_val = np.multiply(input4_val,1e-9) #convert current to A

    input5_val = input5_entry.get() #desired distance of capacitor plates in µm

    if input5_val == "":
        input5_val = 1
    else:
        input5_val = float(input5_val)
        input5_val = np.multiply(input5_val,1e-6) #convert distance to m

    output1_val = capacitance(input4_val,input3_val,input2_val) #current capacitance in F
    output1_val = np.multiply(output1_val,1e12) #convert capacitance to pF

    output2_val = dist_current(input4_val,input3_val,input2_val) #current capacitor plates distance in m
    output2_val = np.multiply(output2_val,1e6) #convert capacitor distance to µm

    output3_val = dist_current(input5_val,input3_val,input2_val) #desired goal current in A
    corr_ampere = output3_val #saves current value in A
    output3_val = np.multiply(output3_val,1e9) #convert goal current to nA

    output4_val = capacitance(corr_ampere,input3_val,input2_val) #desired goal capacitance in F
    output4_val = np.multiply(output4_val,1e12) #convert desired capacitance to pF

    #Output labels
    output1_label.config(text=f"C (pF): {output1_val:.5f}")
    output2_label.config(text=f"d (µm): {output2_val:.2f}")

    if input5_val != 1:
        output3_label.config(text=f"I (nA): {output3_val:.3f}")
        output4_label.config(text=f"C (pF): {output4_val:.5f}")
    else:
        pass

# Create the main window
root = tk.Tk()
root.title("CS100 strain cell")
root.geometry("550x210")

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

output3_label = tk.Label(root, text="I (nA):")
output3_label.grid(row=5, column=2)
output4_label = tk.Label(root, text="C (pF):")
output4_label.grid(row=6, column=2)

output9_label = tk.Label(root, text="Determine next position")
output9_label.grid(row=5, column=3, rowspan=2)

# Start the main event loop
root.mainloop()
