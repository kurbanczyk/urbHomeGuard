from flask import Flask, current_app, make_response
from http import HTTPStatus

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DefaultConfig')

    with app.app_context():
        from guard_coach_service.rest import api
        app.register_blueprint(api)

    return app

app = create_app()

@app.route("/")
def hello_world():
    return make_response(
        {
            'service': {
                'name': 'Urb Home Guard',
                'version': current_app.config['SERVICE_VERSION']
            }
        },
        HTTPStatus.OK,
        {
            'Content-Type': 'application/json'
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')