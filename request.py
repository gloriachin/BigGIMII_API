import requests

## 1: List all the pathway ids and names.
#r1 = requests.get('http://localhost:5000/PathwayLists/')
#print((r1.json()))

## 2: Query the gene list in one pathway(input KEGG id, eg: hsa04010)
#r2 = requests.get('http://localhost:5000/Pathway/hsa04010')
#print((r2.json()))

## 3 Query the target for one drug, return a json file of target genes for the queried drug
#r3 = requests.get('http://localhost:5000/Query_Targets_by_drug/Cetuximab')
#print((r4.json()))

## 4 Query the drugs for one target, return a json file of drugs genes for the queried target
#curl http://localhost:5000/Query_drugs_by_target/<Target>/
#r4 = requests.get('http://localhost:5000/Query_drugs_by_target/EGFR/')
#print((r4.json()))


## 5. Query the synthetic lethylity pairs according one gene mutation
#curl http://localhost:5000/Query_SL_by_mut/<mut_gene>/
r5 = requests.get('http://127.0.0.1:5000/Query_SL_by_mut/EGFR/')
print(r5.json())


## 6. Query the synthetic lethylity pairs according gene knockout effects 
#curl http://localhost:5000/Query_SL_by_ko/<ko_gene>/
#r6 = requests.get('http://127.0.0.1:5000/Query_SL_by_ko/TP53/')
#print(r6.json())