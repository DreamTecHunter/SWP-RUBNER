class Node:
    def __init__(self):
        self.content = None
        self.next_node = None


class SimpleLinkedList:
    def __init__(self):
        self.first_node = None  # auch bekannt als "Head"

    # TODO: Eigentlich wollen wir, dass wenn eine weitere Box hinzugefügt wird, die alte Box bestehen bleibt
    # Das machen wir indem die erste box auf diese neue box "zeigt"
    def append(self, value):  # habe meinen Teddybär denn ich verpacken und in den kasten stellen will
        node = Node()  # ich baue mir meine box wo der Teddy rein "SOLL"
        node.content = value  # ich packe meinen Teddy in die box
        # if first_none ist Null dann
        if self.first_node is None:
            self.first_node = node  # ich packe die box and die stelle "first_node"
        else:
            self.get_last_node().next_node = node
        # node.next_node = Node()

    # mit dieser methode holt sich das object simpleLinkedList
    # den nächsten Knoten/Node und überschreibt den first_node/head
    def next(self):
        node = self.first_node
        next_node = node.next_node
        self.first_node = next_node
        # self.first_node = self.first_node.next_node # vereinfacht

    def has_next(self):
        # wenn es keinen ersten knoten gibt, gibt es auch keine weiteren knoten
        if self.first_node is None:
            return False
        # wenn doch, dann schauen wir, ob es keine nächsten knoten gibt
        if self.first_node.next_node is None:
            return False
        # sonst gibt es einen nächsten knoten
        return True

    def get(self):
        node = self.first_node
        value = node.content
        return value

    def get_last_node(self):
        return self.first_node

    def size(self):
        pass


if __name__ == '__main__':
    sll = SimpleLinkedList()
    # print(sll.first_node)
    sll.append("Teddy")
    # print(sll.first_node)
    # print(sll.get())
    sll.append("Teddy2")
    # print(sll.get())
    # ich will die linkedlist durch-iterieren (unvollständig programmier)
    """
    while sll.has_next():
        print(sll.get())
        sll.next()
    # ist gleich dem was hier kommt
    go_next = True
    while go_next:
        print(sll.get())  # anschauen
        sll.next()  # hingehen
        go_next = sll.has_next()  # schauen ob es was zum hingehen gibt

    go_next = True
    """
    while go_next:
        print(sll.get())  # anschauen
        go_next = sll.has_next()  # schauen ob es was zum hingehen gibt
        sll.next()  # hingehen
# Zusatz: Schreibe eine Main, in der eine SimpleLinkedList mit 10 Sachen befüllt wird und die dann mit einer
# "do-"While-Schleife angeschaut werden (Achtung: Reihenfolge von next und has_next- MEthode beachten)
"""
do{
    print(sll.get())
    sll.next()
}while(has_next())
"""

# do-while-Schleife
check_value = True
while check_value:
    print("do sth")
    check_value = False  # eine Abfrage/ bool'scher Ausdruck,
    # welche wenn er False ist check_value auf False setzt und somit die while-Schleife beende
