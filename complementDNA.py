#Problem: Complementing a Strand of DNA

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

def complement(data):
    table = {
    'A' : 'T', 
    'C' : 'G',
    'G' : 'C',
    'T' : 'A'
    }

    copy = ""
    for nuc in data[::-1]:
        copy += table.get(nuc)
    print(copy)

def main():
    data = "ACTTCTTCCGACCTTGTAAAGAAAACCGACCAGCGGGCGCGTGATTTTCGGTATAGCGTGGTCGAGGTATCTGGACCAGTGTTCGCGTTTGGTTCTAGCTAAACTAAGGGTGCTCCTCAGAATTTACCCCTTTGCTCTGTACCTTGGTATTGTGCATTCGGACATAACCTCTCGACCGTAAGTAAGATGACACCCACGGCTAGAGCGATTAGGTAACAAGGACACAAAGGCACTGTTAAATACCCACGCTAAATTGAGTATATGAGGTATGAGACTATCGTGCAGCGTCTGTCCCCTGCTTTAGTATCCCACACGGGTGTCCCGTTCTCAAACATACACTATCGGCGGGAAGCGGGTCGTCCACAAGACTTCGGTAGGATTTAAATTACCCGTCTCTCTCGAATTCAGCACTTCCAGCGTATGTAGCCCCAATAGGCCAAGCCCGAACTTTGCGCTAACAAGTTGGACCCACTAGACCCTTCAGCGAGTCCCCTGACTCCGGTAACCTGCATTCAACCCTGGCTGCCCAATACCCACATTGCGGAAATAGAGTGGTATGAAGAGTGCAATACTAACTCTCTACAATCCGTAGTCACAATGCCCTGACCGTATCGAGCACTTGTGTGCGCATCATTCGGGGCCACCATTAGTCACTATGTCGAGATACTTAGATTCGCGGGTGAGCGGGATGGCCAACAACACAGCGAGATTTCCGCTCATTCAACACAGGTGCGCATCAAGCAGTGGAAATGGCATAAACTACTCGGCTTGTTACCCCTGTAGCCGCTGGGTCCAGCACGGTCGTGCGAGGGGAGCCACAAACCTCCAATGATTTAGCTAGAACACATTGAGACTATTATCTACTGACTCAAATTGTCAGACAGATCCAGGGCCAA"
    complement(data)

main()