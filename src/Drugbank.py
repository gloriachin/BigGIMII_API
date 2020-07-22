import pandas as pd
import json

def Read_DrugBank():
    File = open("./Datasets/DrugBank/drug_all_result.csv",'r') ##Drugbank version 5.16
    
    Drug_list = []
    Action_list = []
    Stage_list = []
    Target_list = []

    for line in File.readlines():
        words = line.strip('\n').split("::")
        Drug = words[0]
        Action = words[1]
        Stage = words[2]
        Target = words[3]

        Drug_list.append(Drug)
        Action_list.append(Action)
        Stage_list.append(Stage)
        Target_list.append(Target)
    
    result_df = pd.DataFrame({"Drug": Drug_list,
                              "Action": Action_list,
                              "Stage": Stage_list,
                              "Target": Target_list 
                                })
    return(result_df)

def get_Targets_by_drug(drug_name):
    data = Read_DrugBank()
    result_json = {}
    if drug_name  in set(data['Drug']):
        result = list(data.loc[data['Drug'].isin([drug_name])]['Target'].values)
    else:
        result = []
    result_json = {drug_name: result}
    return(result_json)

def get_drugs_by_target(Target_gene):
    data = Read_DrugBank()
    result_json = {}
    if Target_gene in set(data['Target']):
        result = list(data.loc[data['Target'].isin([Target_gene])]['Drug'].values)
    else:
        result = []
    result_json = {Target_gene: result}
    return(result_json)

def list_targets():
    data = Read_DrugBank()
    Targets =list(set(data['Target'])) 
    return(Targets)

def list_approved_drugs():
    data = Read_DrugBank()
    data_approved = data.loc[data['Stage'] == 'approved']
    return(data_approved)

def list_all_drug():
    data = Read_DrugBank()
    Drugs =list(set( data['Drug'])) 
    return(Drugs)


