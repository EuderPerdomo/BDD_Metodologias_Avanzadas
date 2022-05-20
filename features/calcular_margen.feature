# -- FILE: features/calcular_margen.feature

Feature:Informacion de la cuenta
    Como usuario quiero calcular el margen necesario para saber si dispongo
    de los fondos suficientes para realizar una orden de compra/venta
    @slow
    Scenario Outline: consultar margen necesario
        Given el usuario requiere poner una orden de compra, teniendo en cuenta que la moneda de la cuenta es dolar
        When el usuario indica el par de interes <par>
        Then se obtine informacion del margen necesario para efectuar la operacion <respuesta>

        Examples:
            | par     | respuesta         |
            | EURUSD  | margen disponible |
            | uydf    | invalida          |
            | sdgfdgd | invalida          |
            | USDCAD  | margen disponible |






