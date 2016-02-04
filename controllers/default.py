# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

@auth.requires_login()
def especializacion():
    form = SQLFORM.smartgrid(db.Especializacion,onupdate=auth.archive)
    return locals()

def error():
    return dict()
