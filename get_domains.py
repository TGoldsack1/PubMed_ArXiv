import arxiv, re, json, logging, time, random, requests
from datetime import datetime
import xml.etree.ElementTree as ET


index = 22656 # set to 0 if starting from running over all instances

logging.basicConfig(
  filename="./logs/get_domains.log.{}".format(datetime.timestamp(datetime.now())), 
  level=logging.INFO,
  format = '%(asctime)s | %(levelname)s | %(message)s'
)

with open("arxiv_ids.txt", "r") as arxiv_ids_file:
  arxiv_ids = list(arxiv_ids_file.readlines())

pre = ""
pre_paper_ids = [x for x in arxiv_ids if re.sub("[0-9.]", "", x) == pre + "\n"]
print(len(pre_paper_ids))

if index > 0:
  with open("created_data/arxiv_train_dom_map_raw.json", "r") as arxiv_ids_file:
    id_to_dom = json.loads(arxiv_ids_file.read())
else:
  unique_doms = set([re.sub("[0-9.]", "", x) for x in arxiv_ids])
  id_to_dom = {}
  for prefix in unique_doms:
    pre = prefix.strip()
    dom_papers = [x for x in arxiv_ids if re.sub("[0-9.]", "", x) == prefix]
    for paper_id in dom_papers:
      if paper_id.strip():
        id_to_dom[paper_id.strip()] = pre.strip()

current_index = (int(index/1000)) * 1000

for i, paper_id in enumerate(pre_paper_ids[current_index:]):
  ind = i + current_index
  paper_id = paper_id.strip()
  logging.info(f'index={ind}, id={paper_id}')
  
  if i%1000 == 0:
    with open("created_data/arxiv_train_dom_map_raw.json", "w") as out_file:
      out_file.write(json.dumps(id_to_dom, indent=4))
  
  headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

  url = f"http://arXiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:{paper_id}&metadataPrefix=oai_dc"
  response = requests.get(url, headers=headers)

  if response:
    root = ET.fromstring(response.content)
    is_first = True
    for elem in root.iter('{http://purl.org/dc/elements/1.1/}subject'):
      if is_first:
        id_to_dom[paper_id] = elem.text
        is_first = False
