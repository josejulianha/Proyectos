from base_de_datos import bd

class OperacionesAgenciaModel(bd.Model):
    __tablename__ = "t_agencia_movimientos"
    agen_mov_id = bd.Column(bd.Integer, primary_key=True)
    agen_mov_confirmacion=bd.Column(bd.Integer)
    agen_id=bd.Column(bd.Integer, bd.ForeignKey("t_agencia.agen_id"), nullable=False)
    mov_id=bd.Column(bd.Integer, bd.ForeignKey("t_movimientos.mov_id"), nullable=False)

    def __init__(self,confirmacion,agencia_id,movimiento_id):
        self.agen_mov_confirmacion=confirmacion
        self.agen_id=agencia_id
        self.mov_id=movimiento_id
