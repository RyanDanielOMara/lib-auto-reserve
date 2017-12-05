
def getInput(fileName):
	# Future thought, add room number to "entry" for multiple room bookings

	with open (fileName, "r") as file:
	    data = file.readlines()

	# Sanitize input for integers only
	# First line contains the room number
	room = ''.join([i for i in data[0] if i.isdigit()])

	db = [] # Database

	# Parse lines starting at line 1 (line 0 holds room number)
	for entry in data[1:]:

		entry = entry.split(',')

		#     [0]         [1]         [2]       [3]         [4]        [5]
		# First Hour, Second Hour, End Hour, First Name, Last Name, UB Email

		if "\n" in entry[5]:
			entry[5] = entry[5][:-1] # Removing "\n" from in [5]

		if entry[3] == "12:00am": # Prevent Day Error (also human error)
			entry[3] = "11:59pm"
		
		db.append(entry)

	# print(db)
	return room, db

getInput("DATABASE.csv")