# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:34:21 2022

@author: euder
"""

# -- FILE: features/steps/downloadData_steps.py
from behave import given, when, then, step
import sys
sys.path.append('C:/Users/euder/OneDrive/Escritorio/BDD/MT5_Python')
from Download_Data import  funciones

@given('en el menu inicial')
def step_impl(context):
    pass

@when('el usuario selecciona la opcion {opcion}')
def step_impl(self,opcion): 
    print('La opcion introducisda',opcion)
    #funciones.menu(self,opcion)
    self.response = funciones.balance(self)
    print('La respuesta Obtenida: ',self.response)


@then('se obtine informacion de saldo disponible {saldo}')
def step_impl(self,saldo):
    assert(self.response==float(saldo))

        
    
