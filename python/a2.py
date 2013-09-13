def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)	

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2)!=-1

def is_valid_sequence(dna):
    """(str) -> bool

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGX')
    False

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    """
    for c in dna:
		if c not in 'ACGT':
			return False 
    return True 

def insert_sequence(dna1,dna2,index):
    """(str, str, int) -> str
    >>> insert_sequence('CCGG', 'AT',2)
    'CCATGG'
    """
    return dna1[:index]+dna2+dna1[index:]

def get_complement(dna):
    """(str) -> stri
    >>> get_complement('AG') 
    'TC'
    """
    data={'A':'T','C':'G','T':'A','G':'C'}
    res=''
    for c in dna:
		res=res+data[c]
    return res

def get_complementary_sequence(dna):
    """(str) -> stri
    >>> get_complementary_sequence('AG') 
    'TC'
    """
    data={'A':'T','C':'G','T':'A','G':'C'}
    res=''
    for c in dna:
        res=res+data[c]
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
