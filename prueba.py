from gluon.contrib.webclient import WebClient
client = WebClient('http://127.0.0.1:8000/Proyecto_Fase_I/default/')
client.get('index')

# register
data = dict(first_name='Homer',
            last_name='Simpson',
            email='homer@web2py.com',
            password='test',
            password_two='test',
            _formname='register')
client.post('user/register', data=data)

# logout
client.get('user/logout')

# login
data = dict(email='danigay@gmail.com',
            password='1234',
            _formname='login')
client.post('user/login', data=data)

# check registration and login were successful
client.get('user/profile')
assert 'Welcome danigay' in client.text

# Prueba funcional para la funcion Agregar Especialidad
# Detalle='especialidad' Detalle es el atributo como lo defini en dbwizard, si hay mas atributos se agregan con "," 
# _formname='registro' Esto se queda asi
# data1 es el nombre del objeto que tiene los mismo atributos que mi tabla
# client.post('especializacion', data=data1) especializacion es el nombre de la pagina html, que va despues de default/ 
data1 = dict(Detalle='especialidad',
            _formname='registro')
client.post('especializacion', data=data1)
#######Aca termina la funcionalidad, debe haber insertado especialidad en mi base de datos#######################
#######Web2py debe estar corriendo

# logout
client.get('user/logout')

# print some variables
print
for method, url, status, t in client.history:
    if  status==200:
        print url+' superada'
