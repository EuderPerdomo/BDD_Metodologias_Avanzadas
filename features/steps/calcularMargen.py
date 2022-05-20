# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:34:21 2022

@author: euder
"""

# -- FILE: features/steps/downloadData_steps.py
from behave import given, when, then, step
import sys

from sklearn.linear_model import PassiveAggressiveClassifier
sys.path.append('C:/Users/euder/OneDrive/Escritorio/BDD/MT5_Python')
from Download_Data import  funciones

@given('el usuario requiere poner una orden de compra, teniendo en cuenta que la moneda de la cuenta es dolar')
def step_impl(context):
    pass

@when('el usuario indica el par de interes {divisa}')
def step_impl(self,divisa): 
    self.response = funciones.calcular_margen(self,divisa)

@then('se obtine informacion del margen necesario para efectuar la operacion {margen}')
def step_impl(self,margen):
    assert(self.response==margen)




        
    
