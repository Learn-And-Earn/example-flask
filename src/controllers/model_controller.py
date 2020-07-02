from flask import request, Blueprint
from ..models.model import ExampleModel, ModelSchema
from ..utils.ResponseUtils import custom_response
import src.database.ibm_db2_dml as ibm_db2_dml

model_controller = Blueprint('controller', __name__)


@model_controller.route('/', methods=['POST'])
def update():
    """
    Add a Model
    """
    req_data = request.get_json()
    schema = ModelSchema()
    model = ExampleModel(req_data)
    schema.dump(model)
    response = ibm_db2_dml.update(ExampleModel, model=model)
    return custom_response(response, 201)


@model_controller.route('/', methods=['GET'])
def get_all():
    """
    Get All Models
    """
    response = ibm_db2_dml.get_all(ExampleModel)
    return custom_response(response, 200)


@model_controller.route('/<int:id>', methods=['GET'])
def get_one(id):
    """
    Get A Model
    """
    response = ibm_db2_dml.get(ExampleModel, id=id)
    return custom_response(response, 200)


@model_controller.route('/', methods=['PUT'])
def create():
    """
    Update A Model
    """
    req_data = request.get_json()
    schema = ModelSchema()
    model = ExampleModel(req_data)
    schema.dump(model)
    response = ibm_db2_dml.create(ExampleModel,model)
    return custom_response(response, 201)


@model_controller.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Delete A Model
    """
    ibm_db2_dml.delete(ExampleModel,id=id)
    return custom_response({'message': 'deleted'}, 200)
