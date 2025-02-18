class DecimalToRomanInterface():
    def decimalToRoman(self, valor):
        if type(valor) != int:
            raise ValueError("Método não implementado")