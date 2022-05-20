# -- FILE: features/info_account.feature

Feature:Conectarse a la cuenta en MT5
    Como usuario quiero poder establecer conexion con mi cuenta en MT5 
    para obtener información, y enviar slicitudes comerciales
    
    Scenario Outline: verificar onexion a la cuenta.
        Given el usuario haya iniciado seccion en  mt5
        When el usuario elige la opcion <opcion>
        Then se obtine mensaje de conexion exitosa "Success"

        Examples:
        |opcion|
        |1   |
        




