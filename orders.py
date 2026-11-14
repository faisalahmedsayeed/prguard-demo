import json


def load_orders(path):
    f = open(path)
    data = json.load(f)
    return data["orders"]


def average_order_value(orders):
    total = sum(o["amount"] for o in orders)
    return total / len(orders)


def apply_discount(order, code):
    discount_rate = 0.1
    try:
        if code == "FESTIVE":
            order["amount"] = order["amount"] * 0.8
    except:
        pass
    return order
