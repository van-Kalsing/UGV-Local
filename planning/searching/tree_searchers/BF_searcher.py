from planning.searching.tree_searchers.searcher import Searcher







class BFSearcher(Searcher):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__perspective_states_records = []
		
		
		
		
		
	@property
	def _contains_perspective_states_records(self):
		return bool(self.__perspective_states_records)
		
		
		
	def _insert_perspective_state_record(self, perspective_state_record):
		self.__perspective_states_records.append(
			perspective_state_record
		)
		
		
		
	def _retrieve_perspective_state_record(self):
		if self.__perspective_states_records:
			perspective_state_record = self.__perspective_states_records.pop(0)
		else:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		return perspective_state_record
		