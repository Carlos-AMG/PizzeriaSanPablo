from sqlalchemy import Date, Column, Integer, String, ForeignKey, Float, func, Time
from sqlalchemy.orm import relationship
from database import Base

class Persona(Base):
    __tablename__ = "PERSONA"
    ID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre1 = Column(String)
    Nombre2 = Column(String)
    ApellidoP = Column(String)
    ApellidoM = Column(String)

class Empleado(Base):
    __tablename__ = "EMPLEADO"
    RFC = Column(String, primary_key=True, nullable=False, unique=True)
    PersonaID = Column(Integer, ForeignKey("PERSONA.ID", ondelete="CASCADE"), nullable=False) #pendiente
    Cargo = Column(String, nullable=False)
    Salario = Column(Float, nullable=False)
    FechaInicio = Column(Date, nullable=False, default=func.current_date())

class Direccion(Base):
    __tablename__ = "DIRECCION"
    DireccionID = Column(Integer, primary_key=True, autoincrement=True)
    Calle = Column(String)
    CodigoPostal = Column(String)
    InfoAdicional = Column(String)

class Cliente(Base):
    __tablename__ = "CLIENTE"
    NumCliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Telefono = Column(String)
    PersonaID = Column(Integer, ForeignKey("PERSONA.ID", ondelete="CASCADE"), nullable=False)
    DireccionID = Column(Integer, ForeignKey("DIRECCION.DireccionID", ondelete="CASCADE"))

class Pedido(Base):
    __tablename__ = "PEDIDO"
    NumPedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    FechaPedido = Column(Date, nullable=False, default=func.current_date())
    Hora = Column(Time, nullable=False, default=func.current_time())
    Cantidad = Column(Integer, nullable=False)
    Estado = Column(String, nullable=False)
    Total = Column(Float,  nullable=False)
    RFC_Empleado = Column(String, ForeignKey("EMPLEADO.RFC", ondelete="CASCADE"), nullable=False)
    NumCliente = Column(Integer, ForeignKey("CLIENTE.NumCliente", ondelete="CASCADE"), nullable=False)

class Producto(Base):
    __tablename__ = "PRODUCTO"
    NumProducto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre = Column(String, nullable=False)
    Precio = Column(Float, nullable=False)
    Descripcion = Column(String)

class Inventario(Base):
    __tablename__ = "INVENTARIO"
    NumIngrediente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre = Column(String, nullable=False)
    CantDisponible = Column(Integer, nullable=False)
    Precio = Column(Float, nullable=False)

class Utiliza(Base):
    __tablename__ = "UTILIZA"
    NumIngrediente = Column(Integer, ForeignKey("INVENTARIO.NumIngrediente", ondelete="CASCADE"), nullable=False, primary_key=True)
    NumProducto = Column(Integer, ForeignKey("PRODUCTO.NumProducto", ondelete="CASCADE"), nullable=False, primary_key=True)

class Contiene(Base):
    __tablename__ = "CONTIENE"
    NumProducto = Column(Integer, ForeignKey("PRODUCTO.NumProducto" ,ondelete="CASCADE"), nullable=False, primary_key=True)
    NumPedido = Column(Integer, ForeignKey("PEDIDO.NumPedido", ondelete="CASCADE"), nullable=False, primary_key=True)