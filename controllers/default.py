# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def alumnos():
    form = SQLFORM.smartgrid(db.ALUMNO,onupdate=auth.archive)
    return locals()

def ayuda():
    return dict()
