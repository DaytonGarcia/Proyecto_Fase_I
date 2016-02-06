db.define_table('Catedratico',
                Field('Nombre', type='string', label=T('Nombre'),notnull=True),
                Field('Dpi', type='string', label=T('DPI'),notnull=True,unique=True),
                Field('Telefono', type='integer', label=T('TELEFONO'),notnull=True),
                Field('Especializacion', type='integer', label=T('ESPECIALIZACION'),notnull=False),
                migrate=False)
