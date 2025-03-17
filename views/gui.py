import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class GUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Travel Agent Record Management System")
        self.root.geometry("800x600")
        
        self.setup_gui()
    
    def setup_gui(self):
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Create tabs for different record types
        self.client_frame = ttk.Frame(self.notebook)
        self.airline_frame = ttk.Frame(self.notebook)
        self.flight_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.client_frame, text='Clients')
        self.notebook.add(self.airline_frame, text='Airlines')
        self.notebook.add(self.flight_frame, text='Flights')
        
        self.setup_client_tab()
        self.setup_airline_tab()
        self.setup_flight_tab()
    
    def setup_client_tab(self):
        # Client form
        form_frame = ttk.LabelFrame(self.client_frame, text="Client Information")
        form_frame.pack(fill='x', padx=5, pady=5)
        
        # Add ID field first (read-only)
        ttk.Label(form_frame, text="ID").grid(row=0, column=0, padx=5, pady=2)
        id_entry = ttk.Entry(form_frame, state='readonly')
        id_entry.grid(row=0, column=1, padx=5, pady=2)
        
        # Create entry fields
        fields = ['name', 'address_line1', 'address_line2', 'address_line3', 
                 'city', 'state', 'zip_code', 'country', 'phone_number']
        self.client_entries = {'id': id_entry}
        
        for i, field in enumerate(fields, start=1):
            ttk.Label(form_frame, text=field.replace('_', ' ').title()).grid(row=i, column=0, padx=5, pady=2)
            self.client_entries[field] = ttk.Entry(form_frame)
            self.client_entries[field].grid(row=i, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(self.client_frame)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Create", command=self.create_client).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_client).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_client).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Search", command=self.search_client).pack(side='left', padx=5)
    
    def setup_airline_tab(self):
        # Airline form
        form_frame = ttk.LabelFrame(self.airline_frame, text="Airline Information")
        form_frame.pack(fill='x', padx=5, pady=5)
        
        # Add ID field first (read-only)
        ttk.Label(form_frame, text="ID").grid(row=0, column=0, padx=5, pady=2)
        self.airline_id_entry = ttk.Entry(form_frame, state='readonly')
        self.airline_id_entry.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(form_frame, text="Company Name").grid(row=1, column=0, padx=5, pady=2)
        self.airline_entry = ttk.Entry(form_frame)
        self.airline_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(self.airline_frame)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Create", command=self.create_airline).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_airline).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_airline).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Search", command=self.search_airline).pack(side='left', padx=5)
    
    def setup_flight_tab(self):
        # Flight form
        form_frame = ttk.LabelFrame(self.flight_frame, text="Flight Information")
        form_frame.pack(fill='x', padx=5, pady=5)
        
        # Add ID field first (read-only)
        ttk.Label(form_frame, text="ID").grid(row=0, column=0, padx=5, pady=2)
        id_entry = ttk.Entry(form_frame, state='readonly')
        id_entry.grid(row=0, column=1, padx=5, pady=2)
        
        # Create entry fields
        fields = ['client_id', 'airline_id', 'start_city', 'end_city']
        self.flight_entries = {'id': id_entry}
        
        for i, field in enumerate(fields, start=1):
            ttk.Label(form_frame, text=field.replace('_', ' ').title()).grid(row=i, column=0, padx=5, pady=2)
            self.flight_entries[field] = ttk.Entry(form_frame)
            self.flight_entries[field].grid(row=i, column=1, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(self.flight_frame)
        button_frame.pack(fill='x', padx=5, pady=5)
        
        ttk.Button(button_frame, text="Create", command=self.create_flight).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Update", command=self.update_flight).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_flight).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Search", command=self.search_flight).pack(side='left', padx=5)
    
    def create_client(self):
        data = {k: v.get() for k, v in self.client_entries.items() if k != 'id'}
        try:
            self.controller.create_record('client', data)
            messagebox.showinfo("Success", "Client record created successfully!")
            self.clear_client_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def create_airline(self):
        data = {'company_name': self.airline_entry.get()}
        try:
            self.controller.create_record('airline', data)
            messagebox.showinfo("Success", "Airline record created successfully!")
            self.clear_airline_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def create_flight(self):
        data = {k: v.get() for k, v in self.flight_entries.items() if k != 'id'}
        data['date'] = datetime.now()
        try:
            self.controller.create_record('flight', data)
            messagebox.showinfo("Success", "Flight record created successfully!")
            self.clear_flight_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_client(self):
        data = {k: v.get() for k, v in self.client_entries.items()}
        try:
            record_id = int(data['id'])
            if self.controller.update_record(record_id, data):
                messagebox.showinfo("Success", "Client record updated successfully!")
                self.clear_client_form()
            else:
                messagebox.showerror("Error", "Record not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_airline(self):
        try:
            record_id = int(self.airline_id_entry.get())
            data = {
                'id': record_id,
                'company_name': self.airline_entry.get()
            }
            if self.controller.update_record(record_id, data):
                messagebox.showinfo("Success", "Airline record updated successfully!")
                self.clear_airline_form()
            else:
                messagebox.showerror("Error", "Record not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_flight(self):
        data = {k: v.get() for k, v in self.flight_entries.items()}
        try:
            record_id = int(data['id'])
            # Convert client_id and airline_id to integers
            data['client_id'] = int(data['client_id'])
            data['airline_id'] = int(data['airline_id'])
            if self.controller.update_record(record_id, data):
                messagebox.showinfo("Success", "Flight record updated successfully!")
                self.clear_flight_form()
            else:
                messagebox.showerror("Error", "Record not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid ID numbers")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_client(self):
        try:
            record_id = int(self.client_entries['id'].get())
            self.controller.delete_record(record_id)
            messagebox.showinfo("Success", "Client record deleted successfully!")
            self.clear_client_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_airline(self):
        try:
            record_id = int(self.airline_entry.get())
            self.controller.delete_record(record_id)
            messagebox.showinfo("Success", "Airline record deleted successfully!")
            self.clear_airline_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_flight(self):
        try:
            record_id = int(self.flight_entries.get('id', 0).get())
            self.controller.delete_record(record_id)
            messagebox.showinfo("Success", "Flight record deleted successfully!")
            self.clear_flight_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def search_client(self):
        try:
            # Temporarily enable ID field for input
            self.client_entries['id'].config(state='normal')
            record_id = int(self.client_entries['id'].get())
            self.client_entries['id'].config(state='readonly')
            
            record = self.controller.search_record(record_id)
            if record and record.get('type') == 'client':
                for key, entry in self.client_entries.items():
                    entry.config(state='normal')
                    entry.delete(0, tk.END)
                    entry.insert(0, str(record.get(key, '')))
                    if key == 'id':
                        entry.config(state='readonly')
                messagebox.showinfo("Success", "Client record found!")
            else:
                messagebox.showerror("Error", "Client record not found!")
                # Clear the ID field if record not found
                self.client_entries['id'].config(state='normal')
                self.client_entries['id'].delete(0, tk.END)
                self.client_entries['id'].config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
            # Clear the ID field if invalid input
            self.client_entries['id'].config(state='normal')
            self.client_entries['id'].delete(0, tk.END)
            self.client_entries['id'].config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def search_airline(self):
        try:
            # Temporarily enable ID field for input
            self.airline_id_entry.config(state='normal')
            record_id = int(self.airline_id_entry.get())
            self.airline_id_entry.config(state='readonly')
            
            record = self.controller.search_record(record_id)
            if record and record.get('type') == 'airline':
                self.airline_id_entry.config(state='normal')
                self.airline_id_entry.delete(0, tk.END)
                self.airline_id_entry.insert(0, str(record.get('id', '')))
                self.airline_id_entry.config(state='readonly')
                
                self.airline_entry.delete(0, tk.END)
                self.airline_entry.insert(0, str(record.get('company_name', '')))
                messagebox.showinfo("Success", "Airline record found!")
            else:
                messagebox.showerror("Error", "Airline record not found!")
                # Clear the ID field if record not found
                self.airline_id_entry.config(state='normal')
                self.airline_id_entry.delete(0, tk.END)
                self.airline_id_entry.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
            # Clear the ID field if invalid input
            self.airline_id_entry.config(state='normal')
            self.airline_id_entry.delete(0, tk.END)
            self.airline_id_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def search_flight(self):
        try:
            # Temporarily enable ID field for input
            self.flight_entries['id'].config(state='normal')
            record_id = int(self.flight_entries['id'].get())
            self.flight_entries['id'].config(state='readonly')
            
            record = self.controller.search_record(record_id)
            if record and record.get('type') == 'flight':
                for key, entry in self.flight_entries.items():
                    entry.config(state='normal')
                    entry.delete(0, tk.END)
                    entry.insert(0, str(record.get(key, '')))
                    if key == 'id':
                        entry.config(state='readonly')
                messagebox.showinfo("Success", "Flight record found!")
            else:
                messagebox.showerror("Error", "Flight record not found!")
                # Clear the ID field if record not found
                self.flight_entries['id'].config(state='normal')
                self.flight_entries['id'].delete(0, tk.END)
                self.flight_entries['id'].config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
            # Clear the ID field if invalid input
            self.flight_entries['id'].config(state='normal')
            self.flight_entries['id'].delete(0, tk.END)
            self.flight_entries['id'].config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def display_record(self, record, entries):
        for key, entry in entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, str(record.get(key, '')))
    
    def clear_client_form(self):
        for entry in self.client_entries.values():
            entry.delete(0, tk.END)
    
    def clear_airline_form(self):
        self.airline_entry.delete(0, tk.END)
    
    def clear_flight_form(self):
        for entry in self.flight_entries.values():
            entry.delete(0, tk.END)
    
    def run(self):
        self.root.mainloop() 