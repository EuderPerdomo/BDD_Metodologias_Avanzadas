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

@given('el usuario envia una orden de compra')
def step_impl(context):
    pass

@when('se desee compra algun par {par}')
def step_impl(self,par): 
    self.response = funciones.orden_compra(self,par)


@then('se obtine mensaje con confirmacion de posicion creada {mensaje}')
def step_impl(self,mensaje):
    assert(self.response==mensaje)

        
    
