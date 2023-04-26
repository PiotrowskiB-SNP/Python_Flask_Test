import flask
import uuid

app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid4())


@app.route('/')
def go_home_param():
    return flask.redirect(flask.url_for('show_users'))


@app.route('/secret)')
def show_secret():
    return '<h1>Secret</h1>'


@app.route('/user')
def show_users():
    users = ['Bartosz', 'Patric', 'Christian']
    return flask.render_template('users.html', users=users)


@app.route('/user(<username>)')
def show_user(username: str):

    return f'Main Site for the fine user<h2>{flask.escape(username)}</h2>' if username != 'Bartosz' else f'Main Site for the BEST user<h2>{flask.escape(username)}</h2>'


if __name__ == '__main__':
    # execute app on localhost - for local testing only
    app.run(host='0.0.0.0', port=5000)
