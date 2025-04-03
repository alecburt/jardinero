from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from new_plant_be import NewplantBE


class NewplantGUI:
    def __init__(top, master): 
        newplantbe = NewplantBE()
        master.title('New Plant')
        master.config(padx = 10, pady = 20) 
        master.iconbitmap('canary_icon.ico')
        top.canvas = Canvas(height=300, width=200)

        # image
        #global flower_image
        top.flower_image = ImageTk.PhotoImage(Image.open("flower.png"))
        top.top_pic = Label(image = top.flower_image)
        top.top_pic.grid(row = 0, column = 0, columnspan = 4)

        # labels
        top.opening_label = Label(text = 'Woohoo New Plantitas!!!', font=('', 14))
        top.opening_label.grid(row = 1, column = 0, columnspan = 4)
        top.instructions = Label(text = "What we got? What we go? What we got?")
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
        top.date_entry.grid(pady = 10, row = 3, column = 0, sticky = 'W')

        ### frames
        ## new plant frame
        top.new_plant_frame = LabelFrame(text = "New Plant", padx = 5, pady = 5)
        top.new_plant_frame.grid(padx = 2, pady = 2, row = 4, column = 0, columnspan = 2)

        # name entry 
        top.name_var = StringVar()                   
        top.name_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.name_var, foreground="gray")
        top.name_entry.insert(0, "anon")
        top.name_entry.grid(row = 0, column = 0, sticky = 'NSEW')

        # quantity entry
        top.quantity_var = StringVar()
        def on_quantity_entry_click(quantity_var):
            if top.quantity_entry.get() == "How many planted?":
                top.quantity_entry.delete(0, tk.END)
                top.quantity_entry.configure(foreground="black")
            
        def on_quantity_entry_focus_out(event):
            if top.quantity_entry.get() == "":
                top.quantity_entry.insert(0, "How many planted?")
                top.quantity_entry.configure(foreground="gray")
                    
        top.quantity_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.quantity_var, foreground="gray")
        top.quantity_entry.insert(0, "How many planted?")

        top.quantity_entry.bind("<FocusIn>", on_quantity_entry_click)
        top.quantity_entry.bind("<FocusOut>", on_quantity_entry_focus_out)
        top.quantity_entry.grid(row = 0, column = 1, sticky = 'NSEW')

        # main category entry
        top.main_category_var = StringVar()
        def on_main_category_entry_click(main_category_var):
            if top.main_category_entry.get() == "Whats the main category?":
                top.main_category_entry.delete(0, tk.END)
                top.main_category_entry.configure(foreground="black")
            
        def on_main_category_entry_focus_out(event):
            if top.main_category_entry.get() == "":
                top.main_category_entry.insert(0, "Whats the main category?")
                top.main_category_entry.configure(foreground="gray")
                    
        top.main_category_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.main_category_var, foreground="gray")
        top.main_category_entry.insert(0, "Whats the main category?")
        top.main_category_entry.bind("<FocusIn>", on_main_category_entry_click)
        top.main_category_entry.bind("<FocusOut>", on_main_category_entry_focus_out)
        top.main_category_entry.grid(row = 1, column = 0, sticky = 'NSEW')

        # sub category entry
        top.sub_category_var = StringVar()
        def on_sub_category_entry_click(sub_category_var):
            if top.sub_category_entry.get() == "Whats the sub category?":
                top.sub_category_entry.delete(0, tk.END)
                top.sub_category_entry.configure(foreground="black")
            
        def on_sub_category_entry_focus_out(event):
            if top.sub_category_entry.get() == "":
                top.sub_category_entry.insert(0, "Whats the sub category?")
                top.sub_category_entry.configure(foreground="gray")
                    
        top.sub_category_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.sub_category_var, foreground="gray")
        top.sub_category_entry.insert(0, "Whats the sub category?")
        top.sub_category_entry.bind("<FocusIn>", on_sub_category_entry_click)
        top.sub_category_entry.bind("<FocusOut>", on_sub_category_entry_focus_out)
        top.sub_category_entry.grid(row = 1, column = 1, sticky = 'NSEW')

        # classification entry
        top.classification_var = StringVar()
        def on_classification_entry_click(classification_var):
            if top.classification_entry.get() == "Whats the classification?":
                top.classification_entry.delete(0, tk.END)
                top.classification_entry.configure(foreground="black")
            
        def on_classification_entry_focus_out(event):
            if top.classification_entry.get() == "":
                top.classification_entry.insert(0, "Whats the classification?")
                top.classification_entry.configure(foreground="gray")
                    
        top.classification_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.classification_var, foreground="gray")
        top.classification_entry.insert(0, "Whats the classification?")
        top.classification_entry.bind("<FocusIn>", on_classification_entry_click)
        top.classification_entry.bind("<FocusOut>", on_classification_entry_focus_out)
        top.classification_entry.grid(row = 2, column = 0, sticky = 'NSEW')

        # seed class entry
        top.seed_class_var = StringVar()
        def on_seed_class_entry_click(seed_class_var):
            if top.seed_class_entry.get() == "Whats the seed class?":
                top.seed_class_entry.delete(0, tk.END)
                top.seed_class_entry.configure(foreground="black")
            
        def on_seed_class_entry_focus_out(event):
            if top.seed_class_entry.get() == "":
                top.seed_class_entry.insert(0, "Whats the seed class?")
                top.seed_class_entry.configure(foreground="gray")
                    
        top.seed_class_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.seed_class_var, foreground="gray")
        top.seed_class_entry.insert(0, "Whats the seed class?")
        top.seed_class_entry.bind("<FocusIn>", on_seed_class_entry_click)
        top.seed_class_entry.bind("<FocusOut>", on_seed_class_entry_focus_out)
        top.seed_class_entry.grid(row = 2, column = 1, sticky = 'NSEW')

        # perennial or annual entry
        top.per_ann_var = StringVar()
        def on_per_ann_entry_click(per_ann_var):
            if top.per_ann_entry.get() == "Am I Perennial or Annual?":
                top.per_ann_entry.delete(0, tk.END)
                top.per_ann_entry.configure(foreground="black")
            
        def on_per_ann_entry_focus_out(event):
            if top.per_ann_entry.get() == "":
                top.per_ann_entry.insert(0, "Am I Perennial or Annual?")
                top.per_ann_entry.configure(foreground="gray")
                    
        top.per_ann_entry = Entry(top.new_plant_frame, width = 30, borderwidth = 2, textvariable = top.per_ann_var, foreground="gray")
        top.per_ann_entry.insert(0, "Am I Perennial or Annual?")
        top.per_ann_entry.bind("<FocusIn>", on_per_ann_entry_click)
        top.per_ann_entry.bind("<FocusOut>", on_per_ann_entry_focus_out)
        top.per_ann_entry.grid(row = 3, column = 0, sticky = 'NSEW')

        # clear button.
        def button_clear():
            """Define what the clear button does."""
            top.name_entry.delete(0, END)
            top.quantity_entry.delete(0, END)
            top.main_category_entry.delete(0, END)
            top.sub_category_entry.delete(0, END)
            top.classification_entry.delete(0, END)
            top.seed_class_entry.delete(0, END)
            top.per_ann_entry.delete(0, END)
                
        top.clear_button = Button(top.new_plant_frame, width = 30, text = "Clear", command = button_clear)
        top.clear_button.grid(pady = 10, row = 4, column = 0, sticky = 'NSEW')

        # submit button
        top.submit_button = Button(top.new_plant_frame, width = 30, text = "Submit", command = top.new_plant_save_data)
        top.submit_button.grid(pady = 10, row = 4, column = 1, sticky = 'NSEW')
    
    def new_plant_save_data(top):
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

                    
        # name check
        # TODO this needs work I want to be able to leave blank.
        name = top.name_var.get()
        if len(name) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a name or leave the message!')
        elif name == "What's my name? or write anon":
            name = "anon"        
        #elif name == 'no':
        #    name = 'anon'
        else:
            name_ver_str = str(name)

        # main category check
        main_category = top.main_category_var.get()
        if main_category == "Whats the main category?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the main category box!')
        elif len(main_category) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a main category!')
        else:
            main_category_ver = main_category
            main_category_ver_str = str(main_category_ver)

        # sub category check
        sub_category = top.sub_category_var.get()
        if sub_category == "Whats the sub category":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the sub category box!')
        elif len(sub_category) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a sub category!')
        else:
            sub_category_ver = sub_category
            sub_category_ver_str = str(sub_category_ver)

        # quantity check
        quantity = top.quantity_var.get()
        if quantity == "How many planted?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the quantity box!')
        elif len(quantity) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a quantity!')
        else:
            quantity_ver = quantity
            quantity_ver_int = int(quantity_ver)

        # classification check
        classification = top.classification_var.get()
        if classification == "Whats the classification?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the classification box!')
        elif len(classification) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a classification!')
        else:
            classification_ver = classification
            classification_ver_str = str(classification_ver)

        # perennial or annual check
        per_ann = top.per_ann_var.get()
        if per_ann == "Am I Perennial or Annual?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the per ann box!')
        elif len(per_ann) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a per ann!')
        else:
            per_ann_ver = per_ann
            per_ann_ver_str = str(per_ann_ver)
              
        # seed class check
        seed_class = top.seed_class_var.get()
        if seed_class == "Whats the seed class?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the seed class box!')
        elif len(seed_class) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a seed class!')
        else:
            seed_class_ver = seed_class
            seed_class_ver_str = str(seed_class_ver)

        NewplantBE.new_plant_save_data(name_ver_str, main_category_ver_str, sub_category_ver_str, quantity_ver_int, date_ver, classification_ver_str, per_ann_ver_str, seed_class_ver_str)
        messagebox.showinfo(title = 'Congrats', message = 'Good Job!')


#def main(): tab the bottom 3 lines to work from main
root = Tk()
new_plant_gui = NewplantGUI(root)
root.mainloop()        
