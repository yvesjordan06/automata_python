class Transition:
	def __init__(self, _from, _on, _to = None):
		self.__from = str(_from)
		self.__to = str(_to) if _to is not None else _to
		self.__on = str(_on)
	def __repr__(self):
		return 'Transtion ('+str(self)+')'

	def __hash__(self):
		return hash(repr(self))
	
	def __eq__(self, other):
	 	return hash(self) == hash(other)
	def get_from(self):
		return self.__from

	def get_to(self):
		return self.__to

	def get_on(self):
		return self.__on
	def get_transition(self):
		return {'from':self.__from,'on':self.__on,'to':self.__to}


	def __str__(self):
 		return "from: " + self.__from + " , " + "on: " + self.__on + " , " + "to: " + self.__to

pass
