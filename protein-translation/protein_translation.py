def proteins(strand):
    polypeptides = []
    protein_codons = {
        'Methionine': ['AUG'],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"]
        }
    for pos in range(0, len(strand), 3):
        for protein, codons in protein_codons.items():
            for codon in codons:
                if strand[pos:pos+3] == codon and protein == "STOP":
                    return polypeptides
                elif strand[pos:pos+3] == codon and protein != "STOP":
                    polypeptides.append(protein)
    return polypeptides
