import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Contact Book")
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone fields are required!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def clear_search():
    search_entry.delete(0, tk.END)
    update_contact_list()

def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone:
            contacts[selected_index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            clear_entries()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Name and phone fields are required!")

def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        clear_entries()
        update_contact_list()

def view_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["Name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["Phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["Email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["Address"])

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky='e')
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, sticky='e')
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, sticky='e')
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, sticky='e')
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=2)

update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.grid(row=1, column=2)

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.grid(row=2, column=2)

view_button = tk.Button(root, text="View Contact", command=view_selected_contact)
view_button.grid(row=3, column=2)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=4, column=0, sticky='e')
search_entry = tk.Entry(root)
search_entry.grid(row=4, column=1)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=4, column=2)

clear_search_button = tk.Button(root, text="Clear Search", command=clear_search)
clear_search_button.grid(row=5, column=2)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=6, column=0, columnspan=3)

root.mainloop()
