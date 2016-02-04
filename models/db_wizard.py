### we prepend t_ to tablenames and f_ to fieldnames for disambiguity
db.define_table('ALUMNO',
                Field('ID', 'id'),
                Field('Carne', type='string', label=T('Carne')),
                Field('Nombres', type='string', label=T('Nombres')),
                Field('Apellidos', type='string', label=T('Apellidos')),
                Field('Direccion', type='string', label=T('Direccion')),
                Field('Telefono', type='string', label=T('Telefono')),
                Field('Correo', type='string', label=T('Correo')),
                migrate=False)



db.define_table('ALUMNO_archive',db.ALUMNO,Field('current_record','reference ALUMNO',readable=False,writable=False))
