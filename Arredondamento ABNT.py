# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:01:52 2026

@author: anderson.takehara
"""

"""
Módulo: abnt_rounding.py
Descrição: Implementa arredondamento conforme norma ABNT NBR 5891
Autor: Anderson
"""

def arredondar_abnt(valor: float, casas_decimais: int = 2) -> float:
    """
    Arredonda um número conforme norma ABNT (round half to even).
    
    Parâmetros:
        valor (float): número a ser arredondado
        casas_decimais (int): número de casas decimais desejadas
    
    Retorno:
        float: número arredondado conforme ABNT
    """
    # Multiplica para deslocar casas decimais
    fator = 10 ** casas_decimais
    valor_expandido = valor * fator
    
    # Usa round() do Python, que já implementa "round half to even"
    valor_arredondado = round(valor_expandido) / fator
    
    return valor_arredondado


# Exemplos de uso
if __name__ == "__main__":
    exemplos = [2.345, 2.355, 2.365, 2.375]
    for num in exemplos:
        print(f"{num} -> {arredondar_abnt(num, 2)}")
        
"""        
import unittest
from abnt_rounding import arredondar_abnt

class TestArredondamentoABNT(unittest.TestCase):
    def test_meio_para_par(self):
        self.assertEqual(arredondar_abnt(2.345, 2), 2.34)
        self.assertEqual(arredondar_abnt(2.355, 2), 2.36)
        self.assertEqual(arredondar_abnt(2.365, 2), 2.36)
        self.assertEqual(arredondar_abnt(2.375, 2), 2.38)

if __name__ == "__main__":
    unittest.main()        
"""        
        