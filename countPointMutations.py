#Problem: Counting Point Mutations

#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

def diff(seq1, seq2):
    count = sum(1 for a, b in zip(seq1, seq2) if a != b) + abs(len(seq1) - len(seq2))
    print(count)


seq1 = "ACTTACCATAGCAATTTCAGGTAAGCTCGAGTATCTTATGGTTAATTGGCGGCGAGCTTAAAAGGGCAACTACCATGTCTTACCTACTAACTGATAGTTCCCGGACTGTTCGCTCGCGACCTGGATTCATCCGTCCGCTATTTTGAACGCGGAAAGCCGGGCCGCGGCACTATCACGTTCGGTGGCGCCTAACACTATTTTTTTACAGCACGCATTCTAGAGGGGACTCAGATCGTTCGTCTCAGCGCCGCTCGGTGGCCTTATTCATGGAGACGTACCGTTACGCGGGCGAGGCCCCGCTTACTGACACGAGGAGTCCGCTCCAACAATACCTGGGCCACATGCGGGTCACCGGCGTAAATAGGCCCGTGGTAAGGGCGTACTGCATTTAAGGAGTTGCCTTAAACGTAGAGGATATGATATCGCTTCGGTCTGCAGGCATATTTATTTATCTTGATAGACCCCTTGAAACAGGAAGCAGGTTGGCTGAGTCAGCATACCGCCTAACAGTATATATAACACCTCTGCTCATGCCCTTTATGGCGTCTCTGTAAGCAGGAGCTCGCATGTTAATTGGGGTGAGTACTCGAAATAATGGATGGGTAATACGTAAACGGCGGATATAACCTTATTCCGTTTTCTGAGATCAACCTGGTTGTCAACAACTCAATGGTAAAGCTGACCTGAGGCAATATCACATTCACTTCTACAAACTAGCATTGTCGCGAAAGAAAAGACACTGAATCGTGCGTCCTGTACTTTGCATTCAAGTAGGGAATCAATGGGCCCCTGAACATGGAAATGTATGGTCATGCGACTTCCAAGGATGTCCGGTACCGTTGTTTTCATTTCGCTTTAGGAGTCCACGATTTAACCCGGCCAATAGGAGAGAGACAAGATGGTTGTCGCCTCTAGTGGCCCTGTTTCATTCAAGAACGCAGAGTCCA"
seq2 = "AGGGGCCAGTGAAATTGGAATCAGATTCATGGACCTTTGGTGTAACTGGCGCTGAAATTGCTCGTGAAGCATTAATGTGTACCTCTCTAACTGAGATTATCCCGACTTTAAGGTCTCACCCTGCATGCATATGTCAGTTAGCTGTTCCGTCCAATGCCAGGGTCCGGCAAGTTGCCGCCCGGTGGCGACAAAGATTCCTTTGGGCTAGGACACATTATCTATCGTGCTAACAACGCTTGTTTGAGGGGTCCAGCGTGTGTTAAGCGAGGGACACGGGACCTGTGGCGCTGGAAGCTACATTTTCCGGTGCGAGGCGCCCGATTGGTCCTTAACTGAGTGCACTGAGTAGCGACGGAAAGAGGAGGGCTATGTTTACCAGGTATTCCCTTCGCTGAGCTAACGCAAAATAAAAGCATATGATGGGGCCACTTCGTAGAGCCATATGGCCCCCTGGCGTCTAGCCGTATGAAACCTGCTGCGGATGGCCTCACGTAGCGTAGCGTAGTCAGGCACATATAGCAACTCGGACTTTGATCATTATAGCAGGAAGGTAAGGAGGTGCGTGCGTTTCAAGTCATATTCGGCGTCATTATACTTAATGGGCAATACTGAAAATTACCATGATCAACTTTGCCTCCTACAACGACCAAGCACGAAGTCAGCGGACACCTGCTTCCTCCGTATTACGAAACTACATATTCCATCACTGCACAAACACATTGTCTACATGCAAGAGTCAAATAGTCGAGCTTAAATATTTGTGAGTTCATCGATGGAATTAGGCTGTCTTGGTCCGTGGTACGGGAAATTCAGGGGACATTTAAGGTAGCTTGGAACTTTTCCTGTAGGGTCTCTTCTAGCGGGGACGATTTTGTCCATTAACTCACTCTGGGTCTAGCGTGCCTACGCGATTGCGGCGCCAGCGTCACGGAGTAGCGCAATGTCTA"
diff(seq1, seq2)