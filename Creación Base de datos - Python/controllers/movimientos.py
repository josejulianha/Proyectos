from base_de_datos import bd
from flask_restful import Resource, reqparse
from models.t_movimientos import MovimientosModel
from models.t_cliente import ClientesModel
from models.cuenta import CuentaModel

class MovimientosController(Resource):
        
    def post(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument(
            'tipo',
            type=str,
            required=True,
            help="Falta la direccion"
        )
        parser.add_argument(
            'monto',
            type=str,
            required=True,
            help="Falta la direccion"
        )
        parser.add_argument(
            'fecha',
            type=str,
            required=True,
            help="Falta la direccion"
        )
        parser.add_argument(
            'destino',
            type=str,
            required=True,
            help="Falta la direccion"
        )
         data = parser.parse_args()

        movimientos = MovimientosModel(data['tipo'], data['monto'], data['fecha'], data['destino'])
        movimientos.guardar_en_la_bd()

        
 