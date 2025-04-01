# jardinero
My gardening app

Welcome to my gardening app Jardinero.

A few pointers about my gardening first:

	I have a terrace growing trees which are long term so I want to create a history.
	I also grow vegetables I want to create a history/comparison of the timings, cultivars, pot size etc and to accurately look at harvest weights so I can improve year on year.
	I have a bunch of indoor house plants and cactus. I want to use a lot of the practices above but I'm a bit more focused on the watering/fertiliser on these plants as it is more controlled.
	I have somewhere in the region of 100+- plants growing at all times.

How the app is built:

	Primarily built with python.
    	I am using a SQL database using python's SQLite3 library. 
    		I am currently only using DB browser to see the database but I plan to
	  		start moving to DBeaver once I have a better understanding.
    	The inputs I am using a TKinter GUI.
    		I will be continuosly updating this and adding bits as I get them ready
	  		the details on those will be below.

Forward Plan:

	I want to keep collecting information and making the inputs is a priority here's the status.
    Main Window - main.py
    	I am not sure how I want this yet it is currently just a window to open a class in another file.
        	I have a lot of very different ideas for this but I do want to set up a title window first to load the other input GUI windows.
    Status - status.py
    	Sets the rating out of 10.
    	Sets what the plant is currently doing.
    	Location - location.py
        	Sets where the location is.
    	Pot Size - pot_size.py
        	I need to change this to make the pots more specific and use cm's not big/small
        	Sets the pot size.
      	Notes - Notes.py
        	I need to work on the catagories of the notes I will look at when I have more notes to evaluate.
        	Adds a note this will be on the bottom of most windows.
    Harvest - harvest.py
      Add a harvest weight in grams standard but can be changed plus the quantity if needed.
      I would like something in the future to tell me if it is the first or last harvest so I am prompted to update status.
      I have come up with a problem of plants being too close together so I would like a joint harvest possibility.

  I want to set up the queries.
    Every quarter I want to add 3 more queries with table.

  I want to set up some graphical charts/ tables.
    Every quarter I want to produce a quarterly update.

I will update as I go along and hopefully make things clearer as I update things they will be updated in pieces at the minute.

Also this readme needs a lot of work.

  
    
