import tkinter as tk  # Importing the tkinter module for GUI
from tkinter import messagebox  # Importing messagebox from tkinter for displaying messages
import pickle  # Importing pickle module for serialization

class Guest:
    def __init__(self, root):
        self.root = root
        self.root.title("Guest Section")  # Setting up the root window
        self.root.geometry("500x500")
        self.root.configure(bg="#FFFFFF")  # Setting background color

    # Method to add a new guest
    def add_guest(self, guest_id, name, address, contact_details):
        # Validate Guest ID
        if not guest_id.isdigit():
            tk.messagebox.showerror("Error", "Guest ID must be numeric.")
            return
        # Validate Name
        if not name.strip().isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return
        
        # Create a dictionary for the new guest
        new_guest = {
            "guest_id": guest_id,
            "name": name,
            "address": address,
            "contact_details": contact_details
        }

        # Save guest data to binary file using Pickle
        try:
            with open("guests.pkl", "ab") as file:
                pickle.dump(new_guest, file)
            tk.messagebox.showinfo("Success", "Guest added successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add guest: {str(e)}")

    # Method to create the UI for adding a guest
    def add_screen(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Guest")
        add_window.geometry("400x400")
        add_window.configure(bg="#FFFFFF")

        # Labels and entry fields for guest details
        id_label = tk.Label(add_window, text="Guest ID:", font=("Arial", 14), bg="#FFFFFF")
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

        # Button to submit the guest details
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_guest(id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get()), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    # Method to display guest details
    def display_guest_details_ui(self):
        details_window = tk.Toplevel(self.root)
        details_window.title("Guest Details")
        details_window.geometry("400x300")
        details_window.configure(bg="#FFFFFF")

        # Function to display guest details
        def display_details():
            guest_id = id_entry.get()
            try:
                with open("guests.pkl", "rb") as file:
                    while True:
                        try:
                            guest = pickle.load(file)
                            if guest["guest_id"] == guest_id:
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")
                                details_frame.pack(pady=20)

                                details_labels = [
                                    "Guest ID:", "Name:", "Address:", "Contact Details:"
                                ]

                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    value_label = tk.Label(details_frame, text=guest[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Guest Not Found", "No guest found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve guest details: {str(e)}")

        # Label and entry field for entering guest ID
        id_label = tk.Label(details_window, text="Enter Guest ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        # Button to display guest details
        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    # Method to delete a guest
    def delete_guest(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Guest")
        delete_window.geometry("400x200")
        delete_window.configure(bg="#FFFFFF")

        # Function to delete a guest
        def delete():
            guest_id = id_entry.get()
            try:
                with open("guests.pkl", "rb") as file:
                    guests = []
                    while True:
                        try:
                            guest = pickle.load(file)
                            if guest["guest_id"] != guest_id:
                                guests.append(guest)
                        except EOFError:
                            break

                with open("guests.pkl", "wb") as file:
                    for g in guests:
                        pickle.dump(g, file)

                tk.messagebox.showinfo("Success", "Guest deleted successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to delete guest: {str(e)}")

        # Label and entry field for entering guest ID to delete
        id_label = tk.Label(delete_window, text="Enter Guest ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        # Button to trigger guest deletion
        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    # Method to modify guest details
    def modify_guest_ui(self):
        modify_input_screen = tk.Toplevel(self.root)
        modify_input_screen.title("Modify Guest")
        modify_input_screen.geometry("300x200")
        modify_input_screen.configure(bg="#FFFFFF")

        # Label and entry field for entering guest ID
        id_label = tk.Label(modify_input_screen, text="Enter Guest ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify guest screen
        def open_modify_screen():
            guest_id = id_entry.get()
            try:
                with open("guests.pkl", "rb") as file:
                    while True:
                        try:
                            guest = pickle.load(file)
                            if guest["guest_id"] == guest_id:
                                modify_input_screen.destroy()
                                self.modify_guest_screen(guest)
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Guest Not Found", "No guest found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve guest details: {str(e)}")

        # Button to submit guest ID for modification
        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

        modify_input_screen.mainloop()

    # Method to create UI for modifying guest details
    def modify_guest_screen(self, guest):
        modify_screen = tk.Toplevel(self.root)
        modify_screen.title("Edit Guest")
        modify_screen.geometry("400x400")
        modify_screen.configure(bg="#FFFFFF")

        # Filling the entries with guest details
        id_label = tk.Label(modify_screen, text="Guest ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        id_entry.insert(0, guest["guest_id"])

        name_label = tk.Label(modify_screen, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(modify_screen, font=("Arial", 14))
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_entry.insert(0, guest["name"])

        address_label = tk.Label(modify_screen, text="Address:", font=("Arial", 14), bg="#FFFFFF")
        address_label.grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(modify_screen, font=("Arial", 14))
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.insert(0, guest["address"])

        contact_label = tk.Label(modify_screen, text="Contact Details:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.grid(row=3, column=0, padx=10, pady=5)
        contact_entry = tk.Entry(modify_screen, font=("Arial", 14))
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_entry.insert(0, guest["contact_details"])

        # Function to update guest details
        def update_guest():
            updated_guest = {
                "guest_id": id_entry.get(),
                "name": name_entry.get(),
                "address": address_entry.get(),
                "contact_details": contact_entry.get()
            }

            try:
                # Open the file in read mode
                with open("guests.pkl", "rb") as file:
                    guests = []
                    # Load existing guest details
                    while True:
                        try:
                            guest = pickle.load(file)
                            # Check if the loaded guest ID matches the ID of the guest being updated
                            if guest["guest_id"] == guest["guest_id"]:
                                # Append the updated guest details to the list
                                guests.append(updated_guest)
                            else:
                                guests.append(guest)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("guests.pkl", "wb") as file:
                    # Write the updated guest details back to the file
                    for g in guests:
                        pickle.dump(g, file)

                tk.messagebox.showinfo("Success", "Guest details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update guest details: {str(e)}")

        # Button to update guest details
        update_button = tk.Button(modify_screen, text="Update", command=update_guest, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Guest(root)
    app.add_screen()  # Display the add guest screen when the program starts
    root.mainloop()  # Run the tkinter event loop
