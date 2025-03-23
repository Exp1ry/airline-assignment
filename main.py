from controllers.record_controller import RecordController
from views.gui import GUI

def main():
    """Initialize and run the main application.
    
    This function serves as the entry point for the application. It:
    1. Creates a new RecordController instance to manage data operations
    2. Initializes the GUI with the controller
    3. Starts the GUI main loop
    
    The application will continue running until the user closes the window.
    """
    # Initialize the controller
    controller = RecordController()
    
    # Initialize and run the GUI
    gui = GUI(controller)
    gui.run()

if __name__ == "__main__":
    main() 