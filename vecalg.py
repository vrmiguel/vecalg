'''
vecalg - A concise library for row-vector algebra.
Vinícius Rodrigues Miguel - Federal University of São Paulo
github.com/vrmiguel/vecalg
'''

norm_type = "l2" 		# You can modify this in order to select either the Euclidean norm ("l2") or the Manhattan distance ("l1").

def set_norm(selection):
		if (isinstance(selection, str)):
			if selection.lower() == 'l1' or selection.lower() == 'manhattan':
				norm_type = 'l1'
			elif selection.lower() == 'l2' or selection.lower() == 'euclidean':
				norm_type = 'l2'
			else:
				print("Unknown norm. Euclidean norm will be assumed.")
				norm_type = 'l2'
		else:
			return TypeError()

class vector:
	elems = []

	def __init__(self, *args):
		if isinstance(args[0], list):
			self.elems = [arg for arg in args][0]
		elif isinstance(args[0], (int, float)):
			for arg in args:
				if not isinstance(arg, (int, float)):  	# If the first given argument was a number, but a non-number is also found, then raise an exception
					raise ValueException("can't construct vector with types int/float and {%s}" % type(arg))
			self.elems = [x for x in args]
		else: raise Exception("type ", str(type(args[0])), " unknown for vector construction")

	def __str__(self):
		return str(self.elems).replace('[', '<').replace(']', '>')

	def __repr__(self):
		return str(self)

	def __add__(self, operand):
		if isinstance(operand, list):
			if len(self.elems) == len(operand.elems):
				return vector([x+y for x, y in zip(self.elems, operand.elems)])
			else:
				raise ValueException("can't add vectors of different size.")			
		else: raise ValueException("unknown operation.")

	#	TODO: make multiplication transitive
	def __mul__(self, operand):
		if isinstance(operand, (int, float)):
			return vector([elem * operand for elem in self.elems]) # Return multiplication by scalar
		elif isinstance(operand, vector):
			if len(operand.elems) != len(self.elems):
				raise ValueException("can't multiply")
			else:
				return vector([x*y for x, y in zip(self.elems, operand.elems)])

	def __rmul__(self, operand):
		return self * operand

	'''
	def __eq__(self, operand):
		if not isinstance(operand, (int, float)):
			return False
		else:
	'''

	def __truediv__(self, operand):
		if isinstance(operand, (int, float)):
			return vector([elem/operand for elem in self.elems])
		else: raise ValueError("there is no well-behaved division of vectors.")

	def __floordiv__(self, operand):
		if isinstance(operand, (int, float)):
			return vector([x//operand for x in self.elems])
		else: raise TypeException()		

	def norm(self):
		if norm_type == 'l2':
			return sum([elem**2 for elem in self.elems])**0.5 	# Return the L2-norm, that is, the Euclidean norm of the given vector
		elif norm_type == 'l1':
			return sum([abs(elem) for elem in self.elems])		# Return the L1-norm, that is, the Manhattan distance of the given vector
		else:
			raise ValueError("unknown norm type")

	def magnitude(self):
		return self.norm()

	def to_unit_vector(self):
		if norm_type == 'l1':
			norm_type = l2
			norm_ = self.norm()
			norm_type = 'l1'
			return self/norm_
		elif norm_type == 'l2':
			return self/norm_
		else:
			raise ValueError("unknown norm_type")

	def __abs__(self):
		return self.norm()

	def set_norm(self, selection):
		if (isinstance(selection, str)):
			if selection.lower() == 'l1' or selection.lower() == 'manhattan':
				norm_type = 'l1'
			elif selection.lower() == 'l2' or selection.lower() == 'euclidean':
				norm_type = 'l2'
			print("Unknown norm. Euclidean norm will be assumed.")
				norm_type = 'l2'
		else:
			return TypeError()

	def angle(self):
		print("Angle not yet implemented.")
		pass	#todo

if __name__ == '__main__':
	s = vector(2, 3)
	y = vector(5, 6)
	z = vector(2, 3)

	#print("s*y:", s*y)
	#print("s*y*z:", s*y*z)
	print(abs(s))