from marshmallow import fields, Schema
from datetime import datetime
from ..database.base import Base, session_factory
from sqlalchemy import Column, Integer, String


class ExampleModel(Base):
    """
    Model
    """
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    contents = Column(String(30))
    created_at = Column(String(30))
    modified_at = Column(String(30))

    def __init__(self, data):
        super(ExampleModel, self).__init__()
        if data is not None:
            self.id = data.get('id')
            self.title = data.get('title')
            self.contents = data.get('contents')
            self.created_at = str(data.get('created_at')) if data.get(
                'created_at') is not None else str(datetime.utcnow())
            self.modified_at = str(datetime.utcnow())

    def __repr__(self):
        return "<Model(title='%s', contents='%s', created_at='%s', modified_at='%s')>" % (
            self.title, self.contents, self.created_at, self.modified_at)


class ModelSchema(Schema):
    """
    Model Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    contents = fields.Str(required=True)
    created_at = fields.Str(dump_only=True)
    modified_at = fields.Str(dump_only=True)
