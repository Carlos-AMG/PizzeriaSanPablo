from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
import models
from database import Base
import random
import sys

# Create the engine with echo=True to print SQL statements
engine = create_engine('postgresql://postgres:admin@localhost:5432/pizzaSanPablo', echo=True)

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create fake data using Faker
fake = Faker('es_MX')

# Add values to the PERSONA table
personas = []
for _ in range(10):
    persona = models.Persona(
        Nombre=fake.first_name(),
        ApellidoP=fake.last_name(),
        ApellidoM=fake.last_name(),
        Direccion=fake.street_address()
    )
    personas.append(persona)

session.add_all(personas)
session.commit()

# Add values to the DIRECCION table
# direcciones = []
# guadalajara_zip_codes = ['44100', '44110', '44120', '44130', '44140', '44150', '44160', '44170', '44180', '44190']
# for _ in range(10):
#     choice = random.choice(guadalajara_zip_codes)
#     guadalajara_zip_codes.remove(choice)
#     direccion = models.Direccion(
#         Calle=fake.street_address(),
#         CodigoPostal=choice,
#         InfoAdicional=fake.random_element(["Apartment", "House", "Office"]),
#     )
#     direcciones.append(direccion)

# session.add_all(direcciones)
# session.commit()

# Add values to the PRODUCTO table
productos = []
pizzas = [
    {"nombre": "Margherita", "descripcion": "Pizza clásica con salsa de tomate, queso mozzarella y albahaca fresca."},
    {"nombre": "Pepperoni", "descripcion": "Deliciosa pizza cubierta con salsa de tomate, queso mozzarella y rodajas de pepperoni picante."},
    {"nombre": "Hawaiana", "descripcion": "Pizza tropical con jamón, trozos de piña, salsa de tomate y queso mozzarella."},
    {"nombre": "Cuatro Quesos", "descripcion": "Exquisita pizza con una combinación de cuatro quesos: mozzarella, gorgonzola, parmesano y provolone."},
    {"nombre": "Vegetariana", "descripcion": "Pizza repleta de sabrosas verduras frescas, como champiñones, pimientos, cebolla y aceitunas."},
    {"nombre": "Barbacoa", "descripcion": "Sabrosa pizza con salsa barbacoa, pollo desmenuzado, cebolla roja y queso mozzarella."},
    {"nombre": "Mediterránea", "descripcion": "Pizza inspirada en los sabores mediterráneos con aceitunas, tomates cherry, espinacas y queso feta."},
    {"nombre": "Mexicana", "descripcion": "Deliciosa pizza con carne molida, jalapeños, tomates, cebolla y salsa picante."},
    {"nombre": "Carbonara", "descripcion": "Pizza cremosa con salsa carbonara, panceta, huevo, queso parmesano y cebollino."},
    {"nombre": "Marinera", "descripcion": "Pizza de mariscos con camarones, calamares, mejillones y salsa de tomate."},
]
for pizza in pizzas:
    producto = models.Producto(
        Nombre=pizza["nombre"],
        Precio=round(random.uniform(70, 150), 2),
        Descripcion=pizza["descripcion"],
    )
    productos.append(producto)

session.add_all(productos)
session.commit()

# Add values to the INVENTARIO table
inventarios = []
ingredientes = [
    "Tomate",
    "Queso",
    "Pepperoni",
    "Jamón",
    "Champiñones",
    "Aceitunas",
    "Cebolla",
    "Pimiento",
    "Salchicha",
    "Jalapeños",
    "Anchoas",
    "Maíz",
    "Piña",
    "Pollo",
    "Carne de res",
    "Bacon",
    "Atún",
    "Rúcula",
    "Espárragos",
    "Aceite de oliva",
]
for _ in range(10):
    choice = random.choice(ingredientes)
    ingredientes.remove(choice)
    inventario = models.Inventario(
        Nombre=choice,
        CantDisponible=fake.random_int(min=1, max=100),
        Precio=round(random.uniform(10, 100), 2),
    )
    inventarios.append(inventario)

session.add_all(inventarios)
session.commit()


# Add values to the EMPLEADO table
person_ids = [persona.ID for persona in session.query(models.Persona).all()]
cargos = [
    "Supervisor",
    "Encargado de Ventas",
    "Camarero",
    "Bartender",
    "Chef",
    "Ayudante de Cocina",
    "Repostero",
    "Mesero",
    "Host/Hostess",
    "Auxiliar Administrativo",
    "Recursos Humanos",
    "Contador",
]
rfcs = [
    "ABCX930528ABC",
    "DEFY851013DEF",
    "GHIZ750715GHI",
    "JKLA891224JKL",
    "MNOB820605MNO",
    "PQRW941001PQR",
    "STUV730309STU",
    "WXYZ880822WXY",
    "123A900201123",
    "456B811117456",
]
empleados = []
for _ in range(10):
    id_choice = random.choice(person_ids)
    rfc_choice = random.choice(rfcs)
    rfcs.remove(rfc_choice)
    person_ids.remove(id_choice)
    empleado = models.Empleado(
        RFC=rfc_choice,
        PersonaID=id_choice,
        Cargo=random.choice(cargos),
        Salario=round(random.uniform(1000, 13000), 2),
        FechaInicio=func.current_date(),
    )
    empleados.append(empleado)

session.add_all(empleados)
session.commit()


# Add values to the CLIENTE table
clientes = []
for x in range(1, 9):
    cliente = models.Cliente(
        Telefono=fake.phone_number(),
        PersonaID=x,
    )
    clientes.append(cliente)

session.add_all(clientes)
session.commit()


# Add values to the PEDIDO table
pedidos = []
estado = ["pendinete", "entregado", "cancelado"]
for _ in range(10):
    empleado = session.query(models.Empleado).order_by(func.random()).first()  # Retrieve a random employee
    cliente = session.query(models.Cliente).order_by(func.random()).first()  # Retrieve a random client
    choice = random.choice(estado)
    pedido = models.Pedido(
        FechaPedido=fake.date(),
        Hora=fake.time(),
        Cantidad=random.randint(3,9),
        Estado=choice,
        Total=round(random.uniform(100, 500), 2),
        RFC_Empleado=empleado.RFC,
        NumCliente=cliente.NumCliente
    )
    pedidos.append(pedido)

session.add_all(pedidos)
session.commit()


# Get a list of pedido NumPedido
num_pedidos = [pedido.NumPedido for pedido in session.query(models.Pedido).all()]
# Get a list of NumIngrediente
num_ingredientes = [inventario.NumIngrediente for inventario in session.query(models.Inventario).all()]
# Get a list of NumProducto
num_productos = [producto.NumProducto for producto in session.query(models.Producto).all()]

# Add values to the UTLIZA table
utiliza_data = []
for _ in range(10):
    choice1 = random.choice(num_ingredientes)
    choice2 = random.choice(num_productos)
    num_ingredientes.remove(choice1)
    num_productos.remove(choice2)
    utiliza = models.Utiliza(NumIngrediente=choice1, NumProducto=choice2)
    utiliza_data.append(utiliza)
session.add_all(utiliza_data)
session.commit()

num_productos = [producto.NumProducto for producto in session.query(models.Producto).all()]
# Add values to the CONTIENE table
contiene_data = []
for _ in range(10):
    choice1 = random.choice(num_pedidos)
    choice2 = random.choice(num_productos)
    num_productos.remove(choice2)
    num_pedidos.remove(choice1)
    contiene = models.Contiene(NumProducto=choice2, NumPedido=choice1)
    contiene_data.append(contiene)
session.add_all(contiene_data)
session.commit()


# Close the session
session.close()
