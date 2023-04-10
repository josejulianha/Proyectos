from base_de_datos import bd

class agenciasModel(bd.Model):
    __tablename__=("t_agencia")
    agen_id = bd.Column(bd.Integer,primary_key=True)
    agen_nom = bd.Column(bd.String(45))
    agen_direc = bd.Column(bd.String(45))
    agen_lat = bd.Column(bd.DECIMAL(7,5))
    agen_lng = bd.Column(bd.DECIMAL(7,5))
    agen_horarios = bd.Column(bd.String(45))

    def __init__(self,nombre,latitud,longitud,direccion,horarios):
        self.agen_nom=nombre
        self.agen_direc=direccion
        self.agen_lat=latitud
        self.agen_lng=longitud
        self.agen_horarios= horarios
    
        
        
        