class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.is_end = False

class BSTDict:

    def __init__(self):
        self.root = Node(None)

    def insert_key(self, string):
        temp = self.root
        for element in string:
            if element == "0":
                if temp.left is not None and temp.is_end is False: 
                    temp = temp.left
                    continue
                elif temp.left is None:
                    temp.left = Node(0)
                    temp = temp.left
                    temp.left = None
                    temp.right = None
                    continue
            elif element == "1":
                if temp.right is not None and temp.is_end is False:
                    temp = temp.right
                    continue
                if temp.right is None:
                    temp.right = Node(1)
                    temp = temp.right
                    temp.right = None
                    temp.left = None
                    continue
        temp.is_end = True

    def display(self):

        def _display_aux(self):
        #Returns list of strings, width, height and horizontal coordinate of the root

        #no child
            if self.right is None and self.left is None:
                line = '%s' % self.key
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle
            
        #only left child
            if self.right is None:
                lines, n, p ,x = _display_aux(self.left)
                s = '%s' % self.key
                u = len(s)
                first_line = (x+1) * ' ' + (n-x-1) * '_' + s
                second_line = x * ' ' + '/' + (n-x-1+u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n+u, p+2, n+u //2

        #only right child
            if self.left is None:
                lines, n, p ,x = _display_aux(self.right)
                s = '%s' % self.key
                u = len(s)
                first_line = s + x * '_' + (n-x) * ' '
                second_line = (u+x) * ' ' + '\\' + (n-x-1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u //2

        #two children
            left, n, p, x = _display_aux(self.left)
            right, m, q, y = _display_aux(self.right)
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2


        lines, _, _, _ = _display_aux(self.root)
        for line in lines:
            print(line)




tree = BSTDict()
tree.insert_key("1010101")
tree.insert_key("1111111")
tree.insert_key("1000001")
tree.insert_key("0000001")
tree.insert_key("0001")
tree.insert_key("000001")
tree.insert_key("00010")
tree.display()
