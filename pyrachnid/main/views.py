from flask import (
    jsonify,
    make_response,
    render_template,
    request
)

from . import main


@main.route('/healthcheck')
def healthcheck():
    return make_response(jsonify({
        'status_code': 200,
        'text': 'OK'
    }))


@main.route('/')
def home():
    context = {'action': None}
    return render_template('index.html')


@main.route('/add')
def add_new_site():
    context = {
        'action': 'set domain'
    }
    return render_template('add_new_site.html', context=context)


@main.route('/')
def view_existing_site():
    return render_template('view_existing_site.html')