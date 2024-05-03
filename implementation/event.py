import tkinter as tk
from tkinter import messagebox
import pickle

class Event:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Section")
        self.root.geometry("500x500")
        self.root.configure(bg="#FFFFFF")

    def add_event(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company_name, invoice):
        # Validate Event ID
        if not event_id.isdigit():
            tk.messagebox.showerror("Error", "Event ID must be numeric.")
            return
        #dictionay for employee fields
        new_event = {
            "event_id": event_id,
            "event_type": event_type,
            "theme": theme,
            "date": date,
            "time": time,
            "duration": duration,
            "venue_address": venue_address,
            "client_id": client_id,
            "guest_list": guest_list,
            "company_name": company_name,
            "invoice": invoice
        }

        # Save event data to binary file using Pickle
        try:
            with open("events.pkl", "ab") as file:
                pickle.dump(new_event, file)
            tk.messagebox.showinfo("Success", "Event added successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add event: {str(e)}")

    def add_screen(self):
        # Method to create the UI for adding a new event
        
        # Create a new window for adding an event
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Event")
        add_window.geometry("400x650")
        add_window.configure(bg="#FFFFFF")

        # Create a canvas to enable scrolling
        canvas = tk.Canvas(add_window, bg="#FFFFFF")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar for the canvas
        scrollbar = tk.Scrollbar(add_window, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure canvas to use scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas
        frame = tk.Frame(canvas, bg="#FFFFFF")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Define fields for event details
        fields = [
            ("Event ID:", 5), ("Event Type:", 6), ("Theme:", 7), ("Date:", 8), ("Time:", 9),
            ("Duration:", 10), ("Venue Address:", 11), ("Client ID:", 12), ("Guest List:", 13),
            ("Company Name:", 14), ("Invoice:", 15)
        ]

        for label_text, row in fields:
            # Loop through each field and its corresponding row number
            
            # Create a label for the field
            label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="#FFFFFF")
            label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

            # Create an entry field for user input
            entry = tk.Entry(frame, font=("Arial", 14))
            entry.grid(row=row, column=1, padx=10, pady=5)

        submit_button = tk.Button(frame, text="Submit", command=lambda: self.add_event(
            entry_list[0].get(),  # Get value from event_id_entry
            entry_list[1].get(),  # Get value from event_type_entry
            entry_list[2].get(),  # Get value from theme_entry
            entry_list[3].get(),  # Get value from date_entry
            entry_list[4].get(),  # Get value from time_entry
            entry_list[5].get(),  # Get value from duration_entry
            entry_list[6].get(),  # Get value from venue_entry
            entry_list[7].get(),  # Get value from client_entry
            entry_list[8].get(),  # Get value from guest_entry
            entry_list[9].get(),  # Get value from compnay_entry
            entry_list[10].get()  # Get value from invoice_entry
        ), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.grid(row=16, columnspan=2, pady=20)

        entry_list = []
        for i in range(len(fields)):
            entry_list.append(tk.Entry(frame, font=("Arial", 14)))
            entry_list[i].grid(row=fields[i][1], column=1, padx=10, pady=5)

    def display_event_details_ui(self):
        # Create a new window to display event details
        details_window = tk.Toplevel(self.root)
        details_window.title("Event Details")
        details_window.geometry("400x300")
        details_window.configure(bg="#FFFFFF")

        # Function to display event details
        def display_details():
            # Retrieve the event ID entered by the user
            event_id = id_entry.get()
            try:
                # Open the events file in read mode
                with open("events.pkl", "rb") as file:
                    while True:
                        try:
                            # Load each event from the file
                            event = pickle.load(file)
                            # Check if the event ID matches the one entered by the user
                            if event["event_id"] == event_id:
                                # Create a frame to display event details
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")
                                details_frame.pack(pady=20)

                                # Define labels for event details
                                details_labels = [
                                    "Event ID:", "Event Type:", "Theme:", "Date:", "Time:",
                                    "Duration:", "Venue Address:", "Client ID:", "Guest List:",
                                    "Company Name:", "Invoice:"
                                ]

                                # Display event details in labels
                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    # Retrieve the corresponding value from the event dictionary and display it
                                    value_label = tk.Label(details_frame, text=event[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                # If no event is found with the provided ID, show a message
                tk.messagebox.showinfo("Event Not Found", "No event found with the provided ID.")
            except Exception as e:
                # If an error occurs during retrieval, show an error message
                tk.messagebox.showerror("Error", f"Failed to retrieve event details: {str(e)}")

        # Label and entry field for entering the event ID
        id_label = tk.Label(details_window, text="Enter Event ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=5)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        # Button to trigger the display of event details
        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def delete_event(self):
        # Create a new window for deleting an event
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Event")
        delete_window.geometry("400x200")
        delete_window.configure(bg="#FFFFFF")

        # Function to delete an event
        def delete():
            # Get the event ID entered by the user
            event_id = id_entry.get()
            try:
                # Open the events file in read mode
                with open("events.pkl", "rb") as file:
                    events = []
                    # Iterate through each event in the file
                    while True:
                        try:
                            event = pickle.load(file)
                            # Check if the event ID does not match the one to be deleted
                            if event["event_id"] != event_id:
                                # If not, add the event to the list of events to keep
                                events.append(event)
                        except EOFError:
                            break

                # Open the events file in write mode to update it
                with open("events.pkl", "wb") as file:
                    # Write all events except the one to be deleted back to the file
                    for ev in events:
                        pickle.dump(ev, file)

                # Show a success message after deleting the event
                tk.messagebox.showinfo("Success", "Event deleted successfully!")
            except Exception as e:
                # Show an error message if deletion fails
                tk.messagebox.showerror("Error", f"Failed to delete event: {str(e)}")

        # Label and entry field for entering the event ID to be deleted
        id_label = tk.Label(delete_window, text="Enter Event ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        # Button to trigger the event deletion function
        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_event_ui(self):
        modify_input_screen = tk.Toplevel(self.root)
        modify_input_screen.title("Modify Event")
        modify_input_screen.geometry("300x200")
        modify_input_screen.configure(bg="#FFFFFF")

        id_label = tk.Label(modify_input_screen, text="Enter Event ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=5)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify event screen
        def open_modify_screen():
            event_id = id_entry.get()
            try:
                with open("events.pkl", "rb") as file:
                    while True:
                        try:
                            event = pickle.load(file)
                            if event["event_id"] == event_id:
                                modify_input_screen.destroy()
                                self.modify_event_screen(event)
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Event Not Found", "No event found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve event details: {str(e)}")

        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_event_screen(self, event):
        modify_screen = tk.Toplevel(self.root)
        modify_screen.title("Edit Event")
        modify_screen.geometry("400x600")
        modify_screen.configure(bg="#FFFFFF")

        # Filling the entries with event details
        event_id_label = tk.Label(modify_screen, text="Event ID:", font=("Arial", 14), bg="#FFFFFF")
        event_id_label.grid(row=0, column=0, padx=10, pady=5)
        event_id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        event_id_entry.grid(row=0, column=1, padx=10, pady=5)
        event_id_entry.insert(0, event["event_id"])

        event_type_label = tk.Label(modify_screen, text="Event Type:", font=("Arial", 14), bg="#FFFFFF")
        event_type_label.grid(row=1, column=0, padx=10, pady=5)
        event_type_entry = tk.Entry(modify_screen, font=("Arial", 14))
        event_type_entry.grid(row=1, column=1, padx=10, pady=5)
        event_type_entry.insert(0, event["event_type"])

        theme_label = tk.Label(modify_screen, text="Theme:", font=("Arial", 14), bg="#FFFFFF")
        theme_label.grid(row=2, column=0, padx=10, pady=5)
        theme_entry = tk.Entry(modify_screen, font=("Arial", 14))
        theme_entry.grid(row=2, column=1, padx=10, pady=5)
        theme_entry.insert(0, event["theme"])

        date_label = tk.Label(modify_screen, text="Date:", font=("Arial", 14), bg="#FFFFFF")
        date_label.grid(row=3, column=0, padx=10, pady=5)
        date_entry = tk.Entry(modify_screen, font=("Arial", 14))
        date_entry.grid(row=3, column=1, padx=10, pady=5)
        date_entry.insert(0, event["date"])

        time_label = tk.Label(modify_screen, text="Time:", font=("Arial", 14), bg="#FFFFFF")
        time_label.grid(row=4, column=0, padx=10, pady=5)
        time_entry = tk.Entry(modify_screen, font=("Arial", 14))
        time_entry.grid(row=4, column=1, padx=10, pady=5)
        time_entry.insert(0, event["time"])

        duration_label = tk.Label(modify_screen, text="Duration:", font=("Arial", 14), bg="#FFFFFF")
        duration_label.grid(row=5, column=0, padx=10, pady=5)
        duration_entry = tk.Entry(modify_screen, font=("Arial", 14))
        duration_entry.grid(row=5, column=1, padx=10, pady=5)
        duration_entry.insert(0, event["duration"])

        venue_label = tk.Label(modify_screen, text="Venue Address:", font=("Arial", 14), bg="#FFFFFF")
        venue_label.grid(row=6, column=0, padx=10, pady=5)
        venue_entry = tk.Entry(modify_screen, font=("Arial", 14))
        venue_entry.grid(row=6, column=1, padx=10, pady=5)
        venue_entry.insert(0, event["venue_address"])

        client_label = tk.Label(modify_screen, text="Client ID:", font=("Arial", 14), bg="#FFFFFF")
        client_label.grid(row=7, column=0, padx=10, pady=5)
        client_entry = tk.Entry(modify_screen, font=("Arial", 14))
        client_entry.grid(row=7, column=1, padx=10, pady=5)
        client_entry.insert(0, event["client_id"])

        guest_label = tk.Label(modify_screen, text="Guest List:", font=("Arial", 14), bg="#FFFFFF")
        guest_label.grid(row=8, column=0, padx=10, pady=5)
        guest_entry = tk.Entry(modify_screen, font=("Arial", 14))
        guest_entry.grid(row=8, column=1, padx=10, pady=5)
        guest_entry.insert(0, event["guest_list"])

        company_label = tk.Label(modify_screen, text="Company Name:", font=("Arial", 14), bg="#FFFFFF")
        company_label.grid(row=9, column=0, padx=10, pady=5)
        company_entry = tk.Entry(modify_screen, font=("Arial", 14))
        company_entry.grid(row=9, column=1, padx=10, pady=5)
        company_entry.insert(0, event["company_name"])

        invoice_label = tk.Label(modify_screen, text="Invoice:", font=("Arial", 14), bg="#FFFFFF")
        invoice_label.grid(row=10, column=0, padx=10, pady=5)
        invoice_entry = tk.Entry(modify_screen, font=("Arial", 14))
        invoice_entry.grid(row=10, column=1, padx=10, pady=5)
        invoice_entry.insert(0, event["invoice"])

        # Function to update the event details
        def update_event():
            updated_event = {
                "event_id": event_id_entry.get(),
                "event_type": event_type_entry.get(),
                "theme": theme_entry.get(),
                "date": date_entry.get(),
                "time": time_entry.get(),
                "duration": duration_entry.get(),
                "venue_address": venue_entry.get(),
                "client_id": client_entry.get(),
                "guest_list": guest_entry.get(),
                "company_company": company_entry.get(),
                "invoice": invoice_entry.get()
            }

            try:
                # Open the file in read mode
                with open("events.pkl", "rb") as file:
                    events = []
                    # Load existing event details
                    while True:
                        try:
                            ev = pickle.load(file)
                            # Check if the loaded event ID matches the ID of the event being updated
                            if ev["event_id"] == event["event_id"]:
                                # Append the updated event details to the list
                                events.append(updated_event)
                            else:
                                events.append(ev)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("events.pkl", "wb") as file:
                    # Write the updated event details back to the file
                    for ev in events:
                        pickle.dump(ev, file)

                tk.messagebox.showinfo("Success", "Event details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update event details: {str(e)}")

        update_button = tk.Button(modify_screen, text="Update", command=update_event, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Event(root)
    app.add_screen()
    root.mainloop()
