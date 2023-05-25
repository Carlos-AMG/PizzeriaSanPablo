from sqlalchemy import Date, Column, Integer, String, ForeignKey, Float, func, Time, DECIMAL
from database import Base

class Persona(Base):
    __tablename__ = 'PERSONA'
    ID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre = Column(String(30), nullable=False)
    ApellidoP = Column(String(30), nullable=False)
    ApellidoM = Column(String(30))
    Direccion = Column(String(150))

class Empleado(Base):
    __tablename__ = 'EMPLEADO'
    RFC = Column(String(13), primary_key=True, nullable=False, unique=True)
    PersonaID = Column(Integer, ForeignKey("PERSONA.ID", ondelete="CASCADE"), nullable=False) 
    Cargo = Column(String(30), nullable=False)
    Salario = Column(DECIMAL(10, 2), nullable=False)
    FechaInicio = Column(Date, nullable=False, default=func.current_date())

class Cliente(Base):
    __tablename__ = 'CLIENTE'
    NumCliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Telefono = Column(String(20))
    PersonaID = Column(Integer, ForeignKey("PERSONA.ID", ondelete="CASCADE"), nullable=False)

class Pedido(Base):
    __tablename__ = 'PEDIDO'
    NumPedido = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    FechaPedido = Column(Date, nullable=False, default=func.current_date())
    Hora = Column(Time, nullable=False, default=func.current_time())
    Cantidad = Column(Integer, nullable=False)
    Estado = Column(String(50), nullable=False)
    Total = Column(DECIMAL(10, 2),  nullable=False)
    RFC_Empleado = Column(String(13), ForeignKey("EMPLEADO.RFC", ondelete="CASCADE"), nullable=False)
    NumCliente = Column(Integer, ForeignKey("CLIENTE.NumCliente", ondelete="CASCADE"), nullable=False)

class Producto(Base):
    __tablename__ = 'PRODUCTO'
    NumProducto = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre = Column(String(30), nullable=False)
    Precio = Column(DECIMAL(10, 2), nullable=False)
    Descripcion = Column(String(100))

class Inventario(Base):
    __tablename__ = 'INVENTARIO'
    NumIngrediente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Nombre = Column(String(30), nullable=False)
    CantDisponible = Column(Integer, nullable=False)
    Precio = Column(DECIMAL(10, 2), nullable=False)

class Utiliza(Base):
    __tablename__ = 'UTILIZA'
    NumIngrediente = Column(Integer, ForeignKey("INVENTARIO.NumIngrediente", ondelete="CASCADE"), nullable=False, primary_key=True)
    NumProducto = Column(Integer, ForeignKey("PRODUCTO.NumProducto", ondelete="CASCADE"), nullable=False, primary_key=True)

class Contiene(Base):
    __tablename__ = 'CONTIENE'
    NumProducto = Column(Integer, ForeignKey("PRODUCTO.NumProducto" ,ondelete="CASCADE"), nullable=False, primary_key=True)
    NumPedido = Column(Integer, ForeignKey("PEDIDO.NumPedido", ondelete="CASCADE"), nullable=False, primary_key=True)