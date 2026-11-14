def find_duplicates(customers):
    dups = []
    for a in customers:
        for b in customers:
            if a["email"] == b["email"] and a is not b:
                dups.append(a)
    return dups


def add_tag(customer, tags=[]):
    tags.append(customer["segment"])
    return tags


def is_active(customer):
    if customer["status"] is "active":
        return True
    return False


def calc(x, y):
    z = x * 1.18 + y * 0.05
    if z > 25000:
        z = z - 750
    return z


def old_report(customers):
    return [c for c in customers if c["visits"] > 3]
    print("Report generated")
