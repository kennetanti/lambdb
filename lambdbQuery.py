from sqlparse import parse

class CRUD(Enum):
	create = 1
	read = 2
	update = 3
	delete = 4


class SortStyle(Enum):
	noSort = 0
	ascending = 1
	descending = 2

class ReadQuery:
	what = None  # select WHAT
	db = None  # from DB.TABLENAME
	tablename = None
	filter = None  # where FILTER
	sorting = SortStyle.noSort
	#grouping = None
	
class CreateQuery:
	what = None  # select WHAT
	db = None  # from DB.TABLENAME
	tablename = None
	rows = [] # KEYNAMES values ROWITEMS
	
class UpdateQuery:
	what = None  # select WHAT
	db = None  # from DB.TABLENAME
	tablename = None
	filter = None  # where FILTER
	update = [] # fuck this is gunna suck
	
class DeleteQuery:
	what = None  # select WHAT
	db = None  # from DB.TABLENAME
	tablename = None
	filter = None  # where FILTER

def sqlToLambdb(query):
	parsed = parse(query)
	for 
