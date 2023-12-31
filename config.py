import pathlib
import connexion
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
ma = Marshmallow(app)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
