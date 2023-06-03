if __name__ == '__main__':
    def divisionBorder(start, k):
        if(start.next is None):
            return 1;
        pivot = start
        current = start.next
        prev = start
        to_cut = None
        to_cut_curr = None
        to_connect = start
        n = 1;

        for i in range(k):
            if current.next is None:
                break
            if current.val > pivot.val:
                if to_cut is None:
                    to_cut = current
                    to_cut_curr = to_cut
                else:
                    to_cut_curr.next = current
                    to_cut_curr = to_cut_curr.next
                #print("prev.next " + str(prev.next.val) + " curr.next " + str(current.next.val))
                #print("lista tym")
                prev.next = current.next
                #printList(start)
            else:
                n += 1
                to_connect = current
                prev = current
            current = current.next
        if to_cut is not None:
            to_cut_curr.next = None
            #print("to_cut" + str(to_cut.val))
            #print("to_cut_curr" + str(to_cut_curr.val))
            #print("current" + str(to_connect.val))
            #print("cut list: ")
            #printList(to_cut)
            #print("---------")
            #print("list to add: ")
            #printList(start)
            #print("---------------")
            to_cut_curr.next = to_connect.next
            to_connect.next = to_cut

        temp = to_connect.val
        to_connect.val = pivot.val
        pivot.val = temp
        return n

    def sort(start, k):
        if k == 0 or start.next is None:
            return
        n = divisionBorder(start, k)
        sort(start, n - 1)
        sort(start.next, k)

    def printList(start):
        current = start
        while current.next is not None:
            print(current.val)
            current = current.next
        print(current.val)

    class Node:
        def __init__(self):
            self.val = None
            self.next = None

    start = Node()
    start.val = 3
    start.next = Node()
    start.next.val = 2
    start.next.next = Node()
    start.next.next.val = 1
    start.next.next.next = Node()
    start.next.next.next.val = 4

    #print(start.next.next.next.next.next.val)
    printList(start)
    print("Po: ")
    printList(start)
    print("ile elementów po lewej: " + str(divisionBorder(start, 5)))
    sort(start, 2)
    printList(start)