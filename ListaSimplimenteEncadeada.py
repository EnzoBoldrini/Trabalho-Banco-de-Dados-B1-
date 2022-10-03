# This Python file uses the following encoding: utf-8

class ListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode  # None self.antNode = None

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


# Lista Simplesmente Encadeada com Iterador
class SinglyLinkedListIterator:  # LinkedList

    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode = firstNode
        self.iterator = firstNode
        if firstNode:
            self.size = 1
        else:
            self.size = 0

    def getSize(self):
        return self.size

    def get_firstNode(self):
        return self.firstNode

    def get_lastNode(self):
        return self.lastNode

    def get_iterator(self):
        return self.iterator

    def setSize(self, size):
        self.size = size

    def addNode(self, data):  # attach or anexar um Node depois do iterador:
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh depois do iterador. O iterador fica sobre este Noh
        """
        newNode = ListNode(data, None)  # treats the empty list ; trata a lista vazia
        newNode.nextNode = None
        if (self.size == 0):  # treats the empty list ; trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:  # iterator is on the last element ; o iterador está no último elemento
            self.lastNode.nextNode = newNode  # este Noh para a ser agora o ultimo Noh
            self.iterator = newNode
            self.lastNode = newNode  # por o ponteiro lastNode sobre o ultimo Noh
        else:  # iterator is on an inner element ; o iterador está em algum elemento interno
            newNode.nextNode = self.iterator.nextNode  # novo Noh aponta para o noh seguinte do iterador
            self.iterator.nextNode = newNode  # faz o prox do no sob o iterador apontar para o novo no
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

    def insNode(self, data):  # insere um Node antes do iterador
        """Pre condicao: Iterador definido
           Pos condicao: O data eh inserido em um Noh antes do iterador. O iterador fica sobre este Noh.
        """
        newNode = ListNode(data, None)  # treats the empty list ; trata a lista vazia
        newNode.nextNode = None
        if (self.size == 0):  # treats the empty list ; trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.firstNode:  # iterator is on the first element ; o iterador está no primeiro elemento
            newNode.nextNode = self.firstNode  # o novo noh aponta para o antigo primeiro noh
            self.firstNode = newNode  # firstNode aponta para o novoNoh que passa a ser o primeiro noh
            self.iterator = newNode  # o iterador fica sob o novoNoh que foi inserido
        else:  # iterator is on an inner element ; o iterador está em algum elemento interno
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            newNode.nextNode = self.iterator  # novo Noh aponta para o noh onde esta o iterador
            currentNode.nextNode = newNode  # o campo nextNode do noh corrente aponta para o novo no
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

        # o nextNode do noh 4 vai apontar para o noh com o 5
        # self.iterator.antNode.nextNode = newNode
        # newNode.antNode = self.iterator.antNode
        # newNode.nextNode = self.iterator
        # self.iterator.antNode = newNode
        # self.iterator = newNode

    def elimNode(self):  # elimina o elemento que está sobre o iterador e avanca o iterador para proximo Noh.
        if (self.iterator == self.firstNode):  # iterador sobre o primeiro elemento
            if (self.lastNode == self.firstNode):  # tem so um Noh
                self.lastNode = None  # aponta para nada
                self.firstNode = None
                self.iterator = None
            else:  # tem mais de um Node
                # self.firstNode = self.firstNode.nextNode # firstNode aponta para o proximo noh que passa a ser o primeiro
                self.firstNode = self.firstNode.nextNode  # self.iterator.nextNode
                self.iterator.nextNode = None  # isola o Noh
                self.iterator = self.firstNode  # avanca para o proximo Noh
        else:  # iterator pode estar sob o ultimo ou um elemento interno
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            if self.iterator == self.lastNode:  # o iterador esta sob o ultimo:
                # por lastNode sob o penultimo elemento: percorrer a lista ate parar antes do iterador
                # para tal usar um ponteiro auxiliar currentNode
                self.lastNode = currentNode  # o penultimo(currentNode) agora passa a ser o ultimo Noh
                self.iterator.nextNode = None  # isola o Node
                self.iterator = None  # iterador fica indefinido
                currentNode.nextNode = None  # ultimo Node nao tem proximo
            else:  # iterador sobre elemento intermediario
                currentNode.nextNode = self.iterator.nextNode  # o noh anterior ao que sera eliminado aponta para o seguinte deste noh
                currentNode = self.iterator  # guarda o Noh que vai ser eliminado
                self.iterator = self.iterator.nextNode  # avanca o iterador para o proximo noh
                currentNode.nextNode = None  # isola o noh
        self.size = self.size - 1  # decrementa o tamanho da lista
        return True

    def first_Node(self):  # coloca o iterador sobre o primeiro Node da Lista
        self.iterator = self.firstNode
        return True

    def last_Node(self):  # coloca o iterador sobre o útlimo Node da Lista
        self.iterator = self.lastNode
        return True

    def nextNode(self):  # avança o iterador uma posição. para tal o iterador deve estar definido(sobre um Noh)
        if (self.iterator):
            self.iterator = self.iterator.nextNode
        return True

    # def antNode(self):

    def posNode(self, position):  # coloca o iterador sobre a posição position
        """o iterador eh posto sobre o Nod da posicao que vai de 1 ate size.
           qualquer outro valor leva o iterador a ficar indefinido(None)
           Return True para posicao valida e False para iterador indefinido
        """
        if (position > 0 and position <= self.size):
            i = 1
            self.iterator = self.firstNode  # poe o iterador sob o primeiro Node
            while (i < position):
                if (self.iterator.nextNode != None):
                    self.iterator = self.iterator.nextNode
                    i = i + 1
            return True
        else:
            return False

    def isUndefinedIterator(self):  # retorna verdadeiro se o iterador estiver indefinido
        if (self.iterator == None):
            return True
        else:
            return False

    def printNode(self):
        curr = self.firstNode
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


if __name__ == '__main__':

    # def printLista2(Lista):
    #     currentNode = Lista.firstNode
    #     while currentNode:
    #         print(currentNode.data)
    #         currentNode = currentNode.getNextNode()
    #         #currentNode = currentNode.nextNode

    novo_noh = ListNode(5)
    novo_noh.setData(10)
    lista22 = SinglyLinkedListIterator(novo_noh)
    lista = SinglyLinkedListIterator()
    lista.addNode(10)
    lista.addNode(20)
    lista.addNode(30)
    lista.addNode(40)


    def printLista(lista):
        lista.first_Node()  # por o iterador sobre o primeiro elemento
        while not lista.isUndefinedIterator():
            # print(lista.get_iterator().getData(), end=" ")
            print(lista.get_iterator().getData())
            # print("teste", end=" ")
            # lista.iterator.data
            lista.nextNode()  # avanca iterador para proximo noh
            # lista.iterator = lista.iterador.nextNode
        print('\n')

"""1) Verificar se duas listas são iguais. Duas listas são iguais se ambas as estruturas têm o mesmo 
número de elementos, e estes são iguais um a um. Em particular, duas listas vazias são iguais. 
int iguaisListas(Lista lst1, Lista lst2){...} """


# nova implementacao
def iguais_listas(lst1, lst2):
    if (lst1.size != lst2.size):  # listas com o mesmo tamanho
        return False
    else:  # lst1 e lst2 tem o mesmo tamanho
        # por o iterador sobre o primeiro no
        lst1.first_Node()  # lst1.iterator = lst1.firstNode
        lst2.first_Node()
        # loop para percorrer a lista
        while not lst1.undefinedIterator():
            # verificar se os elementos sob o iterador são diferentes
            if (lst1.iterator.data != lst2.iterator.data):
                return False
            else:  # avanca o iterador para o proximo No
                lst1.nextNode()
                lst2.nextNode()
        # as duas lista sao iguais
        return True


def iguaisListas(lst1, lst2):
    if lst1.getSize() != lst2.getSize():  # as listas tem tamanhos diferentes
        return False  # lst1.size != lst2.size
    else:
        nodeLst1 = lst1.firstNode  # lst1.get_firstNode()
        nodeLst2 = lst2.firstNode  # lst2.get_firstNode()
        while nodeLst1:
            if (nodeLst1.data != nodeLst2.data):
                return False
            else:
                nodeLst1 = nodeLst1.getNextNode()
                nodeLst2 = nodeLst2.getNextNode()
        return True


"""6) Adiciona o elemento elem no final de lst: 
void adicLista( Lista lst, TipoL elem){...} """


# lista vazia
# lista cheia
def adicionar_final_lista(lst1, data):
    if (lst1.size == 0):  # lista vazia
        lst1.addNode(data)
    else:  # lista cheia
        lst1.last_Node()  # ponho iterador sobre ultimo no
        lst1.addNode(data)  # adiciono o elemento data


def adicLista(lst1, data):
    lst1.last_Node()  # iterator sobre o ultimo elemento
    lst1.addNode(data)


def insLista(lst1, data):  # insere um elemento no inicio da lista
    lst1.first_Node()  # iterator sobre o primeiro elemento
    lst1.insNode(data)


def concat_lista(lst1, lst2):  # concatenar a lst2 no final da lst1
    # lst1: por o iterador sobre o ultimo elemento
    lst1.last_Node()
    # lst2: por o iterador sobre o primeiro elemento
    lst2.first_Node()
    # loop para percorrer a lista 2:
    while not lst2.undefinedIterator():
        # adicionar o elmento do iterador da lista 2 na lista 1
        lst1.addNode(lst2.iterator.data)
        lst2.nextNode()  # avancar o iterador da lista 2


def concatLista(lst1, lst2):  # concatenar a lst2 no final da lst1
    # newNode = ListNode(None)
    lst1.last_Node()  # iterator da lista1 sobre o ultimo elemento
    lst2.first_Node()  # iterator da lista2 sobre o primeiro elemento
    # nodeLst2 = lst2.get_iterator() # li o node do iterador
    while not lst2.isUndefinedIterator():  # enquanto o iterador nao ficar indefinido(None)
        newNode = lst2.get_iterator()
        # print('valor do no= {}'.format(newNode.getData()))
        lst1.addNode(
            newNode.getData())  # lst2.get_iterator().getData()  adiciona o node na lista 1 e o iterador da lista 1 fica sobre este noh
        lst2.nextNode()  # avanco o iterador da lst2 para o proxima no


"""verfica se data esta na lista"""


def esta_na_lista(lst: SinglyLinkedListIterator, data):
    # verificar se a lista esta vazia
    if (lst.size == 0):
        return False
    else:  # lista esta cheia: o elemento pode estar na lista
        # por o iterador sobre o primeiro elemento
        lst.first_Node()
        # loop para percorrer a lista
        while not lst.isUndefinedIterator():
            # verifica se o elemento esta no noh
            if lst.iterator.data == data:
                return True
            else:  # avanca o iterador
                lst.nextNode()
        # elemento nao esta na lista
        return False


def esta_na_lista_hardcoded(lst: SinglyLinkedListIterator, data):
    # verificar se a lista esta vazia
    if (lst.size == 0):
        return False
    else:  # lista esta cheia: o elemento pode estar na lista
        # por o iterador sobre o primeiro elemento
        lst.iterator = lst.firstNode
        # loop para percorrer a lista
        while lst.iterator != Null:
            # verifica se o elemento esta no noh
            if lst.iterator.data == data:
                return True
            else:  # avanca o iterador
                lst.iterator = lst.iterator.nextNode
        # elemento nao esta na lista
        return False


def estaNaLista(lst: SinglyLinkedListIterator, data):
    if lst.getSize() == 0:  # lista vazia lst.size == 0
        return False
    else:  # lista cheia
        lst.first_Node()  # iterador sobre o primeiro elemento
        while not lst.isUndefinedIterator():  # lst.iterator
            if lst.get_iterator().getData() == data:  # lst.iterator.data == data
                return True
            else:
                lst.nextNode()
        return False  # iterator saiu da lista(indefinido): iterator == None


"""verifica se a lista esta ordenada de forma crescente"""


def estaOrdenada(lst: SinglyLinkedListIterator):
    if lst.getSize() == 0:  # lista vazia
        return True
    elif lst.getSize() == 1:  # lst.size == 1
        return True
    else:  # lst tem 2 ou mais elementos: comparar o anterior com proximo
        lst.first_Node()
        while lst.get_iterator().getNextNode():  # lst.iterator.nextNode
            if (lst.get_iterator().getData() > lst.get_iterator().getNextNode().getData()):
                return False
            lst.nextNode()
        return True


# lst.iterator.data > lst.iterator.nextNode.data

# 4) Verificar se uma lista lst2 está contida numa lista lst1.
# Para tal, todos os elementos de lst2 devem estar em lst1,
# mesmo em ordem diferente.
# int contidaLista(Lista lst1, Lista lst2){...}
# True ou False
# Python: def contidaLista(lst1, lst2):{...}

# lst2: < 2, 40, [30]>
# lst1: <[2], [30]>[]

# caso 0: as duas listas sao vazias: return True
# caso 1: lst1 nao tem o elmento: return False
# implica o iterador da lista lst1 ficar indefinido

# caso 2: lst1 tem o elemento: verificar o proximo elemento de lst2
# se o iterador na lista lst1 ficar indefinido, quer dizer que eu
# percorri todos os elementos de lst2, e todos estavam na lista lst1,
# ou seja, o caso 1 nao aconteceu.

def contidaLista(lst1, lst2):
    # caso 0: as duas listas sao vazias
    if (lst1.size == 0 and lst2.size == 0):
        return True
    elif (lst1.size == 0 and lst2.size != 0):
        return False
    elif (lst1.size != 0 and lst2.size == 0):
        return False
    elif (lst1.size < lst2.size):
        return False
    else:
        # percorrer a lista lst2
        lst2.first_Node()  # iterador sobre o primeiro elemento
        while not lst2.isUndefinedIterator():
            elem = lst2.get_iterator().getData()  # li o elemento de lst2
            # elem = lst2.iterator.data
            # percorrer a lista lst1
            lst1.first_Node()
            while not lst1.isUndefinedIterator():
                if lst1.get_iterator().getData() != elem:
                    lst1.nextNode()  # avanca para o proximo node
                    if lst1.isUndefinedIterator():
                        return False
                else:
                    # avancar o iterador de lst2 para o proximo
                    # lst2.nextNode()
                    break
            # se o iterador de lst1 estiver indefinido: saiu da lista
            # e nao encontrou elem
            # if lst1.isUndefinedIterator():
            #     return False
            # avancar o iterador de lst2 para o proximo
            lst2.nextNode()
        if lst2.isUndefinedIterator():
            return True  # encontrou todos os elementos
        else:
            return False

        # inverter uma lista lst, destruindo a lista original


# lst < >
# lstInv <    [60], 50, 40, 3 >
# lista vazia: retornar uma lista vazia
# lista tiver so um ou mais elementos: retorna uma lista invertida com um ou mais elementos
# e a lista lst ficará sem elementos
#
def invLista(lst: SinglyLinkedListIterator):
    lstInv = SinglyLinkedListIterator()
    # por o iterador sobre o primeiro elemento da lista lst
    lst.first_Node()
    while (lst.iterator):
        # inserir o elemento na lista lstInv
        lstInv.insNode(lst.get_iterator().getData())  # lst.iterator.data
        lst.elimNode()  # nao destruir a lista original: lst.nextNode()
    return lstInv