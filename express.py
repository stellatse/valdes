#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import json
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

web.config.debug = False
urls = (
    '/', 'index',
    '/signup', 'signup',
    '/login', 'login',
    '/about', 'about',
    '/contact', 'contact',
    '/service', 'service',
    '/mioder', 'myorder',
    '/user', 'account'
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
session = web.session.Session(app, web.session.DiskStore('sessions'))
params = {'context': session}
global_vars = dict(settings.GLOBAL_PARAMS.items() + params.items())
render = web.template.render('templates/', base='layout', globals=global_vars)
render_plain = web.template.render('templates/')


class index:
    def GET(self):
        if session.get('logged_in', False):
            auth = False
        else:
            auth = True
        content = "test"
        return render.index()


class signup:
    def GET(self):
        return render.signup()

    def POST(self):
        try:
            i = web.input()
            data = web.data()
            u = User(name='', fullname='', password=i.password, email=i.email, phone=i.phone, address='', section=0)
            web.ctx.orm.add(u)
        except Exception, e:
            return json.dumps(["reg_error"])
        else:
            return web.seeother('/user')


class login:
    def GET(self):
        return render.login()

    def POST(self):
        i = web.input()
        u = User.login(i.email, i.password)
        if u:
            session.login = True
            return render.index()
        else:
            return json.dumps(["login_error"])


class account:
    def GET(self):
        return render.account()


if __name__ == "__main__":
    app.run()
