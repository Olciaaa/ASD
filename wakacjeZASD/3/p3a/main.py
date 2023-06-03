from egzP3atesty import runtests

class Node:
    def __init__(self, wyborcy: int, koszt: int, fundusze: int):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze

    def __str__(self) -> str:
        return f'Node({self.wyborcy}, {self.koszt}, {self.fundusze})'


def dynamik(TablicaPom: list, head: Node, fundusze: int, index: int) -> int:
    if TablicaPom[index][fundusze] != -1:
        return TablicaPom[index][fundusze]
    if head.next is None:
        if head.koszt <= fundusze:
            TablicaPom[index][fundusze] = head.wyborcy
        else:
            TablicaPom[index][fundusze] = 0
        return TablicaPom[index][fundusze]
    option1 = dynamik(TablicaPom, head.next, fundusze, index + 1)
    option2 = 0
    if fundusze - head.koszt >= 0:
        option2 = dynamik(TablicaPom, head.next, fundusze - head.koszt, index + 1) + head.wyborcy
    TablicaPom[index][fundusze] = max(option1, option2)
    return TablicaPom[index][fundusze]


def policzN(head: Node) -> int:
    n = 0
    while head is not None:
        n += 1
        head = head.next
    return n


def wybory(T: list) -> int:
    lacznaLiczbaGlosow = 0
    for head in T:
        head_tmp = head
        n = policzN(head_tmp)
        TablicaPom = [[-1 for _ in range(head.fundusze + 1)] for _ in range(n)]
        lacznaLiczbaGlosow += dynamik(TablicaPom, head, head.fundusze, 0)
    return lacznaLiczbaGlosow


if __name__ == '__main__':
    # wyb1ok1 = Node(3, 8, 15)
    # wyb1ok2 = Node(2, 7, 15)
    # wyb1ok3 = Node(4, 5, 15)
    # wyb1ok1.next = wyb1ok2
    # wyb1ok2.next = wyb1ok3
    # wyb2ok1 = Node(4, 7, 8)
    # wyb2ok2 = Node(5, 2, 8)
    # wyb2ok1.next = wyb2ok2
    # wyb3ok1 = Node(3, 5, 10)
    # wyb3ok2 = Node(3, 5, 10)
    # wyb3ok1.next = wyb3ok2
    # T = [wyb1ok1, wyb2ok1, wyb3ok1]
    # print(wybory(T))
    # Wywołanie wybory( T )powinno zwrócić wynik 18 (Podczas pierwszych wyborów Partia X
    # zdobyła 7 głosów, podczas drugich 5 głosów, a podczas trzecich 6 głosów)
    runtests(wybory, True)