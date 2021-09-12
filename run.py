from app import create_app
from config import config_options
from commands import config_app


app = create_app('development')

app.config.from_object(config_options['development'])
config_app(app)

