from flask_restful import Resource, reqparse

from models.cuenta import CuentaModel

class CuentaController(Resource):
    def get(self,nro_cuenta):
        resultado = CuentaModel.query.filter_by(cue_nro=nro_cuenta).first()        
        if resultado:
            return resultado.retornar_json()
        return {
            'message':'No hay ninguna cuenta con el id '+str(id)
        },404

    def post(self):
        parser = reqparse.RequestParser()        
        parser.add_argument(
            'nro',
            type=str,
            required=True,
            help='Falta el nro de cuenta'
        )
        parser.add_argument(
            'tipo_cuenta',
            type=str,
            required=True,
            help='Falta el tipo_cuenta'
        )
        parser.add_argument(
            'saldo',
            type=float,
            required=True,
            help='Falta el saldo'
        )
        parser.add_argument(
            'estado',
            type=bool,
            required=False,
            help='Falta el estado'
        )
        parser.add_argument(
            'moneda',
            type=int,
            required=True,
            help='Falta la moneda'
        )
        parser.add_argument(
            'cliente_id',
            type=int,
            required=True,
            help='Falta el cliente_id'
        )
        parser.add_argument(
            'agencia_id',
            type=int,
            required=False,
            help='Falta la  agencia_id'
        )
        data = parser.parse_args()
        consultaDuplicado = CuentaModel.query.filter_by(cue_nro=data['nro']).first()
        if consultaDuplicado:
            {
                'message':'ya existe una cuenta con ese numero',
            },201
        else:            
            cuenta = CuentaModel(data['nro'],data['tipo_cuenta'],data['saldo'],data['estado'],data['moneda'],data['cliente_id'],data['agencia_id'])
            try:
                cuenta.guardar_en_la_bd()
            except:
                return {'message':'Hubo un error al registrar la cuenta, intente nuevamente'},500
            return {'message':'Cuenta guardada con exito',
            'contenido':cuenta.retornar_json()},201
    
class CuentasController(Resource):
    def get(self,id_cliente):
        resultado = CuentaModel.query.filter_by(cliente_id=id_cliente).all()
        if resultado:            
            arregloResultado = []
            for item in resultado:
                arregloResultado.append(item.retornar_json())
            print(arregloResultado) 
            return arregloResultado
        print(resultado)
        return {'message':'No se pudo conseguir alguna cuenta'}

    