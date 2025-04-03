class DNA_DFA:
    def __init__(self, sequence):
        """
        Initializes the DFA with a given DNA sequence.
        :param sequence: A string representing the DNA sequence.
        """
        self.sequence = sequence
        self.length = len(sequence)
    
    def detect_start_codon(self):
        """
        Detects the ATG start codon in the DNA sequence.
        :return: Index of the first occurrence of ATG or -1 if not found.
        """
        for i in range(self.length - 2):  # Ensure enough characters remain for a triplet
            if self.sequence[i:i+3] == "ATG":
                return i  # Return index of ATG occurrence
        return -1  # Return -1 if not found
    
    def detect_huntingtons_gene(self, start_index):
        """
        Detects three consecutive CAG repeats after ATG.
        :param start_index: Index where ATG was found.
        :return: True if three consecutive CAG repeats are found, otherwise False.
        """
        for i in range(start_index + 3, self.length - 8):  # Ensure enough room for three repeats
            if (self.sequence[i:i+3] == "CAG" and 
                self.sequence[i+3:i+6] == "CAG" and 
                self.sequence[i+6:i+9] == "CAG"):
                return True  # Return True if the pattern is found
        return False  # Return False if not found
    
    def detect_possible_cancer_mutation(self, start_index):
        """
        Detects the pattern GGT followed by GAT after ATG.
        :param start_index: Index where ATG was found.
        :return: True if GGT followed by GAT is found, otherwise False.
        """
        for i in range(start_index + 3, self.length - 5):  # Ensure enough room for both codons
            if self.sequence[i:i+3] == "GGT" and self.sequence[i+3:i+6] == "GAT":
                return True  # Return True if mutation is found
        return False  # Return False if not found
    
    def run(self):
        """
        Runs the DFA to analyze the DNA sequence for specific patterns.
        :return: A message indicating the detected pattern or absence of patterns.
        """
        start_index = self.detect_start_codon()
        if start_index == -1:
            return "Start codon not found."
        
        if self.detect_huntingtons_gene(start_index):
            return "Huntington's disease gene found."
        
        if self.detect_possible_cancer_mutation(start_index):
            return "Possible cancer mutation found."
        
        return "No significant patterns found."

# Example usage
dna_sequence = "TACATGCAGCAGCAGGGTGAT"
dfa = DNA_DFA(dna_sequence)
result = dfa.run()
print(result)