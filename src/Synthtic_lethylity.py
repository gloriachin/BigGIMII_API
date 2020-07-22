import pandas as pd
import json

def Read_mutation_dependent_SL():
    data = pd.read_csv('./Datasets/SL/driver_gene_SL.csv')
    mut_list = []
    for gene in list(data['Gene_mut'].values):
        mut_list.append(gene.split("_")[0])
    data['Mut'] = mut_list
    data = data.loc[:,["Mut", "Gene_ko", "p", "Effect Size", "FDR"]]
    return(data)

def select_SL_by_mutation(mut_gene_lsit):
    data = Read_mutation_dependent_SL()
    result = data.loc[data['Mut'].isin(mut_gene_lsit)]
    result = result.sort_values(by = ['p'])
    
    result = result.to_json(orient='records', lines=True)
    return(result)

def select_SL_by_ko(ko_gene_lsit):
    data = Read_mutation_dependent_SL()
    result = data.loc[data['Gene_ko'].isin(ko_gene_lsit)]
    result = result.sort_values(by = ['p'])
    
    result = result.to_json(orient='records', lines=True)
    return(result)

