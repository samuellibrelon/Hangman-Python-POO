# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra.lower() # Palavra Secreta 
        self.letras_certas = ["_"] * len(palavra) # Estado da Palavra adicionada
        self.letras_erradas = [] # Lista de letras erradas
        self.tentativas = 0 # Contador de erros
        
	# Método para adivinhar a letra
    def advinhaLetra(self, letra):
        letra = letra.lower()
        if letra in self.palavra:
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.letras_certas[i] = letra
        else:
            if letra not in self.letras_erradas:
                self.letras_erradas.append(letra)
                self.tentativas += 1
        
	# Método para verificar se o jogo terminou
    def verificaJogoTerminou(self):
        return self.tentativas >= len(board) -1 or "_" not in self.letras_certas
        
	# Método para verificar se o jogador venceu
    def verificaSeJogadorVenceu(self):
        return "_" not in self.letras_certas
        
	# Método para checar o status do game e imprimir o board na tela
    def checaStatusImprimeBoard(self):
        print(board[self.tentativas])
        print("Palavra:", " ".join(self.letras_certas))
        print("Letras erradas:", ", ".join(self.letras_erradas))

def jogar():
    palavras = ["python", "java", "ruby", "javascript", "kotlin"]
    palavra_secreta = random.choice(palavras)
    jogo = Hangman(palavra_secreta)

    while not jogo.verificaJogoTerminou():
        jogo.checaStatusImprimeBoard()
        letra = input("\nDigite uma letra: ").strip().lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.\n")
            continue

        jogo.advinhaLetra(letra)

    if jogo.verificaSeJogadorVenceu():
        print("\nPalavra correta: ",palavra_secreta)
        print("\nParabéns! Você venceu! 🎉")
    else:
        print("\nGame Over! A palavra era:", palavra_secreta)

# Iniciar o jogo
if __name__ ==  "__main__":
    jogar()