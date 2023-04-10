from base_de_datos import bd
import bcrypt


class usarioModel(bd.Model):
    __tablename__ = "t_usuario"
    usu_id = bd.Column(bd.Integer, primary_key=True)

    usu_hash = bd.Column(bd.Text)
    usu_salt = bd.Column(bd.Text)
    usu_mail = bd.Column(bd.String(45))
    usu_dir = bd.Column(bd.String(45))
    usu_tel = bd.Column(bd.Integer)
    usu_tipo = bd.Column(bd.Integer)
    # t_cliente= bd.Column(bd.Integer,bd.ForeignKey('t_cliente.id_cliente'))

    def __init__(self, password, correo, direccion, telefono, tipo):
        password_convertida = bytes(password, 'utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_convertida, salt)
        salt = salt.decode('utf-8')
        hashed = hashed.decode('utf-8')
        self.usu_hash = hashed
        self.usu_salt = salt
        self.usu_mail = correo
        self.usu_dir = direccion
        self.usu_tel = telefono
        self.usu_tipo = tipo

    def guardar_en_la_bd(self):
        bd.session.add(self)
        bd.session.commit()
