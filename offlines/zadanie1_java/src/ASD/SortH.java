package ASD;

public class SortH {

    class Node {
        int value;
        Node next;

        Node(int value) {
            this.value = value;
        }
    }

    class List {
        Node firstNode = null;
        Node lastNode = null;

        void addNode(Node node) {
            if (firstNode == null) {
                firstNode = node;
                lastNode = node;
            } else {
                lastNode.next = node;
                lastNode = node;
            }
        }
    }

    private Node sort(List list, int kScale) {
        System.out.println("Orig list: " + asString(list));
        sortBlock(list.firstNode, kScale, kScale);
        System.out.println("After 1 pass: " + asString(list));

        return null;
    }

    private int sortBlock(Node startNode, int kScale, int lastNodeIdx) {
        List cutOffList = new List();
        Node previousNode = startNode;
        int prevIdx = lastNodeIdx;

        for (int i = 0; i < kScale + 1; i++) {
            Node currentNode = startNode.next;
            if (currentNode != null && currentNode.value > startNode.value) {
                cutOffList.addNode(currentNode);
                previousNode.next = currentNode.next;
                currentNode.next = null;
                prevIdx -= 1;
            }
            previousNode = currentNode;
        }

        if (cutOffList.firstNode != null) {
            cutOffList.lastNode.next = previousNode.next;
            previousNode.next = cutOffList.firstNode;
        }

        int swap = startNode.value;
        startNode.value = previousNode.value;
        previousNode.value = swap;
        System.out.println(prevIdx);
        return prevIdx;
    }

    private String asString(List list) {
        Node node = list.firstNode;
        String message = "[ ";
        while (node != null) {
            message += node.value + " ";
            node = node.next;
        }
        return message += "]";
    }

    private List buildList(int... values) {
        List list = new List();
        for (int i = 0; i < values.length; i++) {
            Node next = new Node(values[i]);
            list.addNode(next);
        }

        return list;
    }

    public static void main(String[] args) {
        SortH sortH = new SortH();

        int[] testArray = new int[] { 1, 2, 0, 4, 11, 5, 6 };
        int k = 2;

        List list = sortH.buildList(testArray);
        sortH.sort(list, 2);
    }
}
