# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:44:12 2022

@author: euder
"""
#https://www.mql5.com/es/docs/integration/python_metatrader5/mt5copyratesfrompos_py
import MetaTrader5 as mt5
import pandas as pd


class funciones():    
    def orden_compra(self,divisa):
        
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())

        symbol = divisa
        symbol_info = mt5.symbol_info(symbol)
        
        if symbol_info is None:
            print(symbol, "not found, can not call order_check()")
            mt5.shutdown()
            return 'invalid'
         
        # si el símbolo no está disponible en MarketWatch, lo añadimos
        if not symbol_info.visible:
            print(symbol, "is not visible, trying to switch on")
            if not mt5.symbol_select(symbol,True):
                print("symbol_select({}}) failed, exit",symbol)
                mt5.shutdown()
                return 'invalid'
    
        lot = 0.01
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - 300 * point,
        "tp": price + 1000 * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "Pruebas de BDD",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
        }         
        
        # enviamos la solicitud comercial
        result = mt5.order_send(request)
        # comprobamos el resultado de la ejecución
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
        
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
           # solicitamos el resultado en forma de diccionario y lo mostramos elemento por elemento
            result_dict=result._asdict()           
            for field in result_dict.keys():
                print("   {}={}".format(field,result_dict[field]))
                # si se trata de la estructura de una solicitud comercial, también la mostramos elemento por elemento
                if field=="request":
                    traderequest_dict=result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))        
            return 'invalid'
        else:
            print('orden enviada correctamente')        
            return 'Success'
    
    def descargar_datos(self,divisa,cantidad):
        cantidad=int(cantidad)
        # establecemos la conexión con el terminal MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
         
        # solicitamos 10 barras de GBPUSD D1 desde el día actual
        rates = mt5.copy_rates_from_pos(divisa, mt5.TIMEFRAME_D1, 0, cantidad)
         
        # finalizamos la conexión con el terminal MetaTrader 5
        mt5.shutdown()
         
        # mostramos cada elemento de los datos obtenidos en una nueva línea
        print("Mostramos los datos obtenidos como son")
        for rate in rates:
            print(rate)
         
        # creamos un DataFrame de los datos obtenidos
        rates_frame = pd.DataFrame(rates)
        # convertimos la hora en segundos al formato datetime
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
         
        # mostramos los datos
        #print("\nMostramos el frame de datos con la información")
        #print('Longitud ',len(rates_frame)) 
        return len(rates_frame)
    
    def conectar_cuenta(self):
        
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
        else:
            print('conectado a la cuenta correctamente',mt5.last_error())
            return mt5.last_error()[1]         
    
    def balance(self):
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())

        account_info=mt5.account_info()
        
        if account_info!=None:
            account_info_dict = mt5.account_info()._asdict()
           # transformamos el diccionario en DataFrame y lo imprimimos
            df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
            balance=df.iloc[10][1]
            print(balance)
            
        mt5.shutdown()
        return balance
    
    def calcular_margen(self,divisa):
        # establecemos la conexión con el terminal MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
         
        # obtenemos la divisa de la cuenta
        account_currency=mt5.account_info().currency
        print("Account сurrency:",account_currency)        
        action=mt5.ORDER_TYPE_BUY
        lot=0.1
        symbol_info=mt5.symbol_info(divisa)
        print(symbol_info)
        if symbol_info is None:
            return 'invalida'
         
        else:
            ask=mt5.symbol_info_tick(divisa).ask
            margin=mt5.order_calc_margin(action,divisa,lot,ask)
            if margin != None:
                print("   {} buy {} lot margin: {} {}".format(divisa,lot,margin,account_currency));
            else:
                print("order_calc_margin failed: , error code =", mt5.last_error())
             
            mt5.shutdown()
            return 'margen disponible'

    def menu(self,opcion):
        
        
        print("""
                  */-----------------------------------------\*
                  |    Menu:                                  |
                  |       1. Conectar a la cuenta             |
                  |       2. Obtener Balance de la cuenta     | 
                  |       3. Obtener datos de Divisas         |
                  |       4. Calcular margen necesario        |
                  |       5. Enviar una Orden                 |
                  |       6. Salir                            |
                  *\-----------------------------------------/*
              """
              )
        
        #opcion=0
        while opcion != 6:
            
           if opcion==1:
               x.conectar_cuenta()
           elif opcion==2:
               balance=self.balance()
               print(balance)
               return balance
           elif opcion==3:
               
               divisa=input('Dijite el nombre de la divisa: ')
               cantidad=input('Ingrese la cantidad de datos requeridos: ')
               x.descargar_datos(divisa,cantidad)
               
           elif opcion==4:
               
               divisa=input('Dijite el nombre de la divisa: ')
               self.calcular_margen(divisa)
               
           elif opcion==5:
               print('Oc 5')
           else:
               if opcion !=0:
                   print('Digite una opción del menu')
               else:
                   pass
           try:
               opcion=int(input('Dijite una opción:'))
           except:
               print('Ingrese solo valores numericos')
        print('Programa Terminado')
        
x=funciones()
#x.d_d('EURUSD',10)









