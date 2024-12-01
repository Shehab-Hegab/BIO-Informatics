def find_orfs(dna_sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    for i in range(len(dna_sequence) - 2):
        codon = dna_sequence[i:i+3]
        if codon == start_codon:
            for j in range(i + 3, len(dna_sequence) - 2, 3):
                stop_codon = dna_sequence[j:j+3]
                if stop_codon in stop_codons:
                    orfs.append((i, j + 3))
                    break
    return orfs

def filter_orfs(orfs, min_length):
    return [orf for orf in orfs if orf[1] - orf[0] >= min_length]