### we prepend t_ to tablenames and f_ to fieldnames for disambiguity
db.define_table('Catedratico',
                Field('Nombre', type='string', label=T('Nombre')),
                Field('Dpi', type='string', label=T('DPI')),
                Field('Telefono', type='integer', label=T('TELEFONO')),
                Field('Especializacion', type='integer', label=T('ESPECIALIZACION')),
                migrate=False)

db.define_table('Catedratico_archive',db.Catedratico,Field('current_record','reference Catedratico',readable=False,writable=False))
