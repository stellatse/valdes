#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import settings

db = web.database(dbn='mysql', db='express', user=settings.MYSQL_USERNAME, pw=settings.MYSQL_PASSWORD)