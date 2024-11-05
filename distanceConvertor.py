import tkinter
import customtkinter

# creating app frame

root = customtkinter.CTk()
root.geometry('600x400')
root.title('Unit Convertor')
root.resizable(False, False)
customtkinter.set_appearance_mode("dark")

# input field
input_field = customtkinter.CTkFrame(root, width=400, height=100)
input_field.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

# input entry
input_label = customtkinter.CTkLabel(input_field, text='Enter Your Measurement:', font=("Times New Roman", 15))
input_label.pack()
user_input = tkinter.StringVar()
input_entry = customtkinter.CTkEntry(input_field, textvariable=user_input, width=200, border_width=2,
                                     border_color="white")
input_entry.pack(pady=10)

# unit field
unit_field = customtkinter.CTkFrame(root, width=400, height=300, border_width=1, border_color="white")
unit_field.pack_propagate(False)
unit_field.pack(padx=10, pady=20, side="bottom")

selected_unit = customtkinter.StringVar()
desired_unit = customtkinter.StringVar()

# from field
from_field = customtkinter.CTkFrame(unit_field, width=400, height=140)
from_field.grid(row=0, column=0, padx=10, pady=10)

from_label = customtkinter.CTkLabel(from_field, text='From:', font=('Times New Roman', 15))
from_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# from field - unit buttons
kilometers = customtkinter.CTkRadioButton(from_field, text='Km', variable=selected_unit, value="Km")
miles = customtkinter.CTkRadioButton(from_field, text='Miles', variable=selected_unit, value="Miles")
kilograms = customtkinter.CTkRadioButton(from_field, text='Kg', variable=selected_unit, value="Kg")
pounds = customtkinter.CTkRadioButton(from_field, text='Pounds', variable=selected_unit, value="Pounds")
centimeters = customtkinter.CTkRadioButton(from_field, text='Cm', variable=selected_unit, value="Cm")
inches = customtkinter.CTkRadioButton(from_field, text='Inc', variable=selected_unit, value="In")
kilometers.grid(row=1, column=0, padx=5, pady=5)
miles.grid(row=1, column=1, padx=5, pady=5)
kilograms.grid(row=2, column=0, padx=5, pady=5)
pounds.grid(row=2, column=1, padx=5, pady=5)
centimeters.grid(row=3, column=0, padx=5, pady=5)
inches.grid(row=3, column=1, padx=5, pady=5)

# to field

to_field = customtkinter.CTkFrame(unit_field, width=400, height=145)

to_field.grid(row=0, column=1, padx=10, pady=10)

to_label = customtkinter.CTkLabel(to_field, text='To:', font=('Times New Roman', 15))
to_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# to_field- unit buttons
kilometer = customtkinter.CTkRadioButton(to_field, text='Km', variable=desired_unit, value="Km")
mile = customtkinter.CTkRadioButton(to_field, text='Miles', variable=desired_unit, value="Miles")
kilogram = customtkinter.CTkRadioButton(to_field, text='Kg', variable=desired_unit, value="Kg")
pound = customtkinter.CTkRadioButton(to_field, text='Pounds', variable=desired_unit, value="Pounds")
centimeter = customtkinter.CTkRadioButton(to_field, text='Cm', variable=desired_unit, value="Cm")
inch = customtkinter.CTkRadioButton(to_field, text='Inc', variable=desired_unit, value="Inc")
kilometer.grid(row=1, column=0, padx=5, pady=5)
mile.grid(row=1, column=1, padx=5, pady=5)
kilogram.grid(row=2, column=0, padx=5, pady=5)
pound.grid(row=2, column=1, padx=5, pady=5)
centimeter.grid(row=3, column=0, padx=5, pady=5)
inch.grid(row=3, column=1, padx=5, pady=5)


# main function
def convert_distance():
    # users input try-except
    try:
        measurement = float(user_input.get())
    except ValueError:
        input_label.configure(text="Please enter a valid number.", text_color="red")
        return
    # conversion parameters
    conversion_rates_dict = {
        ("Km", "Miles"): 0.621371,
        ("Miles", "Km"): 1.60934,
        ("Pounds", "Kg"): 0.453592,
        ("Kg", "Pounds"): 2.20462,
        ("Inc", "Cm"): 2.54,
        ("Cm", "Inc"): 0.3937
    }
    # getting the units
    from_unit = selected_unit.get()
    to_unit = desired_unit.get()

    # the control block
    if from_unit == to_unit:
        input_label.configure(text="Can not convert same units!", text_color="red")
    elif (from_unit, to_unit) in conversion_rates_dict:
        result = measurement * conversion_rates_dict[(from_unit, to_unit)]
        input_label.configure(text=f"The measurement is {result}", text_color="green")
    else:
        input_label.configure(text="Conversion between selected units are not available.", text_color="red")
        return


# convertion button
convert_button = customtkinter.CTkButton(root, text="Convert", command=convert_distance)
convert_button.pack(pady=10)

# run the frame
root.mainloop()
