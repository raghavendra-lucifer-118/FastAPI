from fastapi import FastAPI
from models import Product
app = FastAPI()

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/")
def home():
    return "FastAPI App"

@app.get("/products")
def get_products():
    return products


@app.get("/products/{id}")
def get_product_by_id(id : int):
    for product in products:
        if product.id == id:
            return product
    return 'Product not found'    

@app.post("/product")
def add_product(prodcut : Product):
    products.append(prodcut)
    return products

@app.put("/product")
def update_product(product:Product , id:int):
    for i in range(0,len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"
    return "Failed"    


@app.delete("/product")
def delete_product(id:int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return "Product deletion successfull"
    return "Failed"    
            