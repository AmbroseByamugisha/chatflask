from config import create_app

app = create_app(config_name='testing')

from api.views import chat_blueprint

app.register_blueprint(chat_blueprint, url_prefix = '/v2/api/')

# find a way to test on a different db_url
# coz this one that calls config_name= testing
# doesnt work.
# u have to change the app declaration the other side of the api too.
