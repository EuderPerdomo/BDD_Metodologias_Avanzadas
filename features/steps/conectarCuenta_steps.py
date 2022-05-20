# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:34:21 2022

@author: euder
"""

# -- FILE: features/steps/ConectarCuenta_steps.py
from behave import given, when, then, step
import sys
sys.path.append('C:/Users/euder/OneDrive/Escritorio/BDD/MT5_Python')
from Download_Data import  funciones

@given('el usuario haya iniciado seccion en  mt5')
def step_impl(context):
    pass

@when('el usuario elige la opcion {opcion}')
def step_impl(self,opcion): 
    print('La opcion introducida',opcion)
    #funciones.menu(self,opcion)
    self.response = funciones.conectar_cuenta(self)
    print('La respuesta Obtenida: ',self.response)


@then('se obtine mensaje de conexion exitosa {texto}')
def step_impl(self,texto):
    if self.response ==texto:
        print('Conexion exitosa')
        pass

        
    
