from string import maketrans

rnatrans = maketrans('GCTA', 'CGAU')

def to_rna(dna_strand=""):
    if type(dna_strand) is not str:
        raise Exception('Not a string')
    else:
        return dna_strand.translate(rnatrans)

print (to_rna(1))
