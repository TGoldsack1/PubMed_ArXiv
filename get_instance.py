import json

#aid = "1103.6094"
# aid = "cond-mat9811411"
# aid = "hep-ph0411093"
aid = "1410.3417"

arxiv_filepath = "./arxiv-dataset/train.txt"
pubmed_filepath = "./pubmed-dataset/train.txt"

with open(arxiv_filepath, "r") as ds:
  for ind, line in enumerate(ds):
    line_dict  = json.loads(line)
    if line_dict['article_id'] == aid:
      for ab_sent in line_dict['abstract_text']:
        print(ab_sent)
      break