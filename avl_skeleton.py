#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	# new size that we added
	"""returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return self.size

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		setParent(node, self)
	#	return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		setParent(node, self)
		# return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		# return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value
		# return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		# return None

	"""sets the rank of the node

	@type h: int
	@param h: the size
	"""
	def setSize(self, x):
		self.size = x
		# return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if (self.height == -1) or (self.value == None):
			return False
		return True


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	# added self.length as a field
	def __init__(self):
		self.root = None
		self.length = 0 #remove this!!! we have lenght function
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	# if root == none then Tree is empty
	def empty(self):
		if (self.root == None):
			return True
		return False


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	# we will use in Tree select for retrieve
	#if i not legal index return none
	def retrieve(self, i):
		if (i<0 or i>= self.length): #remove thisssss we have function
			return None
		return TreeSelectRec(self.root ,i+1)
	
	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 1 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	# pseudo code TreeSelectRec(x, i)
	# r = x.left.size +1
	# if x = r
	# 	return x.value
	# else if i<r
	#  	return TreeSelectRec(x.left, i)
	#  else:
	# 		return TreeSelectRec(x.right, i-r) 
	def TreeSelectRec(x, i)
		r = getSize(getLeft(x)) +1
		if i==r:
			return x.value
		elif i<r:
			return TreeSelectRec(getLeft(x), i)
		else:
			return TreeSelectRec(getRight(x), i-r) 


	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	# Insert(𝐿,𝑖,𝑧):
	# if i=n (|𝐿|=𝑛):
  	# 	 1.1 find the maximum and make z its right child
	# else (𝑖<𝑛):
  	# 	2.1 find the current node of rank i+1 (indices begin at 0)
  	# 	2.2 if it has no left child:
	# 		2.2.1 make z its left child.
  	#   	2.3 else:
	#  		2.3.1 find its predecessor
	# 		2.3.2 make z its right child
	# 3.  fix the tree
	def insert(self, i, val):
		#נאתחל צומת חדש
		node = AVLNode(val)
		if (i == self.length):
			maxnode = TreeMax(self)
			#update this! remove maxnode and change to last, bc thats a function we have to make anyways
			setRight(maxnode,node)
			#צריך לעדכן גודל וגובה של  כל הצמתים במסלול לשורש
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None


