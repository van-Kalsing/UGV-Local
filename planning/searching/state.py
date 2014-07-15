import abc





class State(metaclass = abc.ABCMeta):
	@abc.abstractproperty
	def is_final(self):
		pass
		
		
		
	@abc.abstractproperty
	def successors(self):
		pass
		
		
		
	@abc.abstractmethod
	def get_transfer_cost(self, successor):
		pass
		
		
		
		
		
		
		
class EvaluatedState(State):
	@abc.abstractproperty
	def estimation(self):
		pass
		