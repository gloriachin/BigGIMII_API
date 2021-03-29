#### AML_KG

import pandas as pd
import json

def Fun_read_Ensemble_symbol_annotation():
    data = pd.read_csv('./Datasets/AML/EnsemblId_sybol/Ensemble_symbol_annotation.csv', index_col= "Unnamed: 0")
    data.columns = ['Ensemble_id','symbol'] 
    return(data)

def Fun_dic_ensemble_symbol():
    data = Fun_read_Ensemble_symbol_annotation()
    dic_ensemble_symbol = {}
    dic_symbol_ensemble = {}

    Ensemble_list = data['Ensemble_id'].values
    symbol_list = data['symbol'].values

    for i in range(0,len(Ensemble_list)):
        ensemble_id = Ensemble_list[i]
        symbol = symbol_list[i]

        if ensemble_id not in dic_ensemble_symbol:
            dic_ensemble_symbol[ensemble_id] = symbol

        if symbol not in dic_symbol_ensemble:
            dic_symbol_ensemble[symbol] = ensemble_id

    return (dic_ensemble_symbol, dic_symbol_ensemble)

    
def Fun_read_co_exp():
    data = pd.read_csv('./Datasets/AML/co_exp/co_expression_beatAML_RPMK.csv')
    #data = pd.read_csv('./Datasets/AML/co_exp/test.csv')
    return(data)

def Fun_Double_node_check(graph, node_list):
    sele1 = graph.loc[graph['Node_1'].isin(node_list)]
    sele2 = sele1.loc[sele1['Node_2'].isin(node_list)]
    return(sele2)

def Fun_single_node_check(graph, node_list):
    sele1 = graph.loc[graph['Node_1'].isin(node_list)]
    sele2 = graph.loc[graph['Node_2'].isin(node_list)]
    result = pd.concat([sele1,sele2])
    result = result.drop_duplicates()
    return(result)

def Fun_format_graph(graph, dic_ensemble_symbol):
    Node1_list = graph['Node_1'].values
    Node2_list = graph['Node_2'].values

    Node1_attr = []
    for i in Node1_list:
        if i in dic_ensemble_symbol:
            Node1_attr.append(dic_ensemble_symbol[i])
        else:
            Node1_attr.append('NA')
    Node2_attr = []
    for i in Node2_list:
        if i in dic_ensemble_symbol:
            Node2_attr.append(dic_ensemble_symbol[i])
        else:
            Node2_attr.append('NA')
    graph['Node1_attr'] = Node1_attr
    graph['Node2_attr'] = Node2_attr
    return(graph)

def Fun_select_co_exp_inGroup(Gene_list):
    #Check which of the genes in the Gene_list are co-expresssed with each other
    data = Fun_read_co_exp()
    dic_ensemble_symbol, dic_symbol_ensemble = Fun_dic_ensemble_symbol()
    Gene_list_format = []
    for gene in Gene_list:
        if gene in dic_ensemble_symbol:
            Gene_list_format.append(gene)
        elif gene in dic_symbol_ensemble:
            Gene_list_format.append(dic_symbol_ensemble[gene])
    
    result = Fun_Double_node_check(data,Gene_list_format)
    result = Fun_format_graph(result, dic_ensemble_symbol)
    result = result.to_json(orient='records', lines=True)
    return(result)

def Fun_select_co_exp_expandGroup(Gene_list):
    #Check which of the genes in the Gene_list are co-expresssed with each other
    data = Fun_read_co_exp()
    dic_ensemble_symbol, dic_symbol_ensemble = Fun_dic_ensemble_symbol()
    Gene_list_format = []
    for gene in Gene_list:
        if gene in dic_ensemble_symbol:
            Gene_list_format.append(gene)
        elif gene in dic_symbol_ensemble:
            Gene_list_format.append(dic_symbol_ensemble[gene])
    result = Fun_single_node_check(data,Gene_list_format)
    result = Fun_format_graph(result, dic_ensemble_symbol)
    result.sort_values(by = ['rho'])
    result = result.to_json(orient='records', lines=True)
    return(result)
