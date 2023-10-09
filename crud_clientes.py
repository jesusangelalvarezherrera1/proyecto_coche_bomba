import crud_restaurante
db = crud_restaurante.crud()


class crud_clientes:
    def consultar_clientes(self, buscar):
        return db.consultar("select * from clientes where codigo like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, clientes):
        if clientes["accion"] == "nuevo":
            sql = """
                INSERT INTO clientes (codigo, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s)
            """
            val = (clientes["codigo"], clientes["nombre"], clientes["direccion"], clientes["telefono"])
        elif clientes["accion"] == "modificar":
            sql = """
                UPDATE clientes
                    SET codigo=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idCliente=%s
            """
            val = (clientes["codigo"], clientes["nombre"], clientes["direccion"], clientes["telefono"], clientes["idCliente"])
        elif clientes["accion"] == "eliminar":
            sql = """
                DELETE FROM clientes
                WHERE idCliente=%s
            """
            val = (clientes["idCliente"],)
        return db.ejecutar_consultas(sql, val)