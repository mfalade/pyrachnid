import os

from flask_script import Server, Manager

from pyrachnid import create_app


app_env = os.environ.get('APP_ENV', 'dev')
port = os.environ.get('PORT', '3000')

app = create_app(app_env)

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=port))


if __name__ == '__main__':
    manager.run()