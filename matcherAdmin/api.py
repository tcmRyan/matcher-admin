from flask_restful import Resource, reqparse, abort, fields, marshal_with 
from matcherAdmin import db, api
from matcherAdmin.models import User, Gamedata, Gametable

game_table_fields = {
    'id': fields.Integer,
    'author': fields.String,
    'table': fields.String,
    'seed': fields.String
}

game_row_fields = {
    'base': fields.String,
    'combination': fields.String,
    'result': fields.String,
}

game_data_fields = {'data': fields.List(fields.Nested(game_row_fields))}

parser = reqparse.RequestParser()
parser.add_argument('author', type=str, help='Creator of this game')

class Data(Resource):

    @marshal_with(game_data_fields)
    def get(self, table_id):
        table = Gametable.query.get(table_id)
        return table.data
        
class Table(Resource):

    @marshal_with(game_table_fields)
    def get(self):
        author = parser.parse_args().get('author')
        if author:
            return Gametable.query.filter(author=author).all()
        else:
            return Gametable.query.all()

api.add_resource(Data, '/gamedata/<table_id>')
api.add_resource(Table, '/gametables')

