#### Before geting started, please install all packages from the requirementlist

### In the home directory, run the following command to initate the server
python api.py


## Ways to set up the queries:

#### In another Command window, run the follwoing comments to get the Knowledge graphs.

### Section 1: get the information of KEGG pathways

##### 1: List all the pathway ids and names.
curl http://localhost:5000/PathwayLists/  


##### 2: Query the gene list in one pathway(input KEGG id, eg: hsa04010)
curl http://localhost:5000/Pathway/<pathwayid>
(eg. http://localhost:5000/Pathway/hsa04010)


### Section 2: get the information from the DrugBank

##### 3 Query the target for one drug, return a json file of target genes for the queried drug
curl http://localhost:5000/Query_Targets_by_drug/<DrugName>
(eg. curl http://localhost:5000/Query_Targets_by_drug/Cetuximab)

##### 4 Query the drugs for one target, return a json file of drugs genes for the queried target
curl http://localhost:5000/Query_drugs_by_target/<Target>/
(eg. curl http://localhost:5000/Query_drugs_by_target/EGFR/)

##### 5 Query all FDA approved drugs, return a list of drugs
curl http://localhost:5000/list_FDA_Drugs/

##### 6 Query the KG from Drug-Target-action

##### Upcoming KGs

### Setion 3: SL pairs
##### 7. Query the synthetic lethylity pairs according to gene knockout effects 
#curl http://localhost:5000/Query_SL_by_ko/<ko_gene>/
(eg. curl http://localhost:5000/Query_SL_by_ko/EGFR/))

##### 8. Query the synthetic lethylity pairs according to gene mutations 
#curl http://localhost:5000/Query_SL_by_mut/<mut_gene>/
(eg. curl http://localhost:5000/Query_SL_by_mut/EGFR/)

##### Section 4: get the disease associated gene

##### Section 5: get the gene associated drug

##### Section 6: get the gene mutation associateed differential gene expression