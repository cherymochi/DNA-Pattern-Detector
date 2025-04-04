# Programmer: Nathalea Evans - 2101707

# GUI Design

# Imports
import tkinter as tk
from tkinter import ttk


# Functions
def pattern():
    # Function to detect DNA pattern
    
    start = "ATG" # Start codon
    can_pattern = "GGTGAT"
    hunt_pattern = "CAGCAGCAG"
    sequence = dna_sequence.get()
    
    # Convert to uppercase
    upp_seq = sequence.upper()
    
    # Check for start codon
    if start in upp_seq:
        start_index = upp_seq.index(start)
        # Check for can_pattern
        if can_pattern in upp_seq[start_index:]:
            can_index = upp_seq.index(can_pattern, start_index)
            output_label.config(text="Pattern Detected: Cancer")
            # Check for hunt_pattern
            if hunt_pattern in upp_seq[can_index:]:
                hunt_index = upp_seq.index(hunt_pattern, can_index)
                output_label.config(text="Pattern Detected: Huntington's Disease")
            else:
                output_label.config(text="No Pattern Detected")
                return


# Create Window
window = tk.Tk()
window.title("DNA Pattern Detector")
window.geometry("500x400")

# Tile
title_label = ttk.Label(master = window, text="DNA Pattern Detector", font="Calibri 24")
title_label.pack(pady=20)

# Input 

# Variables
dna_sequence = tk.StringVar()

in_frame = tk.Frame(master = window)
input_label = ttk.Label(master = in_frame, text="Enter DNA sequence:")
entry = ttk.Entry(master = in_frame, width=50, textvariable=dna_sequence)
button = ttk.Button(master = window, text="Go", command = pattern)
button.config(width=10, padding=3)



# Output
out_str = tk.StringVar()
output_label = ttk.Label(master = window, text="Output", font="Calibri 16", textvariable=out_str)

# Pack widgets
in_frame.pack(pady=10)
input_label.pack(side=tk.LEFT, padx=5)
entry.pack(side=tk.LEFT, padx=5)
output_label.pack(pady=10)
button.pack(pady=10)



# Run
window.mainloop()