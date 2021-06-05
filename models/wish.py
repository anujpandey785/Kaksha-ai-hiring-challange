from db import db

class WishListModel(db.Model):
    __tablename__ = 'wishlist'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('UserModel')

    item_id= db.Column(db.Integer, db.ForeignKey('items.item_id'))
    items = db.relationship('ItemModel')
    date = db.Column(db.String(80))
    w_id = db.Column(db.Integer, primary_key=True)

   
    
    def __init__(self, user_id,item_id,date):
        self.user_id = user_id
        self.item_id = item_id
        self.date = date

    def json(self):
        return {'date': self.date, 'user_id': self.user_id, 'items': self.items.json()}

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
