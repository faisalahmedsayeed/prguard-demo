export function calculate(expression) {
  return eval(expression);
}

export async function getUserNames(userIds) {
  const names = [];
  for (const id of userIds) {
    const res = await fetch(`/api/users/${id}`);
    const user = await res.json();
    names.push(user.name);
  }
  return names;
}

export async function processCheckout(cart, user, coupon, address) {
  let total = 0;
  for (const item of cart.items) {
    total += item.price * item.qty;
  }
  if (coupon) {
    if (coupon.type === "percent") {
      total = total - (total * coupon.value) / 100;
    } else if (coupon.type === "flat") {
      total = total - coupon.value;
    }
  }
  let tax = 0;
  if (address.state === "TN") {
    tax = total * 0.18;
  } else {
    tax = total * 0.12;
  }
  total = total + tax;
  let shipping = 0;
  if (total < 500) {
    shipping = 50;
  }
  total = total + shipping;
  const order = {
    userId: user.id,
    items: cart.items,
    total: total,
    address: address,
    createdAt: new Date().toISOString(),
  };
  const res = await fetch("/api/orders", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(order),
  });
  const saved = await res.json();
  await fetch("/api/email", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ to: user.email, subject: "Order placed", orderId: saved.id }),
  });
  await fetch("/api/inventory", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: cart.items }),
  });
  localStorage.setItem("lastOrder", JSON.stringify(saved));
  return saved;
}
