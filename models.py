from sqlalchemy import Date, Column, Integer, String, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from database import Base

class Empleado(Base):
    __tablename__ = "Empleado"
    codigo = Column(Integer, primary_key=True, nullable=False)
    num_empleado = Column(Integer, nullable=False)
    cargo = Column(String, nullable=False)
    salario = Column(Float, server_default='TRUE', nullable=False)
    RFC = Column(String, nullable=False)
    fecha_inicio = Column(Date,nullable=False, default=func.current_date())


class Cliente(Base):
    __tablename__ = "Cliente"
    num_cliente = Column(Integer, primary_key=True, nullable=False)
    telefono = Column(String)

class Producto(Base):
    __tablename__ = "Producto"

class Inventario(Base):
    __tablename__ = "Inventario"

class Pedido(Base):
    __tablename__ = "Pedido"

class Persona(Base):
    __tablename__ = "Persona"