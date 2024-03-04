import random

from yacut.constants import STR_FOR_GEN_URL
from yacut.models import URLMap


def get_unique_short_id():
    while True:
        short_url = ''.join(random.choices(population=STR_FOR_GEN_URL, k=6))
        if URLMap.query.filter_by(short=short_url).first() is None:
            return short_url
