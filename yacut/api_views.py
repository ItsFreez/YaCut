from flask import jsonify, request

from yacut import app
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap


@app.route('/api/id/<string:url>/', methods=('GET',))
def get_original_url(url):
    url_obj = URLMap.get_obj_by_short(url)
    if url_obj is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_obj.original}), 200


@app.route('/api/id/', methods=('POST',))
def generate_short_url():
    data = request.get_json()
    url_obj, error_message = URLMap.validate_and_create_obj(data)
    if len(error_message) > 0:
        raise InvalidAPIUsage(error_message)
    return jsonify(url_obj.to_dict()), 201