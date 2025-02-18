class BinaryToRomanInterface():
    def binaryToRoman(self, valor):
        if type(valor) != int:
            raise ValueError("Método não implementado")