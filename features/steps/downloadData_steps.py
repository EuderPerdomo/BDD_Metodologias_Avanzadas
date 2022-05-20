# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:38:06 2022

@author: euder
"""
# -- FILE: features/steps/downloadData_steps.py
from behave import given, when, then, step
import sys
sys.path.append('C:/Users/euder/OneDrive/Escritorio/BDD/MT5_Python')
from Download_Data import  funciones

@given('en el menu de inicio')
def step_impl(context):
    pass

@when('el usuario seleciona la opcion descargar datos {opcion}')
def step_impl(self,opcion): 
    #funciones.menu(self,opcion)
    pass
@when('ingresa la divisa {nombre} y {cantidad} de datos requeridos')
def step_impl(self,nombre,cantidad):
    funciones.descargar_datos(self,nombre,cantidad)

@then('se obtiene un dataframe con {longitud} de tamaño')
def step_impl(context,longitud):
    pass
