class Item:
    def __init__(self,id=1,descripcion="camisa",unidades=10,precio=40):
        self.descripcion=descripcion
        self.id=id
        self.unidades=unidades
        self.precio=precio

    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,descripcion):
        if not isinstance(descripcion,(str)):
            raise ValueError("descripción debe ser un texto")
        self.__descripcion=descripcion

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        if not isinstance(id,(int,float)):
            raise ValueError("id debe ser un numero")
        if id<0:
            raise ValueError("id debe ser mayor a 0")
        self.__id=id
    
    @property
    def unidades(self):
        return self.__unidades
    
    @unidades.setter
    def unidades(self,unidades):
        if not isinstance (unidades,(int,float)):
            raise ValueError ("unidades debe ser un numero")
        if unidades<0:
            raise ValueError ("unidades debe ser mayor a 0")
        self.__unidades=unidades

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
        if not isinstance (precio,(int,float)):
            raise ValueError ("precio debe ser un numero")
        if precio<0:
            raise ValueError ("precio debe ser mayor a 0")
        self.__precio=precio
    
    def get_inventario(self):
        return ((self.unidades)*(self.precio))

    def __str__(self):
        return f"Item: [Descripcion: {self.descripcion} | Id: {self.id} | Unidades: {self.unidades} | Precio: {self.precio}]"