class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def create_tree():
    root = None
    print("Вводите значения узлов, -1 для завершения:")
    while True:
        value = input("Значение узла: ")
        if value == '-1': 
            break
            
        if value == 'пусто':
            value = None
        else:
            value = int(value)
            
        node = Node(value)
        
        if root is None:
            root = node
        else:
            inserted = insert_by_level(root, node)
            if not inserted:
                break
                
    print("\nПостроено дерево:")
    print_tree(root)  
    return root

def insert_by_level(root, node):
    current_level = [root] 
    next_level = []
    
    while len(current_level) > 0:
        for n in current_level:
            if n.left is None:
                n.left = node
                return True 
            else:
                next_level.append(n.left)
                
            if n.right is None:
                n.right = node
                return True
            else:
                next_level.append(n.right)
                
        current_level = next_level
        next_level = []
        
    return False  

def print_tree(node, level=0):
    if node is None:
        return
    
    print_tree(node.right, level + 1)
    print(' ' * 4 * level + '->', node.value) 
    print_tree(node.left, level + 1)

root = create_tree()
print("\nГотово!")  
   
target = int(input("Введите целевое число: "))

def find_paths(root, target):
    result = []
    
    def dfs(node, target, path):
        if not node:
            return  
        path.append(node.value)
        if not node.left and not node.right and sum(path) == target:
            result.append(list(path))
        else:
            dfs(node.left, target, path)
            dfs(node.right, target, path)
        path.pop()
        
    dfs(root, target, [])
    return result


paths = find_paths(root, target)
print(paths)




