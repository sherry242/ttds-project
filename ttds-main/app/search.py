import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template,current_app, request,Blueprint, flash
from .flask_paginate1 import Pagination, get_page_parameter,get_per_page_parameter
import pandas

# 数组传参
# num=["","",""]

# 字典传参
num = {
	1: ['10001', '123', 'Mike', '2017-5-6'],
	2: ['10002', '123', 'Sam', '2018-5-6'],
	3: ['10003', '123', 'hong', '2019-5-6'],
	4: ['10004', '123', 'xiao', '2019-5-6']
}
data_pd = pandas.DataFrame.from_dict(num,orient='index',columns=['Songs','Albums','Artists','date'])
data_dict = data_pd.to_dict(orient = 'records')

def get_users(offset=0, per_page=20):
    return data_dict[offset: offset + per_page]

bp = Blueprint('search', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search_Songs', methods=('GET', 'POST'))
def search_Songs():
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	total = len(data_dict)
	pagination_users = get_users(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')

	return render_template('music.html',
						   data=pagination_users,
						   page=page,
						   per_page=per_page,
						   pagination=pagination,
						   data_num=data_num,
						   time=time
						   )


@bp.route('/search_Artists',methods=('GET', 'POST'))
def search_Artists():
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	total = len(data_dict)
	pagination_users = get_users(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')

	return render_template('artists.html',
						   data=pagination_users,
						   page=page,
						   per_page=per_page,
						   pagination=pagination,
						   data_num=data_num,
						   time=time
						   )

@bp.route('/search_Albums',methods=('GET', 'POST'))
def search_Albums():
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	total = len(data_dict)
	pagination_users = get_users(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')

	return render_template('albums.html',
						   data=pagination_users,
						   page=page,
						   per_page=per_page,
						   pagination=pagination,
						   data_num=data_num,
						   time=time
						   )

@bp.route('/search_Lyrics',methods=('GET', 'POST'))
def search_Lyrics():
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	total = len(data_dict)
	pagination_users = get_users(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')

	return render_template('lyrics.html',
						   data=pagination_users,
						   page=page,
						   per_page=per_page,
						   pagination=pagination,
						   data_num=data_num,
						   time=time
						   )


@bp.route('/search', methods=('GET', 'POST'))
def search():
	Result = ''
	choice = ''
	# if request.method == 'POST':
	# 	# 	content = request.form['search']
	# 	# 	choice = request.values.get("search_method")
	# 	# 	Result = "search method: "+choice+"\nsearch content: "+content
	# 	# 	# print(Result)
	# 	# 	error = None
	# 	#
	# 	# 	if not content:
	# 	# 		error = 'Content Cannot be None.'
	# 	#
	# 	# 	flash(error)

	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	total = len(data_dict)
	pagination_users = get_users(offset=offset, per_page=per_page)
	pagination = Pagination(page=page, per_page=per_page, total=total,
							css_framework='bootstrap4')

	return render_template('music.html',
						   data=pagination_users,
						   page=page,
						   per_page=per_page,
						   pagination=pagination,
						   kwd=keyword,
						   data_num=data_num,
						   time=time)



def get_page_args(
    page_parameter=None, per_page_parameter=None, for_test=False, **kwargs
):
    """param order: 1. passed parameter 2. request.args 3: config value
    for_test will return page_parameter and per_page_parameter"""
    args = request.args.copy()
    args.update(request.view_args.copy())

    page_name = get_page_parameter(page_parameter, args)
    per_page_name = get_per_page_parameter(per_page_parameter, args)
    for name in (page_name, per_page_name):
        if name in kwargs:
            args.setdefault(name, kwargs[name])

    if for_test:
        return page_name, per_page_name

    page = int(args.get(page_name, 1, type=int))
    per_page = args.get(per_page_name, type=int)
    if not per_page:
        per_page = int(current_app.config.get(per_page_name.upper(), 3))   #这里改per_page
    else:
        per_page = int(per_page)

    offset = (page - 1) * per_page
    return page, per_page, offset


def algorithm(content):
	return content

##############################################################################################################
keyword='Mike'
data_num=len(data_dict)
time='0.3451s'
#############################################################################################################