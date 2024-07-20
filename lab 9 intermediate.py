import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Membuat dan menghubungkan ke database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()

# Membuat tabel contacts
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                alamat TEXT,
                no_telp TEXT,
                email TEXT
            )''')

conn.commit()
conn.close()

# Fungsi CRUD
def insert_contact(nama, alamat, no_telp, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (nama, alamat, no_telp, email) VALUES (?, ?, ?, ?)", (nama, alamat, no_telp, email))
    conn.commit()
    conn.close()

def get_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts

def update_contact(contact_id, nama, alamat, no_telp, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET nama = ?, alamat = ?, no_telp = ?, email = ? WHERE id = ?", (nama, alamat, no_telp, email, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

# Fungsi untuk merefresh listbox
def refresh_contacts_list():
    contacts_listbox.delete(0, tk.END)
    for contact in get_contacts():
        contacts_listbox.insert(tk.END, f"ID: {contact[0]}, Nama: {contact[1]}, Alamat: {contact[2]}, No Telp: {contact[3]}, Email: {contact[4]}")

def add_contact():
    nama = simpledialog.askstring("Input", "Nama:")
    alamat = simpledialog.askstring("Input", "Alamat:")
    no_telp = simpledialog.askstring("Input", "No Telp:")
    email = simpledialog.askstring("Input", "Email:")
    if nama and alamat and no_telp and email:
        insert_contact(nama, alamat, no_telp, email)
        refresh_contacts_list()
    else:
        messagebox.showwarning("Warning", "All fields are required!")

def delete_selected_contact():
    selected_contact = contacts_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_id = int(selected_contact.split(",")[0].split(":")[1].strip())
        delete_contact(contact_id)
        refresh_contacts_list()
    else:
        messagebox.showwarning("Warning", "No contact selected!")

def update_selected_contact():
    selected_contact = contacts_listbox.get(tk.ACTIVE)
    if selected_contact:
        contact_id = int(selected_contact.split(",")[0].split(":")[1].strip())
        nama = simpledialog.askstring("Input", "Nama:")
        alamat = simpledialog.askstring("Input", "Alamat:")
        no_telp = simpledialog.askstring("Input", "No Telp:")
        email = simpledialog.askstring("Input", "Email:")
        if nama and alamat and no_telp and email:
            update_contact(contact_id, nama, alamat, no_telp, email)
            refresh_contacts_list()
        else:
            messagebox.showwarning("Warning", "All fields are required!")
    else:
        messagebox.showwarning("Warning", "No contact selected!")

root = tk.Tk()
root.title("Contact Manager")

contacts_listbox = tk.Listbox(root, width=80)
contacts_listbox.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
update_button.pack()

refresh_button = tk.Button(root, text="Refresh List", command=refresh_contacts_list)
refresh_button.pack()

refresh_contacts_list()

root.mainloop()
