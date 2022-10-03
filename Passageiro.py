class Passageiro:
    def __init__(self, nome, sobrenome, rg, cpf, endereco, tel_celular, tel_fixo, status_voo, assento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.rg = rg
        self.cpf = cpf
        self.endereco = endereco
        self.tel_celular = tel_celular
        self.tel_fixo = tel_fixo
        self.status_voo = status_voo
        self.assento = assento


class ListNode:
    def __init__(self, data):
        self.data = data
        self.antNode = None
        self.nextNode = None


class DoubleLinkedListIterator:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.iterator = None
        self.size = 0

    # Representa o tamanho do nosso objeto criado
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

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

    def addNode(self, data):  # anexar um Node depois do iterador:

        newNode = ListNode(data)

        if self.size == 0:  # trata a lista vazia
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        elif self.iterator == self.lastNode:  # o iterador está no último elemento
            self.lastNode.nextNode = newNode  # este Noh para a ser agora o ultimo Noh
            # ou self.lastNode Linha para fazer a lista ser duplamente encadeada
            newNode.antNode = self.iterator
            self.iterator = newNode
            self.lastNode = newNode  # por o ponteiro lastNode sobre o ultimo Noh
        else:  # iterator is on an inner element ; o iterador está em algum elemento interno
            # novo Noh aponta para o noh seguinte do iterador
            newNode.nextNode = self.iterator.nextNode
            newNode.antNode = self.iterator
            self.iterator.nextNode.antNode = newNode
            # faz o prox do no sob o iterador apontar para o novo no
            self.iterator.nextNode = newNode
            self.iterator = newNode  # por o iterador sob o novo no

        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
        return True

    def insNode(self, data):
        """ Acrescenta um novo no a lista. """
        # Cria um novo noh apontando para None (anterior e proximo)
        newNode = ListNode(data, None, None)

        # Se a cabeca eh None a lista esta vazia
        # Tanto a cabeca quanto o rabo recebem o novo no
        if self.size:
            self.iterator = newNode
            self.firstNode = newNode
            self.lastNode = newNode
        # Caso contrario, se ja existir algum valor na lista

        elif self.iterator == self.firstNode:  # o iterador está no primeiro elemento
            newNode.nextNode = self.firstNode  # o novo noh aponta para o antigo primeiro noh
            # firstNode aponta para o novoNoh que passa a ser o primeiro noh
            self.firstNode = newNode
            self.iterator = newNode

        else:
            currentNode = self.firstNode  # aponta para o primeiro noh da lista
            while currentNode.nextNode != self.iterator:  # percorrer a lista e parar uma posicao antes do iterador
                currentNode = currentNode.nextNode  # avanca para o proximo noh
            newNode.nextNode = self.iterator  # novo Noh aponta para o noh onde esta o iterador
            # o campo nextNode do noh corrente aponta para o novo no
            currentNode.nextNode = newNode
            self.iterator = newNode  # por o iterador sob o novo no
        self.size += 1  # incrementa o contador e retorna true pois teve sucesso na adicao
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

    def elimNode(self, data):
        """ Remove um no da lista. """
        # O no atual eh o primeiro no da lista
        self.iterator = self.firstNode

        # Vamos procurar pelo dado que queremos remover
        # Equanto o no atual for valido
        while self.iterator is not None:
            # Verifica se eh o dado que estamos buscando
            if self.iterator.data == data:
                # Se o dado que estamos buscando esta no primeiro no
                # da lista, nao temos anterior
                if self.iterator.antNode is None:
                    # A cabeca 'aponta' para o proximo no da lista
                    self.firstNode = self.iterator.nextNode
                    # E o anterior do proximo no aponta para None
                    self.iterator.nextNode.antNode = None
                else:
                    # Exemplo: Removendo o valor 5
                    # ... <---> | 2 | <---> | 5 | <---> | 12 | <---> ...
                    #
                    # O proximo do valor 2 passa a apontar para o 12 e
                    # o anterior do valor 12 passa a apontar para o 2
                    #                     ---------------
                    # ... <---> | 2 | <---|--- | 5 | ---|---> | 12 | <---> ...
                    self.iterator.antNode.nextNode = self.iterator.nextNode
                    self.iterator.nextNode.antNode = self.iterator.antNode

            # Se nao eh o no que estamos buscando va para o proximo
            self.iterator = self.iterator.nextNode

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

    # retorna verdadeiro se o iterador estiver indefinido
    def isUndefinedIterator(self):
        if (self.iterator == None):
            return True
        else:
            return False

    def printNode(self):
        print("Lista Duplamente Encadeada:")
        curr = self.firstNode
        while curr:
            print(curr.data)
            curr = curr.nextNode
        print("=" * 80)


class Queue:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.size = 0

    def push(self, elem):
        # Insere um elemento na fila
        newNode = ListNode(elem)
        if self.lastNode is None:  # Se estiver vazio
            self.lastNode = newNode
        else:  # Se já tiver elem
            self.lastNode.nextNode = newNode  # Estamos linkando os elems
            self.lastNode = newNode

        if self.firstNode is None:
            self.firstNode = newNode

        self.size = self.size + 1

    def pop(self):
        # Remove o elemento do topo da fila, por isso não passa parâmetro elem
        if self.size > 0:
            elem = self.firstNode.data  # Vai associar o valor do primerio ao elem
            self.firstNode = self.firstNode.nextNode  # Vai empurrar o primeiro pro próximo
            self.size = self.size - 1  # Vai diminuir o tamanha da fila
            return elem  # Retorna elemento excluído
        raise IndexError("The queue is empty")

    def peek(self):
        # Retorna o topo da fila sem remover
        if self.size > 0:
            elem = self.firstNode.data  # Vai associar o valor do primerio ao elem
            return elem  # Retorna o valor do primeiro elem da fila
        raise IndexError("The queue is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size

    def __repr__(self):
        if self.size > 0:
            r = ""
            iterator = self.firstNode
            while (iterator):
                r = r + str(iterator.data) + " "
                iterator = iterator.nextNode  # Avança até chegar no último nó
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()

    # '__main__'


lista = DoubleLinkedListIterator()

lista.addNode(2)
lista.printNode()

lista.addNode(5)
lista.printNode()

lista.addNode(12)
lista.printNode()

lista.addNode(20)
lista.printNode()

lista.elimNode(12)
lista.printNode()

lista.elimNode(5)
lista.printNode()