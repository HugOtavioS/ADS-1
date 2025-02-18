from Interfaces.OperRomanInterface import OperRomanInterface

class DecimalToRoman:
    def operRoman(self, valor):
        i = -1
        while i < int(len(valor) - 1):
            c = -1
            while c < len(self.roman):
                if valor[i] == self.roman[c][0]:
                    valor[i] = self.roman[c][1]
                c += 1
            i += 1

        res = 0
        i = 0
        while i < int(len(valor) - 1):
            if valor[i] >= valor[i + 1]:
                res = res + valor[i]
            elif valor[i] < valor[i + 1]:
                res = res - valor[i]
            i += 1
        res = res + valor[len(valor) - 1]

        return res