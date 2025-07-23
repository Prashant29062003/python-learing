# 🧠 **Challenge: Vehicle Hierarchy & Type Counter**

Create a class hierarchy with the following rules:

## ✅ Requirements:

1. **Class:** `Vehicle` (Base class)

   * Private attributes: `__brand`, `__wheels`
   * `@property` for brand
   * `@staticmethod` → `general_info()` returns: `"Vehicles are used for transport."`
   * Class variable: `vehicle_count` (counts all vehicles created)

2. **Class:** `Bike` (Inherits from `Vehicle`)

   * Default wheels = 2
   * Overrides `fuel_type()` to return `"Petrol"`

3. **Class:** `Truck` (Inherits from `Vehicle`)

   * Default wheels = 6
   * Overrides `fuel_type()` to return `"Diesel"`

4. **Extra:**

   * Add a method `show_details()` in `Vehicle` that prints:
     `"Brand: <brand>, Wheels: <wheels>"`

---

## 🔸 **Your Tasks:**

Write code that:

1. Creates 1 Bike and 2 Trucks
2. Prints:

   * All vehicle details
   * Their fuel type
   * Total number of vehicles

---

Would you like a hint, template, or go all in?

