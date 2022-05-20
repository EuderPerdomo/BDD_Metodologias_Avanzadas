# -- FILE: features/enviar_orden.feature

Feature:Envio de ordenes
    Como usuario quiero enviar órdenes de compra/venta para aumentar capital de la cuenta y saber siestas se
    ejecutaron correctamente

    Scenario Outline: confirmacion de orden de compra
        Given el usuario envia una orden de compra
        When se desee compra algun par <par>
        Then se obtine mensaje con confirmacion de posicion creada <mensaje>

        Examples:
            | par    | mensaje |
            | EURUSD | Success |
            | dgsdg  | invalid |






