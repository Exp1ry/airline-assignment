from controllers.record_controller import RecordController
from views.gui import GUI

def main():
    # Initialize the controller
    controller = RecordController()
    
    # Initialize and run the GUI
    gui = GUI(controller)
    gui.run()

if __name__ == "__main__":
    main() 