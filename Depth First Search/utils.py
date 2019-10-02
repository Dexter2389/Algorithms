
class Node:
    '''
    Node is a tree node which stores data, a parent and a list of children

    '''

    def __init__(self, data, parent=None, children=None):

        # Setting default varialbes
        self.data = data

        if parent is None:
            self.parent = None
        else:
            self.parent = parent

        if children is None:
            self.children = []
        else:
            self.children = children

    def __str__(self):
        string = self.data + " " + "[ "
        for i in range(len(self.children)):
            string += str(self.children[i]) + ", "

        string += "]"
        return string

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
        return

    def getChildren(self):
        return self.children

    def addChild(self, node):
        self.children.append(node)
        return node

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
        return
    
class Tree:
    '''
    An implementation of a tree structure. Trees can be constructed independently or given a file to create the tree from
    
    '''
    def __init__(self):
        # Initializing the tree structure
        self.root = None

    def getRoot(self):
        # Accessing the Root element
        return self.root

    def setRoot(self, root):
        # Setting the Root element
        self.root = root
        return

    def isEmpty(self):
        # Bool for status for the tree
        if self.root == None:
            return True
        else:
            return False

    def makeTree(self, textFile):
        """
		Creates the tree structure based on input from a file. 
        Elements in brackets represent child nodes.
		
        Text File Ex: a[b[cd]ef[g]]
		
        Represents tree: 
				     a
				    /|\
				   b e f
				  /\   |
				 c  d  g
		
        Parameters:
			textFile: a text file that houses a tree data structure
			tree: an initialized tree structure
		
        Returns: None, if empty file
		"""

        text = open(textFile, "r")
        current = None
        line = text.readline()

        # Check for valid file
        if len(line) == 0:
            return None

        # Initializing variables
        node = Node(line[0])
        self.root = node
        current = node
        place = 1 # Used to traverse text

        # Traversing text file to set up tree
        while place < len(line):
            # '[' means the following char will represent a child node 
			#  so we create a node for the following char, update current node
            if line[place] == "[":
                place += 1
                node = Node(line[place], current)
                current.addChild(node)
                current = node

            # ']' means we've just finished the whole array of children 
			#  for an element, so we reset current to a parent element which
			#  may still need to add child elements
            elif line[place] == "]":
                current = current.getParent()

            # We create a node for the char, and set it's parent
            else:
                current = current.getParent()
                node = Node(line[place], current)
                current.addChild(node)
                current = node

            place += 1 # Updating position in text

        return
