#Importaciones Python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from tkinter import scrolledtext as st
import sqlite3

#Variable donde almacenará el nombre de la base de datos
nombreBBDD = ""

#Variables utilizadas para realizar la conexion a la BBDD
nombre = ""
correo = ""
contrasenya = ""

#Variables utilizadas para añadir un nuevo contacto a la BBDD
identificador = ""
nombreContacto = ""
telefono = ""
correoElectronico = ""
IVA = ""
calle = ""
codigoPostal = ""
ciudad = ""
pais = ""

#Variables utilzadas para añadir una nueva oportunidad
identificador_nuevaOportunidad = ""
identificadorCliente_nuevaOportunidad = ""
nombreOportunidad_nuevaOportunidad = ""
correoElectronico_nuevaOportunidad = ""
numeroTelefono_nuevaOportunidad = ""
ingresoEsperado_nuevaOportunidad = ""
estadoOportunidad_nuevaOportunidad = ""

#Variables utilizadas para añadir un nuevo presupuesto
identificador_nuevoPresupuesto = ""
identificadorCliente_nuevoPresupuesto = ""
identificadorPedido_nuevoPrespuesto = ""
fechaInicio_nuevoPresupuesto = ""
fechaFin_nuevoPresupuesto = ""

#Variables utilizadas para añadir un nuevo producto
identificadorProducto_producto = ""
nombreProducto_producto = ""
descripcionProducto_producto = ""
cantidadStock_producto = ""
precioUnitario_producto = ""


class Ventana():
    #Constructor de la clase y definición de los distintos frames
    def __init__(self, root):       
        self.root = root

        self.frameVentanaInicial = tk.Frame(self.root)
        self.frameVentanaInicial.pack(fill="both", expand="True")
        self.frameVentanaInicial.config(bd=10, bg="azure2")
        
        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.frameVentanaContacto = tk.Frame(self.root)
        self.frameVentanaContacto.pack(fill="both", expand="True")
        self.frameVentanaContacto.config(bd=10, bg="azure2")
        
        self.frameVentanaNuevaOportunidad = tk.Frame(self.root)
        self.frameVentanaNuevaOportunidad.pack(fill="both", expand="True")
        self.frameVentanaNuevaOportunidad.config(bd=10, bg="azure2")

        self.frameVentanaNuevoPresupuesto = tk.Frame(self.root)
        self.frameVentanaNuevoPresupuesto.pack(fill="both", expand="True")
        self.frameVentanaNuevoPresupuesto.config(bd=10, bg="azure2")

        self.frameVentanaProducto = tk.Frame(self.root)
        self.frameVentanaProducto.pack(fill="both", expand="True")
        self.frameVentanaProducto.config(bd=10, bg="azure2")

        self.frameNuevo = tk.Frame(self.root)
        self.frameNuevo.pack(fill="both", expand="True")
        self.frameNuevo.config(bd=10, bg="azure2")

        self.frameCalificado = tk.Frame(self.root)
        self.frameCalificado.pack(fill="both", expand="True")
        self.frameCalificado.config(bd=10, bg="azure2")

        self.framePropuesta = tk.Frame(self.root)
        self.framePropuesta.pack(fill="both", expand="True")
        self.framePropuesta.config(bd=10, bg="azure2")

        self.frameGanado = tk.Frame(self.root)
        self.frameGanado.pack(fill="both", expand="True")
        self.frameGanado.config(bd=10, bg="azure2")

        self.frameVisualizarDatos = tk.Frame(self.root)
        self.frameVisualizarDatos.pack(fill="both", expand="True")
        self.frameGanado.config(bd=10, bg="azure2")
        
        self.ventanaInicial()

    #Método para definiciar la ventana inicial 
    def ventanaInicial(self):
        nombre = tk.StringVar()
        correo = tk.StringVar()
        contrasenya = tk.StringVar()

        self.root.geometry("500x300")

        self.root.resizable(width=False, height=False)
        
        self.label = tk.Label(self.frameVentanaInicial, text="CRM", font=("Courier", 20, "bold"), bg="azure2")
        self.label.pack()
        
        self.marcoInformacion = tk.LabelFrame(self.frameVentanaInicial, text="Información básica", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack(padx=10, pady=15)
        
        self.labelNombre = tk.Label(self.marcoInformacion, text="Nombre", font=("Courier", 14), bg="azure3")
        self.labelNombre.pack()
        
        self.campoNombre = ttk.Entry(self.marcoInformacion, textvariable=nombre)
        self.campoNombre.pack()
        
        self.labelCorreo = tk.Label(self.marcoInformacion, text="Correo electrónico", font=("Courier", 14), bg="azure3")
        self.labelCorreo.pack()
        
        self.campoCorreo = ttk.Entry(self.marcoInformacion, textvariable=correo)
        self.campoCorreo.pack()
        
        self.labelContrasenya = tk.Label(self.marcoInformacion, text="Contraseña", font=("Courier", 14), bg="azure3")
        self.labelContrasenya.pack()
        
        self.campoContrasenya = tk.Entry(self.marcoInformacion, show="*", textvariable=contrasenya)
        self.campoContrasenya.pack()
        
        self.botonConfirmar = ttk.Button(self.marcoInformacion, command=lambda: self.confirmar(nombre.get(), correo.get(), contrasenya.get()) ,text="Confirmar información", width=40)
        self.botonConfirmar.pack()
        
    #Método para definir la ventana del pipeline
    def ventanaPipeline(self):
        self.root.geometry("1100x350")
        self.root.resizable(width=False, height=False)

        self.tituloPipeline = tk.Label(self.frameVentanaPipeline, text="Opciones CRM", font=("Courier", 20, "bold"), bg="azure2")
        self.tituloPipeline.grid(row=0, column=0, columnspan=4)

        self.botonPipelineNuevo = tk.Button(self.frameVentanaPipeline, text="NUEVO", font=("Courier", 17), command=lambda: self.nuevo())
        self.botonPipelineNuevo.grid(row=1, column=0, padx=10, pady=10)
        
        self.botonPipelineCalificado = tk.Button(self.frameVentanaPipeline, text="CALIFICADO", font=("Courier", 17), command=lambda: self.calificado())
        self.botonPipelineCalificado.grid(row=1, column=1, padx=10, pady=10)
        
        self.botonPipelinePropuesta = tk.Button(self.frameVentanaPipeline, text="PROPUESTA", font=("Courier", 17), command=lambda: self.propuesta())
        self.botonPipelinePropuesta.grid(row=1, column=2, padx=10, pady=10)
        
        self.botonPipelineGanado = tk.Button(self.frameVentanaPipeline, text="GANADO", font=("Courier", 17), command=lambda: self.ganado())
        self.botonPipelineGanado.grid(row=1, column=3, padx=10, pady=10)
        
        self.botonContacto = tk.Button(self.frameVentanaPipeline, command=lambda: self.contacto(), text="Contactos", font=("Courier", 17))
        self.botonContacto.grid(row=2, column=0, padx=25, pady=10)
        
        self.botonNuevaOportunidad = tk.Button(self.frameVentanaPipeline, command=lambda: self.nuevaOportunidad(), text="Nueva oportunidad", font=("Courier", 17))
        self.botonNuevaOportunidad.grid(row=2, column=1, padx=25, pady=10)

        self.botonNuevoPrespuesto = tk.Button(self.frameVentanaPipeline, command=lambda: self.nuevoPrespuesto(), text="Nuevo presupuesto", font=("Courier", 17))
        self.botonNuevoPrespuesto.grid(row=2, column=2, padx=25, pady=10)

        self.botonNuevoPedido = tk.Button(self.frameVentanaPipeline, text="Nuevo producto", font=("Courier", 17), command=lambda: self.nuevoProducto())
        self.botonNuevoPedido.grid(row=2, column=3, padx=25, pady=10)

        self.botonVisualizarInformacion = tk.Button(self.frameVentanaPipeline, text="Visualizar datos", font=("Courier", 17), command=lambda: self.visualizar_datos())
        self.botonVisualizarInformacion.grid(row=3, column=0, padx=25, pady=10, columnspan=4)

        self.botonCerrarSesion = tk.Button(self.frameVentanaPipeline, text="Cerrar sesión", font=("Courier", 17), command=lambda: self.cerrar_sesion())
        self.botonCerrarSesion.grid(row=4, column=0, padx=25, pady=10, columnspan=4)
        
    #Método para definir la ventana del contacto
    def ventanaContacto(self):       
        identificador = tk.StringVar()
        nombreContacto = tk.StringVar()
        telefono = tk.StringVar()
        correoElectronico = tk.StringVar()
        IVA = tk.StringVar()
        calle = tk.StringVar()
        codigoPostal = tk.StringVar()
        ciudad = tk.StringVar()
        pais = tk.StringVar()

        self.root.geometry("500x680")

        self.labelTituloNuevoContacto = tk.Label(self.frameVentanaContacto, text="Nuevo contacto", font=("Courier", 20, "bold"), bg="azure2")
        self.labelTituloNuevoContacto.pack()
        
        self.marcoInformacion = tk.LabelFrame(self.frameVentanaContacto, text="Información nuevo contacto", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack(padx=10, pady=15)

        self.labelIdentificador = tk.Label(self.marcoInformacion, text="Identificador", font=("Courier", 14), bg="azure3")
        self.labelIdentificador.pack()
        self.campoIdentificador = ttk.Entry(self.marcoInformacion, textvariable=identificador)
        self.campoIdentificador.pack()

        self.labelNombre = tk.Label(self.marcoInformacion, text="Nombre", font=("Courier", 14), bg="azure3")
        self.labelNombre.pack()
        self.campoNombre = ttk.Entry(self.marcoInformacion, textvariable=nombreContacto)
        self.campoNombre.pack()

        self.labelTelefono = tk.Label(self.marcoInformacion, text="Telefono", font=("Courier", 14), bg="azure3")
        self.labelTelefono.pack()
        self.campoTelefono = ttk.Entry(self.marcoInformacion, textvariable=telefono)
        self.campoTelefono.pack()

        self.labelCorreoElectronico = tk.Label(self.marcoInformacion, text="Correo eléctronico", font=("Courier", 14), bg="azure3")
        self.labelCorreoElectronico.pack()
        self.campoCorreoElectronico = ttk.Entry(self.marcoInformacion, textvariable=correoElectronico)
        self.campoCorreoElectronico.pack()

        self.labelIVA = tk.Label(self.marcoInformacion, text="Porcertanje IVA", font=("Courier", 14), bg="azure3")
        self.labelIVA.pack()
        self.campoIVA = ttk.Entry(self.marcoInformacion, textvariable=IVA)
        self.campoIVA.pack()

        self.marcoDireccion = tk.LabelFrame(self.frameVentanaContacto, text="Direccion", font=("Courier", 17), bg="azure3")
        self.marcoDireccion.pack(padx=10, pady=15)

        self.labelCalle = tk.Label(self.marcoDireccion, text="Calle", font=("Courier", 14), bg="azure3")
        self.labelCalle.pack()
        self.campoCalle = ttk.Entry(self.marcoDireccion, textvariable=calle)
        self.campoCalle.pack()

        self.labelCodigo = tk.Label(self.marcoDireccion, text="Codigo postal", font=("Courier", 14), bg="azure3")
        self.labelCodigo.pack()
        self.campoCodigo = ttk.Entry(self.marcoDireccion, textvariable=codigoPostal)
        self.campoCodigo.pack()

        self.labelCiudad = tk.Label(self.marcoDireccion, text="Ciudad", font=("Courier", 14), bg="azure3")
        self.labelCiudad.pack()
        self.campoCiudad = ttk.Entry(self.marcoDireccion, textvariable=ciudad)
        self.campoCiudad.pack()

        self.labelPais = tk.Label(self.marcoDireccion, text="Pais", font=("Courier", 14), bg="azure3")
        self.labelPais.pack()
        self.campoPais = ttk.Entry(self.marcoDireccion, textvariable=pais)
        self.campoPais.pack()
        
        self.botonConfirmar_contacto= ttk.Button(self.frameVentanaContacto, command=lambda: self.confirmaDatos_botonNuevoContacto(identificador.get(), nombreContacto.get(), telefono.get(), correoElectronico.get(), IVA.get(), calle.get(), codigoPostal.get(), ciudad.get(), pais.get()), text="Confirmar datos")
        self.botonConfirmar_contacto.pack()
        
        self.botonSalir_contacto = ttk.Button(self.frameVentanaContacto, command=lambda: self.salir_contacto(), text="Salir")
        self.botonSalir_contacto.pack()
        
    #Método para definir la ventana de la nueva oportunidad
    def ventanaNuevaOportunidad(self):
        identificador_nuevaOportunidad = tk.StringVar()
        identificadorCliente_nuevaOportunidad = tk.StringVar()
        nombreOportunidad_nuevaOportunidad = tk.StringVar()
        correoElectronico_nuevaOportunidad = tk.StringVar()
        numeroTelefono_nuevaOportunidad = tk.StringVar()
        ingresoEsperado_nuevaOportunidad = tk.StringVar()
        estadoOportunidad_nuevaOportunidad = tk.StringVar()

        self.root.geometry("500x530")

        self.tituloNuevaOportunidad = tk.Label(self.frameVentanaNuevaOportunidad, text="Nueva oportunidad", font=("Courier", 20, "bold"), bg="azure2")
        self.tituloNuevaOportunidad.pack()

        self.marcoInformacion = tk.LabelFrame(self.frameVentanaNuevaOportunidad, text="Datos principales", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack(padx=10, pady=15)
        
        self.labelIdentificadorOportunidad = tk.Label(self.marcoInformacion, text="Identficador de la oportunidad", font=("Courier", 14), bg="azure3")
        self.labelIdentificadorOportunidad.pack()
        self.campoIdentificadorOportunidad = ttk.Entry(self.marcoInformacion, textvariable=identificador_nuevaOportunidad)
        self.campoIdentificadorOportunidad.pack()

        self.labelIdentificadorCliente = tk.Label(self.marcoInformacion, text="Identificador del cliente", font=("Courier", 14), bg="azure3")
        self.labelIdentificadorCliente.pack()
        self.campoIdentificadorCliente = ttk.Entry(self.marcoInformacion, textvariable=identificadorCliente_nuevaOportunidad)
        self.campoIdentificadorCliente.pack()
        
        self.labelNombreOportunidad = tk.Label(self.marcoInformacion, text="Nombre de la oportunidad", font=("Courier", 14), bg="azure3")
        self.labelNombreOportunidad.pack()
        self.campoNombreOportunidad = ttk.Entry(self.marcoInformacion, textvariable=nombreOportunidad_nuevaOportunidad)        
        self.campoNombreOportunidad.pack()

        self.labelCorreoElectronico = tk.Label(self.marcoInformacion, text="Correo electrónico", font=("Courier", 14), bg="azure3")
        self.labelCorreoElectronico.pack()
        self.campoCorreoElectronico = ttk.Entry(self.marcoInformacion, textvariable=correoElectronico_nuevaOportunidad)
        self.campoCorreoElectronico.pack()
        
        self.labelTelefono = tk.Label(self.marcoInformacion, text="Número de teléfono", font=("Courier", 14), bg="azure3")
        self.labelTelefono.pack()
        self.campoNumeroTelefono = ttk.Entry(self.marcoInformacion, textvariable=numeroTelefono_nuevaOportunidad)
        self.campoNumeroTelefono.pack()
        
        self.labelIngresoEsperado = tk.Label(self.marcoInformacion, text="Ingreso esperado", font=("Courier", 14), bg="azure3")
        self.labelIngresoEsperado.pack()
        self.campoIngresoEsperado = ttk.Entry(self.marcoInformacion, textvariable=ingresoEsperado_nuevaOportunidad)
        self.campoIngresoEsperado.pack()
        
        self.labelEstado = tk.Label(self.marcoInformacion, text="Estado de la oportunidad", font=("Courier", 14), bg="azure3")
        self.labelEstado.pack()
        self.comboEstado = ttk.Combobox(self.marcoInformacion, state="readonly", values=["Nuevo", "Calificado", "Propuesta", "Ganado"], textvariable=estadoOportunidad_nuevaOportunidad)
        self.comboEstado.pack()

        self.botonConfirmar = ttk.Button(self.frameVentanaNuevaOportunidad, text="Confirmar datos", command= lambda: self.confirmarDatos_botonNuevaOportunidad(identificador_nuevaOportunidad.get(), identificadorCliente_nuevaOportunidad.get(), nombreOportunidad_nuevaOportunidad.get(), correoElectronico_nuevaOportunidad.get(), ingresoEsperado_nuevaOportunidad.get(), estadoOportunidad_nuevaOportunidad.get(), numeroTelefono_nuevaOportunidad.get()))
        self.botonConfirmar.pack()
        
        self.botonSalir = ttk.Button(self.frameVentanaNuevaOportunidad, text="Salir", command=lambda: self.salir_oportunidad())
        self.botonSalir.pack()

    #Método para definir la ventana del nuevo presupuesto
    def ventanaNuevoPresupusto(self):
        identificador_nuevoPresupuesto = tk.StringVar()
        identificadorCliente_nuevoPresupuesto = tk.StringVar()
        identificadorPedido_nuevoPrespuesto = tk.StringVar()
        fechaInicio_nuevoPresupuesto = tk.StringVar()
        fechaFin_nuevoPresupuesto = tk.StringVar()

        self.root.geometry("500x450")
        
        self.tituloNuevoPresupuesto = tk.Label(self.frameVentanaNuevoPresupuesto, text="Nuevo prespupuesto", font=("Courier", 20, "bold"), bg="azure2")
        self.tituloNuevoPresupuesto.pack()

        self.marcoInformacion = tk.LabelFrame(self.frameVentanaNuevoPresupuesto, text="Datos principales", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack(padx=10, pady=15)

        self.labelIdentificador = tk.Label(self.marcoInformacion, text="Identificador del presupuesto", font=("Courier", 14), bg="azure3")
        self.labelIdentificador.pack()
        self.campoIdentificador = ttk.Entry(self.marcoInformacion, textvariable=identificador_nuevoPresupuesto)
        self.campoIdentificador.pack()

        self.labelIdentificadorCliente = tk.Label(self.marcoInformacion, text="Identificador del cliente", font=("Courier", 14), bg="azure3")
        self.labelIdentificadorCliente.pack()
        self.campoIdentificadorCliente = ttk.Entry(self.marcoInformacion, textvariable=identificadorCliente_nuevoPresupuesto)
        self.campoIdentificadorCliente.pack()

        self.labelIdentificadorPedido = tk.Label(self.marcoInformacion, text="Identificador del pedido", font=("Courier", 14), bg="azure3")
        self.labelIdentificadorPedido.pack()
        self.campoIdentificadorPedido = ttk.Entry(self.marcoInformacion, textvariable=identificadorPedido_nuevoPrespuesto)
        self.campoIdentificadorPedido.pack()

        self.labelFechaInicio = tk.Label(self.marcoInformacion, text="Fecha de inicio", font=("Courier", 14), bg="azure3")
        self.labelFechaInicio.pack()
        self.campoFechaInicio = ttk.Entry(self.marcoInformacion, textvariable=fechaInicio_nuevoPresupuesto)
        self.campoFechaInicio.pack()

        self.labelFechaFin = tk.Label(self.marcoInformacion, text="Fecha fin", font=("Courier", 14), bg="azure3")
        self.labelFechaFin.pack()
        self.campoFechaFin = ttk.Entry(self.marcoInformacion, textvariable=fechaFin_nuevoPresupuesto)
        self.campoFechaFin.pack()
        
        self.botonConfirmar = ttk.Button(self.frameVentanaNuevoPresupuesto, text="Confirmar datos", command=lambda: self.confimarDatos_botonConfirmarNuevoPrespuesto(identificador_nuevoPresupuesto.get(), identificadorCliente_nuevoPresupuesto.get(), identificadorPedido_nuevoPrespuesto.get(), fechaInicio_nuevoPresupuesto.get(), fechaFin_nuevoPresupuesto.get()))
        self.botonConfirmar.pack()
        
        self.botonSalir = ttk.Button(self.frameVentanaNuevoPresupuesto, text="Salir", command=lambda: self.salir_presupuesto())
        self.botonSalir.pack()

    #Método para definir la ventana donde nuevo producto
    def ventanaNuevoProducto(self):
        identificadorProducto_producto = tk.StringVar()
        nombreProducto_producto = tk.StringVar()
        descripcionProducto_producto = tk.StringVar()
        cantidadStock_producto = tk.StringVar()
        precioUnitario_producto = tk.StringVar()

        self.root.geometry("500x400")

        self.tituloNuevoProducto = tk.Label(self.frameVentanaProducto, text="Nuevo producto", font=("Courier", 20, "bold"), bg="azure2")
        self.tituloNuevoProducto.pack()

        self.marcoInformacion = tk.LabelFrame(self.frameVentanaProducto, text="Datos principales", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack()

        self.labelIdentificadorProducto = tk.Label(self.marcoInformacion, text="Identificador del producto", font=("Courier", 14), bg="azure3")
        self.labelIdentificadorProducto.pack()
        self.campoIdentificadorProducto = ttk.Entry(self.marcoInformacion, textvariable=identificadorProducto_producto)
        self.campoIdentificadorProducto.pack()

        self.labelNombreProducto = tk.Label(self.marcoInformacion, text="Nombre del producto", font=("Courier", 14), bg="azure3")
        self.labelNombreProducto.pack()
        self.campoNombreProducto = ttk.Entry(self.marcoInformacion, textvariable=nombreProducto_producto)
        self.campoNombreProducto.pack()

        self.labelDescripcion = tk.Label(self.marcoInformacion, text="Descripción del producto", font=("Courier", 14), bg="azure3")
        self.labelDescripcion.pack()
        self.campoDescripcion = ttk.Entry(self.marcoInformacion, textvariable=descripcionProducto_producto)
        self.campoDescripcion.pack()

        self.labelCantidadStock = tk.Label(self.marcoInformacion, text="Cantidad de Stock", font=("Courier", 14), bg="azure3")
        self.labelCantidadStock.pack()
        self.campoCantidadStock = ttk.Entry(self.marcoInformacion, textvariable=cantidadStock_producto)
        self.campoCantidadStock.pack()

        self.labelPrecioUnitario = tk.Label(self.marcoInformacion, text="Precio unitario", font=("Courier", 14), bg="azure3")
        self.labelPrecioUnitario.pack()
        self.campoPrecioUnitario = ttk.Entry(self.marcoInformacion, textvariable=precioUnitario_producto)
        self.campoPrecioUnitario.pack()

        self.botonConfirmar = ttk.Button(self.frameVentanaProducto, text="Confirmar datos", command=lambda: self.confirmarDatos_botonConfirmarNuevoProducto(identificadorProducto_producto.get(), nombreProducto_producto.get(), descripcionProducto_producto.get(), cantidadStock_producto.get(), precioUnitario_producto.get()))
        self.botonConfirmar.pack()

        self.botonSalir = ttk.Button(self.frameVentanaProducto, text="Salir", command=lambda: self.salir_producto())
        self.botonSalir.pack()

    #Método para definir la ventana de visualización del presupuesto con estado "Nuevo"
    def ventanaNuevo(self):
        self.marcoInformacion = tk.LabelFrame(self.frameNuevo)
        self.marcoInformacion.pack()

        self.root.geometry("500x500")

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.listaNuevo())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_nuevo())
        self.botonSalir.pack()

        self.informacion = st.ScrolledText(self.marcoInformacion, width=50, height=30)
        self.informacion.pack()

    #Método para definir la ventana de visualización del presupuesto con estado "Calificado"
    def ventanaCalificado(self):
        self.marcoInformacion = tk.LabelFrame(self.frameCalificado)
        self.marcoInformacion.pack()

        self.root.geometry("500x500")

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.listaCalificado())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_calificado())
        self.botonSalir.pack()

        self.informacion = st.ScrolledText(self.marcoInformacion, width=50, height=30)
        self.informacion.pack()

    #Método para definir la ventana de visualización del presupuesto con estado "Propuesto"
    def ventanaPropuesta(self):
        self.marcoInformacion = tk.LabelFrame(self.framePropuesta)
        self.marcoInformacion.pack()

        self.root.geometry("500x500")

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.listaPropuesta())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_propuesta())
        self.botonSalir.pack()

        self.informacion = st.ScrolledText(self.marcoInformacion, width=50, height=30)
        self.informacion.pack()

    #Método para definir la ventana de visualización del presupuesto con estado "Ganado"
    def ventanaGanado(self):
        self.marcoInformacion = tk.LabelFrame(self.frameGanado)
        self.marcoInformacion.pack()

        self.root.geometry("500x500")

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.listaGanado())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_ganado())
        self.botonSalir.pack()

        self.informacion = st.ScrolledText(self.marcoInformacion, width=50, height=30)
        self.informacion.pack()

    #Método para definir la ventana de visualización de datos
    def visualizarDatos(self):
        self.root.geometry("800x500")

        self.cuaderno = ttk.Notebook(self.frameVisualizarDatos, width=700, height=800)
        self.cuaderno.pack()

        self.visualizarClientes()
        self.visualizarOportunidades()
        self.visualizarPresupuestos()
        self.visualizarProducto()

    #Método para definir el apartado de visualizar a los clientes de la ventana de visualización de datos
    def visualizarClientes(self):
        self.apartadoCliente = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.apartadoCliente, text="Clientes")
        
        self.marcoInformacion = tk.LabelFrame(self.apartadoCliente, text="Visualizar clientes", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack()

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.resultado_consulta_cliente())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_visualizar_datos())
        self.botonSalir.pack()

        self.informacionCliente = st.ScrolledText(self.marcoInformacion, width=50, height=50)
        self.informacionCliente.pack()

    #Método para definir el apartado de visualizar a las oportunidades de la ventana de visualización de datos
    def visualizarOportunidades(self):
        self.apartadoOportunidad = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.apartadoOportunidad, text="Oportunidades")

        self.marcoInformacion = tk.LabelFrame(self.apartadoOportunidad, text="Visualizar oportunidades", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack()

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.resultado_consulta_oportunidad())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_visualizar_datos())
        self.botonSalir.pack()

        self.informacionOportunidad = st.ScrolledText(self.marcoInformacion, width=50, height=50)
        self.informacionOportunidad.pack()

    #Método para definir el apartado de visualizar los presupuestos de la ventana de visualización de datos
    def visualizarPresupuestos(self):
        self.apartadoPresupuesto = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.apartadoPresupuesto, text="Presupuestos")

        self.marcoInformacion = tk.LabelFrame(self.apartadoPresupuesto, text="Visualizar presupuestos", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack()
        
        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.resultado_consulta_presupuesto())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_visualizar_datos())
        self.botonSalir.pack()

        self.informacionPresupuesto = st.ScrolledText(self.marcoInformacion, width=50, height=50)
        self.informacionPresupuesto.pack()

    #Método para definir el apartado de visualizar los productos de la ventana de visualización de datos
    def visualizarProducto(self):
        self.apartadoProducto = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.apartadoProducto, text="Productos")

        self.marcoInformacion = tk.LabelFrame(self.apartadoProducto, text="Visualizar productos", font=("Courier", 17), bg="azure3")
        self.marcoInformacion.pack()

        self.botonRealizarConsulta = ttk.Button(self.marcoInformacion, text="Realizar consulta", command=lambda: self.resultado_consulta_producto())
        self.botonRealizarConsulta.pack()

        self.botonSalir = ttk.Button(self.marcoInformacion, text="Salir", command=lambda: self.salir_visualizar_datos())
        self.botonSalir.pack()

        self.informacionProducto = st.ScrolledText(self.marcoInformacion, width=50, height=50)
        self.informacionProducto.pack()

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los presupuestos con estado "Nuevo"
    def listaNuevo(self):
        resultadoNuevo = self.consultaNuevo()
        self.informacion.delete("1.0", tk.END)
        for i in resultadoNuevo:
            self.informacion.insert(tk.END, "\nIdentificador de la oportunidad: " + str(i[0]) + "\nIdentificador cliente: " + str(i[1]) + "\nNombre de la oportunidad: " + str(i[2]) + "\nIngreso esperado: " + str(i[3]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los presupuestos con estado "Calificado"
    def listaCalificado(self):
        resultadoNuevo = self.consultaCalificado()
        self.informacion.delete("1.0", tk.END)
        for i in resultadoNuevo:
            self.informacion.insert(tk.END, "\nIdentificador de la oportunidad: " + str(i[0]) + "\nIdentificador cliente: " + str(i[1]) + "\nNombre de la oportunidad: " + str(i[2]) + "\nIngreso esperado: " + str(i[3]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los presupuestos con estado "Propuesto"
    def listaPropuesta(self):
        resultadoNuevo = self.consultaPropuesta()
        self.informacion.delete("1.0", tk.END)
        for i in resultadoNuevo:
            self.informacion.insert(tk.END, "\nIdentificador de la oportunidad: " + str(i[0]) + "\nIdentificador cliente: " + str(i[1]) + "\nNombre de la oportunidad: " + str(i[2]) + "\nIngreso esperado: " + str(i[3]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los presupuestos con estado "Ganado"
    def listaGanado(self):
        resultadoNuevo = self.consultaGanado()
        self.informacion.delete("1.0", tk.END)
        for i in resultadoNuevo:
            self.informacion.insert(tk.END, "\nIdentificador de la oportunidad: " + str(i[0]) + "\nIdentificador cliente: " + str(i[1]) + "\nNombre de la oportunidad: " + str(i[2]) + "\nIngreso esperado: " + str(i[3]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los clietes
    def resultado_consulta_cliente(self):
        resultadoCliente = self.consulta_total("cliente")   
        self.informacionCliente.delete("1.0", tk.END)
        for i in resultadoCliente:
            self.informacionCliente.insert(tk.END, "\nID del cliente: " + str(i[0]) + "\nNombre del cliente: " + str(i[1]) + "\nNúmero de teléfono: " + str(i[2]) + "\nCorre electrónico: " + str(i[3]) + "\nPorcentaja IVA: " + str(i[4]) + "\nCalle: " + str(i[5]) + "\nCódigo postal: " + str(i[6]) + "\nCiudad: " + str(i[7]) + "\nPais: " + str(i[7]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de las oportunidades
    def resultado_consulta_oportunidad(self):
        resultadoOportunidad = self.consulta_total("oportunidad")
        self.informacionOportunidad.delete("1.0", tk.END)
        for i in resultadoOportunidad:
            self.informacionOportunidad.insert(tk.END, "\nID de la oportunidad: " + str(i[0]) + "\nID del cliente: " + str(i[1]) + "\nNombre de la oportunidad: " + str(i[2]) + "\nCorreo electrónico: " + str(i[3]) + "\nIngreso esperado: " + str(i[4]) + "\nEstado de la oportunidad: " + str(i[5]) + "\nTeléfono: " + str(i[6]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los presupuestos
    def resultado_consulta_presupuesto(self):
        resultadoPresupuesto = self.consulta_total("presupuesto")
        self.informacionPresupuesto.delete("1.0", tk.END)
        for i in resultadoPresupuesto:
            self.informacionPresupuesto.insert(tk.END, "\nID del presupuesto: " + str(i[0]) + "\nID del cliente: " + str(i[1]) + "\nID del producto: " + str(i[2]) + "\nFecha de inicio: " + str(i[3]) + "\nFecha fin: " + str(i[4]) + "\n\n ------------------------------------------------ ")

    #Método para mostrar en el ttk.scrolledText la información de la consulta de los productos
    def resultado_consulta_producto(self):
        resultadoOportunidad = self.consulta_total("producto")
        self.informacionProducto.delete("1.0", tk.END)
        for i in resultadoOportunidad:
            self.informacionProducto.insert(tk.END, "\nID del producto: " + str(i[0]) + "\nNombre producto: " + str(i[1]) + "\nDescripción producto: " + str(i[2]) + "\nStock del producto: " + str(i[3]) + "\nPrecio unitario: " + str(i[4]) + "\n\n ------------------------------------------------ ")

    #Método para visualizar la ventana del pipeline
    def ventanaPipeline_mostrar(self):
        self.frameVentanaInicial.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de añadir el nuevo contacto
    def contacto(self):
        self.frameVentanaPipeline.destroy()      

        self.frameVentanaContacto = tk.Frame(self.root)
        self.frameVentanaContacto.pack(fill="both", expand="True")
        self.frameVentanaContacto.config(bd=10, bg="azure2")

        self.ventanaContacto()
        
    #Método para salir de la ventana de añadir nuevo contacto
    def salir_contacto(self):
        self.frameVentanaContacto.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()
    
    #Método para visualizar la ventana de añadir la nueva oportunidad
    def nuevaOportunidad(self):
        self.frameVentanaPipeline.destroy()

        self.frameVentanaNuevaOportunidad = tk.Frame(self.root)
        self.frameVentanaNuevaOportunidad.pack(fill="both", expand="True")
        self.frameVentanaNuevaOportunidad.config(bd=10, bg="azure2")

        self.ventanaNuevaOportunidad()

    #Método para salir de la ventana de añadir la nueva oportunidad
    def salir_oportunidad(self):
        self.frameVentanaNuevaOportunidad.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de añadir un nuevo presupuesto
    def nuevoPrespuesto(self):
        self.frameVentanaPipeline.destroy()

        self.frameVentanaNuevoPresupuesto = tk.Frame(self.root)
        self.frameVentanaNuevoPresupuesto.pack(fill="both", expand="True")
        self.frameVentanaNuevoPresupuesto.config(bd=10, bg="azure2")

        self.ventanaNuevoPresupusto()

    #Método para salir de la ventana de añadir el nuevo presupuesto
    def salir_presupuesto(self):
        self.frameVentanaNuevoPresupuesto.destroy()
        
        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de añadir el nuevo producto
    def nuevoProducto(self):
        self.frameVentanaPipeline.destroy()

        self.frameVentanaProducto = tk.Frame(self.root)
        self.frameVentanaProducto.pack(fill="both", expand="True")
        self.frameVentanaProducto.config(bd=10, bg="azure2")
        
        self.ventanaNuevoProducto()

    #Método para salir de la ventana del nuevo producto
    def salir_producto(self):
        self.frameVentanaProducto.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de consultar los prespuestos con estado "Nuevo"
    def nuevo(self):
        self.frameVentanaPipeline.destroy()

        self.frameNuevo = tk.Frame(self.root)
        self.frameNuevo.pack(fill="both", expand="True")
        self.frameNuevo.config(bd=10, bg="azure2")

        self.ventanaNuevo()

    #Método para salir de la ventana de visualizar los prespuestos con estado "Nuevo"
    def salir_nuevo(self):
        self.frameNuevo.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de consultar los prespuestos con estado "Calificado"
    def calificado(self):
        self.frameVentanaPipeline.destroy()

        self.frameCalificado = tk.Frame(self.root)
        self.frameCalificado.pack(fill="both", expand="True")
        self.frameCalificado.config(bd=10, bg="azure2")

        self.ventanaCalificado()

    #Método para salir de la ventana de visualizar los prespuestos con estado "Calificado"
    def salir_calificado(self):
        self.frameCalificado.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de consultar los prespuestos con estado "Propuesto"
    def propuesta(self):
        self.frameVentanaPipeline.destroy()

        self.framePropuesta = tk.Frame(self.root)
        self.framePropuesta.pack(fill="both", expand="True")
        self.framePropuesta.config(bd=10, bg="azure2")

        self.ventanaPropuesta()

    #Método para salir de la ventana de visualizar los prespuestos con estado "Propuesto"
    def salir_propuesta(self):
        self.framePropuesta.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana de consultar los prespuestos con estado "Ganado"
    def ganado(self):
        self.frameVentanaPipeline.destroy()

        self.frameGanado = tk.Frame(self.root)
        self.frameGanado.pack(fill="both", expand="True")
        self.frameGanado.config(bd=10, bg="azure2")

        self.ventanaGanado()

    #Método para salir de la ventana de visualizar los prespuestos con estado "Ganado"
    def salir_ganado(self):
        self.frameGanado.destroy()

        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para visualizar la ventana inicial
    def cerrar_sesion(self):
        self.frameVentanaPipeline.destroy()

        self.frameVentanaInicial = tk.Frame(self.root)
        self.frameVentanaInicial.pack(fill="both", expand="True")
        self.frameVentanaInicial.config(bd=10, bg="azure2")
        
        self.ventanaInicial()

    #Método para visualiazar la ventana de visualización de los datos
    def visualizar_datos(self):
        self.frameVentanaPipeline.destroy()

        self.frameVisualizarDatos = tk.Frame(self.root)
        self.frameVisualizarDatos.pack(fill="both", expand="True")
        self.frameVisualizarDatos.config(bd=10, bg="azure2")

        self.visualizarDatos()

    #Método para salir de la ventana de visualización de los datos
    def salir_visualizar_datos(self):
        self.frameVisualizarDatos.destroy()
        
        self.frameVentanaPipeline = tk.Frame(self.root)
        self.frameVentanaPipeline.pack(fill="both", expand="True")
        self.frameVentanaPipeline.config(bd=10, bg="azure2")

        self.ventanaPipeline()

    #Método para realizar la insercción del nuevo contato a la BBDD
    def confirmaDatos_botonNuevoContacto(self, identificador, nombreContacto, telefono, correoElectronico, IVA, calle, codigoPostal, ciudad, pais):
        try:    
            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO cliente VALUES (" + identificador + ", '" + nombreContacto + "', '" + telefono + "', '" + correoElectronico + "', " + IVA + ", '" + calle + "', '" + codigoPostal + "', '" + ciudad + "', '" + pais + "')")                  
            opcion = ms.askyesno(message="¿Confimar el nuevo contacto?", title="Nuevo cliente")
            
            if opcion == True:
                conexion.commit()
                conexion.close()
                
                ms.showinfo("Nuevo cliente", "El cliente se ha añadido de forma correcta")
            elif opcion == False:
                conexion.close()
                ms.showwarning("Nuevo Cliente", "El cliente no se ha añadido")
        except:
            ms.showerror("ERROR", "Ha ocurrido un error, revise los datos o pongase en contato con el administrador del CRM")
            conexion.close()
        
    #Método para realizar la insercción de la nueva oportunidad a la BBDD
    def confirmarDatos_botonNuevaOportunidad(self, identificador, identificadorCliente, nombreOportunidad, correoElectronico, ingresoEsperado, estadoOportunidad, numeroTelefono):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO oportunidad VALUES (" + identificador + ", " + identificadorCliente + ", '" + nombreOportunidad + "', '" + correoElectronico + "', " + ingresoEsperado + ", '" + estadoOportunidad + "', '" + numeroTelefono + "')")

            opcion = ms.askyesno(message="¿Confirmar nueva oportunidad?", title="Nueva oportunidad")

            if opcion == True:
                conexion.commit()
                conexion.close()

                ms.showinfo("Nueva oportunidad", "La nueva oportunidad ha sido añadida de forma correcta")
            elif opcion == False:
                ms.showwarning("Nueva oportunidad", "La oportunidad no ha sido añadida")
                conexion.close()
        except:
            ms.showerror("ERROR", "Ha ocurrido un error, revise los datos o pongase en contato con el administrador del CRM")

    #Método para realizar la insercción del nuevo presupuesto
    def confimarDatos_botonConfirmarNuevoPrespuesto(self, identificador, identificadorCliente, identificadorProducto, fechaInicio, fechaFin):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO presupuesto VALUES (" + identificador + ", " + identificadorCliente + ", " + identificadorProducto + ", '" + fechaInicio + "', '" + fechaFin + "')")

            opcion = ms.askyesno(message="¿Confirmar nuevo presupuesto?", title="Nuevo presupuesto")

            if opcion == True:
                conexion.commit()
                conexion.close()

                ms.showinfo("Nuevo prespuesto", "El nuevo prespuesto ha sifo añadido de forma correcta")
            elif opcion == False:
                ms.showwarning("Nueva oportunidad", "El prespuesto no ha sido añadido")

        except:
            ms.showerror("ERROR", "Ha ocurrido un error, revise los datos o pongase en contacto con el administrador del CRM")

    #Método para realizar la insercción del nuevo producto
    def confirmarDatos_botonConfirmarNuevoProducto(self, identificador, nombreProducto, descripcion, stock, precio):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO producto VALUES (" + identificador + ", '" + nombreProducto + "', '" + descripcion + "', " + stock + ", " + precio + ")")
            
            opcion = ms.askyesno(message="¿Confirmar nuevo producto?", title="Nuevo producto")

            if opcion == True:
                conexion.commit()
                conexion.close()

                ms.showinfo("Nuevo producto", "El nuevo producto ha sido añadido de forma correcta")
            elif opcion == False:
                conexion.close()
            
        except:
            ms.showerror("ERROR", "Ha ocurrido un error, revise los datos o pongase en contacto con el administrador del CRM")

    #Método para realizar la consulta de los prespuestos con estado "Nuevo"
    def consultaNuevo(self):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("SELECT identificadorOportunidad, identificadorCliente, nombreOportunidad, ingresoEsperado FROM oportunidad WHERE estado = 'Nuevo' or estado = 'nuevo'")
            
            return cursor.fetchall()

        except:
            ms.showerror(title="ERROR", message="Pongase en contacto con el administrador del CRM")

    #Método para realizar la consulta de los prespuestos con estado "Calificado"
    def consultaCalificado(self):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("SELECT identificadorOportunidad, identificadorCliente, nombreOportunidad, ingresoEsperado FROM oportunidad WHERE estado = 'Calificado' or estado = 'calificado'")
            
            return cursor.fetchall()

        except:
            ms.showerror(title="ERROR", message="Pongase en contacto con el administrador del CRM")

    #Método para realizar la consulta de los prespuestos con estado "Propuesto"
    def consultaPropuesta(self):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("SELECT identificadorOportunidad, identificadorCliente, nombreOportunidad, ingresoEsperado FROM oportunidad WHERE estado = 'Propuesta' or estado = 'propuesta'")
            
            return cursor.fetchall()

        except:
            ms.showerror(title="ERROR", message="Pongase en contacto con el administrador del CRM")

    #Método para realizar la consulta de los prespuestos con estado "Ganado"
    def consultaGanado(self):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("SELECT identificadorOportunidad, identificadorCliente, nombreOportunidad, ingresoEsperado FROM oportunidad WHERE estado = 'Ganado' or estado = 'ganado'")
            
            return cursor.fetchall()

        except:
            ms.showerror(title="ERROR", message="Pongase en contacto con el administrador del CRM")
    
    #Métodopara obtener todos los registos dependiendo del nuevo de la tabla pasada como parámetro
    def consulta_total(self, nombreTabla):
        try:
            global nombreBBDD

            conexion = sqlite3.connect(nombreBBDD)
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM " + nombreTabla)

            return cursor.fetchall()

        except:
            ms.showerror(title="ERROR", message="Pongase en contacto con el administrador del CRM")

    #Función cuya función es realizar la conexión a la BBDD (en caso de que la BBDD no exista, creará una nueva con la información que haya en el campo del nombre)
    def confirmar(self, nombre, correo, contrasenya):
        if len(nombre) == 0 or len(correo) == 0 or len(contrasenya) == 0:
            ms.showerror(title="ERROR", message="Rellene los campos")
        else:
            try:
                conexion = sqlite3.connect(nombre)
                cursor = conexion.cursor()

                cursor.execute("CREATE TABLE empresa(nombreCliente TEXT, correo TEXT, contrasenya TEXT, PRIMARY KEY(nombreCliente))")
                cursor.execute("CREATE TABLE cliente(identificadorCliente INT, nombreCliente TEXT, telefono VARCHAR(9), correoElectronico TEXT, procentajeIVA FLOAT, calle TEXT, codigoPostal VARCHAR(5), ciudad TEXT, pais TEXT, PRIMARY KEY(identificadorCliente))")
                cursor.execute("CREATE TABLE producto( identificadorProducto INT, nombreProducto TEXT, descripcionProducto TEXT, stock INT, precioUnitario REAL, PRIMARY KEY(identificadorProducto))")
                cursor.execute("CREATE TABLE oportunidad(identificadorOportunidad INT, identificadorCliente INT, nombreOportunidad TEXT, correoElectronico TEXT, ingresoEsperado FLOAT, estado TEXT, telefono VARCHAR(9), PRIMARY KEY(identificadorOportunidad), FOREIGN KEY(identificadorCliente) REFERENCES cliente(identificadorCliente))")
                cursor.execute("CREATE TABLE presupuesto(identificadorPresupuesto INT, identificadorCliente INT, identificadorProducto INT, fechaInicio VARCHAR(10), fechaFin VARCHAR(10), PRIMARY KEY(identificadorPresupuesto), FOREIGN KEY(identificadorCliente) REFERENCES cliente(identificadorCliente), FOREIGN KEY(identificadorProducto) REFERENCES Producto(identificadorProducto))")
                
                cursor.execute("INSERT INTO empresa VALUES ('" + nombre + "', '" + correo + "', '" + contrasenya + "')")

                conexion.commit()
                conexion.close()

                ms.showinfo("Estado BBDD", "La Base de Datos " + nombre + " ha sido creada")
            except:
                conexion = sqlite3.connect(nombre)
                cursor = conexion.cursor()

                cursor.execute("SELECT contrasenya FROM empresa WHERE nombreCliente = '" + nombre + "'")
                consultaContrasenya = cursor.fetchall()

                cursor.execute("SELECT correo FROM empresa WHERE nombreCliente = '" + nombre + "'")
                consultaCorreo = cursor.fetchall()
                
                contenidoContrasenya = ""
                contenidoCorreo = ""

                for c in consultaContrasenya:
                    contenidoContrasenya = c[0]

                for c in consultaCorreo:
                    contenidoCorreo = c[0]

                if (contenidoContrasenya == contrasenya and contenidoCorreo == correo):
                    ms.showinfo("Estado BBDD", "Datos correctos. INICIANDO SESIÓN")
                    
                    global nombreBBDD
                    nombreBBDD = nombre
                    
                    self.ventanaPipeline_mostrar()

                else:
                    ms.showerror("Estado BBDD", "Datos incorrecta. VUELVA A INTENTARLO")

def main(): 
    root = tk.Tk()
    ventana = Ventana(root)
    root.title("CRM_Jesús Escudero Gabarre")
    root.mainloop()

if __name__ == '__main__':
    main()