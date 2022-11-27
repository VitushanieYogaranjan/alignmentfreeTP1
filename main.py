from loading import load_directory
from kmers import stream_kmers, hash_sketch, kmer2str

def list_file(sequences, taille_sketch, k):
    genome = []

    # Fusionner les séquences
    for seq in sequences:
        genome+=seq
        
    lst = hash_sketch(genome, taille_sketch, k)

    return lst

def intersect_sorted_lists(lst1, lst2):
    idx1 = idx2 = 0
    # Dataset specific or intersection kmer counts
    A = inter = B = 0

    while (idx1 < len(lst1) and idx2 < len(lst2)):
        kmer1 = lst1[idx1]
        kmer2 = lst2[idx2]

        # Same kmer => intersection
        if kmer1 == kmer2:
            inter += 1
            idx1 += 1
            idx2 += 1
        # first list specific
        elif kmer1 < kmer2:
            A += 1
            idx1 += 1
        # second list specific
        else:
            B += 1
            idx2 += 1

    # Add remaining kmers of the non empty list
    A += len(lst1) - idx1
    B += len(lst2) - idx2

    return A, inter, B

def similarity(A, inter, B):
    # +1 added for pseudocount. Avoid divisions by 0
    A_similarity = inter / (inter + A)
    B_similarity = inter / (inter + B)

    return A_similarity, B_similarity


def jaccard(A, inter, B):
    return inter / (A + inter + B)

if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("data")
    k = 21

    # Loading
    lists = {f:list_file(files[f], 100, k) for f in files}

    filenames = list(files.keys())

    for i in range(len(files)):
                    for j in range(i+1, len(files)):
                        
                        A, inter, B = intersect_sorted_lists(lists[filenames[i]], lists[filenames[j]])
                        print("nombre de kmers :",A, inter, B)
                        print(filenames[i], filenames[j], jaccard(A, inter, B), similarity(A, inter, B))
                        print("")
