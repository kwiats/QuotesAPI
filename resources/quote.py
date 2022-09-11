from ast import parse
from flask_restful import Resource, reqparse
from flask import render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt


from models.quote import QuoteModel


class Quote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quote', type=str, required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('origin', type=str, required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('authorId', type=int, required=True,
                        help="This field cannot be left blank.")
    def get(self, id_quote):
        quote = QuoteModel.find_by_id(id_quote)
        if quote:
            return quote.json()
        return {'message': 'Quote not found.'}, 404

    def post(self, id_quote):
        if QuoteModel.find_by_id(id_quote):
            return {'message': "An quote with id '{}' already exists.".format(id_quote)}, 400

        data = Quote.parser.parse_args()

        quote = QuoteModel(
            id_quote, data['quote'], data['origin'], data['authorId'])
        try:
            quote.save_to_db()
        except:
            return {'message': 'An error occurred inserting the quote'}, 500

        return quote.json(), 201

    @jwt_required()
    def delete(self, id_quote):
        claims = get_jwt()
        if not claims['is_admin']:
            return {'message':'You need admin permissions.'}, 401
            
        quote = QuoteModel.find_by_id(id_quote)
        if quote:
            quote.delete_from_db()
 
        return {'message': 'Quote ID:{} has been deleted.'.format(id_quote)}, 404

    @jwt_required()
    def put(self, id_quote):
        data = Quote.parser.parse_args()

        quote = QuoteModel.find_by_id(id_quote)

        if quote is None:
            quote = QuoteModel(id_quote, data['quote'], data['origin'], data['authorId'])
        else:
            quote.quote = data['quote']
            quote.origin = data['origin']
            quote.authorId = data['authorId']

        quote.save_to_db()
        return quote.json()
            

class QuoteList(Resource):

    def get(self):
        return {'quotes': [quote.json() for quote in QuoteModel.find_all()]}
