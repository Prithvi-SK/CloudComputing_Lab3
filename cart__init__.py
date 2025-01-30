from typing import List, Dict
from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: Dict) -> "Product":
        """Create a Product instance from a dictionary."""
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data.get('qty', 0)
        )


def list_products() -> List[Product]:
    """Retrieve and return a list of all products."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Retrieve and return a product by its ID."""
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} does not exist.")
    return Product.load(product_data)


def add_product(product: Dict) -> None:
    """Add a new product to the database."""
    required_fields = {'id', 'name', 'description', 'cost'}
    if not required_fields.issubset(product.keys()):
        raise ValueError(f"Missing required fields: {required_fields - product.keys()}")
    dao.add_product(product)


def update_qty(product_id: int, qty: int) -> None:
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative.')
    dao.update_qty(product_id, qty)
