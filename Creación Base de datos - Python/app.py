from flask import Flask
from flask_restful import Api

from base_de_datos import bd

from controllers.tipoMoneda import TipoMonedaController,TiposMonedasController
from controllers.cuenta import CuentaController, CuentasController
from models.agencia import agenciasModel
from models.tipoMoneda import TipoMonedaModel
from models.usuario import usarioModel
# from models.t_cliente  import  ClientesModel
from controllers.clientes import ClientesController
from models.cuenta import CuentaModel
from models.t_movimientos import MovimientosModel
from models.operacionesAgencia import OperacionesAgenciaModel
# from controllers.clientes import ClientesController
# from controllers.movimientos import MovimientosController

from flask_cors import CORS
from flask_jwt import JWT
from seguridad import autentication, identificador


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://QYU30YAalW:QOSS8zlycY@remotemysql.com/QYU30YAalW"

app.config['SECRET_KEY'] = 'clave_secreta'
app.config['JWT_AUTH_URL_RULE']='/usuario/login'
import datetime

app.config['JWT_EXPIRATION_DELTA']=datetime.timedelta(hours=1)
jsonwebtoken = JWT(app, autentication, identificador)

api = Api(app)

@app.route('/')
def inicio():
    return 'Tu Banco mi banco esta escuchando tu peticion'

@app.before_first_request
def iniciar_bd():
    #Para iniciar la aplicacion de SQL ALCHEMY
    bd.init_app(app)
    # bd.drop_all(app=app)
    #Para crear todas las tablas
    bd.create_all(app=app)


# api.add_resourceapi.add_resource(TipoMonedaController,'/tipomoneda/buscar/<string:nombre>','/tipomoneda/crear')
api.add_resource(TiposMonedasController,'/tiposmonedas/mostrartodos')
api.add_resource(CuentaController,'/cuenta/buscar/<string:nro_cuenta>','/cuenta/crear')
api.add_resource(CuentasController,'/cuentas/mostrartodas/<int:id_cliente>')
# api.add_resource(CuentaController,'/cuenta/buscar/<int:id>','/cuenta/crear')
api.add_resource(ClientesController, '/cliente/registrar', '/movimientos/buscar/<int:id>')
# api.add_resource(MovimientosController, '/movimientos/buscar/<int:id>')

if(__name__=="__main__"):
    app.run(debug=True)
