
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(text, k):

    encode = {"A":0, "C":1, "T":2, "G":3}
    list_kmer = []
    kmer = 0

    #lecture du premier kmer
    for i in range(k-1):
        kmer = kmer<<2
        kmer += encode[text[i]]

    mask = (1<<((k-1)*2))-1
    #lecture des kmers suivants
    for nucl in text[k-1:]:
        kmer = kmer&mask
        kmer = kmer<<2
        kmer += encode[nucl]
        list_kmer.append(kmer)

    return list_kmer

#print(stream_kmers("TGTA", 3))
