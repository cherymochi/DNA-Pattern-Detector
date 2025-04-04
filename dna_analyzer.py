# TOC Group Assignment - DNA Pattern Analyzer
# Members: Nathalea Evans - 2101707
#          Tianna Lue-Lim - 
#          Nathan White - 2101708


# DNA Pattern Analyzer
class DNA:

    def __init__ (self, sequence):
        ''' this function just initializes both the input string 
        and its lenght in 1 variable for later use, and is automatically called
        when an new instance of the class is created'''

        '''__init__ is the constructor method for pyhton and must be used with self 
        self represents an instance of the dna class'''

        self.sequence = sequence.upper()
        self.length = len(sequence)
        # stores the length of the dna string; we will use this to traverse it


    def detect_start_codon(self):
        '''finds the ATG start codon in the DNA sequence.
        then returns the index of where it was found'''

        for i in range(self.length - 2):  
        # the -2 leaves space for enough characters

            if self.sequence[i:i+3] == "ATG":
                return i  # returns index of ATG occurrence
            
        return -1 # if ATG is not found

    def detect_huntingtons_gene(self, index):
        # '''boolean function to detect if 3 consecutive CAG repeats after a ATG'''

        for i in range(index + 3, self.length - 8):
        # leaves enough room for 3 repeats (9 characters)

            if (self.sequence[i:i+3] == "CAG" and 
                self.sequence[i+3:i+6] == "CAG" and 
                self.sequence[i+6:i+9] == "CAG"):
                return True  # if the pattern is found
            
        return False  # if the pattern is not found

    def detect_possible_cancer_mutation(self, index):
            # '''checks if GGT is followed by GAT'''

            for i in range(index + 3, self.length - 5):
            # leaves enough room for both codons

                if self.sequence[i:i+3] == "GGT" and self.sequence[i+3:i+6] == "GAT":
                    return True  # if mutation is found
                
            return False  # if mutation is not found

    def analyze(self):
        # '''analyzes the DNA sequence for specific patterns then returns a message 
        # indicating the detected pattern or absence of patterns'''

        index = self.detect_start_codon()
        # the index at which the 1st ATG occurence was identified

        if index == -1:
            return "Start codon not found."
        
        if self.detect_huntingtons_gene(index) and self.detect_possible_cancer_mutation(index):
            return "Huntington's disease gene found and Possible cancer mutation found."

        if self.detect_huntingtons_gene(index):
            return "Huntington's disease gene found."
        
        if self.detect_possible_cancer_mutation(index):
            return "Possible cancer mutation found."
        
        return "No significant patterns found."

# dna_sequence = input("Enter the DNA sequence you would like to analyze: ").upper()
# # collects and stores the dna sequence string in uppercase

# result = DNA(dna_sequence).analyze()
# # creates an new class object and runs the analyzer on that new object

# # Display Results in GUI output
# gui.out_str.set(result)