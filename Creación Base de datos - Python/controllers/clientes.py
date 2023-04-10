from base_de_datos import bd
from flask_restful import Resource, reqparse
from models.t_cliente import ClientesModel
from models.usuario import usarioModel


class ClientesController(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'direccion',
            type=str,
            required=True,
            help="Falta la direccion"
        )
        parser.add_argument(
            'email',
            type=str,
            required=True,
            help="Falta el email"
        )
        parser.add_argument(
            'contraseña',
            type=str,
            required=True,
            help="Falta la contraseña"
        )
        parser.add_argument(
            'telefono',
            type=int,
            required=True,
            help="Falta el telefono"
        )
        parser.add_argument(
            'nombre',
            type=str,
            required=True,
            help="Falta el nombre"
        )
        parser.add_argument(
            'apellido',
            type=str,
            required=True,
            help="Falta el apellido"
        )
        parser.add_argument(
            'usu_tipo',
            type=int,
            required=True,
            help="Falta el tipo de usuario"
        )
        parser.add_argument(
            'fecha_nac',
            type=str,
            required=True,
            help="Falta el tipo de usuario"
        )

        data = parser.parse_args()

        usuario = usarioModel(data['contraseña'], data['email'],
                              data['direccion'], data['telefono'], data['usu_tipo'])
        usuario.guardar_en_la_bd()

        cliente = ClientesModel(
            data['nombre'], data['apellido'], data['fecha_nac'], usuario.usu_id)
        cliente.guardar_en_la_bd()
        # try:

        # except:
        #     return {'message': 'Hubo un error en el registro'}, 500
        # return {
        #     'message': 'Usuario registrado con exito'}, 201

    def get(self, id):
        sentencia = ClientesModel.query.filter_by(id_cliente=id).first()
        resultado = []
        print(sentencia.cuenta)
        for cuenta in sentencia.cuenta:
            print(cuenta.tipo)
            for movimiento in cuenta.tipo:
                resultado.append({
                    'Nro de Cuenta': cuenta.cue_nro,
                    'tipo movimiento': movimiento.mov_tipo,
                    'monto movimiento': str(movimiento.mov_monto),
                    'fecha': str(movimiento.mov_fecha)})
                
        return resultado
            
