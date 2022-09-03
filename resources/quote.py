from flask_restful import Resource, reqparse

from models.quote import QuoteModel


class Quote(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quote', type=str, required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('author', type=str, required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('origin', type=str, required=True,
                        help="This field cannot be left blank.")

    def get(self, id_quote):
        quote = QuoteModel.find_by_id(id_quote)
        if quote:
            return quote.json()
        return {'message': 'Quote not found.'}, 404

    def post(self, id_quote):
        if QuoteModel.find_by_id(id_quote):
            return {'message': "An author with id '{}' already exists.".format(id_quote)}, 400

        data = Quote.parser.parse_args()

        quote = QuoteModel(
            id_quote, data['quote'], data['author'], data['origin'])
        try:
            quote.save_to_db()
        except:
            return {'message': 'An error occurred inserting the quote'}, 500

        return quote.json(), 201

    def delete(self):
        pass


class QuoteList(Resource):
    def get(self):
        return {'quotes': list(map(lambda quote: quote.json(), QuoteModel.query.all()))}
