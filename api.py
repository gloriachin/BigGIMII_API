from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import sys
sys.path.append('./src/')
import Pathway_Gene

app = Flask(__name__)
api = Api(app)


def abort_if_pathway_doesnt_exist(pathway_id):
    if len(Pathway_Gene.GetPathways([pathway_id]))==0:
        abort(404, message="pathway_id {} doesn't exist".format(pathway_id))

parser = reqparse.RequestParser()


class PathwayLists(Resource):
    def get(self,):
        result = Pathway_Gene.ListPathways(KEGG=True)
        
        return(result)


class Pathway(Resource):
    def get(self, Pathway_id):
        abort_if_pathway_doesnt_exist(Pathway_id)
        result = {Pathway_id: Pathway_Gene.GetKEGGgenes([Pathway_id])}
        return(result)

## Actually setup the Api resource routing here
##

api.add_resource(PathwayLists, '/PathwayLists/')
api.add_resource(Pathway, '/Pathway/<Pathway_id>')


if __name__ == '__main__':
    app.run(debug=True)