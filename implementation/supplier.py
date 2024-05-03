import tkinter as tk
from tkinter import messagebox
import pickle

class Supplier:
    def __init__(self, root):
        self.root = root
        self.root.title("Supplier Section")
        self.root.geometry("500x500")
        self.root.configure(bg="#FFFFFF")

    def add_supplier(self, supplier_id, name, address, contact_details, menu=None, min_guests=None, max_guests=None):
        # Validate Supplier ID
        if not supplier_id.isdigit():
            tk.messagebox.showerror("Error", "Supplier ID must be numeric.")
            return
        # Validate Name
        if not name.strip().isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return
        
        new_supplier = {
            "supplier_id": supplier_id,
            "name": name,
            "address": address,
            "contact_details": contact_details,
            "menu": menu,
            "min_guests": min_guests,
            "max_guests": max_guests
        }

        # Save supplier data to binary file using Pickle
        try:
            with open("suppliers.pkl", "ab") as file:
                pickle.dump(new_supplier, file)
            tk.messagebox.showinfo("Success", "Supplier added successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add supplier: {str(e)}")

    def add_screen(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Supplier")
        add_window.geometry("400x400")
        add_window.configure(bg="#FFFFFF")

        id_label = tk.Label(add_window, text="Supplier ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(add_window, font=("Arial", 14))
        id_entry.pack()

        name_label = tk.Label(add_window, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.pack(pady=10)
        name_entry = tk.Entry(add_window, font=("Arial", 14))
        name_entry.pack()

        address_label = tk.Label(add_window, text="Address:", font=("Arial", 14), bg="#FFFFFF")
        address_label.pack(pady=10)
        address_entry = tk.Entry(add_window, font=("Arial", 14))
        address_entry.pack()

        contact_label = tk.Label(add_window, text="Contact Details:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.pack(pady=10)
        contact_entry = tk.Entry(add_window, font=("Arial", 14))
        contact_entry.pack()

        menu_label = tk.Label(add_window, text="Menu:", font=("Arial", 14), bg="#FFFFFF")
        menu_label.pack(pady=10)
        menu_entry = tk.Entry(add_window, font=("Arial", 14))
        menu_entry.pack()

        min_guests_label = tk.Label(add_window, text="Min Guests:", font=("Arial", 14), bg="#FFFFFF")
        min_guests_label.pack(pady=10)
        min_guests_entry = tk.Entry(add_window, font=("Arial", 14))
        min_guests_entry.pack()

        max_guests_label = tk.Label(add_window, text="Max Guests:", font=("Arial", 14), bg="#FFFFFF")
        max_guests_label.pack(pady=10)
        max_guests_entry = tk.Entry(add_window, font=("Arial", 14))
        max_guests_entry.pack()

        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_supplier(id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), menu_entry.get(), min_guests_entry.get(), max_guests_entry.get()), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def display_supplier_details_ui(self):
        details_window = tk.Toplevel(self.root)
        details_window.title("Supplier Details")
        details_window.geometry("400x300")
        details_window.configure(bg="#FFFFFF")

        def display_details():
            supplier_id = id_entry.get()
            try:
                with open("suppliers.pkl", "rb") as file:
                    while True:
                        try:
                            supplier = pickle.load(file)
                            if supplier["supplier_id"] == supplier_id:
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")
                                details_frame.pack(pady=20)

                                details_labels = [
                                    "Supplier ID:", "Name:", "Address:", "Contact Details:",
                                    "Menu:", "Min Guests:", "Max Guests:"
                                ]

                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    value_label = tk.Label(details_frame, text=supplier[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Supplier Not Found", "No supplier found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve supplier details: {str(e)}")

        id_label = tk.Label(details_window, text="Enter Supplier ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def delete_supplier(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Supplier")
        delete_window.geometry("400x200")
        delete_window.configure(bg="#FFFFFF")

        def delete():
            supplier_id = id_entry.get()
            try:
                with open("suppliers.pkl", "rb") as file:
                    suppliers = []
                    while True:
                        try:
                            supplier = pickle.load(file)
                            if supplier["supplier_id"] != supplier_id:
                                suppliers.append(supplier)
                        except EOFError:
                            break

                with open("suppliers.pkl", "wb") as file:
                    for sup in suppliers:
                        pickle.dump(sup, file)

                tk.messagebox.showinfo("Success", "Supplier deleted successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to delete supplier: {str(e)}")

        id_label = tk.Label(delete_window, text="Enter Supplier ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_supplier_ui(self):
        modify_input_screen = tk.Toplevel(self.root)
        modify_input_screen.title("Modify Supplier")
        modify_input_screen.geometry("300x200")
        modify_input_screen.configure(bg="#FFFFFF")

        id_label = tk.Label(modify_input_screen, text="Enter Supplier ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify supplier screen
        def open_modify_screen():
            supplier_id = id_entry.get()
            try:
                with open("suppliers.pkl", "rb") as file:
                    while True:
                        try:
                            supplier = pickle.load(file)
                            if supplier["supplier_id"] == supplier_id:
                                modify_input_screen.destroy()
                                self.modify_supplier_screen(supplier)
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Supplier Not Found", "No supplier found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve supplier details: {str(e)}")

        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

        modify_input_screen.mainloop()

    def modify_supplier_screen(self, supplier):
        modify_screen = tk.Toplevel(self.root)
        modify_screen.title("Edit Supplier")
        modify_screen.geometry("400x400")
        modify_screen.configure(bg="#FFFFFF")

        # Filling the entries with supplier details
        id_label = tk.Label(modify_screen, text="Supplier ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        id_entry.insert(0, supplier["supplier_id"])

        name_label = tk.Label(modify_screen, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(modify_screen, font=("Arial", 14))
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_entry.insert(0, supplier["name"])

        address_label = tk.Label(modify_screen, text="Address:", font=("Arial", 14), bg="#FFFFFF")
        address_label.grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(modify_screen, font=("Arial", 14))
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.insert(0, supplier["address"])

        contact_label = tk.Label(modify_screen, text="Contact Details:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.grid(row=3, column=0, padx=10, pady=5)
        contact_entry = tk.Entry(modify_screen, font=("Arial", 14))
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_entry.insert(0, supplier["contact_details"])

        menu_label = tk.Label(modify_screen, text="Menu:", font=("Arial", 14), bg="#FFFFFF")
        menu_label.grid(row=4, column=0, padx=10, pady=5)
        menu_entry = tk.Entry(modify_screen, font=("Arial", 14))
        menu_entry.grid(row=4, column=1, padx=10, pady=5)
        menu_entry.insert(0, supplier.get("menu", ""))

        min_guests_label = tk.Label(modify_screen, text="Min Guests:", font=("Arial", 14), bg="#FFFFFF")
        min_guests_label.grid(row=5, column=0, padx=10, pady=5)
        min_guests_entry = tk.Entry(modify_screen, font=("Arial", 14))
        min_guests_entry.grid(row=5, column=1, padx=10, pady=5)
        min_guests_entry.insert(0, supplier.get("min_guests", ""))

        max_guests_label = tk.Label(modify_screen, text="Max Guests:", font=("Arial", 14), bg="#FFFFFF")
        max_guests_label.grid(row=6, column=0, padx=10, pady=5)
        max_guests_entry = tk.Entry(modify_screen, font=("Arial", 14))
        max_guests_entry.grid(row=6, column=1, padx=10, pady=5)
        max_guests_entry.insert(0, supplier.get("max_guests", ""))

        # Function to update the supplier details
        def update_supplier():
            updated_supplier = {
                "supplier_id": id_entry.get(),
                "name": name_entry.get(),
                "address": address_entry.get(),
                "contact_details": contact_entry.get(),
                "menu": menu_entry.get(),
                "min_guests": min_guests_entry.get(),
                "max_guests": max_guests_entry.get()
            }

            try:
                # Open the file in read mode
                with open("suppliers.pkl", "rb") as file:
                    suppliers = []
                    # Load existing supplier details
                    while True:
                        try:
                            supplier = pickle.load(file)
                            # Check if the loaded supplier ID matches the ID of the supplier being updated
                            if supplier["supplier_id"] == updated_supplier["supplier_id"]:
                                # Append the updated supplier details to the list
                                suppliers.append(updated_supplier)
                            else:
                                suppliers.append(supplier)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("suppliers.pkl", "wb") as file:
                    # Write the updated supplier details back to the file
                    for sup in suppliers:
                        pickle.dump(sup, file)

                tk.messagebox.showinfo("Success", "Supplier details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update supplier details: {str(e)}")

        update_button = tk.Button(modify_screen, text="Update", command=update_supplier, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Supplier(root)
    app.add_screen()
    root.mainloop()

