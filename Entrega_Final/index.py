from flask import Flask, render_template,request
import clases.cCliente as cliente
import clases.cDataBase as db

##Constantes
T_TITULO = "BEDU PYTHON TEST APP"
T_CLIENTE = "CREACION DE CLIENTE"
T_REPORTES = "REPORTES DE CLIENTES"

app = Flask(__name__)

##Vista - Enrutamientos

##Enrutamiento Index
@app.route('/')
def index():
  if request.method == 'GET':
    #inicializa objetos de BBDD
    objDB = db.DBUtils()
    objConn = objDB.abrirConexion()
    objDB.crearTablaCliente(objConn)
    objConn.close()
    return render_template("index.html", titulo=T_TITULO)

##Enrutamiento para Creacion de Cliente
@app.route('/create/',methods=['GET', 'POST'])
def create():
  if request.method == 'GET':
    return render_template("create.html", titulo=T_CLIENTE)
  
  if request.method == 'POST':
    nombre = request.form['fNombresCliente']
    correo = request.form['fCorreoElectronico']
    documento = request.form['fDocumento']
    #Inserta Cliente
    mensaje = cliente.Cliente(nombre,correo,documento).CrearCliente()
    #
    return render_template("create.html", titulo=T_CLIENTE, mensaje=mensaje)

##Enrutamiento para la consulta de reportes
@app.route('/reports/',methods=['GET'])
def reports():
  if request.method == 'GET':
    listaClientes = cliente.Cliente(None,None,None).reporteClientes()
    
    return render_template("reports.html", titulo=T_REPORTES,clientes=listaClientes)
  

##
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
