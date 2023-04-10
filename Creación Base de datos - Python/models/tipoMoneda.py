from base_de_datos import bd

class TipoMonedaModel(bd.Model):
    __tablename__="t_tipo_moneda"
    tipo_id = bd.Column(bd.Integer,primary_key=True)
    tipo_desc = bd.Column(bd.String(45),nullable=True)
    
    cuentas = bd.relationship('CuentaModel',lazy=True, backref='tipos_monedas')
    
    def __init__(self,descripcion):
        self.tipo_desc=descripcion

    def retornar_json(self):
        return {
            'id':self.tipo_id,
            'descripcion':self.tipo_desc
        }    
          
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()