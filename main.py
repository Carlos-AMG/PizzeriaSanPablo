from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import models
from database import Base

# Create the engine with echo=True to print SQL statements
engine = create_engine('postgresql://postgres:admin@localhost:5432/pizzaSanPablo', echo=True)

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create fake data using Faker
fake = Faker()
personas = []
for _ in range(10):
    persona = models.Persona(
        Nombre1=fake.first_name(),
        Nombre2=fake.first_name(),
        ApellidoP=fake.last_name(),
        ApellidoM=fake.last_name()
    )
    personas.append(persona)

# Insert fake data into the PERSONA table
session.add_all(personas)
session.commit()

# Close the session
session.close()
