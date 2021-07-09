# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.


class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        
    def __cmp__(self, livro):
        return cmp(self.codigo, livro.codigo)
        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)

    def livrosOrdenadosPeloNome(self, lista):
        for i in range(len(lista)):
            trocou = False
            
            for j in range(len(lista) - i - 1):
                if lista[j].nome > lista[j+1].nome:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                break
        return lista

        


def main():
    entrada = input().split('\t')
    num_livros = int(entrada[0])
    lista_livros = entrada[1:]
    b = Biblioteca()

    count = 0
    while count < len(lista_livros):
        codigo = int(lista_livros[count])
        nome = lista_livros[count+1]
        autor = lista_livros[count+2]
        b.inserir(Livro(codigo, nome, autor))
        count += 3

    # ordenando as listas de livros disponiveis e alugados
    disponiveis_ordenada = b.livrosOrdenadosPeloNome(b.disponiveis)
    alugados_ordenada = b.livrosOrdenadosPeloNome(b.alugados)

    # mesclando ambas as listas
    i = 0
    j = 0
    lista_mesclada = []

    while i < len(disponiveis_ordenada) and j < len(alugados_ordenada):
        if disponiveis_ordenada[i].nome < alugados_ordenada[j].nome:
            lista_mesclada.append(disponiveis_ordenada[i])
            i = i+1

        else:
            lista_mesclada.append(alugados_ordenada[j])
            j = j+1

    while i < len(disponiveis_ordenada):
        lista_mesclada.append(disponiveis_ordenada[i])
        i = i+1

    while j < len(alugados_ordenada):
        lista_mesclada.append(alugados_ordenada[j])
        j = j+1


    for i in range(num_livros):
        if i == num_livros - 1:
            print(lista_mesclada[i].codigo, end='')
        else:
            print(lista_mesclada[i].codigo, end=' ')
main()





