import functools
from flask import Flask, render_template
import json
import os



from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('search', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/search', methods=('POST','GET'))
def search():
	Result = ''
	choice = ''
	# if request.method == 'POST':
	# 	content = request.form['search']
	# 	choice = request.values.get("search_method")
	# 	Result = "search method: "+choice+"\nsearch content: "+content
	# 	# print(Result)
	# 	error = None
	#
	# 	if not content:
	# 		error = 'Content Cannot be None.'
	#
	# 	flash(error)


	#数组传参
	#num=["","",""]

	if request.method == 'POST':
		content = request.form
		num = {
			1: ['10001', '123', 'Mike', '2017-5-6'],
			2: ['10002', '123', 'Sam', '2018-5-6'],
			3: ['10003', '123', 'hong', '2019-5-6']                              
		}


		return render_template('music.html', num=num)



def algorithm(content):
	return content



