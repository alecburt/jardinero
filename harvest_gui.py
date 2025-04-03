from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from harvest_be import HarvestBE


class HarvestGUI:
    def __init__(top, master):
        top.harvestbe = HarvestBE()
        master.title('Harvest')
        master.config(padx = 10, pady = 20) 
        master.iconbitmap('canary_icon.ico')
        top.canvas = Canvas(height=300, width=200)

        # image
        #global flower_image
        top.flower_image = ImageTk.PhotoImage(Image.open("flower.png"))
        top.top_pic = Label(image = top.flower_image)
        top.top_pic.grid(row = 0, column = 0, columnspan = 4)

        # labels
        top.opening_label = Label(text = 'Show me the Goodies!!!', font=('', 14))
        top.opening_label.grid(row = 1, column = 0, columnspan = 4)

        top.instructions = Label(text = "How much did we get?   Quantity, weight and unit")
        top.instructions.grid(row = 2, column = 0, columnspan = 2, sticky = 'W')

        ### entries
        # date entry.
        top.date_var = StringVar()
        def on_harvest_date_entry_click(date_var):
            if top.date_entry.get() == "Enter the date. DD/MM/YY  ":
                top.date_entry.delete(0, tk.END)
                top.date_entry.configure(foreground="black")
            
        def on_harvest_date_entry_focus_out(event):
            if top.date_entry.get() == "":
                top.date_entry.insert(0, "Enter the date. DD/MM/YY  ")
                top.date_entry.configure(foreground="gray")
                    
        top.date_entry = Entry(width = 30, borderwidth = 2, textvariable = top.date_var, foreground="gray")
        top.date_entry.insert(0, "Enter the date. DD/MM/YY  ")

        top.date_entry.bind("<FocusIn>", on_harvest_date_entry_click)
        top.date_entry.bind("<FocusOut>", on_harvest_date_entry_focus_out)
        top.date_entry.grid(pady = 10, row = 3, column = 0, sticky = 'NSEW')

        # plant id entry.
        top.plant_id_var = StringVar()
        def on_harvest_plant_id_entry_click(plant_id_var):
            if top.plant_id_entry.get() == "What is the Plant ID?":
                top.plant_id_entry.delete(0, tk.END)
                top.plant_id_entry.configure(foreground="black")
            
        def on_harvest_plant_id_entry_focus_out(event):
            if top.plant_id_entry.get() == "":
                top.plant_id_entry.insert(0, "What is the Plant ID?")
                top.plant_id_entry.configure(foreground="gray")
                    
        top.plant_id_entry = Entry(width = 30, borderwidth = 2, textvariable = top.plant_id_var, foreground="gray")
        top.plant_id_entry.insert(0, "What is the Plant ID?")

        top.plant_id_entry.bind("<FocusIn>", on_harvest_plant_id_entry_click)
        top.plant_id_entry.bind("<FocusOut>", on_harvest_plant_id_entry_focus_out)
        top.plant_id_entry.grid(pady = 10, row = 3, column = 1, sticky = 'NSEW')

        # quantity entry
        top.harvest_units_var = StringVar()
        def on_harvest_units_entry_click(harvest_units_var):
            if top.harvest_units_entry.get() == "How many units? or leave blank":
                top.harvest_units_entry.delete(0, tk.END)
                top.harvest_units_entry.configure(foreground="black")
            
        def on_harvest_units_entry_focus_out(event):
            if top.harvest_units_entry.get() == "":
                top.harvest_units_entry.insert(0, "How many units? or leave blank")
                top.harvest_units_entry.configure(foreground="gray")
                    
        top.harvest_units_entry = Entry(width = 30, borderwidth = 2, textvariable = top.harvest_units_var, foreground="gray")
        top.harvest_units_entry.insert(0, "How many units? or leave blank")

        top.harvest_units_entry.bind("<FocusIn>", on_harvest_units_entry_click)
        #top.harvest_units_entry.bind("<FocusOut>", on_harvest_units_entry_focus_out)
        top.harvest_units_entry.grid(row = 4, column = 0, sticky = 'NSEW')

        # weight entry
        top.harvest_weights_var = StringVar()
        def on_harvest_weights_entry_click(harvest_weights_var):
            if top.harvest_weights_entry.get() == "Whats the weight/volume etc??":
                top.harvest_weights_entry.delete(0, tk.END)
                top.harvest_weights_entry.configure(foreground="black")
            
        def on_harvest_weights_entry_focus_out(event):
            if top.harvest_weights_entry.get() == "":
                top.harvest_weights_entry.insert(0, "Whats the weight/volume etc??")
                top.harvest_weights_entry.configure(foreground="gray")
                    
        top.harvest_weights_entry = Entry(width = 30, borderwidth = 2, textvariable = top.harvest_weights_var, foreground="gray")
        top.harvest_weights_entry.insert(0, "Whats the weight/volume etc??")

        top.harvest_weights_entry.bind("<FocusIn>", on_harvest_weights_entry_click)
        top.harvest_weights_entry.bind("<FocusOut>", on_harvest_weights_entry_focus_out)
        top.harvest_weights_entry.grid(row = 5, column = 0, sticky = 'NSEW')

        # unit entry
        top.harvest_weight_unit_var = StringVar()
        def on_harvest_weight_unit_entry_click(harvest_weight_unit_var):
            if top.harvest_weight_unit_entry.get() == "Whats the units? g, kg, tons":
                top.harvest_weight_unit_entry.delete(0, tk.END)
                top.harvest_weight_unit_entry.configure(foreground="black")
            
        def on_harvest_weight_unit_entry_focus_out(event):
            if top.harvest_weight_unit_entry.get() == "":
                top.harvest_weight_unit_entry.insert(0, "Whats the units? g, kg, tons")
                top.harvest_weight_unit_entry.configure(foreground="gray")
                    
        top.harvest_weight_unit_entry = Entry(width = 30, borderwidth = 2, textvariable = top.harvest_weight_unit_var)
        top.harvest_weight_unit_entry.insert(0, "g")

        top.harvest_weight_unit_entry.bind("<FocusIn>", on_harvest_weight_unit_entry_click)
        top.harvest_weight_unit_entry.bind("<FocusOut>", on_harvest_weight_unit_entry_focus_out)
        top.harvest_weight_unit_entry.grid(row = 5, column = 1, sticky = 'NSEW')
        
        ### buttons
        # clear button.
        def button_clear():
            """Define what the clear button does."""
            top.date_entry.delete(0, END)
            top.plant_id_entry.delete(0, END)
            top.harvest_units_entry.delete(0, END)
            top.harvest_weights_entry.delete(0, END)
            top.harvest_weight_unit_entry.delete(0, END)
                
        top.clear_button = Button(width = 30, text = "Clear", command = button_clear)
        top.clear_button.grid(pady = 10, row = 6, column = 0, sticky = 'NSEW')

        # submit button
        top.submit_button = Button(width = 30, text = "Submit", command = top.harvest_save_data)
        top.submit_button.grid(pady = 10, row = 6, column = 1, sticky = 'NSEW')

    def harvest_save_data(top):
        # date check
        date = top.date_var.get()
        if len(date) <8:
            messagebox.showinfo(title = 'Warning', message = 'Length is less than 8!')
        elif len(date) >8:
            messagebox.showinfo(title = 'Warning', message = 'Length is more than 8!')
        elif (date[2] == '/') and (date[5] == '/'):
            date_ver = date
        else:
            messagebox.showinfo(title = 'Warning', message = 'Wheres the backslashes!')

        # plant id check
        plant_id = top.plant_id_var.get()
        if plant_id == "What is the Plant ID?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the plant id box!')
        elif len(plant_id) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a plant id!')
        else:
            plant_id_ver = plant_id
            plant_id_ver_int = int(plant_id_ver)
            
        # harvest quantity check
        harvest_units = top.harvest_units_var.get()
        if harvest_units == "How many units? or leave blank":
            harvest_units = 0
            harvest_units_ver_int = harvest_units
        elif len(harvest_units) == 0:
            harvest_units = 0
            harvest_units_ver_int = harvest_units
        else:
            harvest_units_ver = harvest_units
            harvest_units_ver_int = int(harvest_units_ver)

        # harvest weight check
        harvest_weights = top.harvest_weights_var.get()
        if harvest_weights == "Where's my new home?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the weight box!')
        elif len(harvest_weights) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a weight!')
        else:
            harvest_weights_ver = harvest_weights
            harvest_weights_ver_int = int(harvest_weights_ver)

        # harvest weight unit check
        harvest_weight_unit = top.harvest_weight_unit_var.get()
        if harvest_weight_unit == "Where's my new home?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the location box!')
        elif len(harvest_weight_unit) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a note!')
        else:
            harvest_weight_unit_ver = harvest_weight_unit
            
        top.harvestbe.harvest_save_data(harvest_units_ver_int, harvest_weights_ver_int, harvest_weight_unit_ver, date_ver, plant_id_ver_int)
        messagebox.showinfo(title = 'Congrats', message = 'Good Job!')


#def main(): tab the bottom 3 lines to work from main
root = Tk()
harvest_gui = HarvestGUI(root)
root.mainloop()        
