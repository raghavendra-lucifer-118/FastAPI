from fastapi import FastAPI ,Depends
from models import Product
from database import session , engine
import database_model
from sqlalchemy.orm import Session
app = FastAPI()

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

database_model.Base.metadata.create_all(bind = engine)

# def init_db():
#     db = Session()
#     for product in products:
#         db.add(database_model.Product(**product.model_dump()))
        
#     db.commit()    

# init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()    
        

@app.get("/")
def home():
    return "FastAPI App"

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products


@app.get("/products/{id}")
def get_product_by_id(id : int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    
    if db_product:
        return db_product
    return " Not Found"
    

@app.post("/product")
def get_product_by_id(product : Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return products

@app.put("/product")
def update_product(product:Product , id:int ,  db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name  
        db_product.description = product.description  
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Successfull"
    return "Not Found"
          


@app.delete("/product")
def delete_product(id:int  , db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(
        database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Successfull"
    return "Not Found"    
            