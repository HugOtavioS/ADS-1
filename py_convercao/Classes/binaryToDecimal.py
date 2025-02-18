from  Interfaces.BinaryToDecimalInterface import BinaryToDecimalInterface

class BinaryToDecimal():
    def binaryToDecimal(self, valor):
        if type(valor) != str or not all(bit in '01' for bit in valor):
            return "Valor deve ser uma string representando um número binário"

        decimal = 0
        for i, bit in enumerate(reversed(valor)):
            decimal += int(bit) * (2 ** i)

        return decimal