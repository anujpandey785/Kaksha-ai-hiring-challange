from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(80))
    rating = db.Column(db.String(80))
    details = db.Column(db.String(80))
    discount = db.Column(db.Float(precision=2))

    wishlist = db.relationship('WishListModel')


    def __init__(self, name,  item_id, category, rating, details, discount):
        self.name = name
        self.item_id = item_id
        self.category = category
        self.rating = rating
        self.details = details
        self.discount = discount

    def json(self):
        return {'name': self.name, 'category': self.category, 'rating': self.rating, 'details': self.details, 'discount': self.discount}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


