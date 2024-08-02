class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self, description=""):
        print(description)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    """
    Функція для реверсування однозв'язного списку
    """
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    """
     Функція для сортування списку методом злиття
     має час виконання O(n**2) у найгіршому випадку
    """

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current is not None:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while sorted_current.next is not None and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node

        self.head = sorted_list


    """
    Функція для сортування списку методом злиття
    має час виконання O(n log n), що робить її більш ефективною 
    для великих списків порівняно з сортуванням вставками
    """ 
    def merge_sort(self, h):
        if h is None or h.next is None:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list
    
    # Допоміжна функція для знаходження середини списку
    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Допоміжна функція для об'єднання двох відсортованих списків
    def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    """
    Функція для об'єднання двох відсортованих списків в один
    """
    def merge_two_sorted_lists(self, l1, l2):
        dummy = Node()
        tail = dummy
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next


# Приклади використання

# Створення і друк списку
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(7)
llist.insert_at_end(-20)
llist.insert_at_end(5)
llist.insert_at_end(100)
llist.print_list("Початковий список:")

# Реверсування списку
llist.reverse()
llist.print_list("Реверсований список:")


# Сортування списку
llist.insertion_sort()
llist.print_list("Відсортований список методом злиття:")


llist.head = llist.merge_sort(llist.head)
llist.print_list("Відсортований список методом вставки:")

# Об'єднання двох відсортованих списків
llist1 = LinkedList()
llist1.insert_at_end(-1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist1.print_list("Перший відсортований список:")

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4.4)
llist2.insert_at_end(6)
llist2.print_list("Другий відсортований список:")

merged_list = LinkedList()
merged_list.head = merged_list.merge_two_sorted_lists(llist1.head, llist2.head)
merged_list.print_list("Об'єднаний відсортований список:")


