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

def draw_tree(tree_root, color_map=None, ax=None):
    """
    Малюємо дерево за допомогою NetworkX та Matplotlib.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    if color_map:
        for node in tree.nodes(data=True):
            node_id = node[0]
            if node_id in color_map:
                colors[list(tree.nodes).index(node_id)] = color_map[node_id]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    if ax is None:
        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()
    else:
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)

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

def hex_color_gradient(start_color, end_color, steps):
    """
    Генерує градієнт кольорів від start_color до end_color.
    """
    start_color = int(start_color.lstrip('#'), 16)
    end_color = int(end_color.lstrip('#'), 16)
    start_r = (start_color >> 16) & 255
    start_g = (start_color >> 8) & 255
    start_b = start_color & 255
    end_r = (end_color >> 16) & 255
    end_g = (end_color >> 8) & 255
    end_b = end_color & 255

    color_list = []
    for step in range(steps):
        r = round(start_r + (step * (end_r - start_r) / (steps - 1)))
        g = round(start_g + (step * (end_g - start_g) / (steps - 1)))
        b = round(start_b + (step * (end_b - start_b) / (steps - 1)))
        color_list.append(f'#{r:02X}{g:02X}{b:02X}')
    return color_list

def dfs_traversal(root):
    """
    Виконує обхід дерева в глибину (DFS).
    """
    if root is None:
        return []

    stack = [(root, 0)]
    order = []

    while stack:
        node, depth = stack.pop()
        if node:
            order.append(node)
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

    return order

def bfs_traversal(root):
    """
    Виконує обхід дерева в ширину (BFS).
    """
    if root is None:
        return []

    queue = [(root, 0)]
    order = []

    while queue:
        node, depth = queue.pop(0)
        if node:
            order.append(node)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

    return order

def visualize_traversals(tree_root, dfs_order, bfs_order):
    """
    Візуалізує обхід дерева (DFS і BFS) з градієнтами кольорів.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Візуалізація DFS
    dfs_color_map = {}
    dfs_colors = hex_color_gradient("#000080", "#FAD8E6", len(dfs_order))
    for i, node in enumerate(dfs_order):
        dfs_color_map[node.id] = dfs_colors[i]
    draw_tree(tree_root, dfs_color_map, ax=axes[0])
    axes[0].set_title("Обход дерева: у глибину DFS")

    # Візуалізація BFS
    bfs_color_map = {}
    bfs_colors = hex_color_gradient("#004000", "#AFC0CB", len(bfs_order))
    for i, node in enumerate(bfs_order):
        bfs_color_map[node.id] = bfs_colors[i]
    draw_tree(tree_root, bfs_color_map, ax=axes[1])
    axes[1].set_title("Обход дерева: у ширину BFS")

    plt.show()

if __name__ == "__main__":
    # Введення масиву для побудови бінарної купи
    heap_array = [0, 3, 7, 6, 2, 12, 11, 20, 13]

    # Створення мін-купу
    min_heap_root = build_min_heap(heap_array)

    # Обхід в глибину (DFS)
    dfs_order = dfs_traversal(min_heap_root)
    print("DFS Order:", [node.val for node in dfs_order])

    # Обхід в ширину (BFS)
    bfs_order = bfs_traversal(min_heap_root)
    print("BFS Order:", [node.val for node in bfs_order])

    # Візуалізація обходів
    visualize_traversals(min_heap_root, dfs_order, bfs_order)
