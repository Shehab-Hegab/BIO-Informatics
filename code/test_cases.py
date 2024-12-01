from find_orfs import find_orfs, filter_orfs
from dot_plot import create_dotplot

# Testing ORF detection
dna_sequence = "ATGCGATAACTGAATGCGTTAATAG"
orfs = find_orfs(dna_sequence)
print("ORFs found:", orfs)

# Testing ORF filtering
filtered_orfs = filter_orfs(orfs, min_length=6)
print("Filtered ORFs:", filtered_orfs)

# Testing Dot Plot
sequence1 = "ATGCGA"
sequence2 = "ATGCTA"
create_dotplot(sequence1, sequence2)