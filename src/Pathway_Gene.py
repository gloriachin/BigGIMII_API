import pandas as pd
from google.cloud import bigquery
import json


client = bigquery.Client.from_service_account_json('./cre/c.json')# This is the credential file which allows users to get access to BigQuery tables. User's private key that is associated to the user's service account for security purposes.

def GetKEGGgenes(Pathway_userDefine):

    count_unique = """
    SELECT GENE 
    FROM `isb-cgc-04-0002.Pathways.KEGG_PATHWAY_GENES`
    WHERE PATHWAY in UNNEST(@PATHWAY)
    """

    if len(Pathway_userDefine) != 0:
        job_config = bigquery.QueryJobConfig()
        query_params = [
        bigquery.ArrayQueryParameter('PATHWAY', 'STRING', Pathway_userDefine)                             
        ]
        job_config.query_parameters = query_params
        query_job = client.query(count_unique, job_config=job_config) # API request - starts the query
        gene_list_dataframe = query_job.result().to_dataframe()
        gene_list = list(set(list(gene_list_dataframe['GENE'].values)))
    else:
        gene_list = []

    return(gene_list)

def GetPathways(Pathway_userDefine):
    count_unique = """
    SELECT Pathway_id 
    FROM `isb-cgc-04-0002.Pathways.KEGG_pathway_list`
    where  Pathway_id in UNNEST(@Pathway_id)
    """
    if len(Pathway_userDefine) != 0:
        job_config = bigquery.QueryJobConfig()
        query_params = [
        bigquery.ArrayQueryParameter('Pathway_id', 'STRING', Pathway_userDefine)                             
        ]
        job_config.query_parameters = query_params
        query_job = client.query(count_unique, job_config=job_config) # API request - starts the query
        pathway_list = query_job.result().to_dataframe()
        pathway_list = list(set(list(pathway_list['Pathway_id'].values)))
    else:
        pathway_list = []
    return(pathway_list)


def ListPathways(KEGG = True):
    count_unique = """
    SELECT Pathway_id, Pathway_Name
    FROM `isb-cgc-04-0002.Pathways.KEGG_pathway_list`
    """
    if KEGG == True :
        job_config = bigquery.QueryJobConfig()
        query_job = client.query(count_unique, job_config=job_config) # API request - starts the query
        result = query_job.result().to_dataframe()
        result = result.loc[:,['Pathway_id','Pathway_Name']]
        dic_pathway_name = {}
        for ids in list(result['Pathway_id'].values):
            dic_pathway_name[ids] = (result.loc[result['Pathway_id'] == ids]['Pathway_Name'].values[0])

    return(dic_pathway_name)
