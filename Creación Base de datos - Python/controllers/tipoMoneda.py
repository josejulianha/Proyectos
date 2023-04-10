from flask_restful import Resource, reqparse

from models.tipoMoneda import TipoMonedaModel

class TipoMonedaController(Resource):
    def get(self,nombre):
        resultado = TipoMonedaModel.query.filter(TipoMonedaModel.tipo_desc.like('%'+nombre+'%')).first()
        if resultado:
            return resultado.retornar_un_tipo_json()
        else:
            return {'message':'No se encontro ese tipo de moneda'},404        

    def post(self):
        parser =  reqparse.RequestParser()
        parser.add_argument('descripcion',
        type=str,
        required=True,
        help='Falta la descripcion'
        )
        data = parser.parse_args()
        consulta = TipoMonedaModel.query.filter_by(tipo_desc=data['descripcion']).first()
        if not consulta:
            insercion = TipoMonedaModel(data['descripcion'])
            try:
                insercion.guardar_en_la_bd()            
            except:
                return {'message':'Hubo un error al guardar en la base de datos'},500
            return {'message':'Se agrego exitosamente el tipo de moneda en la base de datos',
            'contenido':insercion.retornar_json()},201
        return {
            'message':'Ya hay un tipo de moneda creado con esa descripcion'
        },402
        
class TiposMonedasController(Resource):
    def get(self):
        resultado = TipoMonedaModel.query.all()
        if resultado:            
            arregloResultado = []
            for item in resultado:
                arregloResultado.append(item.retornar_json())
            print(arregloResultado) 
            return arregloResultado
        print(resultado)
        return {'message':'No se pudo conseguir algun tipo de moneda'}    