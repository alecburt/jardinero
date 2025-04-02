from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from status_be import StatusBE
from pot_size_be import PotsizeBE
from location_be import LocationBE
from notes_be import NotesBE


class StatusGUI:
    def __init__(top, master):
        # TODO I am still looking into the top, master. I want this as a second window so I think I need top or NOT self but there are 
        # problems with the checkboxes needing self. 
        top.statusbe = StatusBE()
        top.potsizebe = PotsizeBE()
        top.locationbe = LocationBE()
        top.notesbe = NotesBE()
        master.title('Status')
        master.config(padx = 10, pady = 20) 
        master.iconbitmap('canary_icon.ico')
        top.canvas = Canvas(height=300, width=200)

        # flower image
        top.flower_image = ImageTk.PhotoImage(Image.open("flower.png"))
        top.top_pic = Label(image = top.flower_image)
        top.top_pic.grid(row = 0, column = 0, columnspan = 5)

        ### labels
        top.opening_label = Label(text = 'How am I doing? Tell me the good and the bad.', font=('', 14))
        top.opening_label.grid(row = 1, column = 0, columnspan = 5)
        top.instructions = Label(text = "How am I doing?")
        top.instructions.grid(row = 2, column = 0, columnspan = 2, sticky = 'W')
        top.instructions = Label(text = "Set the scale bar to my current rating.")
        top.instructions.grid(row = 4, column = 0, columnspan = 5, sticky = 'W')
        top.instructions = Label(text = "Tick all boxes that apply.")
        top.instructions.grid(row = 6, column = 0, columnspan = 5, sticky = 'W')
        top.pot_label = Label(text = "I'm getting a bigger house?", font=('', 14))
        top.pot_label.grid(row = 11, column = 0, columnspan = 5)
        top.pot_submitted_label = Label(text = 'Check the box to change the pot.  --->')
        top.pot_submitted_label.grid(row = 12, column = 0, sticky = 'W')
        top.location_label = Label(text = 'Nice moving house??', font=('', 14))
        top.location_label.grid(row = 14, column = 0, columnspan = 5)
        top.location_submitted_label = Label(text = 'Check the box to change the location.  --->')
        top.location_submitted_label.grid(row = 15, column = 0, sticky = 'W')
        top.note_label = Label(text = 'Please leave a note and a reason.', font=('', 14))
        top.note_label.grid(row = 19, column = 0, columnspan = 5)
        top.note_submitted_label = Label(text = 'Check the box to leave a note.  --->')
        top.note_submitted_label.grid(row = 20, column = 0, sticky = 'W')

        # status labels
        top.instructions = Label(text = "Rooting")
        top.instructions.grid(row = 7, column = 0, sticky = 'EW')
        top.instructions = Label(text = "Sprouting")
        top.instructions.grid(row = 7, column = 1, sticky = 'EW')
        top.instructions = Label(text = "Growing")
        top.instructions.grid(row = 7, column = 2, sticky = 'EW')
        top.instructions = Label(text = "Flowering")
        top.instructions.grid(row = 7, column = 3, sticky = 'EW')
        top.instructions = Label(text = "Harvesting")
        top.instructions.grid(row = 7, column = 4, sticky = 'EW')
        top.instructions = Label(text = "Dormant")
        top.instructions.grid(row = 9, column = 1, sticky = 'EW')
        top.instructions = Label(text = "Quarantine")
        top.instructions.grid(row = 9, column = 2, sticky = 'EW')
        top.instructions = Label(text = "DEAD")
        top.instructions.grid(row = 9, column = 3, sticky = 'EW')

        ### entries
        # plant id entry.
        top.plant_id_var = StringVar()
        def on_status_plant_id_entry_click(plant_id_var):
            if top.plant_id_entry.get() == "What is the Plant ID?":
                top.plant_id_entry.delete(0, tk.END)
                top.plant_id_entry.configure(foreground="black")
            
        def on_status_plant_id_entry_focus_out(event):
            if top.plant_id_entry.get() == "":
                top.plant_id_entry.insert(0, "What is the Plant ID?")
                top.plant_id_entry.configure(foreground="gray")
                    
        top.plant_id_entry = Entry(width = 15, borderwidth = 2, textvariable = top.plant_id_var, foreground="gray")
        top.plant_id_entry.insert(0, "What is the Plant ID?")

        top.plant_id_entry.bind("<FocusIn>", on_status_plant_id_entry_click)
        top.plant_id_entry.bind("<FocusOut>", on_status_plant_id_entry_focus_out)
        top.plant_id_entry.grid(pady = 10, row = 2, column = 0, sticky = 'NSEW')

        # date entry.
        top.date_var = StringVar()
        def on_status_date_entry_click(date_var):
            if top.date_entry.get() == "Enter the date. DD/MM/YY  ":
                top.date_entry.delete(0, tk.END)
                top.date_entry.configure(foreground="black")
            
        def on_status_date_entry_focus_out(event):
            if top.date_entry.get() == "":
                top.date_entry.insert(0, "Enter the date. DD/MM/YY  ")
                top.date_entry.configure(foreground="gray")
                    
        top.date_entry = Entry(width = 30, borderwidth = 2, textvariable = top.date_var, foreground="gray")
        top.date_entry.insert(0, "Enter the date. DD/MM/YY  ")

        top.date_entry.bind("<FocusIn>", on_status_date_entry_click)
        top.date_entry.bind("<FocusOut>", on_status_date_entry_focus_out)
        top.date_entry.grid(pady = 10, row = 2, column = 4, sticky = 'NSEW')

        # status entry check boxes
        top.check_rooting = IntVar() 
        top.check_sprouting = IntVar() 
        top.check_growing = IntVar() 
        top.check_flowering = IntVar() 
        top.check_harvesting = IntVar() 
        top.check_dormant = IntVar() 
        top.check_quarantine = IntVar() 
        top.check_dead = IntVar() 

        top.rooting_button = Checkbutton(root, variable = top.check_rooting, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.sprouting_button = Checkbutton(root, variable = top.check_sprouting, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.growing_button = Checkbutton(root, variable = top.check_growing, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.flowering_button = Checkbutton(root, variable = top.check_flowering, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.harvesting_button = Checkbutton(root, variable = top.check_harvesting, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.dormant_button = Checkbutton(root, variable = top.check_dormant, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.quarantine_button = Checkbutton(root, variable = top.check_quarantine, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.dead_button = Checkbutton(root, variable = top.check_dead, onvalue = 1, offvalue = 0, height = 2, width = 10) 
            
        top.rooting_button.grid(row = 8, column = 0) 
        top.sprouting_button.grid(row = 8, column = 1) 
        top.growing_button.grid(row = 8, column = 2) 
        top.flowering_button.grid(row = 8, column = 3) 
        top.harvesting_button.grid(row = 8, column = 4) 
        top.dormant_button.grid(row = 10, column = 1) 
        top.quarantine_button.grid(row = 10, column = 2) 
        top.dead_button.grid(row = 10, column = 3) 

        # rating scale
        # TODO scale bar currently needs to be moved off zero and back to zero for zero. Thats shit!
        def scale_event(value):
            global rating
            rating = value
            rating = int(rating)

        top.rating_scale = Scale(master, from_ = 0, to = 10, orient = HORIZONTAL, sliderlength = 100, command = scale_event)    
        top.rating_scale.grid(pady = 10, row = 5, column = 0, columnspan = 5, sticky = 'NSEW')

        # add extras checkboxes
        top.add_pot = IntVar()
        top.add_pot_select = Checkbutton(root, variable = top.add_pot, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.add_pot_select.grid(row = 12, column = 1)
        top.add_location = IntVar()
        top.add_location_select = Checkbutton(root, variable = top.add_location, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.add_location_select.grid(row = 15, column = 1)
        top.add_note = IntVar()
        top.add_note_select = Checkbutton(root, variable = top.add_note, onvalue = 1, offvalue = 0, height = 2, width = 10) 
        top.add_note_select.grid(row = 20, column = 1)

        ### buttons
        # search button.
        top.search_button = Button(width = 15, text = "Search")
        top.search_button.grid(pady = 10, row = 2, column = 2)

        # submit button
        top.submit_button = Button(width = 15, text = "Submit All", command = top.submit_all)
        top.submit_button.grid(pady = 10, row = 30, column = 0, sticky = 'NSEW')

        #####
        # pot entries.
        # pot size entry
        top.pot_size_var = StringVar()
        def on_pot_size_entry_click(pot_size_var):
            if top.pot_size_entry.get() == "What's the size? Small, large, tree.":
                top.pot_size_entry.delete(0, tk.END)
                top.pot_size_entry.configure(foreground="black")
            
        def on_pot_size_entry_focus_out(event):
            if top.pot_size_entry.get() == "":
                top.pot_size_entry.insert(0, "What's the size? Small, large, tree.")
                top.pot_size_entry.configure(foreground="gray")
                    
        top.pot_size_entry = Entry(width = 30, borderwidth = 2, textvariable = top.pot_size_var, foreground="gray")
        top.pot_size_entry.insert(0, "What's the size? Small, large, tree.")

        top.pot_size_entry.bind("<FocusIn>", on_pot_size_entry_click)
        top.pot_size_entry.bind("<FocusOut>", on_pot_size_entry_focus_out)
        top.pot_size_entry.grid(row = 13, column = 0, sticky = 'NSEW')

        # pot material entry
        top.pot_material_var = StringVar()
        def on_pot_material_entry_click(pot_material_var):
            if top.pot_material_entry.get() == "What's it made of? , Plastic, ceramic, canvas":
                top.pot_material_entry.delete(0, tk.END)
                top.pot_material_entry.configure(foreground="black")
            
        def on_pot_material_entry_focus_out(event):
            if top.pot_material_entry.get() == "":
                top.pot_material_entry.insert(0, "What's it made of? , Plastic, ceramic, canvas")
                top.pot_material_entry.configure(foreground="gray")
                    
        top.pot_material_entry = Entry(width = 30, borderwidth = 2, textvariable = top.pot_material_var, foreground="gray")
        top.pot_material_entry.insert(0, "What's it made of? , Plastic, ceramic, canvas")

        top.pot_material_entry.bind("<FocusIn>", on_pot_material_entry_click)
        top.pot_material_entry.bind("<FocusOut>", on_pot_material_entry_focus_out)
        top.pot_material_entry.grid(row = 13, column = 2, sticky = 'NSEW')

        # pot shape entry
        top.pot_shape_var = StringVar()
        def on_pot_shape_entry_click(pot_shape_var):
            if top.pot_shape_entry.get() == "What shape am I? Flower, square, round.":
                top.pot_shape_entry.delete(0, tk.END)
                top.pot_shape_entry.configure(foreground="black")
            
        def on_pot_shape_entry_focus_out(event):
            if top.pot_shape_entry.get() == "":
                top.pot_shape_entry.insert(0, "What shape am I? Flower, square, round.")
                top.pot_shape_entry.configure(foreground="gray")
                    
        top.pot_shape_entry = Entry(width = 30, borderwidth = 2, textvariable = top.pot_shape_var, foreground="gray")
        top.pot_shape_entry.insert(0, "What shape am I? Flower, square, round.")

        top.pot_shape_entry.bind("<FocusIn>", on_pot_shape_entry_click)
        top.pot_shape_entry.bind("<FocusOut>", on_pot_shape_entry_focus_out)
        top.pot_shape_entry.grid(row = 13, column = 4, sticky = 'NSEW')

        # location entry.
        top.location_var = StringVar()
        def on_location_entry_click(location_var):
            if top.location_entry.get() == "Where's my new home?":
                top.location_entry.delete(0, tk.END)
                top.location_entry.configure(foreground="black")
            
        def on_location_entry_focus_out(event):
            if top.location_entry.get() == "":
                top.location_entry.insert(0, "Where's my new home?")
                top.location_entry.configure(foreground="gray")
                    
        top.location_entry = Entry(width = 30, borderwidth = 2, textvariable = top.location_var, foreground="gray")
        top.location_entry.insert(0, "Where's my new home?")

        top.location_entry.bind("<FocusIn>", on_location_entry_click)
        top.location_entry.bind("<FocusOut>", on_location_entry_focus_out)
        top.location_entry.grid(row = 16, column = 0, sticky = 'NSEW')
        
        # note entry.
        top.note_var = StringVar()
        def on_note_entry_click(note_var):
            if top.note_entry.get() == "Please write a note.":
                top.note_entry.delete(0, tk.END)
                top.note_entry.configure(foreground="black")

        def on_note_entry_focus_out(event):
            if top.note_entry.get() == "":
                top.note_entry.insert(0, "Please write a note.")
                top.note_entry.configure(foreground="gray")
                
        top.note_entry = Entry(width = 30, borderwidth = 2, textvariable = top.note_var, foreground="gray")
        top.note_entry.insert(0, "Please write a note.")

        top.note_entry.bind("<FocusIn>", on_note_entry_click)
        top.note_entry.bind("<FocusOut>", on_note_entry_focus_out)
        top.note_entry.grid(row = 21, column = 0, columnspan = 5, sticky = 'NSEW')
                
        # reason entry.
        top.reason_var = StringVar()
        def on_reason_entry_click(note_var):
            if top.reason_entry.get() == "What's the note about?":
                top.reason_entry.delete(0, tk.END)
                top.reason_entry.configure(foreground="black")

        def on_reason_entry_focus_out(event):
            if top.reason_entry.get() == "":
                top.reason_entry.insert(0, "What's the note about?")
                top.reason_entry.configure(foreground="gray")
                
        top.reason_entry = Entry(width = 30, borderwidth = 2, textvariable = top.reason_var, foreground="gray")
        top.reason_entry.insert(0, "What's the note about?")

        top.reason_entry.bind("<FocusIn>", on_reason_entry_click)
        top.reason_entry.bind("<FocusOut>", on_reason_entry_focus_out)
        top.reason_entry.grid(row = 22, column = 0, sticky = 'NSEW')  
                
    #####

    # save data
    def submit_all(top):
        # plant id check
        plant_id = top.plant_id_var.get()
        if plant_id == "What is the Plant ID?":
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the plant id box!')
        elif len(plant_id) == 0:
            messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a plant id!')
        else:
            plant_id_ver = plant_id
            plant_id_ver_int = int(plant_id_ver)

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

        # check boxes
        rooting = top.check_rooting.get()
        sprouting = top.check_sprouting.get() 
        growing = top.check_growing.get() 
        flowering = top.check_flowering.get() 
        harvesting = top.check_harvesting.get() 
        dormant = top.check_dormant.get() 
        quarantine = top.check_quarantine.get() 
        dead = top.check_dead.get() 

        # rating check 
        rating_ver_int = rating

        # add note checkbox
        add_pot_select = top.add_pot.get()
        add_location_select = top.add_location.get()
        add_note_select = top.add_note.get()
        
        top.statusbe.status_save_data(date_ver, plant_id_ver, rooting, sprouting, growing, flowering, harvesting, dormant, quarantine, dead, rating_ver_int)
        messagebox.showinfo(title = 'Congrats', message = 'Good Job!\nStatus Updated.')

        if add_pot_select == 1:
            ### pot
            # pot size check
            pot_size = top.pot_size_var.get()
            if pot_size == "What's the size? Small, large, tree.":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the pot size box!')
            elif len(pot_size) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a pot size!')
            else:
                pot_size_ver = pot_size

            # pot material check
            pot_material = top.pot_material_var.get()
            if pot_material == "What's it made of? , Plastic, ceramic, canvas":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the pot material box!')
            elif len(pot_material) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a pot material!')
            else:
                pot_material_ver = pot_material

            # pot shape check
            pot_shape = top.pot_shape_var.get()
            if pot_shape == "What shape am I? Flower, square, round.":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the pot shape box!')
            elif len(pot_shape) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a pot shape!')
            else:
                pot_shape_ver = pot_shape
                
            top.potsizebe.pot_size_save_data(pot_size_ver, pot_material_ver, pot_shape_ver, date_ver, plant_id_ver_int)
            messagebox.showinfo(title = 'Congrats', message = 'Good Job!\nPot Size Updated.')
        else:
            messagebox.showinfo(message = 'No pot added.')

        if add_location_select == 1:
            # location check
            location = top.location_var.get()
            if location == "Where's my new home?":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the location box!')
            elif len(location) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a note!')
            else:
                location_ver = location
            
            top.locationbe.location_save_data(location_ver, date_ver, plant_id_ver_int)
            messagebox.showinfo(title = 'Congrats', message = 'Good Job!\nLocation Updated.')
        else:
            messagebox.showinfo(message = 'No location added.')

        if add_note_select == 1:
            # note check
            note = top.note_var.get()
            if note == "Please write a note.":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the note box!')
            elif len(note) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a note!')
            else:
                note_ver = note
                
            # reason check
            reason = top.reason_var.get()
            if reason == "What's the note about?":
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you clear the reason box!')
            elif len(reason) == 0:
                messagebox.showinfo(title = 'Warning', message = 'Please make sure you add a reason!')
            else:
                reason_ver = reason

            top.notesbe.note_save_data(date_ver, plant_id_ver, note_ver, reason_ver)
            messagebox.showinfo(title = 'Congrats', message = 'Good Job!\nNote Updated.')
        else:
            messagebox.showinfo(message = 'No note added.')
 


root = Tk()
status_gui = StatusGUI(root)
root.mainloop()        
