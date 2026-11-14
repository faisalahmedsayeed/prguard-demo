"""Small, clean helper module. PRGuard should find little or nothing here."""
from dataclasses import dataclass


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int


def cart_total(items: list[CartItem]) -> float:
    """Return the total price of all items in the cart."""
    return sum(item.price * item.quantity for item in items)


def format_rupees(amount: float) -> str:
    """Format a number as Indian rupees, e.g. 1234.5 -> 'Rs 1,234.50'."""
    return f"Rs {amount:,.2f}"
