from base_de_datos import bd

class CuentaModel(bd.Model):
    __tablename__="t_cuenta"
    cue_id = bd.Column(bd.Integer,primary_key=True)
    cue_nro = bd.Column(bd.String(45))
    cue_tipo = bd.Column(bd.String(45))
    cue_saldo = bd.Column(bd.DECIMAL(9,2))
    cue_estado = bd.Column(bd.Boolean)

    tipo_moneda_id = bd.Column(bd.Integer,bd.ForeignKey('t_tipo_moneda.tipo_id'),nullable=False)
    cliente_id = bd.Column(bd.Integer,bd.ForeignKey('t_cliente.id_cliente'),nullable=True)
    agencia_id = bd.Column(bd.Integer,bd.ForeignKey('t_agencia.agen_id'),nullable=True)
        
    tipo = bd.relationship('TipoMonedaModel',lazy=True)
    cliente = bd.relationship('ClientesModel',lazy=True)
    agencia = bd.relationship('agenciasModel',lazy=True)

    def __init__(self,nro,tipo_cuenta,saldo,estado,tipo,cliente,agencia):
        self.cue_nro = nro
        self.cue_tipo = tipo_cuenta
        self.cue_saldo = saldo
        self.cue_estado = 1
        self.tipo_moneda_id = tipo 
        self.cliente_id = cliente
        self.agencia_id = agencia

    def retornar_json(self):
        return {
            'id':self.cue_id,
            'nro':self.cue_nro,
            # 'tipo':self.cue_tipo,
            'saldo':str(self.cue_saldo),
            # 'estado':str(self.cue_estado),
            'moneda':str(self.tipo.tipo_desc),
            'id_cliente':str(self.cliente_id)
            # 'agencia':str(self.agencia.agen_nom)
        }
            
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()