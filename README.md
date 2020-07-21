In the home directory, run the following command to initate the server
python api.py

In another Command window, run the follwoing comments to get the Knowledge graphs.

#1: Get the gene list in one pathway(input KEGG id, eg: hsa04010)

curl http://localhost:5000/Pathway/<pathwayid>
(eg: http://localhost:5000/Pathway/hsa04010)

#2: List all the pathway ids and names.
curl http://localhost:5000/PathwayLists/  
