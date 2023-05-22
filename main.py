from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import models
from database import Base
import random

# Create the engine with echo=True to print SQL statements

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create fake data using Faker
fake = Faker('es_MX')

# Add values to the PERSONA table
# personas = []
# for _ in range(10):
#     persona = models.Persona(
#         Nombre1=fake.first_name(),
#         Nombre2=fake.first_name(),
#         ApellidoP=fake.last_name(),
#         ApellidoM=fake.last_name()
#     )
#     personas.append(persona)

# session.add_all(personas)
# session.commit()

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

# # Add values to the PRODUCTO table
# productos = []
# pizzas = [
#     {"nombre": "Margherita", "descripcion": "Pizza clásica con salsa de tomate, queso mozzarella y albahaca fresca."},
#     {"nombre": "Pepperoni", "descripcion": "Deliciosa pizza cubierta con salsa de tomate, queso mozzarella y rodajas de pepperoni picante."},
#     {"nombre": "Hawaiana", "descripcion": "Pizza tropical con jamón, trozos de piña, salsa de tomate y queso mozzarella."},
#     {"nombre": "Cuatro Quesos", "descripcion": "Exquisita pizza con una combinación de cuatro quesos: mozzarella, gorgonzola, parmesano y provolone."},
#     {"nombre": "Vegetariana", "descripcion": "Pizza repleta de sabrosas verduras frescas, como champiñones, pimientos, cebolla y aceitunas."},
#     {"nombre": "Barbacoa", "descripcion": "Sabrosa pizza con salsa barbacoa, pollo desmenuzado, cebolla roja y queso mozzarella."},
#     {"nombre": "Mediterránea", "descripcion": "Pizza inspirada en los sabores mediterráneos con aceitunas, tomates cherry, espinacas y queso feta."},
#     {"nombre": "Mexicana", "descripcion": "Deliciosa pizza con carne molida, jalapeños, tomates, cebolla y salsa picante."},
#     {"nombre": "Carbonara", "descripcion": "Pizza cremosa con salsa carbonara, panceta, huevo, queso parmesano y cebollino."},
#     {"nombre": "Marinera", "descripcion": "Pizza de mariscos con camarones, calamares, mejillones y salsa de tomate."},
# ]
# for pizza in pizzas:
#     producto = models.Producto(
#         Nombre=pizza["nombre"],
#         Precio=round(random.uniform(70, 150), 2),
#         Descripcion=pizza["descripcion"],
#     )
#     productos.append(producto)

# session.add_all(productos)
# session.commit()

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
# empleados = []
# alphanumeric_value = fake.random_int(min=10**12, max=(10**13)-1)
# alphanumeric_value = str(alphanumeric_value).zfill(13)
# for _ in range(10):
#     empleado = models.Empleado(
#         RFC=alpha,
#         PersonaID=fake.random_int(min=1, max=10),
#         Cargo=fake.job(),
#         Salario=fake.random_number(digits=5) / 100,
#     )
#     empleados.append(empleado)

# session.add_all(empleados)
# session.commit()



# # Add values to the CLIENTE table
# clientes = []
# for _ in range(10):
#     cliente = models.Cliente(
#         Telefono=fake.phone_number(),
#         PersonaID=fake.random_int(min=1, max=10),
#         DireccionID=fake.random_int(min=1, max=10),
#     )
#     clientes.append(cliente)

# session.add_all(clientes)
# session.commit()

# # Add values to the PEDIDO table
# pedidos = []
# for _ in range(10):
#     pedido = models.Pedido(
#         FechaPedido=fake.date(),
#         Hora=fake.time(),
#         Cantidad=fake.random_int(min=1, max=10),
#         Estado=fake.random_element(["Pending", "In Progress", "Completed"]),
#         Total=fake.random_float(min=10, max=100),
#         RFC_Empleado=fake.unique.random_number(digits=10),
#         NumCliente=fake.random_int(min=1, max=10),
#     )
#     pedidos.append(pedido)

# session.add_all(pedidos)
# session.commit()





# session.add_all(inventarios)
# session.commit()

# # Add values to the UTILIZA table
# utilizas = []
# for _ in range(10):
#     utiliza = models.Utiliza(
#         NumIngrediente=fake.random_int(min=1, max=10),
#         NumProducto=fake.random_int(min=1, max=10),
#     )
#     utilizas.append(utiliza)

# session.add_all(utilizas)
# session.commit()

# # Add values to the CONTIENE table
# contienes = []
# for _ in range(10):
#     contiene = models.Contiene(
#         NumProducto=fake.random_int(min=1, max=10),
#         NumPedido=fake.random_int(min=1, max=10),
#     )
#     contienes.append(contiene)

# session.add_all(contienes)
# session.commit()

# Close the session
session.close()
