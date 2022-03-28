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
		self.HightUpdate = False
		

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


	#new field that we added
	"""returns if HightUpdate in the last updateMeserments

	@rtype: bool
	@returns: the HightUpdate-  true or false 
	"""
	def getHightUpdate(self):
		return self.HightUpdate


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


"""sets the HightUpdate of the node

	@type h: bool
	@param h: the HightUpdate
	"""

	def setHightUpdate(self, boolen):
		self.HightUpdate = boolen



	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(isRealNode(self):
		if (self.height == -1) and (self.value == None):
			return False
		return True


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""

	def __init__(self):
		self.root = AVLNode(self, None)
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	# if root is not real (since we initialized it as virtual node) then Tree is empty
	#O(1) since isRealNode is O(1)
	def empty(self):
		if not isRealNode(self.root):
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
	# time complexity(log(n))


	def retrieve(self, i):
		if (i<0 or i>= length(self)): 
			return None
		return getValue(TreeSelectRec(getRoot(self) ,i+1))
	
	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 1 <= i < self.length()
	@param i: index in the list
	@rtype: node
	@returns: the the node of the i'th item in the list
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
			return x
		elif i<r:
			return TreeSelectRec(getLeft(x), i)
		else:
			return TreeSelectRec(getRight(x), i-r) 

	"""returns BF

	@type node: AVLNode
	@pre: node is not virtual
	@param node: the node we want to calculate's BF
	@rtype: int
	@returns: the BF
	"""
	#gets BF 
	#time complexity: O(1) bc its just math

	def getBF(node):
		return getHight(getLeft(node)) - getHeight(getRight(node))


	"""returns predecessor 

	@type node: AVLNode
	@pre: node is not virtual, node is not first/min
	@param node: the node we want to find's predecessor
	@rtype: node
	@returns: the predecessor node
	"""
	# time complexity(log(n))

	def getPredecessor(node):
		if isRealNode(getLeft(node)):
			return MaxNode(getLeft(node))
		y = getParent(node)
		#לבדוק אולי צריך להוסיף פונצקיית שיווין
		while (y!= None) and (node == getLeft(y)) :
			node = y
			y = getParent(node)
		return y 


	"""returns Successor 

	@type node: AVLNode
	@pre: node is not virtual, node is not last,max
	@param node: the node we want to find's successor
	@rtype: node
	@returns: the successor node 

	"""
	# time complexity(log(n))

	def getSuccessor(node):
	if isRealNode(getRight(node)):
		return MinNode(getRight(node))
	y = getParent(node)
	#לבדוק אולי צריך להוסיף פונצקיית שיווין
	while (y!= None) and (node == getRight(y)) :
		node = y
		y= getParent(node)
	return y







	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	# Insert(L,i,z):
	# if i=n (|L|=n):
  	# 	 1.1 find the maximum and make z its right child
	# else (i<n):
  	# 	2.1 find the current node of rank i+1 (indices begin at 0)
  	# 	2.2 if it has no left child:
	# 		2.2.1 make z its left child.
  	#   	2.3 else:
	#  		2.3.1 find its predecessor
	# 		2.3.2 make z its right child
	# 3.  fix the tree


	def insert(self, i, val):
		newNode = AVLNode(val)
		#if empty tree, we create new tree
		if empty(self):
			self.root = newNode
			virtualRight = AVLNode(None)
			virtualLeft = AVLNode(None)
			setRight(newNode,virtualRight)
			setLeft(newNode,virtualLeft)
		#1
		else:
			if i==length(self) :
			#insert last, max has two virtual nodes, we insert in between max and its virtual node
			#the newNode, than make new leftVirtual to the newNode 
			max = MaxNode(getRoot(self))
			virtualLeft = AVLNode(None)
			virtualRight = getRight(max)
			setRight(newNode,virtualRight)
			setLeft(newNode,virtualLeft)
			setRight(max,newNode)
			else:
				currNode = TreeSelectRec(getRoot(self) ,i+1)
				if not isRealNode(getLeft(currNode)):
					#insert in index i, curr has left virtual nodes, we insert in between curr and its virtual node
					#the newNode, than make new RightVirtual to the newNode  
					virtualLeft = getLeft(currNode)
					virtualRight = AVLNode(None)
					setLeft(newNode,virtualLeft)
					setRight(newNode, virtualRight)
					setLeft(currNode,newNode)
				else:
					#insert in index i, pre has two virtual nodes, we insert in between pre and its virtual node
					#the newNode, than make new leftVirtual to the newNode 
					preNode = getPredecessor(currNode)
					virtualLeft = AVLNode(None)
					virtualRight = getRight(preNode)
					setRight(newNode,virtualRight)
					setLeft(newNode,virtualLeft)
					setRight(preNode,newNode)
					

			updatePathMeasurements(newNode) #update size and hight
			#2
			y = getParent(newNode)
			while (isRealNode(y)) and (y!=None):
				if abs(getBF(y)) < 2 :
					if not getHightUpdate(y):
						break
					else:
						y = getParent(y)
				else: #getBF(y)=2
					InsertRotation(y)
					break

"""rotation for insert
	@pre: node is real
	@returns: None
	"""
	# 	rotation(node)
		# if BF == -2
		# 	if getBF(getright) == -1:
		# 		Left rotation
				
		# 	else:
		# 		right rotation
		# 		left rotation
		# else:
		# 	if getBF(getleft) == +1
		# 		right rotation
		# 	else:
		# 		left rotation
		# right rotation			
	def InsertRotation(node):
		if getBF(node) == -2:
			if  getBF(getRight(node)) ==-1:
				LeftRotation(node)
			else:
				#לא בטוח שזה על אותו node 
				#צריך להבין
				RightRotation(node)
				LeftRotation(node)
		else:
			if getBF(getLeft(node)) == 1:
				RightRotation(node)
			else:
				#לא בטוח שזה על אותו node 
				#צריך להבין
				LeftRotation(node)
				RightRotation(node)


		

	"""update size and hight of path between newNode and root
	@pre: node is real
	@returns: None
	"""
	#We go all the way until we arrive the root
	#time complexity: O(log(n))
	def updatePathMeasurements(node):
		y = node	
		while (y!=None):
			#update hight
			lefthight= getHight(getRight(node))
			righthight = getHight(getLeft(node))
			newhight = max(lefthight, righthight)+1
			if (oldHight==newhight): #y hight hasn't changed
				setHightUpdate(node,False)
			else:	
				setHeight(node,newhight)
				setHightUpdate(node,True)
			#update size
			rightsize = getSize(getRight(node))
			leftsize  = getSize(getLeft(node))
			newsize = rightsize + leftsize + 1
			setSize(node,newsize)
			#go to the parent until you arive the root
			y = getParent(node)

		





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
	#We go all the way left until we arrive at a virtual node
	#time complexity: O(log(n))

	def first(self):
		node = self.root
		while isRealNode(getLeft(node)): 
			node = getLeft(node)
		return getValue(node)

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	#We go all the way Right until we arrive at a virtual node
	#time complexity: O(log(n))

	def last(self):
		node = self.root
		while isRealNode(getRight(node)): 
			node = getRight(node)
		return getValue(node)


	"""given a certain node and returns the min node

	@rtype: AVL node
	@returns: the min Node , Node itself if there is no left node
	"""
	#We go all the way left until we arrive at a virtual node
	#time complexity: O(log(n))
	def MinNode(node):
		while isRealNode(getLeft(node)): 
			node = getLeft(node)
		return node	

	"""given a certain node and returns the max node

	@rtype: AVL node
	@returns: the max Node , Node itself if there is no right node
	"""
	#We go all the way right until we arrive at a virtual node
	#time complexity: O(log(n))
	def MaxNode(node):
		while isRealNode(getRight(node)): 
			node = getRight(node)
		return node	





	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	#did a tree walk with global list result, just like you would in BTS
	#complexity: O(n)
	'''CHECK THAT THIS WORKS, MIGHT NEED TO ADD BASE CASE WITH RETURNS'''

	def listToArray(self):
		result = []

        def listtoArray_rec(node):
            if isRealNode(node):
                listtoArray_rec(getLeft(node))
                result.append(getValue(node))
                listtoArray_rec(getRight(node))

       	listtoArray_rec(self.root)
        return result

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	#root size is the tree length
	#time complexity: O(1)

	def length(self):
		return getSize(self.root)

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
	#recursively found the node with the value, 
	#by using global values that save the node and if value was found
	#then performed tree_rank on found value, if found (else return -1)
	#time complexity: O(n)

	def search(self, val):
		culprit = None
		found = False
		def search_rec(node, val)
			if found:
				return
			if isRealNode(node, value):
         	    search_rec(getLeft(node))
				if found:
					return
          	    elif getValue(node) == val:
					found = True
					culprit = node
					return
				else:
					search_rec(getRight(node))
		search_rec(getRoot(self), val)
		if not found:
			return -1
		else:
			return tree_rank(culprit)


"""returns index of node
	@type node: AVLNode
	@param node: node who's index must be found
	@rtype: int
	@returns: the index of node
	"""
	#we created this function, based on psuedocode from PPT 4a page 36 
	#time complexity: log(n)

	def Tree_rank(node):
		r = getSize(getLeft(node)) + 1
		
		while isRealNode(node):
			if node == getRight(getParent(node)): #if node is right son
				r = r + getSize(getLeft(getParent(node))) + 1
			node = getParent(node)
		return r



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	#if the list isnt empty then we can return a root
	# O(1) since empty is O(1)
	def getRoot(self):
		if not empty(self):
			return getValue(self.root)
		return None


