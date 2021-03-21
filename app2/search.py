import functools
from flask import Flask, render_template
import json
import os



from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('search', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def search():
	Result = ''
	choice = ''
	if request.method == 'POST':
		content = request.form['search']
		choice = request.values.get("search_method")
		Result = "search method: "+choice+"\nsearch content: "+content
		# print(Result)
		error = None

		if not content:
			error = 'Content Cannot be None.'

		flash(error)


	#数组传参
	#num=["","",""]

	#字典传参
	num = {
			1: ['10001', '123', 'Mike', '男', '21'],
			2: ['10002', '123', 'Sam', '男', '25'],
			3: ['10003', '123', 'hong', '女', '20']
		}

	return render_template('find.html', num=num)

def algorithm(content):
	return content



