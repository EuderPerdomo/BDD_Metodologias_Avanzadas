# -- FILE: features/downloadData.feature

Feature:descargardatos de MT5
    Como usuario quiero poder descargar datos de diferentes divisas para poder realizar 
    backtesting de estrategias
    
    Scenario Outline: descarga de datos
        Given en el menu de inicio
        When el usuario seleciona la opcion descargar datos 3
        And ingresa la divisa <nombre> y <cantidad> de datos requeridos
        Then se obtiene un dataframe con <longitud> de tamaño
        
        Examples:
        |nombre|cantidad|longitud|
        |EURUSD|10|10|
        |USDJPY|20|20|
        |USDCAD|30|30|
        |NZDUSD|40|40|
        |EURCAD|200|200|
    




