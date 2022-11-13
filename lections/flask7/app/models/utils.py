from app import db

class ModelMixin(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
