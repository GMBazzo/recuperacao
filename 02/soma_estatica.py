class Soma_estatica:

    @staticmethod
    def soma(numeros):
        resultado = 0
        for numero in numeros:
            resultado = resultado + numero
        return resultado
