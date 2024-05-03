import tkinter as tk  # Importing the tkinter module
from tkinter import messagebox  # Importing the messagebox class from the tkinter module
import pickle  # Importing the pickle module for serializing and deserializing Python objects

class Client:
    def __init__(self, root):
        # Constructor method to initialize the Client class
        self.root = root  # Assigning the root Tkinter window to an instance variable
        self.root.title("Client Section")  # Setting the title of the Tkinter window
        self.root.geometry("500x500")  # Setting the dimensions of the Tkinter window
        self.root.configure(bg="#FFFFFF")  # Setting the background color of the Tkinter window

    def add_client(self, client_id, name, address, contact_details, budget):
        # Method to add a new client to the system
        # Validate Client ID
        if not client_id.isdigit():
            tk.messagebox.showerror("Error", "Client ID must be numeric.")  # Displaying an error message if client ID is not numeric
            return
        # Validate Name
        if not name.strip().isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabetic characters.")  # Displaying an error message if name contains non-alphabetic characters
            return
        new_client = {  # Creating a dictionary to store client details
            "client_id": client_id,
            "name": name,
            "address": address,
            "contact_details": contact_details,
            "budget": budget
        }

        # Save client data to binary file using Pickle
        try:
            with open("clients.pkl", "ab") as file:
                pickle.dump(new_client, file)  # Writing the client data to a binary file using Pickle
            tk.messagebox.showinfo("Success", "Client added successfully!")  # Displaying a success message after adding the client
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add client: {str(e)}")  # Displaying an error message if adding the client fails

    def add_screen(self):
        # Method to create a GUI for adding a new client
        add_window = tk.Toplevel(self.root)  # Creating a new Toplevel window
        add_window.title("Add Client")  # Setting the title of the Toplevel window
        add_window.geometry("400x400")  # Setting the dimensions of the Toplevel window
        add_window.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        # Creating labels and entry fields for entering client details
        client_id_label = tk.Label(add_window, text="Client ID:", font=("Arial", 14), bg="#FFFFFF")
        client_id_label.pack(pady=10)
        client_id_entry = tk.Entry(add_window, font=("Arial", 14))
        client_id_entry.pack()

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

        budget_label = tk.Label(add_window, text="Budget:", font=("Arial", 14), bg="#FFFFFF")
        budget_label.pack(pady=10)
        budget_entry = tk.Entry(add_window, font=("Arial", 14))
        budget_entry.pack()

        # Creating a submit button to add the client
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_client(client_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), budget_entry.get()), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def display_client_details_ui(self):
        # Method to display details of a client
        details_window = tk.Toplevel(self.root)  # Creating a new Toplevel window for displaying client details
        details_window.title("Client Details")  # Setting the title of the Toplevel window
        details_window.geometry("400x300")  # Setting the dimensions of the Toplevel window
        details_window.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        def display_details():
            # Function to retrieve and display client details
            client_id = id_entry.get()  # Getting the client ID entered by the user
            try:
                with open("clients.pkl", "rb") as file:
                    while True:
                        try:
                            client = pickle.load(file)  # Loading client details from the binary file
                            if client["client_id"] == client_id:
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")  # Creating a frame to display client details
                                details_frame.pack(pady=20)

                                details_labels = [
                                    "Client ID:", "Name:", "Address:", "Contact Details:", "Budget:"
                                ]

                                # Displaying client details using labels
                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    # Getting the corresponding value from the client dictionary and displaying it
                                    value_label = tk.Label(details_frame, text=client[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Client Not Found", "No client found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve client details: {str(e)}")

        # Creating labels and entry fields for entering client ID
        id_label = tk.Label(details_window, text="Enter Client ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        # Creating a button to trigger the display of client details
        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def delete_client(self):
        # Method to delete a client
        delete_window = tk.Toplevel(self.root)  # Creating a new Toplevel window for deleting a client
        delete_window.title("Delete Client")  # Setting the title of the Toplevel window
        delete_window.geometry("400x200")  # Setting the dimensions of the Toplevel window
        delete_window.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        def delete():
            # Function to delete the client
            client_id = id_entry.get()  # Getting the client ID entered by the user
            try:
                with open("clients.pkl", "rb") as file:
                    clients = []
                    while True:
                        try:
                            client = pickle.load(file)  # Loading client details from the binary file
                            if client["client_id"] != client_id:
                                clients.append(client)  # Appending clients other than the one to be deleted
                        except EOFError:
                            break

                with open("clients.pkl", "wb") as file:
                    for cl in clients:
                        pickle.dump(cl, file)  # Writing the remaining clients back to the binary file

                tk.messagebox.showinfo("Success", "Client deleted successfully!")  # Displaying a success message after deleting the client
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to delete client: {str(e)}")  # Displaying an error message if deleting the client fails

        # Creating a label and entry field for entering the client ID to be deleted
        id_label = tk.Label(delete_window, text="Enter Client ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        # Creating a button to trigger the deletion of the client
        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_client_ui(self):
        # Method to create the user interface for modifying a client
        modify_input_screen = tk.Toplevel(self.root)  # Creating a new Toplevel window for modifying a client
        modify_input_screen.title("Modify Client")  # Setting the title of the Toplevel window
        modify_input_screen.geometry("300x200")  # Setting the dimensions of the Toplevel window
        modify_input_screen.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        # Creating a label and entry field for entering the client ID
        id_label = tk.Label(modify_input_screen, text="Enter Client ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify client screen
        def open_modify_screen():
            client_id = id_entry.get()  # Getting the client ID entered by the user
            try:
                with open("clients.pkl", "rb") as file:
                    while True:
                        try:
                            client = pickle.load(file)  # Loading client details from the binary file
                            if client["client_id"] == client_id:
                                modify_input_screen.destroy()  # Closing the modify input screen
                                self.modify_client_screen(client)  # Opening the modify client screen with the selected client
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Client Not Found", "No client found with the provided ID.")  # Displaying a message if no client found with the provided ID
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve client details: {str(e)}")  # Displaying an error message if retrieving client details fails

        # Creating a button to submit the client ID and open the modify client screen
        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

        modify_input_screen.mainloop()  # Running the event loop for the modify input screen

    def modify_client_screen(self, client):
        # Method to create the user interface for modifying client details
        modify_screen = tk.Toplevel(self.root)  # Creating a new Toplevel window for modifying client details
        modify_screen.title("Edit Client")  # Setting the title of the Toplevel window
        modify_screen.geometry("400x400")  # Setting the dimensions of the Toplevel window
        modify_screen.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        # Creating labels and entry fields to display and edit client details
        client_id_label = tk.Label(modify_screen, text="Client ID:", font=("Arial", 14), bg="#FFFFFF")
        client_id_label.grid(row=0, column=0, padx=10, pady=5)
        client_id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        client_id_entry.grid(row=0, column=1, padx=10, pady=5)
        client_id_entry.insert(0, client["client_id"])  # Inserting the client ID into the entry field

        name_label = tk.Label(modify_screen, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.grid(row=1, column=0, padx=10, pady=5)
        name_entry = tk.Entry(modify_screen, font=("Arial", 14))
        name_entry.grid(row=1, column=1, padx=10, pady=5)
        name_entry.insert(0, client["name"])

        address_label = tk.Label(modify_screen, text="Address:", font=("Arial", 14), bg="#FFFFFF")
        address_label.grid(row=2, column=0, padx=10, pady=5)
        address_entry = tk.Entry(modify_screen, font=("Arial", 14))
        address_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.insert(0, client["address"])

        contact_label = tk.Label(modify_screen, text="Contact Details:", font=("Arial", 14), bg="#FFFFFF")
        contact_label.grid(row=3, column=0, padx=10, pady=5)
        contact_entry = tk.Entry(modify_screen, font=("Arial", 14))
        contact_entry.grid(row=3, column=1, padx=10, pady=5)
        contact_entry.insert(0, client["contact_details"])

        budget_label = tk.Label(modify_screen, text="Budget:", font=("Arial", 14), bg="#FFFFFF")
        budget_label.grid(row=4, column=0, padx=10, pady=5)
        budget_entry = tk.Entry(modify_screen, font=("Arial", 14))
        budget_entry.grid(row=4, column=1, padx=10, pady=5)
        budget_entry.insert(0, client["budget"])

        # Function to update the client details
        def update_client():
            updated_client = {
                "client_id": client_id_entry.get(),
                "name": name_entry.get(),
                "address": address_entry.get(),
                "contact_details": contact_entry.get(),
                "budget": budget_entry.get()
            }

            try:
                # Open the file in read mode
                with open("clients.pkl", "rb") as file:
                    clients = []
                    # Load existing client details
                    while True:
                        try:
                            cl = pickle.load(file)
                            # Check if the loaded client ID matches the ID of the client being updated
                            if cl["client_id"] == client["client_id"]:
                                # Append the updated client details to the list
                                clients.append(updated_client)
                            else:
                                clients.append(cl)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("clients.pkl", "wb") as file:
                    # Write the updated client details back to the file
                    for cl in clients:
                        pickle.dump(cl, file)

                tk.messagebox.showinfo("Success", "Client details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update client details: {str(e)}")

        update_button = tk.Button(modify_screen, text="Update", command=update_client, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()
