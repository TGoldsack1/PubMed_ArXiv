import json

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

def process_dataset(in_path, out_path):
  sims = {}

  with open(in_path, "r") as ds:
    with open(out_path, "w") as out_f:
      for ind, line in enumerate(ds):
        line_dict = json.loads(line)
        out_f.write(line_dict['article_id'] + "\n")

process_dataset(arxiv_filepath, f"arxiv_ids.txt")

process_dataset(pubmed_filepath, f"pubmed_ids.txt")