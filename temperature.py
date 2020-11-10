# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:13:57 2019

@author: Alois Froschauer


"""

def in_celsius():
    """ Rechnet Temperatur von Fahrenheit in Grad Celsius um. """
    
    # Wert abfragen
    Fahrenheit = int(input("Geben Sie die Temperatur in Fahrenheit an: "))
    
    # Ergebnis berechnen
    Celsius = 1
 #   (Fahrenheit − 32)* 5/9
    print(Fahrenheit,"F = ",Celsius,"°C")
    
            
#### main() ####
in_celsius()