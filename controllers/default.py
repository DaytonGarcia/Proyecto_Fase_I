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
def cursos():
    form = SQLFORM.smartgrid(db.cursos)
    return locals()
