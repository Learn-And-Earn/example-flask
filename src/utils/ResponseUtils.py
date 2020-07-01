from flask import json, Response


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    if type(res) is list:
        res = deserialize_json_properties_list(res)
    else:
        res = deserialize_json_properties_class(res)

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )


def deserialize_json_properties_list(list_of_objects, *args: str):
    final_list_of_dicts = []
    ignore_keys = ['_sa_instance_state']
    for arg in args:
        ignore_keys.append(arg)

    for objects in list_of_objects:
        dictionary = {k: v for k, v in vars(objects).items() if v is not None and k not in ignore_keys}
        final_list_of_dicts.append(dictionary)

    return final_list_of_dicts


def deserialize_json_properties_class(object, *args: str):
    ignore_keys = ['_sa_instance_state']
    for arg in args:
        ignore_keys.append(arg)

    dictionary = {k: v for k, v in vars(object).items() if v is not None and k not in ignore_keys}

    return dictionary
