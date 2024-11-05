**Unit Converter**
A simple graphical user interface (GUI) application for converting measurements between units. This application uses Tkinter and CustomTkinter to create a dark-themed, modern interface.

**Features**
Converts between various units of measurement:
1- Kilometers (Km) to Miles
2- Miles to Kilometers (Km)
3- Kilograms (Kg) to Pounds
4- Pounds to Kilograms (Kg)
5- Inches (In) to Centimeters (Cm)
6- Centimeters (Cm) to Inches (In)
7- Validates user input to ensure only numbers are accepted.
8- Displays conversion results directly in the GUI.
9- Provides error messages for invalid inputs or unsupported conversions.

**Requirements**
* Python 3.x
* kinter (typically included with Python)
* CustomTkinter (to install, use pip):
  **pip install customtkinter**

**How to Use**
1. Clone this repository or copy the code files into a local directory.
2. Install CustomTkinter using the command above.
3. Run the application:
     **python unit_converter.py**
4. Enter a measurement in the input field.
5. Select the units to convert from and to using the radio buttons.
6. Click the Convert button to see the result.
7. The result will display below the input field. If there is an error, it will be shown in red.

**Code Overview**
* convert_distance: The main function that calculates and displays the conversion based on the selected units.
* Unit Selection: Users can select units to convert between various measurement types (e.g., kilometers, pounds).
* Error Handling: If the user inputs a non-numeric value or selects unsupported unit pairs, the app displays an error message.

  

