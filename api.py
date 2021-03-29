from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import sys
sys.path.append('./src/')
import Pathway_Gene
import Drugbank
import Synthtic_lethylity
import AML_KG

app = Flask(__name__)
api = Api(app)

##https://github.com/NCATS-Tangerine/kgx/blob/master/data-preparation.md #Formating
parser = reqparse.RequestParser()

##Section 1: Parse KEGG pathways
def abort_if_pathway_doesnt_exist(pathway_id):
    if len(Pathway_Gene.GetPathways([pathway_id]))==0:
        abort(404, message="pathway_id {} doesn't exist".format(pathway_id))

class PathwayLists(Resource):
    def get(self,):
        result = Pathway_Gene.ListPathways(KEGG=True)
        
        return(result)


class Pathway(Resource):
    def get(self, Pathway_id):
        abort_if_pathway_doesnt_exist(Pathway_id)
        result = {Pathway_id: Pathway_Gene.GetKEGGgenes([Pathway_id])}
        return(result)


## Section 2: Parse Drug and Target from Drugbank

def abort_if_Drugname_doesnt_exist(drug_name): #This function needs revision
    if len(Drugbank.get_drugs_by_target(drug_name)[drug_name])==0:
        abort(404, message="drug {} doesn't exist in Drugbank v5.16".format(drug_name))

def abort_if_Target_doesnt_exist(Target): #This function needs revison
    if len(Drugbank.get_Targets_by_drug(Target)[Target])==0:
        abort(404, message="target {} doesn't exist in Drugbank v5.16".format(Target))


class Query_Targets_by_drug(Resource):
    def get(self, drug_name):
        #abort_if_Drugname_doesnt_exist(drug_name) ##
        result = Drugbank.get_Targets_by_drug(drug_name)
        #result = {drug_name: Drugbank.get_Targets_by_drug(drug_name)}
        return(result)

class Query_drugs_by_target(Resource):
    def get(self, Target):
        #abort_if_Target_doesnt_exist(Target)
        result = Drugbank.get_drugs_by_target(Target)
        #result = {Target: Drugbank.get_drugs_by_target(Target)}
        return(result)

class list_FDA_Drugs(Resource):
    def get(self,):
        result = Drugbank.list_approved_drugs()
        result = list(set(result['Drug']))
        return(result)


## Section 3: Parse gene mutation dependent gene effects

def abort_if_mut_doesnt_exist(mut_gene):
    if len(Synthtic_lethylity.select_SL_by_mutation([mut_gene]))==0:
        abort(404, message="gene {} is not in the driver gene list".format(mut_gene))

def abort_if_ko_doesnt_exist(ko_gene):
    if len(Synthtic_lethylity.select_SL_by_ko([ko_gene]))==0:
        abort(404, message="gene {} is not in the knockout gene list".format(ko_gene))


class Query_SL_by_mutation(Resource):
    def get(self, mut_gene):
        abort_if_mut_doesnt_exist(mut_gene)
        result = Synthtic_lethylity.select_SL_by_mutation([mut_gene])
        return(result)

class Query_SL_by_ko(Resource):
    def get(self, ko_gene):
        abort_if_mut_doesnt_exist(ko_gene)
        result = Synthtic_lethylity.select_SL_by_ko([ko_gene])
        return(result)

class Query_co_exp_inGroup(Resource):
    def get(self, gene_list):
        result = AML_KG.Fun_select_co_exp_inGroup(gene_list)
        return(result)
## Actually setup the Api resource routing here
##

api.add_resource(PathwayLists, '/PathwayLists/')
api.add_resource(Pathway, '/Pathway/<Pathway_id>/')

api.add_resource(list_FDA_Drugs, '/list_FDA_Drugs/')
api.add_resource(Query_Targets_by_drug, '/Query_Targets_by_drug/<drug_name>/')
api.add_resource(Query_drugs_by_target, '/Query_drugs_by_target/<Target>/')

api.add_resource(Query_SL_by_mutation, '/Query_SL_by_mut/<mut_gene>/')
api.add_resource(Query_SL_by_ko, '/Query_SL_by_ko/<ko_gene>/')

api.add_resource(Query_co_exp_inGroup,'/Query_co_exp_inGroup/<gene_list>')

if __name__ == '__main__':
    app.run(debug=True)