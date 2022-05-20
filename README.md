# Proyecto BDD metodologias Avanzadas de desarrollo de software
## Integrantes:
Euderfabian Perdomo Ospitia

## Herramientas de Software Utilizadas
> Python 3.8.5
> IDE:  Spyder 
> Behave 1.2.6
> Allure 2.18.0
> MetaTrader5 5.0.33

## ¿Qué hace la aplicación?
La aplicación es una integración de Python y la plataforma MetaTrader5 constando de módulos básicos para verificar la conexión con la plataforma y obtener configuración, obtener datos de divisas, calcular márgenes necesarios y enviar órdenes. 
## Historias de usuario

•	Como usuario quiero poder establecer conexión con mi cuenta en MT5 para obtener información, y enviar solicitudes comerciales
•	Como usuario quiero poder descargar datos de diferentes divisas para poder realizar backtesting de estrategias comerciales
•	Como usuario quiero poder solicitar información de mi cuenta para conocer el estado actual de la misma.
•	Como usuario quiero calcular el margen necesario para saber si dispongo de los fondos suficientes para realizar una orden de compra/venta
•	Como usuario quiero enviar órdenes de compra/venta.


## Features

### Feature:Informacion de la cuenta
    Como usuario quiero poder solicitar informacion de mi cuenta para conocer el estado actual de la misma
    
    Scenario Outline: conocer saldo disponible.
        Given en el menu inicial
        When el usuario selecciona la opcion <opcion>
        Then se obtine informacion de saldo disponible <saldo>

        Examples:
        |opcion|saldo|
        |2   |650.05|
 ### Feature:Envio de ordenes
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
 ### Feature:descargardatos de MT5
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
        
 ### Feature:Conectarse a la cuenta en MT5
    Como usuario quiero poder establecer conexion con mi cuenta en MT5 
    para obtener información, y enviar slicitudes comerciales
    
    Scenario Outline: verificar onexion a la cuenta.
        Given el usuario haya iniciado seccion en  mt5
        When el usuario elige la opcion <opcion>
        Then se obtine mensaje de conexion exitosa "Success"

        Examples:
        |opcion|
        |1   |
 ### Feature:Informacion de la cuenta
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

## Conclusiones
Teniendo en cuenta el echo de no haber trabajado anteriormente con el lenguaje Gherkin, se aprendieron nociones básicas del mismo en cuanto a sintaxis y declaraciones así como de Behave necesario para la implementación de este  en Python, también se afianzaron conocimientos con respecto a historias de usuarios.

## Instrucciones Para usar Codigo
#### Clone: https://github.com/EuderPerdomo/BDD_Metodologias_Avanzadas.git
#### Clone GitHub CLI: gh repo clone EuderPerdomo/BDD_Metodologias_Avanzadas
