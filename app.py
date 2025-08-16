import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["vehiclesDB"]
collection = db["vehicles"]

# GUI window
root = tk.Tk()
root.title("Vehicle Store - CRUD App")
root.geometry("500x400")

# Labels & Entry boxes
tk.Label(root, text="Vehicle Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Type (Car/Bike/Truck)").pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Stock").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

# ------------------- CRUD FUNCTIONS -------------------

# CREATE
def add_vehicle():
    name = name_entry.get()
    vtype = type_entry.get()
    price = float(price_entry.get())
    stock = int(stock_entry.get())

    collection.insert_one({"name": name, "type": vtype, "price": price, "stock": stock})
    messagebox.showinfo("Success", "Vehicle Added!")

# READ
def view_vehicles():
    items = collection.find()
    data = ""
    for item in items:
        data += f"{item['name']} - {item['type']} - Rs.{item['price']} - Stock: {item['stock']}\n"
    if data == "":
        data = "No vehicles found."
    messagebox.showinfo("Vehicle List", data)

# UPDATE (update price)
def update_vehicle():
    name = name_entry.get()
    new_price = float(price_entry.get())
    result = collection.update_one({"name": name}, {"$set": {"price": new_price}})
    if result.modified_count > 0:
        messagebox.showinfo("Updated", "Price Updated!")
    else:
        messagebox.showwarning("Not Found", "Vehicle not found!")

# DELETE
def delete_vehicle():
    name = name_entry.get()
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        messagebox.showinfo("Deleted", "Vehicle Deleted!")
    else:
        messagebox.showwarning("Not Found", "Vehicle not found!")

# BUTTONS
tk.Button(root, text="Add", command=add_vehicle).pack(pady=5)
tk.Button(root, text="View", command=view_vehicles).pack(pady=5)
tk.Button(root, text="Update", command=update_vehicle).pack(pady=5)
tk.Button(root, text="Delete", command=delete_vehicle).pack(pady=5)

root.mainloop()
