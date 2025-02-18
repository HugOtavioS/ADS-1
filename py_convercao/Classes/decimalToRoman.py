from Interfaces.DecimalToRomanInterface import DecimalToRomanInterface

class DecimalToRoman:
    def decimalToRoman(self, valor):
        if type(valor) != int:
            return "Valor deve ser um número inteiro"

        numRoman = []

        i = len(self.roman) - 1
        for rom in self.roman:
            while valor - self.roman[i][1] >= 0:
                valor = valor - self.roman[i][1]
                numRoman.append(self.roman[i][0])
                if valor == 0:
                    break
            i -= 1

        i = 0
        c = len(self.roman) - 1
        for rom in self.roman:
            if numRoman.count(self.roman[c][0]) > 3:
                index = numRoman.index(self.roman[c][0])
                while numRoman.count(self.roman[c][0]) != 0:
                    numRoman.pop(numRoman.index(self.roman[c][0]))
                numRoman.insert(index, self.roman[c][0])
                numRoman.insert(index + 1, self.roman[c + 1][0])
            c -= 1

        return numRoman