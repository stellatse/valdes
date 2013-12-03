#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import json
render = web.template.render('templates/', base='layout')
render_plain = web.template.render('templates/')
urls = (
	'/', 'index',
	'/signup', 'signup',
	'/login', 'login',
	'/about', 'about',
	'/contact', 'contact',
	'/service', 'service',
	'/mioder', 'myorder',
	'/user/(\d+)', 'account'
)

class index:
	def GET(self):
		content = "test"
		return render.index()

class signup:
	def GET(self):
		return render.signup()
		
	def POST(self):
		try:
			i = web.input()
			user_id = model.User().new(i.phone, i.email, i.password)
		except Exception, e:
			return json.dumps(["邮箱或手机号码已存在，请重新注册"])
		else:
			if user_id:
				web.setcookie('user_id', str(user_id), settings.COOKIE_EXPIRES)
				raise web.seeother('/user/%d' % user_id)
	
class login:
	def GET(self):
		return render.login()

		
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()