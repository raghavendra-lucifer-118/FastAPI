from pydantic import BaseModel

class Product(BaseModel):
    id : int
    price : float
    name : str
    description : str
    quantity : int
    
    