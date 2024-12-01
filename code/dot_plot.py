import matplotlib.pyplot as plt

def create_dotplot(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    dot_matrix = [[1 if seq1[i] == seq2[j] else 0 for j in range(len2)] for i in range(len1)]
    plt.imshow(dot_matrix, cmap="Greys", interpolation="nearest")
    plt.title("Dot Plot")
    plt.xlabel("Sequence 2")
    plt.ylabel("Sequence 1")
    plt.xticks(range(len2), seq2, fontsize=8)
    plt.yticks(range(len1), seq1, fontsize=8)
    plt.show()