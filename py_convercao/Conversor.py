from Classes.binaryToDecimal import BinaryToDecimal
from Classes.binaryToRoman import BinaryToRoman
from Classes.decimalToBinary import DecimalToBinary
from Classes.decimalToRoman import DecimalToRoman

class Conversor(
    BinaryToDecimal,
    BinaryToRoman,
    DecimalToBinary,
    DecimalToRoman
):

    roman = [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000]
    ]

    def decimalToRoman(self, valor):
        return super().decimalToRoman(valor)
    
    def operRoman(self, valor):
        return super().operRoman(valor)
    
    def decimalToBinary(self, valor):
        return super().decimalToBinary(valor)
    
    def binaryToDecimal(self, valor):
        return super().binaryToDecimal(valor)

    def binaryToRoman(self, valor):
        return super().binaryToRoman(valor)

print(Conversor().decimalToBinary(26))
print(Conversor().binaryToRoman("11010"))