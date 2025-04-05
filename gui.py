# Programmer: Nathalea Evans - 2101707

# This code is a simple GUI application that allows users to input a DNA sequence and analyze it for specific patterns.
# It uses the tkinter library for the GUI and a custom DNA class for analysis.

# Imports
import tkinter as tk
from tkinter import ttk
from dna_analyzer import DNA

class DNAAnalyzerGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("DNA Pattern Detector")
        self.window.geometry("500x400")
        
        # Initialize StringVar first
        self.dna_sequence = tk.StringVar()
        self.out_str = tk.StringVar()
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Create and arrange GUI widgets.
        # Title
        title_label = ttk.Label(
            master=self.window, 
            text="DNA Pattern Detector", 
            font="Calibri 24"
        )
        title_label.pack(pady=20)
        
        # Input Frame
        in_frame = tk.Frame(master=self.window)
        in_frame.pack(pady=10)
        
        input_label = ttk.Label(
            master=in_frame, 
            text="Enter DNA sequence:"
        )
        input_label.pack(side=tk.LEFT, padx=5)
        
        self.entry = ttk.Entry(
            master=in_frame, 
            width=50, 
            textvariable=self.dna_sequence
        )
        self.entry.pack(side=tk.LEFT, padx=5)
        
        # Button Frame
        button_frame = tk.Frame(master=self.window)
        button_frame.pack(pady=10)
        
        # Analyze Button
        self.analyze_button = ttk.Button(
            master=button_frame, 
            text="Analyze", 
            command=self.analyze_sequence
        )
        self.analyze_button.config(width=10, padding=3)
        self.analyze_button.pack(side=tk.LEFT, padx=10)
        
        # Reset Button
        self.reset_button = ttk.Button(
            master=button_frame, 
            text="Reset", 
            command=self.reset_fields
        )
        self.reset_button.config(width=10, padding=3)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Output
        output_label = ttk.Label(
            master=self.window, 
            text="Output", 
            font="Calibri 16", 
            textvariable=self.out_str
        )
        output_label.pack(pady=10)
    
    def analyze_sequence(self):
        # Analyze the DNA sequence and display results.
        sequence = self.dna_sequence.get().strip().upper()
        if not sequence:
            self.out_str.set("Please enter a DNA sequence")
            return
            
        try:
            analyzer = DNA(sequence)
            result = analyzer.analyze()
            self.out_str.set(result)
        except Exception as e:
            self.out_str.set(f"Error: {str(e)}")

    def reset_fields(self):
        # Reset input and output fields.
        self.dna_sequence.set("")
        self.out_str.set("")
        self.entry.focus_set()

# Main function to run the GUI application
def main():
    window = tk.Tk()
    app = DNAAnalyzerGUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()
