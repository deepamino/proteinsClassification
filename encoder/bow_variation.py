import numpy as np

class BOWVariation:

    aminoacids = 'ACDEFGHIKLMNPQRSTVWYXBJU'
    dict_amino = {amino: idx for idx, amino in enumerate(aminoacids)}

    def get_vector_byMaxN(self, seq, alpha,n):
        v = np.zeros(len(self.aminoacids)) 
        for i in range(len(seq)):
            pos = self.dict_amino[seq[i]]
            v[pos] += 1 * alpha(i, n)
        return v
    
    def get_vector_bySeqN(self, seq, alpha):
        n = len(seq)
        v = np.zeros(len(self.aminoacids)) 
        for i in range(len(seq)):
            pos = self.dict_amino[seq[i]]
            v[pos] += 1 * alpha(i, n)
        return v
