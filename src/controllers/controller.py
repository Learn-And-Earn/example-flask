from flask import request, g, Blueprint, json, Response
from ..models.model import ExampleModel, ModelSchema

controller = Blueprint('controller', __name__)

base = []


@controller.route('/', methods=['POST'])
def create():
    """
    Add a Model
    """
    req_data = request.get_json()
    schema = ModelSchema()
    model = ExampleModel(req_data)
    data = schema.dump(model)
    base.append(data)
    return custom_response(data, 201)


@controller.route('/', methods=['GET'])
def get_all():
    """
    Get All Models
    """
    return custom_response(base, 200)


@controller.route('/<int:id>', methods=['GET'])
def get_one(id):
    """
    Get A Model
    """
    data = [each for each in base if ExampleModel(each).id == id]
    if data.__len__ == 0:
        return custom_response({'error': 'post not found'}, 404)
    return custom_response(data, 200)


@controller.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Update A Model
    """
    req_data = request.get_json()
    try:
        index = [index for index, each in enumerate(base) if ExampleModel(each).id == id]
    except:
        return custom_response({'error': 'post not found'}, 404)
    
    if len(index) == 0:
        return custom_response({'error': 'post not found'}, 404)
        
    schema = ModelSchema()
    req_data['created_at'] = base[index[0]].get('created_at')
    model = ExampleModel(req_data)
    data = schema.dump(model)
    base[index[0]] = data
    return custom_response(data, 200)


@controller.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Delete A Model
    """
    post = ExampleModel.get_one_todo(id)
    schema = ModelSchema()
    if not post:
        return custom_response({'error': 'post not found'}, 404)
    data = schema.dump(post)

    post.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
