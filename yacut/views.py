from flask import flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def page_for_generate_url():
    form = URLForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url and URLMap.query.filter_by(short=short_url).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.', 'error')
            return render_template('index.html', form=form)
        elif not short_url:
            short_url = get_unique_short_id()
        url_obj = URLMap(original=form.original_link.data, short=short_url)
        db.session.add(url_obj)
        db.session.commit()
        flash(url_for('redirect_short_url', url=short_url, _external=True), 'url')
    return render_template('index.html', form=form)


@app.route('/<string:url>')
def redirect_short_url(url):
    return redirect(
        URLMap.query.filter_by(short=url).first_or_404().original
    )
