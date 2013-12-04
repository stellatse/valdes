#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import json
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *
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
def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()
app = web.application(urls, globals())
app.add_processor(load_sqla)

class index:
    def GET(self):
        content = "test"
        return render.index()

class signup:
    def GET(self):
        return render.signup()
		
    def POST(self):
        # try:
        i = web.input()
        data = web.data()
        print i
        print data
        u = User(name='', fullname='', password=i.password, email=i.email, phone=i.phone, address='', section=0)
        web.ctx.orm.add(u)
        # except Exception, e:
            # return json.dumps(["reg_error"])
        # else:
        if u.id:
            web.setcookie('uid', str(u.id), settings.COOKIE_EXPIRES)
            raise web.seeother('/user/%d' % u.id)
	
class login:
    def GET(self):
        return render.login()


		
if __name__ == "__main__":
    app.run()
