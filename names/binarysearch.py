class BinarySearch:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value): #Inser value into tree.
        current_node = self.value        
 
        if value < current_node:
            if self.left is None: #Left: new nodes values - current nodes 1 value
                self.left = BinarySearch(value)
                return
            else: #Repeat process.
                left_node = self.left
                left_node.insert(value)
        if value > current_node: #Right: new nodes value > or = current parent value.
            if self.right is None:  #Not child
                self.right = BinarySearch(value) #New one.
                return
            else: 
                right_node = self.right #Repeat Process Right.
                right_node.insert(value)

    def contains(self, target): #Tree contain value = True.
        current_node = self.value
        if current_node == target: 
            return True
        if target < current_node: #Tree does'nt contain value = False.
            if self.left is None:
                return False
            else: #left node contains the target.
                left_node = self.left
                return left_node.contains(target)
        if target > current_node: #Target is > that target.
            if self.right is None:
                return False
            else: #the right node contains target.
                right_node = self.right
                return right_node.contains(target)



