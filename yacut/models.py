from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_short_url', url=self.short, _external=True)
        )

    def from_dict(self, data):
        for key, value in zip(('original', 'short'), ('url', 'custom_id')):
            setattr(self, key, data[value])
