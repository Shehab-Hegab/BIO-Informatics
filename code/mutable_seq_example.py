from Bio.Seq import MutableSeq

mutable_seq = MutableSeq("ATGCGA")
mutable_seq[1] = "T"
print("Modified Sequence:", mutable_seq)