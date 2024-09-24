from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Receipt Generator ")
root.geometry()
root.resizable()

def add():
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    rate = float(rate_entry.get())
    price=rate*quantity
    tree.insert("", "end", values=(item, quantity,rate, price))
    item_entry.delete(0,END)
    quantity_entry.delete(0,END)
    rate_entry.delete(0,END)
    
def clearall():
    item_entry.delete(0,END)
    quantity_entry.delete(0,END)
    rate_entry.delete(0,END)
    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    quantity_entry.insert(0, "1")
    for item in tree.get_children():
        tree.delete(item)
    
def gen_receipt():
    name = name_entry.get()
    phone = phone_entry.get()
    
    c = canvas.Canvas("receipt.pdf", pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Receipt")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Name: {name}")
    c.drawString(50, height - 120, f"Phone no.: +91 {phone}")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 150, "Item")
    c.drawString(200, height - 150, "Quantity")
    c.drawString(350, height - 150, "Rate")
    c.drawString(500, height - 150, "Price")
    
    c.setFont("Helvetica", 12)
    y = height - 170
    total_price = 0
    for row in tree.get_children():
        item, quantity,rate, price = tree.item(row)["values"]
        c.drawString(50, y, str(item))
        c.drawString(200, y, str(quantity))
        c.drawString(350, y, str(rate))
        c.drawString(500, y, str(price))
        c.line(50, y - 5, 550, y - 5)
        total_price += float(price)
        y -= 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(350, y - 20, "Total:")
    c.drawString(500, y - 20, f"{total_price}")
    
    c.save()

title=Label(root,text="Receipt Generator",font=("Segoe UI",20,"bold"))
title.pack(pady=20)
entry_frame=Frame(root)
entry_frame.pack()

name=Label(entry_frame,text="Name :")
name.grid(row=0,column=0,padx=5,pady=5)
name_entry=ttk.Entry(entry_frame)
name_entry.grid(row=0,column=1,padx=5,pady=5)

phone=Label(entry_frame,text="Phone no. :")
phone.grid(row=0,column=2,padx=5,pady=5)
phone_entry=ttk.Entry(entry_frame)
phone_entry.grid(row=0,column=3,padx=5,pady=5)

item_label=Label(entry_frame,text="Item :")
item_label.grid(row=1,column=0,padx=5,pady=5)
item_entry=ttk.Entry(entry_frame)
item_entry.grid(row=1,column=1,padx=5,pady=5)

quantity_label=Label(entry_frame,text="Quantity :")
quantity_label.grid(row=1,column=2,padx=5,pady=5)
quantity_entry=Spinbox(entry_frame,from_=1,to=1000)
quantity_entry.grid(row=1,column=3,padx=5,pady=5)

rate_label=Label(entry_frame,text="Rate :")
rate_label.grid(row=1,column=4,padx=5,pady=5)
rate_entry=ttk.Entry(entry_frame)
rate_entry.grid(row=1,column=5,padx=5,pady=5)

add_button=ttk.Button(entry_frame,text="Add Item",command=add)
add_button.grid(row=3,column=0,columnspan=6)

list_frame=Frame(root)
list_frame.pack(pady=20,padx=20)

tree=ttk.Treeview(list_frame,columns=("Item","Quantity","Rate","Price"),show="headings",style="Treeview")
tree.heading("Item",text="Item")
tree.heading("Quantity",text="Quantity")
tree.heading("Rate",text="Rate")
tree.heading("Price",text="Price")
tree.pack()
tree.column("Item", width=150)
tree.column("Quantity", width=150)
tree.column("Rate", width=150)
tree.column("Price", width=150)

button_frame=Frame(root)
button_frame.pack()

print=ttk.Button(button_frame,text="Print Receipt",width=15,command=gen_receipt)
print.grid(row=0,column=0,padx=20,pady=20)

clear=ttk.Button(button_frame,text="New",command=clearall)
clear.grid(row=0,column=1,padx=20,pady=20)

root.mainloop()

