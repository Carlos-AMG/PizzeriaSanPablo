from sqlalchemy import Date, Column, Integer, String, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from database import Base

class Empleado(Base):
    __tablename__ = "Empleado"
    RFC = Column(Integer, primary_key=True, nullabable=False)
    personaID = Column(Integer, ForeignKey("Persona.id", ondelete="CASCADE"), nullable=False) #pendiente
    cargo = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    fechaInicio = Column(Date, nullable=False, default=func.current_date())

class Persona(Base):
    __tablename__ = "Persona"
    ID = Column(Integer, ForeignKey=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellidoP = Column(String, nullable=False)
    apellidoM = Column(String, nullable=False)

class Cliente(Base):
    __tablename__ = "Cliente"
    numCliente = Column(Integer, primary_key=True, nullable=False)
    telefono = Column(String)
    personaID = Column(Integer, nullable=False, )

class Pedido(Base):
    __tablename__ = "Pedido"
    numPedido = Column(Integer, primary_key=True, nullable=False)
    fechaPedido = Column(Date, nullable=False, default=func.current_date())
    hora = Column(Date, nullable=False, default=func.current_hour())
    cantidad = Column(Integer, nullable=False)
    estado = Column(String, nullable=False)
    total = Column(float,  nullable=False)
    RFC_Empleado = Column(Integer, ForeignKey("Empleado.RFC", ondelete="CASCADE"), nullable=False)
    numCliente = Column(Integer, ForeignKey("Cliente.numCliente", ondelete="CASCADE"), nullable=False)

class Producto(Base):
    __tablename__ = "Producto"
    numProducto = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    deescripcion = Column(String)

