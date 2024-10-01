import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from main import hypixelScrape2

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # Create input widget
        self.input_widget = QLineEdit(self)
        self.input_widget.setPlaceholderText("Enter username here")
        layout.addWidget(self.input_widget)

        # Create button
        self.process_button = QPushButton("Find FKDR", self)
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)

        # Create output widgets
        self.output_widget1 = QLabel("Output 1: ", self)
        layout.addWidget(self.output_widget1)

        self.output_widget2 = QLabel("Output 2: ", self)
        layout.addWidget(self.output_widget2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("FKDR Finder")
        self.setGeometry(100, 100, 300, 200)

    def process_text(self):
        input_text = self.input_widget.text()
        fkdr, dodge = hypixelScrape2(input_text)
        self.output_widget1.setText(f"FKDR: {str(fkdr)}")
        if dodge:
            self.output_widget2.setText("Dodge!")
        else:
            self.output_widget2.setText("All good.")
    #example function from online
    # def process_text(self):
    #     # Get the input text
    #     input_text = self.input_widget.text()

    #     # Process the text (for example, reversing it and converting to uppercase)
    #     output1 = input_text[::-1]  # Reverse the string
    #     output2 = input_text.upper()  # Convert to uppercase

    #     # Update output widgets
    #     self.output_widget1.setText(f"Output 1: {output1}")
    #     self.output_widget2.setText(f"Output 2: {output2}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
