import tkinter as tk
from tkinter import messagebox
import pickle

class Employee:
    def __init__(self, root):
        # Constructor to initialize the root window for the employee section
        self.root = root
        self.root.title("Employee Section")  # Setting the title of the root window
        self.root.geometry("500x500")  # Setting the dimensions of the root window
        self.root.configure(bg="#FFFFFF")  # Setting the background color of the root window

    def add_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # Method to add a new employee
        # Validate Employee ID
        if not employee_id.isdigit():
            tk.messagebox.showerror("Error", "Employee ID must be numeric.")  # Displaying an error message if employee ID is not numeric
            return
        # Validate Name
        if not name.strip().isalpha():
            tk.messagebox.showerror("Error", "Name must contain only alphabetic characters.")  # Displaying an error message if name contains non-alphabetic characters
        
        new_employee = {
            "name": name,
            "employee_id": employee_id,
            "department": department,
            "job_title": job_title,
            "basic_salary": basic_salary,
            "age": age,
            "date_of_birth": date_of_birth,
            "passport_details": passport_details
        }

        # Save employee data to binary file using Pickle
        try:
            with open("employees.pkl", "ab") as file:
                pickle.dump(new_employee, file)
            tk.messagebox.showinfo("Success", "Employee added successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to add employee: {str(e)}")
    # Method to create the user interface for adding a new employee
    def add_screen(self):
         # Creating a new Toplevel window for adding an employee
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")
        add_window.geometry("400x400")
        add_window.configure(bg="#FFFFFF")
        # Creating labels and entry fields for entering employee details
        name_label = tk.Label(add_window, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.pack(pady=10)
        name_entry = tk.Entry(add_window, font=("Arial", 14))
        name_entry.pack()

        id_label = tk.Label(add_window, text="Employee ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(add_window, font=("Arial", 14))
        id_entry.pack()

        department_label = tk.Label(add_window, text="Department:", font=("Arial", 14), bg="#FFFFFF")
        department_label.pack(pady=10)
        department_entry = tk.Entry(add_window, font=("Arial", 14))
        department_entry.pack()

        job_label = tk.Label(add_window, text="Job Title:", font=("Arial", 14), bg="#FFFFFF")
        job_label.pack(pady=10)
        job_entry = tk.Entry(add_window, font=("Arial", 14))
        job_entry.pack()

        salary_label = tk.Label(add_window, text="Basic Salary:", font=("Arial", 14), bg="#FFFFFF")
        salary_label.pack(pady=10)
        salary_entry = tk.Entry(add_window, font=("Arial", 14))
        salary_entry.pack()

        age_label = tk.Label(add_window, text="Age:", font=("Arial", 14), bg="#FFFFFF")
        age_label.pack(pady=10)
        age_entry = tk.Entry(add_window, font=("Arial", 14))
        age_entry.pack()

        dob_label = tk.Label(add_window, text="Date of Birth:", font=("Arial", 14), bg="#FFFFFF")
        dob_label.pack(pady=10)
        dob_entry = tk.Entry(add_window, font=("Arial", 14))
        dob_entry.pack()

        passport_label = tk.Label(add_window, text="Passport Details:", font=("Arial", 14), bg="#FFFFFF")
        passport_label.pack(pady=10)
        passport_entry = tk.Entry(add_window, font=("Arial", 14))
        passport_entry.pack()
        # Creating a button to submit the employee details
        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_employee(name_entry.get(), id_entry.get(), department_entry.get(), job_entry.get(), salary_entry.get(), age_entry.get(), dob_entry.get(), passport_entry.get()), width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def display_employee_details_ui(self):
        # Method to create the user interface for displaying employee details
        details_window = tk.Toplevel(self.root)  # Creating a new Toplevel window for displaying employee details
        details_window.title("Employee Details")  # Setting the title of the Toplevel window
        details_window.geometry("400x300")  # Setting the dimensions of the Toplevel window
        details_window.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        def display_details():
            employee_id = id_entry.get()
            try:
                with open("employees.pkl", "rb") as file:
                    while True:
                        try:
                            employee = pickle.load(file)
                            if employee["employee_id"] == employee_id:
                                details_frame = tk.Frame(details_window, bg="#FFFFFF")
                                details_frame.pack(pady=20)

                                details_labels = [
                                    "Name:", "Employee ID:", "Department:", "Job Title:",
                                    "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:"
                                ]

                                for i, label_text in enumerate(details_labels):
                                    label = tk.Label(details_frame, text=label_text, font=("Arial", 12), bg="#FFFFFF")
                                    label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

                                    value_label = tk.Label(details_frame, text=employee[label_text[:-1].lower().replace(" ", "_")], font=("Arial", 12), bg="#FFFFFF")
                                    value_label.grid(row=i, column=1, sticky="w", padx=10, pady=5)

                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Employee Not Found", "No employee found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve employee details: {str(e)}")

        id_label = tk.Label(details_window, text="Enter Employee ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(details_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(details_window, text="Display Details", command=display_details, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def delete_employee(self):
        # Method to delete an employee
        delete_window = tk.Toplevel(self.root)  # Creating a new Toplevel window for deleting an employee
        delete_window.title("Delete Employee")  # Setting the title of the Toplevel window
        delete_window.geometry("400x200")  # Setting the dimensions of the Toplevel window
        delete_window.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window

        def delete():
            employee_id = id_entry.get()
            try:
                with open("employees.pkl", "rb") as file:
                    employees = []
                    while True:
                        try:
                            employee = pickle.load(file)
                            if employee["employee_id"] != employee_id:
                                employees.append(employee)
                        except EOFError:
                            break

                with open("employees.pkl", "wb") as file:
                    for emp in employees:
                        pickle.dump(emp, file)

                tk.messagebox.showinfo("Success", "Employee deleted successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to delete employee: {str(e)}")

        id_label = tk.Label(delete_window, text="Enter Employee ID to Delete:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(delete_window, font=("Arial", 14))
        id_entry.pack()

        submit_button = tk.Button(delete_window, text="Delete", command=delete, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

    def modify_employee_ui(self):
        # Method to create the user interface for modifying employee details
        modify_input_screen = tk.Toplevel(self.root)  # Creating a new Toplevel window for modifying employee details
        modify_input_screen.title("Modify Employee")  # Setting the title of the Toplevel window
        modify_input_screen.geometry("300x200")  # Setting the dimensions of the Toplevel window
        modify_input_screen.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window
        

        id_label = tk.Label(modify_input_screen, text="Enter Employee ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.pack(pady=10)
        id_entry = tk.Entry(modify_input_screen, font=("Arial", 14))
        id_entry.pack()

        # Function to open the modify employee screen
        def open_modify_screen():
            employee_id = id_entry.get()
            try:
                with open("employees.pkl", "rb") as file:
                    while True:
                        try:
                            employee = pickle.load(file)
                            if employee["employee_id"] == employee_id:
                                modify_input_screen.destroy()
                                self.modify_employee_screen(employee)
                                return
                        except EOFError:
                            break
                tk.messagebox.showinfo("Employee Not Found", "No employee found with the provided ID.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to retrieve employee details: {str(e)}")

        submit_button = tk.Button(modify_input_screen, text="Submit", command=open_modify_screen, width=20, bg="yellow", fg="black", font=("Arial", 14))
        submit_button.pack(pady=20)

        modify_input_screen.mainloop()

    def modify_employee_screen(self, employee):
        # Method to create the user interface for modifying employee details
        modify_screen = tk.Toplevel(self.root)  # Creating a new Toplevel window for modifying employee details
        modify_screen.title("Edit Employee")  # Setting the title of the Toplevel window
        modify_screen.geometry("400x400")  # Setting the dimensions of the Toplevel window
        modify_screen.configure(bg="#FFFFFF")  # Setting the background color of the Toplevel window
    
        # Filling the entries with employee details
        name_label = tk.Label(modify_screen, text="Name:", font=("Arial", 14), bg="#FFFFFF")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(modify_screen, font=("Arial", 14))
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        name_entry.insert(0, employee["name"])

        id_label = tk.Label(modify_screen, text="Employee ID:", font=("Arial", 14), bg="#FFFFFF")
        id_label.grid(row=1, column=0, padx=10, pady=5)
        id_entry = tk.Entry(modify_screen, font=("Arial", 14))
        id_entry.grid(row=1, column=1, padx=10, pady=5)
        id_entry.insert(0, employee["employee_id"])

        department_label = tk.Label(modify_screen, text="Department:", font=("Arial", 14), bg="#FFFFFF")
        department_label.grid(row=2, column=0, padx=10, pady=5)
        department_entry = tk.Entry(modify_screen, font=("Arial", 14))
        department_entry.grid(row=2, column=1, padx=10, pady=5)
        department_entry.insert(0, employee["department"])

        job_label = tk.Label(modify_screen, text="Job Title:", font=("Arial", 14), bg="#FFFFFF")
        job_label.grid(row=3, column=0, padx=10, pady=5)
        job_entry = tk.Entry(modify_screen, font=("Arial", 14))
        job_entry.grid(row=3, column=1, padx=10, pady=5)
        job_entry.insert(0, employee["job_title"])

        salary_label = tk.Label(modify_screen, text="Basic Salary:", font=("Arial", 14), bg="#FFFFFF")
        salary_label.grid(row=4, column=0, padx=10, pady=5)
        salary_entry = tk.Entry(modify_screen, font=("Arial", 14))
        salary_entry.grid(row=4, column=1, padx=10, pady=5)
        salary_entry.insert(0, employee["basic_salary"])

        age_label = tk.Label(modify_screen, text="Age:", font=("Arial", 14), bg="#FFFFFF")
        age_label.grid(row=5, column=0, padx=10, pady=5)
        age_entry = tk.Entry(modify_screen, font=("Arial", 14))
        age_entry.grid(row=5, column=1, padx=10, pady=5)
        age_entry.insert(0, employee["age"])

        dob_label = tk.Label(modify_screen, text="Date of Birth:", font=("Arial", 14), bg="#FFFFFF")
        dob_label.grid(row=6, column=0, padx=10, pady=5)
        dob_entry = tk.Entry(modify_screen, font=("Arial", 14))
        dob_entry.grid(row=6, column=1, padx=10, pady=5)
        dob_entry.insert(0, employee["date_of_birth"])

        passport_label = tk.Label(modify_screen, text="Passport Details:", font=("Arial", 14), bg="#FFFFFF")
        passport_label.grid(row=7, column=0, padx=10, pady=5)
        passport_entry = tk.Entry(modify_screen, font=("Arial", 14))
        passport_entry.grid(row=7, column=1, padx=10, pady=5)
        passport_entry.insert(0, employee["passport_details"])

        # Function to update the employee details
        # Function to update the employee details
        def update_employee():
            updated_employee = {
                "name": name_entry.get(),
                "employee_id": id_entry.get(),
                "department": department_entry.get(),
                "job_title": job_entry.get(),
                "basic_salary": salary_entry.get(),
                "age": age_entry.get(),
                "date_of_birth": dob_entry.get(),
                "passport_details": passport_entry.get()
            }

            try:
                # Open the file in read mode
                with open("employees.pkl", "rb") as file:
                    employees = []
                    # Load existing employee details
                    while True:
                        try:
                            employee = pickle.load(file)
                            # Check if the loaded employee ID matches the ID of the employee being updated
                            if employee["employee_id"] == employee["employee_id"]:
                                # Append the updated employee details to the list
                                employees.append(updated_employee)
                            else:
                                employees.append(employee)
                        except EOFError:
                            break

                # Open the file in write mode
                with open("employees.pkl", "wb") as file:
                    # Write the updated employee details back to the file
                    for emp in employees:
                        pickle.dump(emp, file)

                tk.messagebox.showinfo("Success", "Employee details updated successfully!")
                modify_screen.destroy()  # Close the modify screen after successful update
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to update employee details: {str(e)}")

        update_button = tk.Button(modify_screen, text="Update", command=update_employee, width=20, bg="yellow", fg="black", font=("Arial", 14))
        update_button.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

        modify_screen.mainloop()
