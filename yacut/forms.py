from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            Length(1, 256),
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Некорректная ссылка')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(regex=r'[A-Za-z0-9]+',
                   message='Используются недопустимые символы (разрешены только A-Z, a-z, 0-9).')]
    )
    submit = SubmitField('Создать')