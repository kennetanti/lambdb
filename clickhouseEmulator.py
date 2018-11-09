from flask import Flask, redirect, render_template, request, jsonify

from queryTypes import SQLQuery

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def rootQuery():
	if request.method == "POST":  # clickhouse POST body query
		if request.args.get('query', False):
			query = str(request.args['query']) + " " + request.data
		else:
			query = request.data
		result = SQLQuery(query)
	elif request.method == "GET":  # this is clickhouse GET query
		if request.args.get('query', False):
			result = SQLQuery(request.args['query'])
		else:  # just plain old / returns Ok
			return 'Ok'


if __name__ == '__main__':
	app.run()
