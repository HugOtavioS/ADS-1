class Conversor():

    roman = [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000]
    ]

    def decToRoman(self, valor):
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
    
    def decToBinary(self, valor):
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
    
    def binToDecimal(self, valor):
        if type(valor) != str or not all(bit in '01' for bit in valor):
            return "Valor deve ser uma string representando um número binário"

        decimal = 0
        for i, bit in enumerate(reversed(valor)):
            decimal += int(bit) * (2 ** i)

        return decimal

    def binToRoman(self, valor):
        decimal = self.binToDecimal(valor)
        if isinstance(decimal, str):  # Se retornar uma mensagem de erro
            return decimal
        
        return self.decToRoman(decimal)

# print(Conversor().decToRoman(26))
print(Conversor().decToBinary(26))
print(Conversor().binToRoman("11010"))