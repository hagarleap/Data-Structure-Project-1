#username - hagarleap
#id1      - 206825176 
#name1    - Hagar Paytan
#id2      - 318459666
#name2    - Gal Kariel 

##Note to checker of this project: we created a separate insert for BST called insert_BST. It is the last function in the File, and it is commented out.

"""A class represnting a node in an AVL tree"""
from ast import Global
from hashlib import new
from logging import root


class AVLNode(object):
	"""Constructor:
	@type value: str
	@param value: data of your node
	@type size: int
	@param size: size of subtree including node itself
	@type HeightUpdate: boolean
	@param HeightUpdate: states if height was updated after UpdateMeasurement=
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		self.HeightUpdate = False	

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

	"""returns the size

	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return self.size

	"""returns if HeightUpdate in the last updateMeserments

	@rtype: bool
	@returns: the HeightUpdate-  true or false 
	"""
	def getHeightUpdate(self):
		return self.HeightUpdate

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h

	"""sets the HeightUpdate of the node

	@type h: bool
	@param h: the HeightUpdate
	"""

	def setHeightUpdate(self, boolean):
		self.HeightUpdate = boolean


	"""sets the rank of the node

	@type h: int
	@param h: the size
	"""
	def setSize(self, x):
		self.size = x

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if (self.height == -1) and (self.value == None):
			return False
		return True

	"""update size and height and HeightUpdate of Node 

	@pre: node is real
	@returns: None
	"""
	#time complexity: O(1)

	def updateMeasurements(self):
		#update height	
		oldHeight = self.getHeight()
		leftheight= self.getLeft().getHeight()
		rightheight = self.getRight().getHeight()
		newheight = max(leftheight, rightheight)+1
		if (oldHeight==newheight): #node's height hasn't changed
			self.setHeightUpdate(False)
		else:	
			self.setHeight(newheight)
			self.setHeightUpdate(True)

		#update size
		rightsize = self.getRight().getSize()
		leftsize  = self.getLeft().getSize()
		newsize = rightsize + leftsize + 1
		self.setSize(newsize)	

	"""update size of all nodes starting at given node til root. Useful in insert/delete/join/split. 

	@pre: node is real
	@returns: None
	"""
	#time complexity: O(log(n))

	def fix_size_rec(self):
		while self != None:
				rightsize = self.getRight().getSize()
				leftsize  = self.getLeft().getSize()
				newsize = rightsize + leftsize + 1
				self.setSize(newsize)

				self = self.getParent()



	"""returns BF

	@type node: AVLNode
	@pre: node is not virtual
	@param node: the node we want to calculate's BF
	@rtype: int
	@returns: the BF
	"""
	#time complexity: O(1) 

	def getBF(self):
		if self.isRealNode():
			return self.getLeft().getHeight() - self.getRight().getHeight()
		else:
			return 0


	

	"""returns predecessor 

	@type node: AVLNode
	@pre: node is not virtual, node is not first/min
	@param node: the node we want to find's predecessor
	@rtype: node
	@returns: the predecessor node
	"""
	# time complexity(log(n))

	def getPredecessor(self):
		if self.getLeft().isRealNode():
			return self.getLeft().MaxNode()
		y = self.getParent()
		#check if we need to add an equality function
		while (y!= None) and (self == y.getLeft()) :
			self = y
			y = self.getParent()
		return y 


	"""returns Successor 

	@type node: AVLNode
	@pre: node is not virtual, node is not last,max
	@param node: the node we want to find's successor
	@rtype: node
	@returns: the successor node 

	"""
	# time complexity(log(n))

	def getSuccessor(self):
		if self.getRight().isRealNode():
			return self.getRight().MinNode()
		y = self.getParent()
		#check if we need to add an equality function
		while (y!= None) and (self == y.getRight()) :
			self = y
			y= self.getParent()
		return y	



	""" 'deletes' node by stripping it of all pointers
	@type node: AVLNode
	@param node: a node
	"""
	#time complexity: O(1)

	def AVLdelete(self):
		self.setParent(None)
		self.right = None
		self.left = None
		
	"""returns bool if node is left child
    @pre: node has parent
    @rtype: bool
    @returns: returns true if node is left child
    """
    #time complexity: O(1)

	def is_left_child(self):
		if self == self.getParent().getLeft():
			return True 
		return False



	"""given a certain node and returns the min node of subtree

	@rtype: AVL node
	@returns: the min Node , Node itself if there is no left node
	"""
	#time complexity: O(log(n))

	def MinNode(self):          #We go all the way left until we arrive at a virtual node
		while self.getLeft().isRealNode(): 
			self = self.getLeft()
		return self	

	"""given a certain node and returns the max node of subtree

	@rtype: AVL node
	@returns: the max Node , Node itself if there is no right node
	"""
	#time complexity: O(log(n))

	def MaxNode(self):          #We go all the way right until we arrive at a virtual node
		while self.getRight().isRealNode(): 
			self = self.getRight()
		return self	



	"""returns index of node
	@type node: AVLNode
	@param node: node who's index must be found
	@rtype: int
	@returns: the index of node
	"""
	#time complexity: O(log(n))

	def Tree_rank(self):
		r = self.getLeft().getSize() + 1
		
		while self.isRealNode():
			if self.parent != None:

				if self == self.getParent().getRight(): #if node is right son
					r = r + self.getParent().getLeft().getSize() + 1
				self = self.getParent()
			else:
				break
		return r -1 




"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""

	def __init__(self):
		self.root = AVLNode(None)
		self.min = self.getRoot()
		self.max = self.getRoot()
        

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
   #time complexity: O(1)

	def empty(self):
		if not self.root.isRealNode():
			return True
		return False


	"""retrieves the node of the i'th item in the list

	@type i: int
	@pre: 1 <= i < self.length()
	@param i: index in the list
	@rtype: node
	@returns:  the node of the i'th item in the list
	"""
   #time complexity: O(log(n))
	
	def TreeSelect(self, i):
		
		def TreeSelectRec(x, i):
			r = x.getLeft().getSize() + 1
			if i==r:
				return x
			elif i<r:
				return TreeSelectRec(x.getLeft(), i)
			else:
				return TreeSelectRec(x.getRight(), i-r) 

		return TreeSelectRec(self.root, i)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	# time complexity(log(n))

	def retrieve(self, i):
		if (i<0 or i>= self.length()): 
			return None
		return self.TreeSelect(i+1).getValue()

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	#time complexity: O(log(n))

	def insert(self, i, val):

		newNode = AVLNode(val)
		balancing_steps = 0 #counting how many fixes to height and rotations

		#if empty tree, we create new tree
		if self.empty():
			self.root = newNode
			virtualRight = AVLNode(None)
			virtualLeft = AVLNode(None)
			newNode.setRight(virtualRight)
			newNode.setLeft(virtualLeft)
			newNode.updateMeasurements()

			virtualLeft.setParent(newNode)
			virtualRight.setParent(newNode)

			self.min = newNode
			self.max = newNode #max is now also the root

		#1
		else:
			if i==self.length(): 
				#insert last, last node has two virtual nodes, we insert in between last node and its virtual node
				#the newNode, than make new leftVirtual to the newNode 
				
				last_node = self.max
				virtualLeft = AVLNode(None)
				virtualRight = last_node.getRight()
				newNode.setRight(virtualRight)
				newNode.setLeft(virtualLeft)
				last_node.setRight(newNode)

				virtualLeft.setParent(newNode)
				virtualRight.setParent(newNode)
				newNode.setParent(last_node)

			elif i == 0:	
				#similar idea to inserting in last, but in first.
				#important note: in the grand scheme of things, this is a tiny amount of optimization (since its only relevant to when we insert first or last)
				#before, we used Treeselect to find all indexes
				#but then we found that running tests for Q3 (when we insert first a bunch of times) took a TON of time 
				# (and sometimes recursion limit was hit, so eventually impossible) 
				#so we use min and max just for these two

				first_node = self.min
				virtualRight = AVLNode(None)
				virtualLeft = first_node.getLeft()
				newNode.setRight(virtualRight)
				newNode.setLeft(virtualLeft)
				first_node.setLeft(newNode)

				virtualLeft.setParent(newNode)
				virtualRight.setParent(newNode)
				newNode.setParent(first_node)


			else:
				currNode = self.TreeSelect(i+1)
				if not currNode.getLeft().isRealNode():
					#insert in index i, curr has left virtual nodes, we insert in between curr and its virtual node
					#the newNode, than make new RightVirtual to the newNode  
					virtualLeft = currNode.getLeft()
					virtualRight = AVLNode(None)
					newNode.setLeft(virtualLeft)
					newNode.setRight(virtualRight)
					currNode.setLeft(newNode)

					virtualLeft.setParent(newNode)
					virtualRight.setParent(newNode)
					newNode.setParent(currNode)


				else:
					#insert in index i, pre has two virtual nodes, we insert in between pre and its virtual node
					#the newNode, than make new leftVirtual to the newNode 
					preNode = currNode.getPredecessor()
					virtualLeft = AVLNode(None)
					virtualRight = preNode.getRight()
					newNode.setRight(virtualRight)
					newNode.setLeft(virtualLeft)
					preNode.setRight(newNode)

					virtualLeft.setParent(newNode)
					virtualRight.setParent(newNode)
					newNode.setParent(preNode)
					
			if i==self.length(): #updates max and min only after inserting the node, to help with case when list is empty
				self.max = newNode
			if i == 0:
				self.min = newNode

			newNode.updateMeasurements() #update size and height and balancing_steps without adding to BS since its a new node not updated node
			#2

			y = newNode.getParent()
			while y != None:
				y.updateMeasurements()

				if abs(y.getBF()) < 2 :
					if not y.getHeightUpdate():
						break
					else:
						y = y.getParent()
						balancing_steps += 1
				else: #getBF(y)=2
					balancing_steps = self.ImplementRotation( y, balancing_steps)
					break

			if y != None: ###height may not change now but size certainly has
				y.fix_size_rec()


		return balancing_steps

	"""decides which types of rotations will take place for insert
	@pre: node is real
	@returns: amount of balancing steps so far
	"""

		#time complexity O(1)

	def ImplementRotation(self, node, balancing_steps):
		if node.getBF() == -2:

			if  node.getRight().getBF() ==-1 or node.getRight().getBF() ==0:    #child BF == -1 or 0
				self.LeftRotation(node)
				balancing_steps += 1

			else:															#child BF == +1
				self.RightRotation(node.getRight())
				self.LeftRotation(node)
				balancing_steps+=2
		else:

			if node.getLeft().getBF() == 1 or node.getLeft().getBF() == 0: 		#child BF == +1 or 0
				#print(node.getLeft().getHeight())
				self.RightRotation(node)
				balancing_steps+=1

			else: 															#child BF == -1
				self.LeftRotation(node.getLeft())
				self.RightRotation(node)
				balancing_steps+=2

		return balancing_steps


	"""does right rotation on given node
	@pre: node is real
	@returns: none
	"""
	#time complexity: O(1)

	def RightRotation(self, B):
		
		B_is_root=False

		if B.getParent() == None: ##if none then B is root
			B_is_root = True
		else:
			flag_B_left_child =  B.is_left_child()  #need to save this to avoid running is_left_child on root - will result in error. 

		A = B.getLeft()

		B.setLeft(A.getRight())
		B.getLeft().setParent( B)

		A.setParent(B.getParent())
		
		A.setRight(B)

		if B_is_root:
			self.root = A
			

		else:	#set parent's new child in right spot (left or right son)
			if flag_B_left_child:
				A.getParent().setLeft( A)
			else:
				A.getParent().setRight( A)

		B.setParent(A)

		B.setHeight( max(B.getLeft().getHeight(), B.getRight().getHeight()) + 1 )
		A.setHeight( max(A.getLeft().getHeight(), A.getRight().getHeight()) + 1 )
		B.setSize( B.getLeft().getSize() + B.getRight().getSize() + 1 )
		A.setSize(A.getLeft().getSize() + A.getRight().getSize() + 1 )

	"""does right rotation on given node
	@pre: node is real
	@returns: none
	"""
	#time complexity: O(1)
	
	def LeftRotation(self, B):

		B_is_root=False
			
		if B == self.getRoot():
			B_is_root = True
		else:
			flag_B_left_child =  B.is_left_child()

		A = B.getRight()

		B.setRight(A.getLeft())
		B.getRight().setParent(B)

		A.setParent(B.getParent())

		A.setLeft(B)

		if B_is_root:
			self.root = A

		else:	
			
			if flag_B_left_child:
				A.getParent().setLeft(A)
			else:
				A.getParent().setRight(A)

		B.setParent(A)

		B.setHeight( max(B.getLeft().getHeight(), B.getRight().getHeight()) + 1 )
		A.setHeight( max(A.getLeft().getHeight(), A.getRight().getHeight()) + 1 )
		B.setSize( B.getLeft().getSize() + B.getRight().getSize() + 1 )
		A.setSize(A.getLeft().getSize() + A.getRight().getSize() + 1 )

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	#time complexity: O(log(n))

	def delete(self, i):

		if i>= self.length() or i<0: #check that list isnt empty
			return -1

		balancing_steps = 0 #how many balancing steps we made
		node = self.TreeSelect( i+1)

		#update min and max
		if (i==0):
			self.min = node.getSuccessor()
		elif (i == self.length()-1):
			self.max = node.getPredecessor()	


		y = None					#initiallizing y, the parent of the physically deleted node
		children = 0				#checks how many children, and if so, which one is it (left T or F)
		hasLeft = False
		if node.getLeft().isRealNode():
			children+=1
			hasLeft = True
		if node.getRight().isRealNode():
			children+=1

		if node != self.getRoot():					#set y as parent only if it has a parent: we have special check for root in case 3
			y = node.getParent() 					#2		

		if children == 0: 											#1.case_1  	
			if node == self.getRoot(): #only one node-root in the tree
				virtual_root = node.getRight()
				virtual_root.setParent(None)
				self.root = virtual_root
				self.min = self.getRoot()  #update min and max
				self.max = self.getRoot()
				return balancing_steps

			if node.is_left_child():
				node.getLeft().setParent( y)
				y.setLeft( node.getLeft())
				node.AVLdelete()
			else:
				node.getRight().setParent( y)
				y.setRight(node.getRight())
				node.AVLdelete()  

		elif children == 1:											#1.case_2
			if hasLeft: 
				if node == self.getRoot():							#if node is root&has child, that child has no children. no need for height or size updates, just make it the root
					new_root = node.getLeft()
					new_root.setParent(None)
					self.root = new_root
					self.min = self.getRoot()  #update min and max
					self.max = self.getRoot()
					node.AVLdelete()
					return balancing_steps

				if node.is_left_child(): 							#has left child and is left child
					node.getLeft().setParent( y)
					y.setLeft( node.getLeft())
					node.AVLdelete()  
				else:												#has left child and is right child
					node.getLeft().setParent( y)
					y.setRight( node.getLeft())
					node.AVLdelete() 

			else:
				if node == self.getRoot():							#if node is root&has child, that child has no children. no need for height or size updates, just make it the root
					new_root = node.getRight()
					new_root.setParent(None)
					self.root = new_root
					self.min = self.getRoot()  #update min and max
					self.max = self.getRoot()
					node.AVLdelete()
					return balancing_steps	

				if node.is_left_child():								 #has right child and is left child
					node.getRight().setParent( y)
					y.setLeft( node.getRight())
					node.AVLdelete()  
				else:												#has right child and is right child
					node.getRight().setParent( y)
					y.setRight( node.getRight())
					node.AVLdelete()  

		else:															#1.case_3															
			successor = node.getSuccessor()

			if successor.getParent() != node:
				y = successor.getParent()  									#because of successor being deleted node in terms of shape, we start fixing here
			else:
				y = successor

			successor.getRight().setParent( successor.getParent())		#successor may have a right child and will NEVER have left child (else not successor)
			if successor.is_left_child():
				successor.getParent().setLeft(successor.getRight())
			else:
				successor.getParent().setRight(successor.getRight())

			successor.setParent(node.getParent())     					  #steal node's parent

			if node == self.getRoot():
				self.root = successor

			elif node.is_left_child():
				successor.getParent().setLeft( successor)	#set nodes left child to be successor
			else:
				successor.getParent().setRight(successor )  #set nodes right child to be successor

			successor.setRight( node.getRight())							#steal node's right child
			successor.getRight().setParent( successor)
			
			successor.setLeft(node.getLeft())							#steal node's left child
			successor.getLeft().setParent(successor)
			
			successor.setHeight(node.getHeight())
			successor.setSize(node.getSize())
			
			node.AVLdelete()
		
		########## done with 1 and 2 ####################
		########## start 3 ##############################
			
		balancing_steps = self.delete_style_balancing(y, balancing_steps)


		return balancing_steps


	"""maintains shape of tree after delete and join!

	@type node: AVLNode
	@param node: node that we start fixing and up
	@type  balancing_steps: int
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""	
	#complexity: O(log(n))	

	def delete_style_balancing(self, node, balancing_steps):
		while node!=None:
			node.updateMeasurements()
			if abs(node.getBF()) < 2 :
				if not node.getHeightUpdate():
					break
				else:
					node = node.getParent()
					balancing_steps += 1
			else: #getBF(y)=2
				node_temp = node.getParent()
				balancing_steps = self.ImplementRotation(node, balancing_steps)
				node = node_temp
				
		if node != None: ###height may not change now but size certainly has
			node.fix_size_rec()
		return balancing_steps




	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	#We have a pointer to the min node
	#time complexity: O(1)

	def first(self):
		if self.empty():
			return None
		return self.min.getValue()

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	#We have a pointer to the max node
	#time complexity: O(1)

	def last(self):
		if self.empty():
			return None
		return self.max.getValue()



	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	#did a tree walk with global list result, just like you would in BST
	#complexity: O(n)

	def listToArray(self):
		result = []
		
		def listtoArray_rec(node):
			if node.isRealNode():
				listtoArray_rec(node.getLeft())
				result.append(node.getValue())
				listtoArray_rec(node.getRight())

		listtoArray_rec(self.root)
		return result

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	#root size is the tree length
	#time complexity: O(1)

	def length(self):
		return self.root.getSize()

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	#find node in place i, than go up to the root and join bigger subtrees to Large tree, and smaller subtrees to Small Tree
	# time complexity: O(log(n))

	def split(self, i):

		x = self.TreeSelect(i+1)
		val_x = x.getValue()

		if i == 0:
			tree = AVLTreeList()
			self.delete(i)
			return [tree, val_x, self]
		if i == self.length()-1:
			tree = AVLTreeList()
			self.delete(i)
			return [self, val_x, tree]
			
		small_tree_max = x.getPredecessor()  ##we know these values to be true for THE FINAL TREES. we will udate the final trees min and max to be these values
		small_tree_min = self.min

		large_tree_min = x.getSuccessor()
		large_tree_max = self.max

		small_tree = AVLTreeList()  #initaize small tree with x left child subtree
		small_tree.root = x.getLeft()
		small_tree.root.setParent(None)
		small_tree.min = small_tree_min 
		small_tree.max = small_tree_max

		large_tree = AVLTreeList() #initaize large tree with x right child subtree
		large_tree.root = x.getRight()
		large_tree.root.setParent(None)
		large_tree.min = large_tree_min
		large_tree.max = large_tree_max
		
		
		y = x.getParent()
	
		come_from_left = False

		if x != self.getRoot():
			if x.is_left_child() :
				come_from_left = True


		x.AVLdelete()

		while (y != None):  #go from x to the root

			z = y.getParent()

			if come_from_left:

				if y != self.getRoot():
					if y.is_left_child() :
						come_from_left = True
					else:
						come_from_left = False

				temp_bigger_tree =  AVLTreeList()
				temp_bigger_tree.root = y.getRight()
				temp_bigger_tree.root.setParent(None)
				temp_bigger_tree.min = temp_bigger_tree.root
				temp_bigger_tree.max = temp_bigger_tree.root

				large_tree = large_tree.AVL_join(temp_bigger_tree, y)

			else:  

				if y != self.root:
					if y.is_left_child() :
						come_from_left = True
					else:
						come_from_left = False
				
				temp_smaller_tree =  AVLTreeList()
				temp_smaller_tree.root = y.getLeft()
				temp_smaller_tree.root.setParent(None)
				temp_smaller_tree.min = temp_smaller_tree.root
				temp_smaller_tree.max = temp_smaller_tree.root

				small_tree = temp_smaller_tree.AVL_join(small_tree, y )

			y = z  #go up to the parent
			
		
		small_tree.min = small_tree_min #final touchup to min and max!
		small_tree.max = small_tree_max
		large_tree.min = large_tree_min
		large_tree.max = large_tree_max

		return [small_tree ,val_x, large_tree]

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	#time complexity: O(log(n)) WC

	def concat(self, lst):

		height_difference = abs(self.root.getHeight() - lst.root.getHeight())

		if not self.empty() :
			val_x = self.max.getValue() # val of last node in self
			x = AVLNode(val_x) #create new node x
			last_index = self.length()-1
			self.delete(last_index)
			
			self.AVL_join(lst ,x)

		else:
			self.root = lst.root  #we have only one list
			self.min = lst.min
			self.max = lst.max
		return height_difference


	"""joins two trees given a middle index x
	@preL T1 and T2 are trees, x is a real node
	@type T1 & T2: AVLTreeList
	@type x: AVLNode
	@param T2: a list to be joined to T1 using x as join spot
	@rtype: joined AVLTree
	@returns: the tree formed by T1 T2 and x
	"""
	#time complexity: O(log(n)) WC

	def AVL_join(T1, T2, x):

		def join(small_tree, big_tree, x, is_equal , small_tree_first): #joins given that small_tree <= big_tree

			join_node = big_tree.root ##if both trees empty, root height -1 

			if (small_tree_first):  
				while join_node.getHeight() > small_tree.root.getHeight() and join_node.getHeight() != -1: #find the area of the join node
					join_node = join_node.getLeft()

			else:
				while join_node.getHeight() > small_tree.root.getHeight() and  join_node.getHeight() != -1: #find the area of the join node
					join_node = join_node.getRight()	
				

			def has_left_child(node):
				if node.getLeft().isRealNode():
					return True
				return False 
			
			def has_right_child(node):
				if node.getRight().isRealNode():
					return True
				return False

			if not is_equal:   #avoiding virtual nodes! esp it both trees empty
				join_node = join_node.getParent()
				if (small_tree_first):
					if has_left_child(join_node):
						join_node = join_node.getLeft()
				else:
					if has_right_child(join_node):
						join_node = join_node.getRight() 

			
			if (small_tree_first):  #pointers for x for all cases (also in isEqual == TRUE). if both trees empty then isequal == true, and this is fine- x now has 2 virtual nodes!
				x.setLeft(small_tree.root)
				x.setRight(join_node)
			else:
				x.setRight(small_tree.root)
				x.setLeft(join_node)


			if not is_equal:               
				x.setParent(join_node.getParent())
				if (small_tree_first):
					if x.getParent() != None:					 #in case x took place of root
						x.getParent().setLeft(x)
						if x.getParent().getRight() ==join_node: #in case right child of parent points to joinnode, got to get rid of pointer
							virtual_node = AVLNode(None)
							x.getParent().setRight(virtual_node)
					else:
						big_tree.root = x
				else:
					if x.getParent() != None:					#in case x took place of root
						x.getParent().setRight(x)
						if x.getParent().getLeft() ==join_node: #in case left child of parent points to joinnode, got to get rid of pointer
							virtual_node = AVLNode(None)
							x.getParent().setLeft(virtual_node)
					else:
						big_tree.root = x
			else:
				big_tree.root = x
			
			small_tree.root.setParent(x) 						#finally set pointers back to x
			join_node.setParent(x)

			#now big tree contains small tree
			big_tree.root.setParent(None)			#a fix in case x was not an empty node previously, like in split
			big_tree.delete_style_balancing(x, 0)   #balancing the tree, we dont need balancing steps info, so we put bs number
			small_tree.root = big_tree.root			#now both trees point to the same, joined tree
			return big_tree

		#gets T1 and T2 heights for isequal/ small tree first data later on. 
		# why check if T1 or T2 is empty if concat doesnt send empty T1? bc we use AVL join directly in split!

		T1height = None
		T2height = None

		if not T1.empty():
			T1height = T1.getRoot().getHeight()
		else:
			T1height = -1

		if not T2.empty():
			T2height = T2.getRoot().getHeight()
		else:
			T2height = -1

												#update min and max in the case that:
		if T1height == -1:    					#T1 is empty
			if T2height == -1:					#T1 and T2 are both empty
				T2.min = x
				T2.max = x
				T1.min = x
				T1.max = x
			else:								#T2 is not empty
				T2.min = x
				T1.min = x
				T1.max = T2.max			
		elif T2height == -1:                    #T2 is empty
			T1.max = x
			T2.min = T1.min
			T2.max = x
		else:									#neither are empty
			T2.min = T1.min		
			T1.max = T2.max

		if T1height < T2height:
			return join(T1, T2, x, False, True)  #small_tree_first = true

		elif T1height > T2height:
			return join(T2,T1, x, False, False)  #small_tree_first = false

		else:
			return join(T1, T2, x, True, True)  #save order. correct for case if both are empty 


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

		def search_rec(node, val):

			if not node.isRealNode():
				return False

			found= search_rec(node.getLeft(), val)

				
			if found:
				return True


			if node.getValue() == val:
				global culprit
				culprit = node
				return True


			found= search_rec(node.getRight(), val)
			
			return found

		found = search_rec(self.root, val)
		if not found:
			return -1
		else:
			return culprit.Tree_rank() 


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	#if the list isnt empty then we can return a root

	# Time complexity: O(1)

	def getRoot(self):
		if not self.empty():
			return self.root
		return None



	#our version of BST insert without balancing :)	

	# def insert_BST(self, i, val):

	# 	newNode = AVLNode(val)
	# 	balancing_steps = 0 #counting how many fixes to height and rotations

	# 	#if empty tree, we create new tree
	# 	if self.empty():
	# 		self.root = newNode
	# 		virtualRight = AVLNode(None)
	# 		virtualLeft = AVLNode(None)
	# 		newNode.setRight(virtualRight)
	# 		virtualRight.setParent(newNode)
	# 		newNode.setLeft(virtualLeft)
	# 		virtualLeft.setParent(newNode)
	# 		newNode.updateMeasurements()
	# 		self.min = newNode
	# 		self.max = newNode #max is now also the root

	# 	#1
	# 	else:
	# 		if i==self.length(): 
	# 			#insert last, last node has two virtual nodes, we insert in between last node and its virtual node
	# 			#the newNode, than make new leftVirtual to the newNode 
				
	# 			last_node = self.max
	# 			virtualLeft = AVLNode(None)
	# 			virtualRight = last_node.getRight()
	# 			newNode.setRight(virtualRight)
	# 			newNode.setLeft(virtualLeft)
	# 			last_node.setRight(newNode)

	# 			virtualLeft.setParent(newNode)
	# 			virtualRight.setParent(newNode)
	# 			newNode.setParent(last_node)

	# 		elif i == 0:
	# 			first_node = self.min
	# 			virtualRight = AVLNode(None)
	# 			virtualLeft = first_node.getLeft()
	# 			newNode.setRight(virtualRight)
	# 			newNode.setLeft(virtualLeft)
	# 			first_node.setLeft(newNode)

	# 			virtualLeft.setParent(newNode)
	# 			virtualRight.setParent(newNode)
	# 			newNode.setParent(first_node)


	# 		else:
	# 			currNode = self.TreeSelect(i+1)
	# 			if not currNode.getLeft().isRealNode():
	# 				#insert in index i, curr has left virtual nodes, we insert in between curr and its virtual node
	# 				#the newNode, than make new RightVirtual to the newNode  
	# 				virtualLeft = currNode.getLeft()
	# 				virtualRight = AVLNode(None)
	# 				newNode.setLeft(virtualLeft)
	# 				newNode.setRight(virtualRight)
	# 				currNode.setLeft(newNode)

	# 				virtualLeft.setParent(newNode)
	# 				virtualRight.setParent(newNode)
	# 				newNode.setParent(currNode)


	# 			else:
	# 				#insert in index i, pre has two virtual nodes, we insert in between pre and its virtual node
	# 				#the newNode, than make new leftVirtual to the newNode 
	# 				preNode = currNode.getPredecessor()
	# 				virtualLeft = AVLNode(None)
	# 				virtualRight = preNode.getRight()
	# 				newNode.setRight(virtualRight)
	# 				newNode.setLeft(virtualLeft)
	# 				preNode.setRight(newNode)

	# 				virtualLeft.setParent(newNode)
	# 				virtualRight.setParent(newNode)
	# 				newNode.setParent(preNode)
					
	# 		if i==self.length(): #updates max and min only after inserting the node, to help with case when list is empty
	# 			self.max = newNode
	# 		if i == 0:
	# 			self.min = newNode

	# 		newNode.updateMeasurements() #update size and height without adding to balancing_steps since its a new node not updated node
	# 		#2

	# 		y = newNode.getParent()
	# 		while y != None:
	# 			y.updateMeasurements()

	# 			if not y.getHeightUpdate():
	# 					break
	# 			else:
	# 				y = y.getParent()
	# 				balancing_steps += 1

	# 		if y != None: ###height may not change now but size certainly has
	# 			y.fix_size_rec()

	# 	return balancing_steps