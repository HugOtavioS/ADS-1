from Interfaces.BinaryToRomanInterface import BinaryToRomanInterface

class BinaryToRoman():
    def binaryToRoman(self, valor):
        decimal = self.binaryToDecimal(valor)
        if isinstance(decimal, str):  # Se retornar uma mensagem de erro
            return decimal
        
        return self.decimalToRoman(decimal)