# -- FILE: features/info_account.feature

Feature:Informacion de la cuenta
    Como usuario quiero poder solicitar informacion de mi cuenta para conocer el estado actual de la misma
    
    Scenario Outline: conocer saldo disponible.
        Given en el menu inicial
        When el usuario selecciona la opcion <opcion>
        Then se obtine informacion de saldo disponible <saldo>

        Examples:
        |opcion|saldo|
        |2   |650.05|
        




