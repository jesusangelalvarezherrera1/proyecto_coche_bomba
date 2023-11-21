import crud_restaurante
db = crud_restaurante.crud()


class crud_empleados:
    def consultar_empleados(self, buscar):
        return db.consultar("select * from empleados where codigo like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, empleados):
        if empleados["accion"] == "nuevo":
            sql = """
                INSERT INTO empleados (codigo, nombre, direccion, telefono)
                VALUES (%s, %s, %s, %s)
            """
            val = (empleados["codigo"], empleados["nombre"], empleados["direccion"], empleados["telefono"])
        elif empleados["accion"] == "modificar":
            sql = """
                UPDATE empleados
                    SET codigo=%s, nombre=%s, direccion=%s, telefono=%s
                WHERE idEmpleado=%s
            """
            val = (empleados["codigo"], empleados["nombre"], empleados["direccion"], empleados["telefono"], empleados["idEmpleado"])
        elif empleados["accion"] == "eliminar":
            sql = """
                DELETE FROM empleados
                WHERE idEmpleado=%s
            """
            val = (empleados["idEmpleado"],)
        return db.ejecutar_consultas(sql, val)