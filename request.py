import requests

## 1: List all the pathway ids and names.
r1 = requests.get('http://localhost:5000/PathwayLists/')
#print((r1.json()))

## 2: Query the gene list in one pathway(input KEGG id, eg: hsa04010)
r2 = requests.get('http://localhost:5000/Pathway/hsa04010')
#print((r2.json()))


## 3 Query the target for one drug, return a json file of target genes for the queried drug
r3 = requests.get('http://localhost:5000/Query_Targets_by_drug/Cetuximab')
#print((r4.json()))

## 4 Query the drugs for one target, return a json file of drugs genes for the queried target
#curl http://localhost:5000/Query_drugs_by_target/<Target>/
r4 = requests.get('http://localhost:5000/Query_drugs_by_target/EGFR/')
#print((r5.json()))

