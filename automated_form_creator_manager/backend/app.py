from flask import Flask, redirect, url_for
from flask_oauthlib.client import OAuth

app = Flask(__name__)
# app.secret_key = 'my_secret_key'

oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key='1078283402772-qrn2u9t2o06s4jcto43o6p3k3vltie43.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    # Store the access token securely
    access_token = resp['access_token']
    # Now you can use the access token to make requests to Google APIs
    return 'Access token: {}'.format(access_token)

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

if __name__ == '__main__':
    app.run(debug=True)
