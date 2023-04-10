from base_de_datos import bd

class MovimientosModel(bd.Model):
    __tablename__="t_movimientos"
    mov_id = bd.Column(bd.Integer, primary_key=True)
    mov_tipo = bd.Column(bd.String(45))
    mov_monto = bd.Column(bd.DECIMAL(5,2))
    mov_fecha = bd.Column(bd.DATETIME)
    id_cuenta_destino = bd.Column(bd.Integer)
    t_cuenta_cue_id= bd.Column(bd.Integer,bd.ForeignKey('t_cuenta.cue_id'))
    
    

 
    def __init__(self,tipo, monto, fecha, destino):
        self.mov_tipo= tipo
        self.mov_monto= monto
        self.mov_fecha= fecha
        self.id_cuenta_destino = destino

    def retornar_json(self):
        return {
            'id':self.mov_id,
            'tipo movimiento':self.mov_tipo,
            'monto movimiento': self.mov_monto,
            'fecha':self.mov_fecha,
            'Cta. destino': self.id_cuenta_destino
            
        }
        
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()
