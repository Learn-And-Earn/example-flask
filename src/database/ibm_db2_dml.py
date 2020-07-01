from .base import session_factory, Base


def create(model: Base):
    session = session_factory(model)
    session.add(model)
    session.commit()
    id = model.id
    session.close()
    return id


def update(base_type, id=None, model: Base = None):
    if id is None:
        id = model.id
    ignore_keys = ['_sa_instance_state', 'id']
    session = session_factory(model)
    model_value_pairs = {k: v for k, v in vars(model).items() if k not in ignore_keys}
    session.query(base_type).filter(base_type.id == id).update(model_value_pairs)
    session.commit()
    session.close()
    return get(type(model), id=id)


def get(base_type, id=None, model: Base = None):
    if id is None:
        id = model.id
    session = session_factory(model)
    model = session.query(base_type).filter(base_type.id == id).one()
    session.close()
    return model


def get_all(base_type, model: Base = None):
    session = session_factory(model)
    models = session.query(base_type).all()
    session.close()
    return models


def delete(model: Base):
    session = session_factory(model)
    session.delete(model)
    session.commit()
    session.close()
    return True
