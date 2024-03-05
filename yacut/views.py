from flask import flash, redirect, render_template, url_for

from yacut import app
from yacut.forms import URLForm
from yacut.models import URLMap


@app.route('/', methods=('GET', 'POST'))
def page_for_generate_url():
    form = URLForm()
    if form.validate_on_submit():
        data = dict(url=form.original_link.data, custom_id=form.custom_id.data)
        url_obj, error_message = URLMap.validate_and_create_obj(data)
        if len(error_message) > 0:
            flash(error_message, 'error')
            return render_template('index.html', form=form)
        flash(url_for('redirect_short_url', url=url_obj.short, _external=True), 'url')
    return render_template('index.html', form=form)


@app.route('/<string:url>')
def redirect_short_url(url):
    return redirect(
        URLMap.query.filter_by(short=url).first_or_404().original
    )
