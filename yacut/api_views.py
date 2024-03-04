import re

from flask import jsonify, request

from yacut import app, db
from yacut.constants import PATTERN_FOR_CHECK_URL
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/<string:url>/', methods=('GET',))
def get_original_url(url):
    url_obj = URLMap.query.filter_by(short=url).first()
    if url_obj is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_obj.original}), 200


@app.route('/api/id/', methods=('POST',))
def generate_short_url():
    data = request.get_json()
    error_message = ''
    if not data:
        error_message = 'Отсутствует тело запроса'
    elif 'url' not in data:
        error_message = '"url" является обязательным полем!'
    elif not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    elif data.get('custom_id') and re.search(PATTERN_FOR_CHECK_URL, data['custom_id']) is None:
        error_message = 'Указано недопустимое имя для короткой ссылки'
    elif URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        error_message = 'Предложенный вариант короткой ссылки уже существует.'

    if len(error_message) > 0:
        raise InvalidAPIUsage(error_message)

    url_obj = URLMap()
    url_obj.from_dict(data)
    db.session.add(url_obj)
    db.session.commit()
    return jsonify(url_obj.to_dict()), 201