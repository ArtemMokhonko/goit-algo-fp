import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()



def build_min_heap(arr):
    """
    Створюємо мін-купу з масиву.
    """
    heapq.heapify(arr)  # Використовуємо вбудовану функцію heapify для перетворення масиву на мін-купу
    return build_heap(arr)  # Повертаємо корінь дерева, побудованого з масиву

def build_heap(arr):
    """
    Перетворюємо масив у бінарне дерево (структуру купи).
    """
    if not arr:  # Якщо масив порожній, повертаємо None
        return None

    nodes = [Node(val) for val in arr]  # Створюємо список вузлів з значень масиву
    n = len(nodes)  # Визначаємо довжину списку вузлів

    for i in range(n // 2):  # Прив'язуємо дітей до вузлів
        if 2 * i + 1 < n:  # Якщо лівий нащадок існує
            nodes[i].left = nodes[2 * i + 1]  # Призначаємо лівого нащадка
        if 2 * i + 2 < n:  # Якщо правий нащадок існує
            nodes[i].right = nodes[2 * i + 2]  # Призначаємо правого нащадка

    return nodes[0]  # Повертаємо корінь дерева


# Введення масиву для побудови бінарної купи
heap_array = [0, 3, 7, 6, 2, 12, 11, 20, 13]

# Створення мін-купу
min_heap_root = build_min_heap(heap_array)

# Відображення мін-купу
draw_tree(min_heap_root)

