from datacollector import DataCollector
from Bio import Entrez, SeqIO

class ApiDataCollector(DataCollector):

    def __init__(self):
        self.email = 'susana.suarez102@alu.ulpgc.es'
        self.type = 'protein'

    def collect(self, *args):
        Entrez.email = self.email
        mrna_ids = self.search_mrna("Homo sapiens[ORGN] AND NM_", retmax=10)
        sequences = self.fetch_sequences(mrna_ids)

        for seq_record in sequences:
            yield(seq_record.id, seq_record.seq)
    
    def fetch_sequences(self, id_list):
        ids = ",".join(id_list)
        handle = Entrez.efetch(db=self.type, id=ids, rettype="fasta", retmode="text")
        
        sequences = list(SeqIO.parse(handle, "fasta"))
        handle.close()
        
        return sequences

    def search_mrna(self, term, retmax=10):
        handle = Entrez.esearch(db=self.type, term=term, retmax=retmax)
        record = Entrez.read(handle)
        handle.close()
        
        id_list = record["IdList"]
        print(f"Encontrados {len(id_list)} resultados.")
        return id_list
