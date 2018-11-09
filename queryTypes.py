from sqlparse import parse
from enum import Enum


class CRUD(Enum):
	create = 1
	read = 2
	update = 3
	delete = 4


class SortStyle(Enum):
	noSort = 0
	ascending = 1
	descending = 2


class Query:
	crudType = CRUD.create
	what = None  # select WHAT
	db = None  # from DB.TABLENAME
	tablename = None
	filter = None  # where FILTER
	sorting = SortStyle.noSort

	values = {}  # for insert and update	
	then = None  # for multi queries


class NotYet(NotImplemented):
	def __str__(self):
		return "this shit aint implemented yet"


class SQLQuery(Query):
	def __init__(self, sql=""):
		self.raw_sql = sql
		thing = parse(sql)
		for statement in thing:
			keyword = statement[0].normalized
			if keyword not in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
				print "got unsupported query: " + statement.normalized
				continue  # for now
			for kw in statement:
				if kw.is_whitespace:
					continue
