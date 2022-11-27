import heapq
import string

def xorshift64(x):
    x ^= x << 13
    x ^= x >> 7
    x ^= x << 17
    return x

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
    alphabet = list(string.ascii_uppercase)
    for i in alphabet:
        if i not in ["A","T","C","G"]:
            encode[i]=0


    #list_kmer = []
    kmer = 0
    rkmer = 0

    #lecture du premier kmer
    for i in range(k-1):

        #fwd
        kmer = kmer<<2
        kmer += encode[text[i]]

        #reverse
        rkmer >>= 2
        rev_letter_value = (encode[text[i]] + 2) & 0b11
        rkmer += rev_letter_value << (2 * (k - 1))

    #lecture des kmers suivants
    mask = (1<<((k-1)*2))-1
    for nucl in text[k-1:]:
        kmer = kmer<<2
        kmer += encode[nucl]
        kmer = kmer&mask
        
        #reverse
        rkmer >>= 2
        rev_letter_value = (encode[text[i]] + 2) & 0b11
        rkmer += rev_letter_value << (2 * (k - 1))

        yield kmer, rkmer


def hash_sketch(genome, taille_sketch, k): 

    s = taille_sketch
    L = []

    for km, rkm in stream_kmers(genome, k):
        km = xorshift64(km)
        rkm = xorshift64(rkm)
        kmer=min(km, rkm)
    
        if len(L)<s:
            L.append(-kmer)

        elif len(L) == s:
            heapq.heapify(L)

        else:
            Max = heapq.minheap(L)
            if kmer < -Max:
                heapq.heappop(L)
                heapq.heappush(L, -kmer)

    List = [-x for x in L]     
    List.sort()
    return List



##méthode avec les casiers





