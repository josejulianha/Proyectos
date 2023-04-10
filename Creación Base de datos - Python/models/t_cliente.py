from base_de_datos import bd

class ClientesModel(bd.Model):
    __tablename__="t_cliente"
    id_cliente = bd.Column(bd.Integer, primary_key=True)
    cli_nom = bd.Column(bd.String(45))
    cli_ape = bd.Column(bd.String(45))
    cli_fech = bd.Column(bd.DATETIME)
    t_usuario_usu_id= bd.Column(bd.Integer,bd.ForeignKey('t_usuario.usu_id'))


    cuenta = bd.relationship('CuentaModel',lazy=True)


 
    def __init__(self,nombre,apellido,fecha,id_usu):
        self.cli_nom=nombre
        self.cli_ape= apellido
        self.cli_fech= fecha
        self.t_usuario_usu_id = id_usu
        

        
    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()

