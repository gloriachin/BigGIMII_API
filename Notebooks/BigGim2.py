import requests

import pandas as pd
def Query_fields_Mut_Freq_KP():
    Query_str = "https://biothings.ncats.io/tcga_mut_freq_kp/metadata/fields"
    response = requests.get(Query_str)
    result = response.json()
    return(result)

def format_result_Mut_Freq(result):
    subject_id = []
    subject_symbol = []
    subject_type = []

    object_id = []
    object_name = []
    object_type = []

    edge_context = []
    edge_label = []
    edge_confidence_freq_by_case = []
    edge_confidence_freq_by_sample = []
    
    for i in range(0,len(result['hits'])):
        #Edges 
        edge_label.append(result['hits'][i]['association']['edge_label'])
        edge_confidence_freq_by_case.append(result['hits'][i]['association']['freq_by_case'])
        edge_confidence_freq_by_sample.append(result['hits'][i]['association']['freq_by_sample'])
     
        #Subject
        subject_id.append(result['hits'][i]['subject']['id'])  
        subject_symbol.append(result['hits'][i]['subject']['SYMBOL'])
        subject_type.append(result['hits'][i]['subject']['type'])

        #Object
        object_id.append(result['hits'][i]['object']['id'])
        object_name.append(result['hits'][i]['object']['tcga_name'])
        object_type.append(result['hits'][i]['object']['type'])

    #Generating dataFrame for the results
    result_df = pd.DataFrame({
    "subject_id":subject_id,
    "subject_symbol": subject_symbol,
    "subject_type": subject_type,
        
    "object_id":object_id,
    "object_name":object_name,
    "object_type":object_type,
        
    "edge_label": edge_label,
    "edge_freq_by_case": edge_confidence_freq_by_case,
    "edge_freq_by_sample":edge_confidence_freq_by_sample})
    return(result_df)


def Query_Mut_Freq_KP(Query):
    Query_str = "https://biothings.ncats.io/tcga_mut_freq_kp/query?q="
    
    count = 0
    for i in Query:
        count = count + 1
        if count != len(Query):
            Query_str = Query_str + i + ":"+ Query[i] + "%20AND%20"
        else:
            Query_str = Query_str + i + ":"+ Query[i]+"&size=1000"
    print(Query_str)
    response = requests.get(Query_str)
    result = response.json()
    return(result)

import requests

import pandas as pd
def Query_fields_DrugResponse_KP():
    query_str = "https://biothings.ncats.io/drug_response_kp/metadata/fields"
    response = requests.get(query_str)
    result = response.json()
    return(result)

def format_result_DrugResponse_KP(result):
    subject_id = []
    subject_symbol = []
    subject_type = []

    object_id = []
    object_name = []
    object_type = []

    edge_context = []
    edge_label = []
    edge_effect_size = []
    edge_ic50s_mut = []
    edge_ic50s_wt = []
    edge_median_ic50_mut = []
    edge_median_ic50_wt = []
    edge_provided_by = []
    edge_prevenence_publications = []
    edge_confidence_p = []
    edge_confidence_sample_size = []
    edge_confidence_mut_size = []
    edge_confidence_wt_size = []
    
    for i in range(0,len(result['hits'])):
        #Edges and context
        edge_context.append(result['hits'][i]['association']['context']['disease']['mondo'])
        edge_label.append(result['hits'][i]['association']['edge_label'])
        edge_effect_size.append(result['hits'][i]['association']['effect_size'])
        edge_ic50s_mut.append(result['hits'][i]['association']['ic50s_mut'])
        edge_ic50s_wt.append(result['hits'][i]['association']['ic50s_wt'])
        edge_median_ic50_mut.append(result['hits'][i]['association']['median_ic50_mut'])
        edge_median_ic50_wt.append(result['hits'][i]['association']['median_ic50_wt'])
        edge_provided_by.append(result['hits'][i]['association']['provided_by'])
        edge_prevenence_publications.append(result['hits'][i]['association']['publications'])
        edge_confidence_p.append(result['hits'][i]['association']['pvalue'])
        edge_confidence_sample_size.append(result['hits'][i]['association']['sample_size'])
        edge_confidence_mut_size.append(result['hits'][i]['association']['size_mut'])
        edge_confidence_wt_size.append(result['hits'][i]['association']['size_wt'])

        #Subject
        if 'NCBIGene' in result['hits'][i]['subject']:
            subject_id.append(result['hits'][i]['subject']['NCBIGene'])
        else:
            subject_id.append("")
            
        subject_symbol.append(result['hits'][i]['subject']['SYMBOL'])
        subject_type.append(result['hits'][i]['subject']['type'])

        #Object
        object_id.append(result['hits'][i]['object']['id'])
        object_name.append(result['hits'][i]['object']['name'])
        object_type.append(result['hits'][i]['object']['type'])

    #Generating dataFrame for the results
    result_df = pd.DataFrame({
    "subject_id":subject_id,
    "subject_symbol": subject_symbol,
    "subject_type": subject_type,
    "object_id":object_id,
    "object_name":object_name,
    "object_type":object_type,
    "edge_label": edge_label,
    "edge_context_disease": edge_context,
    "edge_confidence_p":edge_confidence_p,
    "edge_effect_size":edge_effect_size,
    "edge_median_ic50_wt":edge_median_ic50_wt,
    "edge_median_ic50_mut":edge_median_ic50_mut,
    "edge_confidence_sample_size":edge_confidence_sample_size,
    "edge_confidence_mut_size":edge_confidence_mut_size,
    "edge_confidence_wt_size":edge_confidence_wt_size})
    return(result_df)


def Query_DrugResponse_KP(Query):
    Query_str = "https://biothings.ncats.io/drug_response_kp/query?q="
    
    count = 0
    for i in Query:
        count = count + 1
        if count != len(Query):
            Query_str = Query_str + i + ":"+ Query[i] + "%20AND%20"
        else:
            Query_str = Query_str + i + ":"+ Query[i]+"&size=1000" ## Question: if I set the size to a large number, it will not return any results.
    print(Query_str)
    response = requests.get(Query_str)
    result = response.json()
    return(result)