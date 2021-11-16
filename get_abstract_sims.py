import logging, json, sys
from datetime import datetime

from numpy.random import default_rng

sys.path.insert(0, '/home/tomasg/Code/PhD/data')
from utils.similarities import get_sentence_embeddings, get_similarities, print_to_file


logging.basicConfig(
  filename="./logs/get_sims.log.{}".format(datetime.timestamp(datetime.now())), 
  level=logging.INFO,
  format = '%(asctime)s | %(levelname)s | %(message)s'
)

arxiv_filepath = "./arxiv-dataset/train.txt"
pubmed_filepath = "./pubmed-dataset/train.txt"

'''
{ 
  'article_id': str,
  'abstract_text': List[str],
  'article_text': List[str],
  'section_names': List[str],
  'sections': List[List[str]]
}
'''

## SELECT 10000 SAMPLES
rng = default_rng(123)
n = 100


def process_dataset(in_path, out_path):
  sims = {}

  with open(in_path, "r") as ds:
    sample_indexes = list(rng.choice(sum(1 for line in ds), size=n, replace=False))

  with open(in_path, "r") as ds:
    # get random samples 
    print(len(sample_indexes))

    for ind, line in enumerate(ds):
      if ind in sample_indexes:
        print("match")
        inst = json.loads(line)
        logging.info(f'index={ind}, id={inst["article_id"]}')
        abstract_embs = get_sentence_embeddings(inst["abstract_text"])
        section_embs = [get_sentence_embeddings(sec) for sec in inst["sections"]]

        sims[inst['article_id']] = get_similarities(
          inst["section_names"], 
          inst["abstract_text"], 
          inst["sections"], 
          abstract_embs,
          section_embs
        )
        
        print_to_file(out_path, sims)

# logging.info(f'Processing ArXiv')
# process_dataset(arxiv_filepath, f"arxiv_sims_{n}.json")

logging.info(f'Processing PubMed')
process_dataset(pubmed_filepath, f"pubmed_sims_{n}.json")