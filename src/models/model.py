from marshmallow import fields, Schema
from datetime import datetime


class ExampleModel():
    """
    Model
    """

    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.contents = data.get('contents')
        self.created_at = data.get('created_at') if data.get(
            'created_at') is not None else datetime.utcnow()
        self.modified_at = datetime.utcnow()


class ModelSchema(Schema):
    """
    Model Schema
    """
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    contents = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
