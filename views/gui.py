import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class GUI:
    """A graphical user interface for managing travel agent records.

    This class provides a GUI for creating, updating, deleting, and searching
    client, airline, and flight records.

    Attributes:
        controller: The RecordController instance that handles data operations.
        root: The main Tkinter window.
    """

    # Predefined list for cities
    CITIES = [
        "London",
        "New York",
        "Dubai",
        "Singapore",
        "Tokyo",
        "Paris",
        "Sydney",
        "Hong Kong"
    ]

    def __init__(self, controller):
        """Initialize the GUI.

        Args:
            controller: The RecordController instance that handles data operations.
        """
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Travel Agent Record Management System")
        self.root.geometry("800x600")
        self.setup_gui()

        # Predefined cities for dropdowns
        self.cities = [
            "Dubai", "Doha", "Istanbul", "London", "Paris", "Amsterdam",
            "Singapore", "Hong Kong", "Tokyo", "New York", "Los Angeles",
            "Sydney", "Mumbai", "Bangkok", "Seoul", "Berlin", "Rome",
            "Madrid", "Vienna", "Moscow", "Beijing", "Shanghai", "Toronto",
            "Vancouver", "Auckland", "Cairo", "Dubai", "Abu Dhabi", "Riyadh",
            "Kuala Lumpur", "Manila", "Jakarta", "Hanoi", "Ho Chi Minh City",
            "Bangkok", "Phuket", "Seoul", "Busan", "Osaka", "Kyoto",
            "Helsinki", "Stockholm", "Copenhagen", "Oslo", "Reykjavik",
            "Dublin", "Edinburgh", "Glasgow", "Belfast", "Cardiff"
        ]
        
        # Sort cities alphabetically
        self.cities.sort()

    def get_airlines(self):
        """Get list of created airlines from the controller.

        Returns:
            list: List of airline names with their codes.
        """
        try:
            airlines = self.controller.get_all_records('airline')
            if not airlines:
                return ["No airlines found"]
            return [f"{airline['company_name']}" for airline in airlines]
        except Exception as e:
            print(f"Error getting airlines: {e}")
            return ["No airlines found"]

    def get_clients(self):
        """Get list of created clients from the controller.

        Returns:
            list: List of client IDs and names.
        """
        try:
            clients = self.controller.get_all_records('client')
            if not clients:
                return ["No clients found"]
            return [f"{client['id']} - {client['name']}" for client in clients]
        except Exception as e:
            print(f"Error getting clients: {e}")
            return ["No clients found"]

    def refresh_airline_dropdown(self):
        """Refresh the airline dropdown with current airlines from records."""
        if hasattr(self, 'flight_airline'):
            self.flight_airline['values'] = self.get_airlines()
            self.flight_airline.set('')  # Clear current selection

    def refresh_client_dropdown(self):
        """Refresh the client dropdown with current clients from records."""
        if hasattr(self, 'flight_client'):
            self.flight_client['values'] = self.get_clients()
            self.flight_client.set('')  # Clear current selection

    def setup_gui(self):
        """Set up the main GUI components including the notebook and tabs."""
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)

        # Create two main tabs
        self.create_frame = ttk.Frame(self.notebook)
        self.search_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.create_frame, text='Create New Record')
        self.notebook.add(self.search_frame, text='Search Existing Record')

        self.setup_create_tab()
        self.setup_search_tab()

    def setup_create_tab(self):
        """Set up the create tab with record type selection and form."""
        # Record type selection
        select_frame = ttk.LabelFrame(self.create_frame, text="Select Record Type")
        select_frame.pack(fill='x', padx=5, pady=5)

        self.create_record_type = tk.StringVar(value="client")
        ttk.Radiobutton(
            select_frame,
            text="Client",
            value="client",
            variable=self.create_record_type,
            command=self.show_create_form
        ).pack(side='left', padx=5)
        ttk.Radiobutton(
            select_frame,
            text="Airline",
            value="airline",
            variable=self.create_record_type,
            command=self.show_create_form
        ).pack(side='left', padx=5)
        ttk.Radiobutton(
            select_frame,
            text="Flight",
            value="flight",
            variable=self.create_record_type,
            command=self.show_create_form
        ).pack(side='left', padx=5)

        # Container for the form
        self.create_form_frame = ttk.Frame(self.create_frame)
        self.create_form_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Initialize with client form
        self.show_create_form()

    def setup_search_tab(self):
        """Set up the search tab with record type selection and form."""
        # Record type selection
        select_frame = ttk.LabelFrame(self.search_frame, text="Select Record Type")
        select_frame.pack(fill='x', padx=5, pady=5)

        self.search_record_type = tk.StringVar(value="client")
        ttk.Radiobutton(
            select_frame,
            text="Client",
            value="client",
            variable=self.search_record_type,
            command=self.show_search_form
        ).pack(side='left', padx=5)
        ttk.Radiobutton(
            select_frame,
            text="Airline",
            value="airline",
            variable=self.search_record_type,
            command=self.show_search_form
        ).pack(side='left', padx=5)
        ttk.Radiobutton(
            select_frame,
            text="Flight",
            value="flight",
            variable=self.search_record_type,
            command=self.show_search_form
        ).pack(side='left', padx=5)

        # Search ID frame
        self.search_id_frame = ttk.LabelFrame(self.search_frame, text="Search by ID")
        self.search_id_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(self.search_id_frame, text="ID:").pack(side='left', padx=5)
        self.search_id_entry = ttk.Entry(self.search_id_frame)
        self.search_id_entry.pack(side='left', padx=5)
        ttk.Button(
            self.search_id_frame,
            text="Search",
            command=self.search_record
        ).pack(side='left', padx=5)

        # Container for the form
        self.search_form_frame = ttk.Frame(self.search_frame)
        self.search_form_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Buttons frame
        self.search_buttons_frame = ttk.Frame(self.search_frame)
        self.search_buttons_frame.pack(fill='x', padx=5, pady=5)

        ttk.Button(
            self.search_buttons_frame,
            text="Update Record",
            command=self.update_record
        ).pack(side='left', padx=5)
        ttk.Button(
            self.search_buttons_frame,
            text="Delete Record",
            command=self.delete_record
        ).pack(side='left', padx=5)

        # Initialize with client form
        self.show_search_form()

    def setup_client_create_form(self):
        """Set up the client creation form."""
        form_frame = ttk.LabelFrame(self.create_form_frame, text="Client Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        # Create entry fields
        fields = [
            ('name', True),
            ('address_line1', True),
            ('address_line2', False),
            ('address_line3', False),
            ('city', True),
            ('state', True),
            ('zip_code', True),
            ('country', True),
            ('phone_number', True)
        ]
        self.client_entries = {}

        for i, (field, required) in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            if required:
                label_text += "*"
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=2)
            self.client_entries[field] = ttk.Entry(form_frame)
            self.client_entries[field].grid(row=i, column=1, padx=5, pady=2)

        ttk.Button(
            form_frame,
            text="Create Client",
            command=self.create_client
        ).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def setup_airline_create_form(self):
        """Set up the airline creation form."""
        form_frame = ttk.LabelFrame(self.create_form_frame, text="Airline Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(form_frame, text="Company Name*").grid(row=0, column=0, padx=5, pady=2)
        self.airline_entry = ttk.Entry(form_frame)
        self.airline_entry.grid(row=0, column=1, padx=5, pady=2)

        ttk.Button(
            form_frame,
            text="Create Airline",
            command=self.create_airline
        ).grid(row=1, column=0, columnspan=2, pady=10)

    def setup_flight_create_form(self):
        """Set up the flight creation form."""
        form_frame = ttk.LabelFrame(self.create_form_frame, text="Flight Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        # Client dropdown
        ttk.Label(form_frame, text="Client*").grid(row=0, column=0, padx=5, pady=2)
        self.flight_client = ttk.Combobox(form_frame, values=self.get_clients())
        self.flight_client.grid(row=0, column=1, padx=5, pady=2)

        # Refresh button for client dropdown
        ttk.Button(
            form_frame,
            text="Refresh Clients",
            command=self.refresh_client_dropdown
        ).grid(row=0, column=2, padx=5, pady=2)

        # Airline dropdown
        ttk.Label(form_frame, text="Airline*").grid(row=1, column=0, padx=5, pady=2)
        self.flight_airline = ttk.Combobox(form_frame, values=self.get_airlines())
        self.flight_airline.grid(row=1, column=1, padx=5, pady=2)

        # Refresh button for airline dropdown
        ttk.Button(
            form_frame,
            text="Refresh Airlines",
            command=self.refresh_airline_dropdown
        ).grid(row=1, column=2, padx=5, pady=2)

        # Start city dropdown
        ttk.Label(form_frame, text="Start City*").grid(row=2, column=0, padx=5, pady=2)
        self.flight_start_city = ttk.Combobox(form_frame, values=self.cities)
        self.flight_start_city.grid(row=2, column=1, padx=5, pady=2)

        # End city dropdown
        ttk.Label(form_frame, text="End City*").grid(row=3, column=0, padx=5, pady=2)
        self.flight_end_city = ttk.Combobox(form_frame, values=self.cities)
        self.flight_end_city.grid(row=3, column=1, padx=5, pady=2)

        ttk.Button(
            form_frame,
            text="Create Flight",
            command=self.create_flight
        ).grid(row=4, column=0, columnspan=2, pady=10)

    def show_create_form(self):
        """Show the appropriate creation form based on selected record type."""
        # Clear the current form
        for widget in self.create_form_frame.winfo_children():
            widget.destroy()

        # Show the selected form
        record_type = self.create_record_type.get()
        if record_type == "client":
            self.setup_client_create_form()
        elif record_type == "airline":
            self.setup_airline_create_form()
        elif record_type == "flight":
            self.setup_flight_create_form()

    def show_search_form(self):
        """Show the appropriate search form based on selected record type."""
        # Clear the current form
        for widget in self.search_form_frame.winfo_children():
            widget.destroy()

        # Show the selected form
        record_type = self.search_record_type.get()
        if record_type == "client":
            self.setup_client_search_form()
        elif record_type == "airline":
            self.setup_airline_search_form()
        elif record_type == "flight":
            self.setup_flight_search_form()

    def setup_client_search_form(self):
        """Set up the client search form."""
        form_frame = ttk.LabelFrame(self.search_form_frame, text="Client Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        # Create entry fields
        fields = [
            ('name', True),
            ('address_line1', True),
            ('address_line2', False),
            ('address_line3', False),
            ('city', True),
            ('state', True),
            ('zip_code', True),
            ('country', True),
            ('phone_number', True)
        ]
        self.search_client_entries = {}

        for i, (field, required) in enumerate(fields):
            label_text = field.replace('_', ' ').title()
            if required:
                label_text += "*"
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, padx=5, pady=2)
            entry = ttk.Entry(form_frame, state='readonly')
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.search_client_entries[field] = entry

    def setup_airline_search_form(self):
        """Set up the airline search form."""
        form_frame = ttk.LabelFrame(self.search_form_frame, text="Airline Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        ttk.Label(form_frame, text="Company Name").grid(row=0, column=0, padx=5, pady=2)
        self.search_airline_entry = ttk.Entry(form_frame, state='readonly')
        self.search_airline_entry.grid(row=0, column=1, padx=5, pady=2)

    def setup_flight_search_form(self):
        """Set up the flight search form."""
        form_frame = ttk.LabelFrame(self.search_form_frame, text="Flight Information")
        form_frame.pack(fill='x', padx=5, pady=5)

        # Create entry fields
        self.search_flight_entries = {}

        # Start city entry
        ttk.Label(form_frame, text="Start City").grid(row=0, column=0, padx=5, pady=2)
        self.search_flight_start_city = ttk.Entry(form_frame, state='readonly')
        self.search_flight_start_city.grid(row=0, column=1, padx=5, pady=2)

        # End city entry
        ttk.Label(form_frame, text="End City").grid(row=1, column=0, padx=5, pady=2)
        self.search_flight_end_city = ttk.Entry(form_frame, state='readonly')
        self.search_flight_end_city.grid(row=1, column=1, padx=5, pady=2)

        # Associated IDs
        assoc_frame = ttk.LabelFrame(self.search_form_frame, text="Associated Records")
        assoc_frame.pack(fill='x', padx=5, pady=5)

        # Client ID
        ttk.Label(assoc_frame, text="Client ID").grid(row=0, column=0, padx=5, pady=2)
        self.search_flight_client_id = ttk.Entry(assoc_frame, state='readonly')
        self.search_flight_client_id.grid(row=0, column=1, padx=5, pady=2)

        # Airline
        ttk.Label(assoc_frame, text="Airline").grid(row=1, column=0, padx=5, pady=2)
        self.search_flight_airline = ttk.Entry(assoc_frame, state='readonly')
        self.search_flight_airline.grid(row=1, column=1, padx=5, pady=2)

    def validate_required_fields(self, entries, required_fields):
        """Validate that all required fields are filled.

        Args:
            entries: Dictionary of entry widgets.
            required_fields: List of field names that are required.

        Returns:
            bool: True if all required fields are filled, False otherwise.
        """
        for field in required_fields:
            if field in entries:
                value = entries[field].get().strip()
                if not value:
                    messagebox.showerror(
                        "Validation Error",
                        f"Please check the form, required field missing: {field.replace('_', ' ').title()}"
                    )
                    return False
        return True

    def create_client(self):
        """Create a new client record."""
        required_fields = [
            'name', 'address_line1', 'city', 'state',
            'zip_code', 'country', 'phone_number'
        ]

        if not self.validate_required_fields(self.client_entries, required_fields):
            return

        data = {k: v.get().strip() for k, v in self.client_entries.items()}
        try:
            self.controller.create_record('client', data)
            messagebox.showinfo("Success", "Client record created successfully!")
            self.show_create_form()  # Reset the form
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_airline(self):
        """Create a new airline record."""
        if not self.airline_entry.get().strip():
            messagebox.showerror(
                "Validation Error",
                "Please enter the airline company name"
            )
            return

        data = {'company_name': self.airline_entry.get().strip()}
        try:
            self.controller.create_record('airline', data)
            messagebox.showinfo("Success", "Airline record created successfully!")
            self.show_create_form()  # Reset the form
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_flight(self):
        """Create a new flight record."""
        if not self.flight_client.get():
            messagebox.showerror("Validation Error", "Please select a client")
            return
        if not self.flight_airline.get():
            messagebox.showerror("Validation Error", "Please select an airline")
            return
        if not self.flight_start_city.get():
            messagebox.showerror("Validation Error", "Please select a start city")
            return
        if not self.flight_end_city.get():
            messagebox.showerror("Validation Error", "Please select an end city")
            return

        try:
            # Get client ID from selection
            client_selection = self.flight_client.get().strip()
            client_id = int(client_selection.split(' - ')[0])
            
            # Get airline ID from selection
            airline_name = self.flight_airline.get().strip()
            airlines = self.controller.get_all_records('airline')
            airline = next((a for a in airlines if a['company_name'] == airline_name), None)
            
            if not airline:
                messagebox.showerror("Error", "Selected airline not found")
                return

            # Create the flight data
            data = {
                'client_id': client_id,
                'airline_id': airline['id'],
                'start_city': self.flight_start_city.get(),
                'end_city': self.flight_end_city.get(),
                # 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.controller.create_record('flight', data)
            messagebox.showinfo("Success", "Flight record created successfully!")
            self.show_create_form()  # Reset the form
        except ValueError:
            messagebox.showerror("Error", "Invalid client selection")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_record(self):
        """Search for a record based on the selected type and ID."""
        try:
            record_id = int(self.search_id_entry.get().strip())
            record = self.controller.search_record(record_id)
            
            if not record:
                messagebox.showerror("Error", "Record not found!")
                return

            record_type = self.search_record_type.get()
            if record.get('type') != record_type:
                messagebox.showerror(
                    "Error",
                    f"Record {record_id} is not a {record_type} record!"
                )
                return

            # Display the record based on its type
            if record_type == "client":
                self.display_client_record(record)
            elif record_type == "airline":
                self.display_airline_record(record)
            elif record_type == "flight":
                self.display_flight_record(record)

            messagebox.showinfo("Success", f"{record_type.title()} record found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid ID number")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_client_record(self, record):
        """Display client record in the search form."""
        for key, entry in self.search_client_entries.items():
            entry.config(state='normal')
            entry.delete(0, tk.END)
            entry.insert(0, str(record.get(key, '')))

    def display_airline_record(self, record):
        """Display airline record in the search form."""
        self.search_airline_entry.config(state='normal')
        self.search_airline_entry.delete(0, tk.END)
        self.search_airline_entry.insert(0, str(record.get('company_name', '')))

    def display_flight_record(self, record):
        """Display flight record in the search form."""
        print(f"Displaying flight record: {record}")  # Debug log
        
        # Get airline name for display
        airlines = self.controller.get_all_records('airline')
        airline = next((a for a in airlines if a['id'] == record.get('airline_id')), None)
        airline_name = airline['company_name'] if airline else "Unknown Airline"
        print(f"Found airline: {airline_name}")  # Debug log

        # Set city values
        departure_city = record.get('start_city', '')
        arrival_city = record.get('end_city', '')
        print(f"Departure city: {departure_city}, Arrival city: {arrival_city}")  # Debug log
        
        # Update departure city
        self.search_flight_start_city.config(state='normal')
        self.search_flight_start_city.delete(0, tk.END)
        self.search_flight_start_city.insert(0, departure_city)
        self.search_flight_start_city.config(state='readonly')
        
        # Update arrival city
        self.search_flight_end_city.config(state='normal')
        self.search_flight_end_city.delete(0, tk.END)
        self.search_flight_end_city.insert(0, arrival_city)
        self.search_flight_end_city.config(state='readonly')
        
        # Set client ID
        client_id = record.get('client_id', '')
        print(f"Client ID: {client_id}")  # Debug log
        self.search_flight_client_id.config(state='normal')
        self.search_flight_client_id.delete(0, tk.END)
        self.search_flight_client_id.insert(0, str(client_id))
        self.search_flight_client_id.config(state='readonly')

        # Set airline name
        self.search_flight_airline.config(state='normal')
        self.search_flight_airline.delete(0, tk.END)
        self.search_flight_airline.insert(0, airline_name)
        self.search_flight_airline.config(state='readonly')

    def update_record(self):
        """Update the currently displayed record."""
        try:
            record_id = int(self.search_id_entry.get().strip())
            record_type = self.search_record_type.get()

            if record_type == "client":
                self.update_client_record(record_id)
            elif record_type == "airline":
                self.update_airline_record(record_id)
            elif record_type == "flight":
                self.update_flight_record(record_id)
        except ValueError:
            messagebox.showerror("Error", "No record currently selected")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_client_record(self, record_id):
        """Update a client record."""
        data = {
            'id': record_id,
            **{k: v.get().strip() for k, v in self.search_client_entries.items()}
        }
        if self.controller.update_record(record_id, data):
            messagebox.showinfo("Success", "Client record updated successfully!")
        else:
            messagebox.showerror("Error", "Failed to update client record")

    def update_airline_record(self, record_id):
        """Update an airline record."""
        data = {
            'id': record_id,
            'company_name': self.search_airline_entry.get().strip()
        }
        if self.controller.update_record(record_id, data):
            messagebox.showinfo("Success", "Airline record updated successfully!")
        else:
            messagebox.showerror("Error", "Failed to update airline record")

    def update_flight_record(self, record_id):
        """Update a flight record."""
        data = {
            'id': record_id,
            'start_city': self.search_flight_start_city.get(),
            'end_city': self.search_flight_end_city.get()
        }
        if self.controller.update_record(record_id, data):
            messagebox.showinfo("Success", "Flight record updated successfully!")
        else:
            messagebox.showerror("Error", "Failed to update flight record")

    def delete_record(self):
        """Delete the currently displayed record."""
        try:
            record_id = int(self.search_id_entry.get().strip())
            record_type = self.search_record_type.get()

            if messagebox.askyesno(
                "Confirm Delete",
                f"Are you sure you want to delete this {record_type} record?"
            ):
                self.controller.delete_record(record_id)
                messagebox.showinfo(
                    "Success",
                    f"{record_type.title()} record deleted successfully!"
                )
                self.show_search_form()  # Reset the form
                self.search_id_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "No record currently selected")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop() 