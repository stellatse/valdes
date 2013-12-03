#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
render = web.template.render('templates/', base='layout')
render_plain = web.template.render('templates/')
urls = (
	'/', 'index',
	'/signup', 'signup',
	'/about', 'about',
	'/contact', 'contact',
	'/service', 'service',
	'/mioder', 'myorder'
)

class index:
	def GET(self):
		content = "test"
		return render.index()

class signup:
	def GET(self):
		return render.signup()
	


		
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()