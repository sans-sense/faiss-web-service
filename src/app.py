import configparser

from flask import Flask

from internal.blueprint import blueprint as InternalBlueprint
from faiss_index.blueprint import blueprint as FaissIndexBlueprint

config = configparser.ConfigParser()
config.read('faiss-service.ini')

idx_info = config['faiss.service.index.files']

app = Flask(__name__)
app.config['INDEX_PATH'] = idx_info['INDEX_PATH']
app.config['IDS_VECTORS_PATH'] = idx_info['IDS_VECTORS_PATH']

app.register_blueprint(InternalBlueprint)
app.register_blueprint(FaissIndexBlueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
