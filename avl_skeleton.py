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

	#time complexity: O(log(n))

	def insert(self, i, val):

		newNode = AVLNode(val)
		balancing_steps = 0 #counting how many fixes to hight and rotations


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
					

			balancing_steps = updatePathMeasurements(newNode, balancing_steps) #update size and hight and balancing_steps
			#2
			y = getParent(newNode)
			while (isRealNode(y)) and (y!=None):
				if abs(getBF(y)) < 2 :
					if not getHightUpdate(y):
						break
					else:
						y = getParent(y)
				else: #getBF(y)=2
					balancing_steps = ImplementRotation(self, y, balancing_steps)
					break

		return balancing_steps

"""decides which types of rotations will take place for insert
	@pre: node is real
	@returns: amount of balancing steps so far
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

		#time complexity O(1)

	def ImplementRotation(self, node, balancing_steps):

		if getBF(node) == -2:

			if  getBF(getRight(node)) ==-1 or getBF(getRight(node)) ==0:    #child BF == -1 or 0
				LeftRotation(self,node)
				balancing_steps += 1

			else:															#child BF == +1
				RightRotation(self,getRight(node))
				LeftRotation(self,node)
				balancing_steps+=2
		else:

			if getBF(getLeft(node)) == 1 or getBF(getLeft(node)) == 0: 		#child BF == +1 or 0
				RightRotation(self,node)
				balancing_steps+=1

			else: 															#child BF == -1
				LeftRotation(self,getLeft(node))
				RightRotation(self,node)
				balancing_steps+=2

		return balancing_steps


	"""does right rotation on given node
	@pre: node is real
	@returns: none
	"""
	#time complexity: O(1)

	def RightRotation(self, B):
		B_is_root=False

		if getParent(B) == None: ##if none then B is root
			B_is_root = True

		A = getLeft(B)
		setLeft(B, getRight(A))
		setParent(getLeft(B), B)
		setRight(A,B)
		if B_is_root:
			self.root = A

		else:	
			setParent(A, getParent(B))
			if is_left_child(B):
				setLeft(getParent(A), A)
			else:
				setRight(getParent(A), A)

		setParent(B, A)

		setHeight(B, max(getHeight(getLeft(B)), getHeight(getRight(B))) + 1 )
		setSize(B, getSize(getLeft(B)) + getSize(getRight(B)) + 1 )
		setSize(A, getSize(getLeft(A)) + getSize(getRight(A)) + 1 )

	"""does right rotation on given node
	@pre: node is real
	@returns: none
	"""
	#time complexity: O(1)
	
	def LeftRotation(self, B):
		B_is_root=False

		if B == getRoot(self):
			B_is_root = True

		A = getRight(B)
		setRight(B, getLeft(A))
		setParent(getRight(B), B)
		setLeft(A,B)
		if B_is_root:
			self.root = A

		else:	
			setParent(A, getParent(B))
			if is_left_child(B):
				setLeft(getParent(A), A)
			else:
				setRight(getParent(A), A)

		setParent(B, A)

		setHeight(B, max(getHeight(getLeft(B)), getHeight(getRight(B))) + 1 )
		setSize(B, getSize(getLeft(B)) + getSize(getRight(B)) + 1 )
		setSize(A, getSize(getLeft(A)) + getSize(getRight(A)) + 1 )





		

	"""update size and hight of path between newNode and root
	@pre: node is real
	@returns: None
	"""
	#We go all the way until we arrive the root
	#time complexity: O(log(n))
	def updatePathMeasurements(node, balancing_steps):
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
				balancing_steps += 1

			#update size
			rightsize = getSize(getRight(node))
			leftsize  = getSize(getLeft(node))
			newsize = rightsize + leftsize + 1
			setSize(node,newsize)
			#go to the parent until you arive the root
			y = getParent(node)

			return balancing_steps

		





	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
# 	AVL-Delete(T, 𝒛)

# 0. check if root for edge case

# 1. Case 1: 𝑥 is a leaf
	# Case 2: 𝑥 has only one child
	# Case 3: If 𝑥 has two children

# 2. Let 𝑦 be the parent of the (physically) deleted node.
# 3. while 𝑦 ≠ 𝑁𝑢𝑙𝑙 do:
	# 3.1. compute 𝐵𝐹(𝑦)*
	# 3.2. if |𝐵𝐹(𝑦)| < 2 and 𝑦’s height hasn’t changed: terminate
	# 3.3. else if |𝐵𝐹(𝑦)| < 2 and 𝑦’s height changed: go back to stage 3 with 𝑦’s parent
	# 3.4. else (|𝐵𝐹(𝑦)| = 2): perform a rotation and go back to stage 3 with 𝑦’s parent



	def delete(self, i):

		if i>= self.length() or i<0: #check that list isnt empty
			return -1

		balancing_steps = 0 #how many balancing steps we made
		node = TreeSelectRec(getRoot(self), i)

		if node == self.getRoot():  #0
			#insert code here
		else:

			children = 0				#checks how many children, and if so, which one is it (left T or F)
			hasLeft = False
			if isRealNode(getLeft(node)):
				children+=1
				hasLeft = True
			if isRealNode(getRight(node)):
				children+=1


			y = getParent(node) 					#2		

			if children == 0: 										#1.case_1   		
				if is_left_child(node):
					setParent(getLeft(node), y)
					setLeft(y, getLeft(node))
					#AVLdelete(node)  gotta create this
				else:
					setParent(getRight(node), y)
					setRight(y, getRight(node))
					#AVLdelete(node)  gotta create this

			elif children == 1:											#1.case_2
				if hasLeft: 
					if is_left_child(node): 							#has left child and is left child
						setParent(getLeft(node), y)
						setLeft(y, getLeft(node))
						#AVLdelete(node)  gotta create this
					else:												#has left child and is right child
						setParent(getLeft(node), y)
						setRight(y, getLeft(node))
						#AVLdelete(node)  gotta create this

				else:													 
					if is_left_child(node):								 #has right child and is left child
						setParent(getRight(node), y)
						setLeft(y, getRight(node))
						#AVLdelete(node)  gotta create this
					else:												#has right child and is right child
						setParent(getRight(node), y)
						setRight(y, getRight(node))
						#AVLdelete(node)  gotta create this

			else:															#1.case_3
																						
				successor = getSuccessor(node)
				y = getParent(successor)  									#because of successor being deleted node in terms of shape, we start fixing here
				setParent(getRight(successor), getParent(successor))		#successor ALWAYS has right child and is left child
				setLeft(getParent(successor), getRight(successor))

				setParent(successor, getParent(node))     					  #steal node's parent
				if is_left_child(node):
					setLeft(getParent(successor), successor)
				else:
					setRight(getParent(successor), successor)

				setRight(successor, getRight(node))							#steal node's right child
				setParent(getRight(successor), successor)

				setLeft(successor, getLeft(node))							#steal node's left child
				setParent(getLeft(successor), successor)
				
				#AVLdelete(node)  gotta create this
			
			########## done with 1 and 2 ####################
			########## start 3 ##############################

			balancing_steps = updatePathMeasurements(y, balancing_steps) #update size and hight and balancing_steps
				
				
			while (isRealNode(y)) and (y!=None):
				if abs(getBF(y)) < 2 :
					if not getHightUpdate(y):
						break
					else:
						y = getParent(y)
				else: #getBF(y)=2
					balancing_steps = ImplementRotation(self, y, balancing_steps)
					y = getParent(y)

			return balancing_steps	
			





				




				


		
"""returns bool if node is left child
	@pre: node has parent
	@rtype: bool
	@returns: returns true if node is left child
	"""
	def is_left_child(node):
		if node == getLeft(getParent(node)):
			return True 
		return False

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	#We go all the way left until we arrive at a virtual node
	#time complexity: O(log(n))

	def first(self):
		if self.empty():
			return None
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
		if self.empty():
			return None
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


