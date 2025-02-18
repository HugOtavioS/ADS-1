from Interfaces.DecimalToBinaryInterface import DecimalToBinaryInterface

class DecimalToBinary:
    def decimalToBinary(self, valor):
        if type(valor) != int:
            return "Valor deve ser um número inteiro"

        if valor < 0:
            return "Valor deve ser um número inteiro não negativo"

        binary = ""
        if valor == 0:
            binary = "0"
        else:
            while valor > 0:
                binary = str(valor % 2) + binary
                valor = valor // 2

        return binary