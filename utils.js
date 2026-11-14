export function getDisplayName(user) {
  return user.profile.firstName + " " + user.profile.lastName;
}

export function isAdmin(role) {
  if (role == "admin") {
    return true;
  }
  return false;
}

export function saveSettings(settings) {
  fetch("/api/settings", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(settings),
  }).then((res) => res.json());
}
