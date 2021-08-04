#Problem

#The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
#The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by s.

def translate(seq):   
    rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
            "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
            "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
            "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
            "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
            "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
            "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
            "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
            "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
            "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
            "UAA" : "-", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
            "UAG" : "-", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
            "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
            "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
            "UGA" : "-", "CGA" : "R", "AGA" : "R", "GGA" : "G",
            "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
            }
    protein = ""
    x = 0
    while(x < (int(len(seq))) ):
        #print(seq[x:x+3])
        if(rna_codon.get(seq[x:x+3]) == "-"): break
        else: protein += rna_codon.get(seq[x:x+3])
        x += 3
    return protein

print(translate("AUGGUAACGAGGGACGCAAAAGAUAUUGUCAACAGGCCACAUCAUGGUCGUAUUUACUGGGGGAGGCUUAACUUUGACAUCUGUGCCGUAGGUACUCCACUCACGUUGGGAGUUCCCCCACGCUCUGGUCGAUGCGGUGGGUCGCGUGCGAGGGGCAUUUUUCCUCUAUCAUUAGAUAAUGCGGCGUUGCUCGAACCGGUUGGGCACAUAGGGCCGUCUGCAACGGUAUUCCGAGUCACAUCUAAGAUCCUUGCGUGCAGUAGUAAGGGACGAUUGAACUUUCAAGUCCGGGGGGCAACCUGUAGAGUCACCUUUCAGCUGCAGUCUACCCAAUUAUAUAAACCCUACACUAUUGAUGGCGUGUCCCGCAGUCUGGAUGAGAGACUUUACAAGGGUUUUUCCGGCUUGAGUGACAGCCAGAUGUCUCAGUGGCUCGUGCGAGUGCAGCGCAGCAAUAGGCGAACAGUAGAUGGAAUGCUGAGAGAGUGGUCGGCUCUUAAGCUAAGUUUGAAAAAGAAAAUCUCGGGGGCUGGAGUGAGAACGCAGUACAUUCUGACUAUAUCCCUGGCGCGCCUCGGGCGAGCUACGCUUCUCGCGGAGCGACCUACCGCUGUCGUAAUCCGUAUAUUAGGACCCCGCUGGACUCAGGGAUGGGAACUAAAAUCUCAGCACCCCCGAUGCGAUACUAGCGUCUUAAGCAGGUGCUCAGGCAAAAACUGCAUAAGUUGCCGAGGUCAGAGUAGUAGUUGUUUCAAUUGUUUACUAUGCAGAUACCGAGGGCCCCGACGACUUGAACAAAAAGUGAAUUUCGCAAUUCCUUGGCAGGUGCAUAAUAUCCGACCGGGCCGUCAUCCCUCCAACUCAGAUUGCGGAAACUUAUCAUCGGUAUUAACACUGUACACAAGCCUCGGCAACAAAGUUCAACUCGUCGAGAAUGAGGAAUUAAAUGAAAAGAACUCCUCUAUAAAUGAUCCCUUACUAUGGCCUAAAUCCCUCGCUUCGAGGUUGGAAACCUUGGACUCCUCCAUCUUUCGCAAUCCGAGUGGCGGAGGGUUUACAGAUUUCUUGGCCAGAAUUUCAAACCGCUCCUACAGUAAUCCCGCAUUUUCGUGGAUCGUCAGACCUCGUUUAAGCGUGCACGACAGUCCAAGUGCUGCAGGAAUGUACGUCGCGGUCGGACUCUCGACGGGCUGUUCAUGUCGCCGGGGCCUCUCGUCACAAGAAGCCAAUUUGUCAGUCGGGGUAGGGUCGUAUGUUGUCCGUUGCCCGGAACUAAGACGUACAGGGAACAGGGUAGCUCAAGGCUGCAUCUCCGGACACCCUAAUCCGGGUACAGGAGGACGACAGAUCGGUAAGGUCAAGCAUACCUACAUAUUCGUAGAACAGGAAGUACAUGUGUAUUACCGUUUCACAAUGACUGAAUCCUUAGCCGGGAGACCUCCCACCCACGACCUUUCGCACCGUGCAGAGGGGCCGCUCAGGAAGUUCAAUUACUUGUCUCGCACGGAUAAGCAACUCGCGUCGGUACGUGAAACAGGGGGGCUUCGUAAUAAUAGCCCGCUACAGAGGAUGGGAUUAGUUCUAGGCAUGUCUGGGAAUCAUAUUGAAGACAGCGAAACGGGAGUCGCAUCCCUGCCACGCCCAGAGGUAAUGCUUAUCGUACCUUGUGUGCAGCGUCACUGUCCCGCGAAGGUGCCAGGGGCUUCAGGUCUGCCACGUCUAGUUCUCGACACUGUAAAAUUGAAAAUCUGUCAAAGGUUUGCAUACGGCAGCUACGUAGGUUACUCAAUGCCGGGGUGCUUUGUAUGGUAUCUGGUCUUUGCUGAAGCUCGAUUGCCAGAGCCCUCGCUUGCGUGUCUAGGCCGGGGAACACAUCUCAAAAGGUAUUACAUGCGGAUAAGUUCUGGUGUAGAUGUCGGGUUCGAUCGUAGCGGACAGGCAGACCGAUGUCUUAAGACCGUAAAACUGAGCGAAAUUUUGGCUGAGUCAUGGGGCCUUGGGGGAGACAUCGGCACACUUACUGCAGAGACCCACAUUGUUUUGGUUAAAUUCCCCCUCAUCUUACGGAGCACCGGGAUGAACCGUAGCGUAACUAUAACGCCCUGGCGUAUUAAAAGUUGGCGGAGAUUGGCUAGCUUAAGACACAUCGAUCGCCACAAGAUACUUUUCGGUUUUAGCGCGCCUGCUGUGAACGUCUAUGACAAGUUACCAUCCAUAGGUCACCAAGUGCGUGAUCCGCGACCACUCCUAAGCGGACAAGGGGCCCUUAAGUUAAUCGAAAAUAAAAACGCCGCGCUGAUUACUCGGAUAGGGGGUGUCCGAUGUAGCGCUAUCUCCGAACUGGCGUCGCAUUUGACAGGCACGCACACGAGGUGGAAGUUUCGCUCCAAUCGCCGAGACCCGCGCGUCGAGCUCCCACACCGACAUUAUUGGUCCGUAGCCAUACGAUAUUCGAUUUUCUUCCUCGUGGUAAUUCUACGAGGCACUCUAGCGAGUAUUCGCGCUCAACAUCCAUUAACUUCGCAGAAGGUUGAAAACUUUUUUCAUUUCGCCACGAAUUUACGGGGGCUCCCAGAAUCGAUUAGCGAGCGUGUACAGCACCACACCAUAGUGCGAGGGCCGAAGGUUGCCAGUACUGUGCCUCUUAGAAGCUGCUGCCCCUGUUGUUAUUCGCGGCCUGGGCUGCACAAGUCGACUUCUUCUGUUCUAUGUGAUCGUCCAUACACGAAUGUUUAUGGCCGUAGCGUCUGGCGCGCGGCAAGACUCUCGAGAUACCAGCGGCUCGCCGCCUGCGCUAAACAGACCCCUCAAGAGGGGGGAGUAGUGGCAAAUAUAUCAUAUGGAGUACUUAUAGUGGUACUAUGGGCGGCUAUGCCGUCGAUGCGGUUCAGACGGGUAUAUGGCCUAGUGGGUGGAUGUUUAGCGAAAGUUUACCGGGGUAGCCCAAUCCGGGGCUGCGUCUACUCUCGAAGGAUUCGAGCGGAGCGUCAGAUCGCUCCCAUACAAGCUUAUCUGCGGGUUGGAGACUGGUCUAGCCCUCAGCAAUGGUCCAUUUCAUGCGUGCGUGGGGUGUUGUACCCAUACGAACUCGUCACCCCCCUGGAUCGACGCCACGGUCGCCUAAACCAUGGGGAGUCGACUCUGUGUUUGACCGGCAUCAAGCCAAGUAUCCGGUGCGGGCGCUGGGGUUCAUACCAACACCGCGAUGAAGAGAGGGAUCUGACCUCCGAGAACGGAGGAGGAUAUCACAAAGGUCGCGCGAUGCUAUCGCUCGUAUUUCUGGCGAGCCCCACCCUGACCGUAAUAAACCCCACGGUAGACGUCUCCGGCAAGAAUAAGGCGCUCAACUAUAAACUUGCUGCGCAGCAGCGGCUGAGGGCAUACCCCUCUGUAAUCAUUGCGUUGGAUGUGCGGGUGGCCCUCGCGUUCGCACAUGACUAUCCGCCAUUUCUGGGAAUUCUGUUUAAUAUAGGCUUGCACGUUCCUCAUCGGUGCGUACCGCGUGUUGAAAGACGCCUCGUGUGUAGUGUGCACUCGAAGAAUCAAUGUGGCACCAUUAAAUUAUGGAGCUACUCUGGGGUUGGGUUUAUUAGCUUACGGGCCGGCAACCGUUUGCAGGUUUCGCAUUGUUAUGCCUUCUCGCGCACUGUAGGCCCCCUGUCACUAGCCCCGGGUCAACCCCAUGCACCUUCGGGAUUGGAAAAUCGAUUCCUACAAGUUAUAAGCCUGCCGGCGCGUAUUACGAAAUGUAUUACACACCCCUGUCUGCCAUCGGAGGCUACGUGGCUAGCCCGCGCAGGCACAGUAGGAAGAAGUGGCUUGGUCUCGGAGGAAGGCAUUCCGCAGCCGCUGCAAGACAGUCCUGGUAAACAGCCAAAUUGUAGGGUGAUGAUGUUUUACGCAGCUCGGAAGAUGAAAAGUGGCAUACAAUGCUUCGCUUAUGGAUGGGGUUCGCCGAUGUCUCCCGUUCGUCUCUCACCCACAACUACUAGAAAAAGAGUGCACGCUUAUCAUCUUCUGAUGGCCUGUUCGCAACACGUUGCGUCAAACGACAUGUCACGAUUAAAACAAUUUCAGGUUGUCCAGAUACCAAUCGUGGAACGGACGAAGUUAUUCCCUCUUCUCGCUGAAUUAGCGGAGUUGGCACGUUUAGCGGAGGGCUUUAAUGGCUUUCCAUUGACAAGCAUCUUAGCGGUUUUGAUCGAAGACGAUACAGAGACCGUGCAUUAUCGACCUGCUCUAUCCACCAGCGCGGAUGUCGGUAGUCUAAACAUAUUCACUGGUAGCACACUUUUCUGCAAUCCCAGGGGCAAUAUGGAGGAGGGGGCAAGUACUGCGGGGAUACUGCUAGCGCGAGAUUCGGUAGGCACUCGGAGACAGCUCAAAAAAAAGACAUGUAGUACGUUUGAUGUCAAAGACCGCAAUCCUUUUCGUUCGGCAGUUAUGCCGCGACUGCUAUGCAUAUGUGAGCAUCCCCGGCUGUCCGUUGCAUAUUCUAGUCACAGGGUGAAGGCGCAUGGUGAGACUGCGCAUUCCGCGAUUAGAGCGAGUCUGCGAAUGUGGGUUGCUUCGACACGACUCUGUGGCUGCUUGCCUGGUUUGGGUGGCUCUAUGCCGUCAGAAGCGCACAGAGCAAUCUCUCGCUGUAAUUCCACGUUUCUCAAUUGCGGGGUGUCCCGUUCACCGCGAGCUCACGCGGAGAGUUGUCUGCGCACCACAGGAAUAGUCUCACGCAGUCUGAUGCAAUCGGUUGCCGACUACUCUAGAAAUUGUCGGGCGGAGCGUUAUCUAGUACGGCACCGGUGUCAGUCCGUUGUAGUCUCAUUAAGGCGACGUAAGGAAGAUGUUGCGCAACAACUCAUGAUUCUACUGAUCAUGAAAACGGUUGUUAACUCCCGCGGUGGACCCCCAGCUUUAGUCGGUGGACGCAUUAUUACGUAUCCCAGGACGUCAUGGACCUGGACGCACACGUAUUGGCUGCGCUCAGCACAGGGUCCCUUACCUGACAAAAUUAAAUGCUUUGGUGCCACAGGGAACUUGUUUGGCAUAGUGUCUAUCAAUAGCCGAAUCAUACCAACCAUGACGUUGAUCAAUACGCAGCUGUCAAGUUGUACCCAUUAUCCCCUGUAUUUAAAAGUCAUCACCGCUAGAAUUUCCUUUCAUGGCCAGAUUCCGUUAGGGUCCUUGUUUCCAUCCGCCUCCAAGCACCGUUGCAAUCAGAUCCAGCACCUUAGAACCUCUCUAUAUACAGGUGACACGAGAGCUGUGGAGUCCAAGCGGUUAUCGUUGCAUGUUCACGAAACGAAUUGUUUGGUGACGCACGAUGUUGAAACCACAAGAGCGAGAUCUAUUCGUGUGGCCUCACCUAUGCUUGGUUUGUGUCAUGCCGUCAAGACGCAGGAUAGGUUAACUUCACGCUUUGUGUUGGACCAGAUAUUCUACGUUACGGCUCCACCUCGCUUGAGUCACGUGAGUACGUGCCAGCGAAGAUUCGCGAAGAGUAAAACAAACCAAACGUCAAGCUGUCUUAUUUUAUGGACGGUAAGGGUUCUUGACCUGGGGCUCUUAAUAGACCUCAAGGAAAGGUUAACCUCCUCCGCACUUCUAACGCACCCGGCGUUGGCUUCUGUCACGCCCAGGUACCCUCGAACACCUUCGGCGGGUAUAGUUUUUGUGCACACCGCCGGUCCUAGAGUAAUGCUGGACAAGGACACACCACUCGGUACAAUCGGCGGGAAGCCAUCGCUAAGUCCUAUGUUUCCAAUCUUCGUCGCCCUCCAAGAAGAGACGGCCGUCUUGCGUACUGUAUGCGUAUUGAAUCGAUCACUUUCCUUCAAAGUCUGUCUAACUUUUAACGCACUCAAAAUAAUUAAGUUAGUCAGCGAAAGGUCCGGCGGUAAGCGUCGACCCAACUAUCAGAGAACGAGAGGUUCCGGAUACGCGUACUUCUUAGUACAUGACGCCCUCACGGGUGACUUACCGAACGUCGAUGGUUUUCCACACAGAUCGCCGCUGAGACUGGCGGCUACGCAGUGUGAAGGGGUUACAUGGUCCACUAAGUUUCAUAGGGGACCCUGUUAUUCGAAAUACAAAUCUUAUCGUCAGUAUGUCACGGGUCUAAAUAAAACCACGCGAGUGGCGUAUCUUGACUCGUGUACCGAAGUGGCACCUGAGACUGUCCAGAUUGUGCUGCUAGACCAUAUCAAUGUAAGACCAUACCAACAACAGAAGAAUACUUGCUAUCGGAUACCUCGUCGCCCACGGCUCGACCAAAUUCCGGGCAUUGAUAAAAAUACUGACUGGGAACAGUCGGCCAGCCGGGGUCCUCGGCUAGCAUGGAACCUUUCAGGUACUUACCUUUGGUAUACUGGCCGACAAAAUAGGUCCAUGACCGUUUUGGCCAUACUAAUAGAUCUCAGACCGGACCCUCUAAUUGCCUUAGGUUCUAGCGAGCCGCCAGAGGAUUGCAGGGCUUCUAGCUUUCGCGGCCGCGGGGACAUUGGGCUGCGUUCAUACGCGGCGCGGUCCGACAACCAGGGCUUGUUCUAUAAGGAGAACGGCACAUUAUACUCGUACACCAGCCCCCGUUUGCAUGGAGAAGGUGUUACUCUCGCAUUCGGAAUUCUCGUGGGCAUACGUCCCAUCAGAUCGGAUGAGUAUCAACGGGUAUCCCUCUUACCGCACCGCCAUUCAAGCUGGGAACGCCUCUCACCAGGCCGAGUAAGAUCCAGGGAGUGUGACCUGCUGUUACGAGGGAACUGGGGGAGAAAUGCAAGAGUGCGGAACAUAGAAAUGAGGGACCCGUCAAAGAGGUCGGGCGGAAUGACGGGUAGCCUACGGAGUGCUUGUUACCGAGCAGUUGCAGUUAGACUUGGUCGGGUGCAAAGUGUUACUCUGCCCUUAUUAACUUUUUCGGUAUACUCCGCCACUGCUGAUCCGAAUCCACGAACUAUUAUUAUCUACAGAUGUCAGGAUGUAAAUCGGUUUCGAGUUGGUGACGAUGUGCCGCAUCCGCUGUUAUGUGAGCCUGCUCCUGCCGACCAGAAGAGGGUGUGUAACGGGAUAAGUACAGCUGACCAGUUUGGUAUAGCCCCAGGAUUGGGGCUAAGGACCGUAUCAAUACACGAUGGAACCGAAAGGUGCGUGCUUCAUACUUUUACGGCUGGGGCCCGGUCAGCCCACUGGCGACCCCGUUUCUCUCGCACGUACGGAACCAGCUCCGUGCCACCGCAAGCGGUAAGUCCAGCGAGUAGACUUCCUCCGAUCUUUGUCCUUGAGCAAGGUGGGGCCUCCCUGCAUCACAAUGUACGCUGGGUGUCGGCCCCGGACGUCCCACUGGGGCUUAUCAUCAUAAGCUCCUUACAAUGUGCGUCGAUCGCUCCGUCCCCGCUUCACUCCACAUUAACCAUGCUUCAAACCGGACCACGCAUCAGUAAUUAUCAUAUAGAUGCUGGACCUACUAUGUGUCCGCUGAACAGCCUGCGACGUAGUGUCCCCAUGACAGGUAUCUACUUCCUCAGCAGUAUCAAUCAAUUAUUCACAACGCUAGUUGAGAUACAUCGCCAGACCAACCUCAUGUCAGAUAUGAGUGUCGAGAUUAAACUCGUAGGUACGCGGUUAGUUGACUAUCCGACGAGGUCUGCGUACUCAUCUAUUAAAACUAGGUUGGAAUUUAUGGUUAGUCGAUGCUACGGCCUUAGCCGCCUAGGCACGUUAAGCCCGGUGGCAAGCAGCGAGAUCUACAUAGUUUCUUGCUUCUUUGUUAUGGUUGCUAGAGCAAGAGCAAGGACGGCCCUAACGUUUAAAAAAAACAUGUUAGAAGAACGACUUGCUGGUUCACUCUACUCCUUGGACGGGUUGUCUAAAGCUGGCACCCAGUUCUCAACAGUCCGCAGGGAUGGGGAAAGCUGGAUCUGUGUACCCCCACUCAGGUGCUACGAGAAGAAAAAAGGAGCUCUACGAGCAGAUCGCAGGACGUCUCCUUUCCCCUCCGUGGCAAACUGUCGCCGGUUAUUGUACCCCAUUAUCGAGGUACCAGCAAGCACGAAAUUCCAAAAUACUGCUCAAGGGAAUUUCGUAAUGUCGAUAGGCCAGUAUGGGAGACUUUUUAUUAAUUUGAUGCGCCAUUUUCAUAAGACACACGGACGUACGUCCGUAUGCAGGUGGGACGGACGGGUAACUACAGUGCUACGCCUAAGUGCCCGAAUCGAAUCCCUAGAGAUACGUGUCCAUGGGGCCAAAACUCGGUUUCUCCACUUGUUAACCUCAAUUAUAAGAUGCGCACAAUUUGGGUAUGUGAGUGCGCUCCGAAACCAGAUAAUCUCGCUACUACUCUCCGGGACCUUCUGUCUUCAGAUGGAUUUAUGCUUGACUGCCCGGUCCGGCGGGGCACAUGCCGUAGUGGAAAUGCGGGUCCCCCGUAGCGUCGCACUGAUAGCUGGACUGUUCUGCCAACAUACGUUUAUCCCUAUGGAAAGUUGGGCGCCGCGUCGAGAGGUCAUCCUGUCCCGCGGCGAGGAUGGCUCGGCGUUUCAUUAUUUAGUCGGAAGUUACCACCAAAUGUCACUCUUGGCAACAUUUCUUACGGUUCUGUAUGCUCGACAAUGGUGCGAACCGCGCGAGUUUCUCUCACUGGCAGUUACUACCGGCAACAUACAUAGCGUGGCCUCAGUCGAAGUUCGCGAUACAGUUGACGAGUACCCUCUCUCCGAGGAUGAUUGGACAAAACAAGUUUUUUCUGAUGUCGCAACCCAUUAUCAACAACCACUCGCAAAUCGUCGCGGCAUAGGCGCUAUUACAGUAUAUAAGGAAGUAUGUCGCGGUCUGACGGACAAUACGCCGGCCAGGGACGGAGUUUUUCUCAAACGCAUCCUCCGGGAUUUGCGUGGAUCCCUAGUAGUACGAUUCCGGACUGUAAGGACAGUGGUUCCCAGGGUAAUUUCUAGUGGCGCGUACGGAAGGGAUGGCCUACACAGAGCAUUGGUCUUGACACCGUCCCGGCCACGCGAAUCGGUACGUAGUAGAUACCAGCAAACAUCAUUAAUUAUGCGAACCACGGGUGACUUUUUCACCGGCAAAACAAAGCAUCGGAUGUCUGUCUACUGGGGUGCCUGCGUGGUCAGAGCUACUCACCUUGCAUGGAACUACGGGUCGCAGACCACUCCUUUAUACGUCAUGGUGCAACUUGAGGCUGCGGGCGAACGUCUUGUAGUCUCACAAUGGUACGAAGGUUCAAAGAAUACGUGGUUGUUGUUACUGGAGGUAAGAAGCACUUUGUGCGCCGCGCGAGAAAGUGCCAACAUUUAG"))

#alternate solution using Bio-seq module

#from Bio.Seq import Seq
#from Bio.Alphabet import generic_rna
#file = open("rosalind_PROT.txt", "r")
#rna = Seq(file.read(),generic_rna)
#protein = rna.translate()
#print protein