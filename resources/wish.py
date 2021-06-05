from flask_restful import Resource,reqparse
from models.wish import WishListModel

class Wish(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('item_id',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        ) 


    def get(self,user_id):
        wish = WishListModel.find_by_user_id(user_id)
        if wish:
            return wish.json()
        return {'message': 'Wishlist not found'}, 404

    def post(self, user_id):

        data = Wish.parser.parse_args()

        wishlist= WishListModel(user_id,**data)
        try:
            wishlist.save_to_db()
        except:
            return {"message": "An error occurred creating the wishlist."}, 500

        return wishlist.json(), 201

    def delete(self, user_id):
        wishlist = WishListModel.find_by_user_id(user_id)
        if wishlist:
            wishlist.delete_from_db()

        return {'message': 'wishlist deleted'}



class WishList(Resource):
    def get(self):
        return {'Wishlist': list(map(lambda x: x.json(), WishListModel.query.all()))}

