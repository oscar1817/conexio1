from flask import Flask
from flask_cors import CORS
from registro import registro_blueprint
from avistamiento import avistamiento_blueprint
from mapa import mapa_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(registro_blueprint)#registro
app.register_blueprint(avistamiento_blueprint)#avistamiento
app.register_blueprint(mapa_blueprint)#mapa


if __name__ == '__main__':
    
    app.run(debug=True ,port=3306,use_reloader=False)