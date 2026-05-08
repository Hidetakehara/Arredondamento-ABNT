import math                                                                             # Importa o módulo math, que fornece funções matemáticas padrão.

def multiplica_ABNT(numero1, numero2):                                                  # Multiplica dois números e ajusta o resultado para conter o número correto de algarismos significativos, conforme o menor valor entre os dois operandos.
    algarismo = verificar_menor_algarismos_significativos(numero1, numero2)             # Função que retorna o menor número de algarismos significativos entre os dois números. 
    resultado = numero1 * numero2                                                       # Realiza a multiplicação.
    casas_deci = casas_para_arredondar(resultado, algarismo)                            # Conta o numero de casas decimais necessarios para o arredondamento respeitando o numero de algarismos significativos
    resultado = arredondar_ABNT(resultado, casas_deci)                                  # Aplica o arredondamento conforme a norma.        
    return resultado                                                                    # Retorna o valor final ajustado.

def divide_ABNT(numero1, numero2):                                                      # Divide dois números e ajusta o resultado conforme os algarismos significativos.
    if numero2 == 0:                                                                    # Verifica se o divisor é zero
        raise ValueError("Divisão por zero não é permitida.")                           # lança uma exceção para evitar erro matemático.
    
    algarismo = verificar_menor_algarismos_significativos(numero1, numero2)             # Determina o menor número de algarismos significativos entre os dois valores.
    resultado = numero1 / numero2                                                       # Realiza a divisão.
    casas_deci = casas_para_arredondar(resultado, algarismo)                            # Conta o numero de casas decimais necessarios para o arredondamento respeitando o numero de algarismos significativos
    resultado = arredondar_ABNT(resultado, casas_deci)                                  # Aplica o arredondamento conforme a norma.
    return resultado 

def soma_ABNT(numero1, numero2):                                                       # Realizar a soma de dois números e arredondar o resultado com base no menor número de casas decimais entre os dois operandos, conforme as normas da ABNT.
    casas_deci = menor_casas_decimais(numero1, numero2)                                # Função auxiliar que retorna o menor número de casas decimais entre os dois números.
    resultado = numero1 + numero2                                                      # Realiza a soma normalmente.
    resultado = arredondar_ABNT(resultado, casas_deci)                                 # Arredonda o resultado para o número de casas decimais determinado no passo anterior.
    return resultado                                                                   # Retorna o valor final, já arredondado.

def subtrai_ABNT(numero1, numero2):                                                    # Realizar a subtração de dois números e aplicar o arredondamento conforme o menor número de casas decimais entre os operandos.
    casas_deci = menor_casas_decimais(numero1, numero2)                                # Determina a precisão decimal do resultado com base no menor número de casas decimais dos dois números.
    resultado = numero1 - numero2                                                      # Executa a subtração.
    resultado = arredondar_ABNT(resultado, casas_deci)                                 # Aplica o arredondamento conforme a norma.
    return resultado                                                                   # Retorna o valor final ajustado.

def arredondar_ABNT(numero, casas_decimais):
    fator = 10 ** casas_decimais
    numero_ajustado = numero * fator
    inteiro = int(numero_ajustado)
    resto = numero_ajustado - inteiro

    # Caso especial: exatamente 0.5
    if abs(resto - 0.5) < 1e-12:
        if inteiro % 2 == 0:  # último algarismo par → mantém
            return inteiro / fator
        else:                 # último algarismo ímpar → arredonda para cima
            return (inteiro + 1) / fator
    elif resto < 0.5:         # menor que 5 → mantém
        return inteiro / fator
    else:                     # maior que 5 → arredonda para cima
        return (inteiro + 1) / fator
          

# --- Multiplicicação e divisão
        

def verificar_menor_algarismos_significativos(numero1, numero2):                # Determina qual dos dois números tem menos algarismos significativos.
    
    algarismos1 = f"{numero1:.15g}".strip().replace('.', '').lstrip('0')        # Formata o número com até 15 dígitos significativos, remove o ponto decimal e zeros à esquerda.
    algarismos1 = len(algarismos1)
    
    algarismos2 = f"{numero2:.15g}".strip().replace('.', '').lstrip('0')        # Repete o processo para o segundo número.
    algarismos2 = len(algarismos2)
    
    return min(algarismos1, algarismos2)                                        # Retorna o menor número de algarismos significativos entre os dois.

def casas_para_arredondar(numero, algarismos_significativos):                   # Calcula quantas casas decimais são necessárias para manter o número com os algarismos significativos desejados.
    if numero == 0:                                                             # Zero não tem ordem de magnitude definida, então retorna 0.
        return 0
    ordem_magnitude = int(math.floor(math.log10(abs(numero))))                  # Usa logaritmo para determinar a ordem de magnitude do número.
    casas_decimais = algarismos_significativos - 1 - ordem_magnitude            # Calcula quantas casas decimais são necessárias para preservar os algarismos significativos.
    return max(0, casas_decimais)

    
# --- Soma e Subtração 

def menor_casas_decimais(num1, num2):                                           # Determina o numero de casas decimais de dois numeros e retorna o menor entre eles
    casas1 = len(str(num1).split(".")[1]) if "." in str(num1) else 0            # Verifica se há parte decimal e conta os dígitos após o ponto.
    casas2 = len(str(num2).split(".")[1]) if "." in str(num2) else 0            # Verifica se há parte decimal e conta os dígitos após o ponto.
    return min(casas1, casas2)


print(soma_ABNT(4.11, 1))       # Esperado: 5.1
print(subtrai_ABNT(10.55, 2.3)) # Esperado: 8.3
print(arredondar_ABNT(4.55, 1)) # Esperado: 4.6
print(arredondar_ABNT(4.45, 1)) # Esperado: 4.4
print(arredondar_ABNT(5.1328, 2)) # Esperado: 5.13
print(arredondar_ABNT(1.236, 2))  # Esperado: 1.24
