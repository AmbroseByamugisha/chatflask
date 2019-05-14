from config import create_app

app = create_app(config_name='development')

from api.views.auth import chat_blueprint
from api.views.messages import chat_blueprint
from api.views.chat_room import chat_blueprint

app.register_blueprint(chat_blueprint, url_prefix = '/v2/api/')
