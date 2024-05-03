import tkinter as tk
from employee import Employee  # Importing Employee class from employee module
from guest import Guest  # Importing Guest class from guest module
from client import Client  # Importing Client class from client module
from event import Event  # Importing Event class from event module
from venue import Venue  # Importing Venue class from venue module
from supplier import Supplier  # Importing Supplier class from supplier module

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Prime")  # Setting up the root window
        self.root.geometry("500x500")
        self.root.configure(bg="#FFFFFF")

        self.label = tk.Label(root, text="Event Prime", font=("Arial", 24), bg="#FFFFFF")
        self.label.pack(pady=20)

        self.menu_button = tk.Button(root, text="Menu", command=self.show_menu, width=20, bg="#FFA500", fg="black", font=("Arial", 14))
        self.menu_button.pack()

        self.current_menu = None

    # Method to display the main menu
    def show_menu(self):
        self.menu_button.pack_forget()  # Remove the menu button from the screen

        # Creating buttons for various menu options
        self.employee_button = tk.Button(root, text="Employee", command=self.show_employee_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.employee_button.pack(pady=10)

        self.guest_button = tk.Button(root, text="Guest", command=self.show_guest_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.guest_button.pack(pady=10)

        self.supplier_button = tk.Button(root, text="Supplier", command=self.show_supplier_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.supplier_button.pack(pady=10)

        self.event_button = tk.Button(root, text="Event", command=self.show_event_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.event_button.pack(pady=10)

        self.venue_button = tk.Button(root, text="Venue", command=self.show_venue_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.venue_button.pack(pady=10)

        self.client_button = tk.Button(root, text="Client", command=self.show_client_menu, width=20, bg="#FF4500", fg="black", font=("Arial", 14))
        self.client_button.pack(pady=10)

    # Method to clear the current menu
    def clear_current_menu(self):
        if self.current_menu:
            self.current_menu.destroy()

    # Method to display the employee menu
    def show_employee_menu(self):
        self.clear_current_menu()
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        # Creating buttons for employee operations
        add_button = tk.Button(self.current_menu, text="Add Employee", command=self.open_employee_add_screen, width=15, bg="yellow", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Employee", command=self.open_employee_modify_screen, width=15, bg="yellow", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Employee", command=self.open_employee_display_screen, width=15, bg="yellow", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Employee", command=self.open_employee_delete_screen, width=15, bg="yellow", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    # Method to open the employee addition screen
    def open_employee_add_screen(self):
        employee = Employee(self.root)
        employee.add_screen()
    
    # Method to open the employee display screen
    def open_employee_display_screen(self):
        employee = Employee(self.root)
        employee.display_employee_details_ui()

    # Method to open the employee deletion screen
    def open_employee_delete_screen(self):
        employee = Employee(self.root)
        employee.delete_employee()

    # Method to open the employee modification screen
    def open_employee_modify_screen(self):
        employee = Employee(self.root)
        employee.modify_employee_ui()

    def show_guest_menu(self):
        # Clear any existing menu
        self.clear_current_menu()
        # Create a new frame for the guest menu
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        # Create buttons for various guest operations
        add_button = tk.Button(self.current_menu, text="Add Guest", command=self.open_guest_add_screen, width=15, bg="pink", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Guest", command=self.open_guest_modify_screen, width=15, bg="pink", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Guest", command=self.open_guest_display_screen, width=15, bg="pink", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Guest", command=self.open_guest_delete_screen, width=15, bg="pink", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    def open_guest_add_screen(self):
        # Instantiate Guest class and open the add screen
        guest = Guest(self.root)
        guest.add_screen()

    def open_guest_display_screen(self):
        # Instantiate Guest class and open the display screen
        guest = Guest(self.root)
        guest.display_guest_details_ui()

    def open_guest_delete_screen(self):
        # Instantiate Guest class and open the delete screen
        guest = Guest(self.root)
        guest.delete_guest()

    def open_guest_modify_screen(self):
        # Instantiate Guest class and open the modify screen
        guest = Guest(self.root)
        guest.modify_guest_ui()

    def show_supplier_menu(self):
        self.clear_current_menu()
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        add_button = tk.Button(self.current_menu, text="Add Supplier", command=self.open_supplier_add_screen, width=15, bg="green", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Supplier", command=self.open_supplier_modify_screen, width=15, bg="green", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Supplier", command=self.open_supplier_display_screen, width=15, bg="green", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Supplier", command=self.open_supplier_delete_screen, width=15, bg="green", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    def open_supplier_add_screen(self):
        supplier = Supplier(self.root)
        supplier.add_screen()

    def open_supplier_display_screen(self):
        supplier = Supplier(self.root)
        supplier.display_supplier_details_ui()

    def open_supplier_delete_screen(self):
        supplier = Supplier(self.root)
        supplier.delete_supplier()

    def open_supplier_modify_screen(self):
        supplier = Supplier(self.root)
        supplier.modify_supplier_ui()

    def show_event_menu(self):
        self.clear_current_menu()
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        add_button = tk.Button(self.current_menu, text="Add Event", command=self.open_event_add_screen, width=15, bg="brown", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Event", command=self.open_event_modify_screen, width=15, bg="brown", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Event", command=self.open_event_display_screen, width=15, bg="brown", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Event", command=self.open_event_delete_screen, width=15, bg="brown", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    def open_event_add_screen(self):
        event = Event(self.root)
        event.add_screen()

    def open_event_display_screen(self):
        event = Event(self.root)
        event.display_event_details_ui()

    def open_event_delete_screen(self):
        event = Event(self.root)
        event.delete_event()

    def open_event_modify_screen(self):
        event = Event(self.root)
        event.modify_event_ui()

    def show_venue_menu(self):
        self.clear_current_menu()
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        add_button = tk.Button(self.current_menu, text="Add Venue", command=self.open_venue_add_screen, width=15, bg="purple", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Venue", command=self.open_venue_modify_screen, width=15, bg="purple", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Venue", command=self.open_venue_display_screen, width=15, bg="purple", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Venue", command=self.open_venue_delete_screen, width=15, bg="purple", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    def open_venue_add_screen(self):
        venue = Venue(self.root)
        venue.add_screen()

    def open_venue_display_screen(self):
        venue = Venue(self.root)
        venue.display_venue_details_ui()

    def open_venue_delete_screen(self):
        venue = Venue(self.root)
        venue.delete_venue()

    def open_venue_modify_screen(self):
        venue = Venue(self.root)
        venue.modify_venue_ui()

    def show_client_menu(self):
        self.clear_current_menu()
        self.current_menu = tk.Frame(self.root, bg="#FFFFFF")
        self.current_menu.pack(pady=20)

        add_button = tk.Button(self.current_menu, text="Add Client", command=self.open_client_add_screen, width=15, bg="gray", fg="black", font=("Arial", 14))
        add_button.grid(row=0, column=0, padx=10)

        modify_button = tk.Button(self.current_menu, text="Modify Client", command=self.open_client_modify_screen, width=15, bg="gray", fg="black", font=("Arial", 14))
        modify_button.grid(row=0, column=1, padx=10)

        display_button = tk.Button(self.current_menu, text="Display Client", command=self.open_client_display_screen, width=15, bg="gray", fg="black", font=("Arial", 14))
        display_button.grid(row=0, column=2, padx=10)

        delete_button = tk.Button(self.current_menu, text="Delete Client", command=self.open_client_delete_screen, width=15, bg="gray", fg="black", font=("Arial", 14))
        delete_button.grid(row=0, column=3, padx=10)

    def open_client_add_screen(self):
        client = Client(self.root)
        client.add_screen()

    def open_client_display_screen(self):
        client = Client(self.root)
        client.display_client_details_ui()

    def open_client_delete_screen(self):
        client = Client(self.root)
        client.delete_client()

    def open_client_modify_screen(self):
        client = Client(self.root)
        client.modify_client_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
