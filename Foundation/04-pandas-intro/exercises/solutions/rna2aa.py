def translate(rna):
    return  "".join([codon_table[rna[ i:i + 3]] for i in range(0,len(rna),3 )])