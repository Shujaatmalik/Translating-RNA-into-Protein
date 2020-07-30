# Translating-RNA-into-Protein
# Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING

# Code Explaination
First of all we will read all lines of file into one string, (Remove all \n )
than we have to conver DNA into RNA by Replacing the 'T' with 'U'
Third step is find the start index for protein
Fourth Find the Stop Index for protein
now start reading from starting index to Stop Index with a jump of three
and match every three bases with RNA Protein Code.
I used Dict and List for this purposes.
Thank you

