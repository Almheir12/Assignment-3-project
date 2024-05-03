import tkinter as tk
from tkinter import messagebox
import pickle

class Venue:
    def __init__(self, root):
        self.root = root
        self.root.title("Venue Section")
        self.root.geometry("500x500")
        self.root.configure(bg="#FFFFFF")

    def add_venue(self, venue_id, name, address, contact, min_guests, max_guests):
        # Validate Venue ID
        if not venue_id.isdigit():
            tk.messagebox.showerror("Error", "Venue ID must be numeric.")
            return
        # Validate Name
        if not name.strip().isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabetic characters.")
            return
        
        new_venue = {
            "venue_id": venue_id,
            "name": name,
            "address": address,
            "contact": contact,
            "min_guests": min_guests,
            "max_guests": max_guests
        }

        # Save venue data to binary file using Pickle
        try:
            with open("venues.pkl", "ab") as file:
                pickle.dump(new_venue, file)
            tk.messagebox.showinfo("Success", "Venue added successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add venue: {str(e)}")

    def add_screen(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Venue")
        add_window.geometry("400x400")
        add_window.configure(bg="#FFFFFF")

        id_label = tk.Label(add_window, text="Venue ID:", font=("Arial", 14), bg="#FFFFFF")
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

        contact_label = tk.Label(add_window, text="Contact:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.pack(pady=10)
        contact_entry = tk.Entry(add_window, font=("Arial", 14))
        contact_entry.pack()

        min_guests_label = tk.Label(add_window, text="Min Guests:", font=("Arial", 14), bg="#FFFFFF")
        min_guests_label.pack(pady=10)
        min_guests_entry = tk.Entry(add_window, font=("Arial", 14))
        min_guests_entry.pack()

        max_guests_label = tk.Label(add_window, text="Max Guests:", font=("Arial", 14), bg="#FFFFFF")
        max_guests_label.pack(pady=10)
        max_guests_entry = tk.Entry(add_window, font=("Arial", 14))
        max_guests_entry.pack()

        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_venue(id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), min_guests_entry.get(), max_guests_entry.get()), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def display_venue_details_ui(self):
        details_window = tk.Toplevel(self.root)
        details_window.title("Venue Details")
        details_window.geometry("400x300")
        details_window.configure(bg="#FFFFFF")

        def display_details():
            venue_id = id_entry.get()
            try:
                with open("venues.pkl", "rb") as file:
                    while True:
                        try:
                            venue = pickle.load(file)
                            if venue["venue_id"] == venue_id:
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")
                                details_frame.pack(pady=20)

                                details_labels = [
                                    "Venue ID:", "Name:", "Address:", "Contact:",
                                    "Min Guests:", "Max Guests:"
                                ]

                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    value_label = tk.Label(details_frame, text=venue[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Venue Not Found", "No venue found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve venue details: {str(e)}")

        id_label = tk.Label(details_window, text="Enter Venue ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def delete_venue(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Venue")
        delete_window.geometry("400x200")
        delete_window.configure(bg="#FFFFFF")

        def delete():
            venue_id = id_entry.get()
            try:
                with open("venues.pkl", "rb") as file:
                    venues = []
                    while True:
                        try:
                            venue = pickle.load(file)
                            if venue["venue_id"] != venue_id:
                                venues.append(venue)
                        except EOFError:
                            break

                with open("venues.pkl", "wb") as file:
                    for ven in venues:
                        pickle.dump(ven, file)

                tk.messagebox.showinfo("Success", "Venue deleted successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to delete venue: {str(e)}")

        id_label = tk.Label(delete_window, text="Enter Venue ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_venue_ui(self):
        modify_input_screen = tk.Toplevel(self.root)
        modify_input_screen.title("Modify Venue")
        modify_input_screen.geometry("300x200")
        modify_input_screen.configure(bg="#FFFFFF")

        id_label = tk.Label(modify_input_screen, text="Enter Venue ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify venue screen
        def open_modify_screen():
            venue_id = id_entry.get()
            try:
                with open("venues.pkl", "rb") as file:
                    while True:
                        try:
                            venue = pickle.load(file)
                            if venue["venue_id"] == venue_id:
                                modify_input_screen.destroy()
                                self.modify_venue_screen(venue)
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Venue Not Found", "No venue found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve venue details: {str(e)}")

        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

        modify_input_screen.mainloop()

    def modify_venue_screen(self, venue):
        modify_screen = tk.Toplevel(self.root)
        modify_screen.title("Edit Venue")
        modify_screen.geometry("400x400")
        modify_screen.configure(bg="#FFFFFF")

        # Filling the entries with venue details
        id_label = tk.Label(modify_screen, text="Venue ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.grid(row=0, column=0, padx=10, pady=5)
        id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        id_entry.grid(row=0, column=1, padx=10, pady=5)
        id_entry.insert(0, venue["venue_id"])

        name_label = tk.Label(modify_screen, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(modify_screen, font=("Arial", 14))
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_entry.insert(0, venue["name"])

        address_label = tk.Label(modify_screen, text="Address:", font=("Arial", 14), bg="#FFFFFF")
        address_label.grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(modify_screen, font=("Arial", 14))
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.insert(0, venue["address"])

        contact_label = tk.Label(modify_screen, text="Contact:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.grid(row=3, column=0, padx=10, pady=5)
        contact_entry = tk.Entry(modify_screen, font=("Arial", 14))
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_entry.insert(0, venue["contact"])

        min_guests_label = tk.Label(modify_screen, text="Min Guests:", font=("Arial", 14), bg="#FFFFFF")
        min_guests_label.grid(row=4, column=0, padx=10, pady=5)
        min_guests_entry = tk.Entry(modify_screen, font=("Arial", 14))
        min_guests_entry.grid(row=4, column=1, padx=10, pady=5)
        min_guests_entry.insert(0, venue["min_guests"])

        max_guests_label = tk.Label(modify_screen, text="Max Guests:", font=("Arial", 14), bg="#FFFFFF")
        max_guests_label.grid(row=5, column=0, padx=10, pady=5)
        max_guests_entry = tk.Entry(modify_screen, font=("Arial", 14))
        max_guests_entry.grid(row=5, column=1, padx=10, pady=5)
        max_guests_entry.insert(0, venue["max_guests"])

        # Function to update the venue details
        def update_venue():
            updated_venue = {
                "venue_id": id_entry.get(),
                "name": name_entry.get(),
                "address": address_entry.get(),
                "contact": contact_entry.get(),
                "min_guests": min_guests_entry.get(),
                "max_guests": max_guests_entry.get()
            }

            try:
                # Open the file in read mode
                with open("venues.pkl", "rb") as file:
                    venues = []
                    # Load existing venue details
                    while True:
                        try:
                            ven = pickle.load(file)
                            # Check if the loaded venue ID matches the ID of the venue being updated
                            if ven["venue_id"] == updated_venue["venue_id"]:
                                # Append the updated venue details to the list
                                venues.append(updated_venue)
                            else:
                                venues.append(ven)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("venues.pkl", "wb") as file:
                    # Write the updated venue details back to the file
                    for ven in venues:
                        pickle.dump(ven, file)

                tk.messagebox.showinfo("Success", "Venue details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update venue details: {str(e)}")

        update_button = tk.Button(modify_screen, text="Update", command=update_venue, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Venue(root)
    app.add_screen()
    root.mainloop()
