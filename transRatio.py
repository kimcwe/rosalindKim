#Problem: Transitions and Transversions

#For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

#Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#Return: The transition/transversion ratio R(s1,s2).

def ratio(s1, s2):
    transitions = 0.0
    transversions = 0.0
    num = 0
    while num < len(s1):
        if( (s1[num] == 'A' and s2[num] == 'G') or (s1[num] == 'G' and s2[num] == 'A') or (s1[num] == 'C' and s2[num] == 'T') or (s1[num] == 'T' and s2[num] == 'C') ):
            transitions += 1
        elif( (s1[num] == 'A' and s2[num] == 'C') or (s1[num] == 'C' and s2[num] == 'A') or (s1[num] == 'G' and s2[num] == 'T') or (s1[num] == 'T' and s2[num] == 'G') or (s1[num] == 'A' and s2[num] == 'T') or (s1[num] == 'T' and s2[num] == 'A') or (s1[num] == 'C' and s2[num] == 'G') or (s1[num] == 'G' and s2[num] == 'C') ):
            transversions += 1
        num += 1
    
    print(f"transitions: {transitions} | transversions: {transversions}")
    return (transitions/transversions)

seq1 = "TGCCCGCGTTATTTGGTTCAATGTTTGACGGCAAGTCGTTAGGTAGTCGAAAGGTAGGTCAGAGTCAGTCAAGCTCTTATCCCGGATTCGAATTCCTGTTGTGTCAGTAAAGCTTAAAACTGTGTATCCCGAATTGACAATCTGTCTAGTGTTGCTCCGCGGAATTTGCTCGCCTGCATCATCGAAAATAATGCGTCTAATCTGTTTGTCGACCCCATTACGGGCCGAGCCGCCCGTGATGATAGAAGCTATAGACATTCCTGAGATGGGCGCTGTGCGTGAAACTCCAGCGGATGCGACTGGTAGACGGTCTGGATCTTTTAATTCACCAGGACAGACGCGTAGACGCTGACAATGGATGCTAAACTACGTCGTAGCTTTCAAAGTTTATTGTTACGAGATGGTATGTTGATTTTAACCCCTCAGTACTGCAGGGTCCGCGCGGTTGAACTGCCTTACGATCTCACGGTGGCTGACTCAGGCGCGCACCGACCAAAACTAAGTCAGGTAAACAAACCGGACTTCGTCCGTATGGTTTGTGAGGAGGTACAGGCAGGAGAAATGGCACTGATGCAGCACGCTTCCTTGAGGGACCCGACCGCTAACAATGCGCCCGCGATTGACCCCGTCGATCAAGGTATTCGTCTTATTTGGCGTTATTTGAGGAAAGGACCAAAGCCGCAAAAGACTCGATGAGTCATTCACTTTCTTACTCAATTTTGCCAGTCCAGAAGCTCAGCCGTATGACCTGGACCGGCCCCCAATTGGGGATCATGTCCGCAATTGCGTGGCGACTTAGATACGAAAGTACCAATGGATCATCTCTTCGAGTTTCATCTCGACCTGTGCCCGCGCGCCACTATATTGG"
seq2 = "TACCCGCCCTATCGGGTACATGTTTTGATGGCAAGTTAGTGAGTAATAGGAGGGTGGGTCGGGACCAGTCCGGCTTTTATCCCGGACTTAAAATCGTGTTATGTCAGTAAAGCTCAGCACTGTGTGGCCCACACGTGTAATGCATCTAGCATTATCCCGCGGAATTTGCTTGCTTACATCACCGGGAACAGTGAGTCCAATTAACTTGCCAAGCCCATTAGGGGTCGAGACGACCGTGATTATAGAAGCTAGCGATGCTCGTGAAGTTAACGCTTGGCGTGAGCCTCAGGCAAACGCGACGGACAGGCGGTCTGGCCCTCCTGACCTACCGGGGCATACGCGTAGATATTGATATTGGATGCCTGCTTGTGGCTCCGTTTCTAAGTTTCAGTGCTATAGAGTGGTATGTTGGTTTTAACCCCCTAGCACCCCAAGGTCCGCGTGATTTGGCTGCCTTACGATCCCGCATTGCCTGTCTCAGGCGGGTTCCAACCAAAACTAAGTCAGGTAAACAAACCGGACTATGTCAGTAGGGTTTATGAGGAGGTAAAGACTGGAGAGATAGTACTGGTGCAGCACGCTCCCCTGGGACGTCCAACCACGGACAATACACCCATGACCGACCCCACCGATGTACACATACGCTTTATTCGGCGTTGGTTCAGGAAAGGACCCAACTTGCAAAAGAGAGGAGGAATCATCTACTTCCCAGCCCGGTTTTGCTGGTTCAGGAATTGAGCAGAATGACCTGAACCGGCACTCAATCGAGGTTTGCATCCGTAGTTACCTAGCGATTTAAGCATGAAGATCCCACTGGACCATCCCTCAGCGTATAATTTTAATCTGGATCCACGCGCCACCATATCGG"
print(ratio(seq1, seq2))

def ratioBetter(s,t):
    unchanged = sum(a == b for a,b in zip(s,t))
    transversion = sum((a in ('A', 'G')) != (b in ('A', 'G')) for a,b in zip(s,t))
    return (len(s)-transversion-unchanged) / transversion