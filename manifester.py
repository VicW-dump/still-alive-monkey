import json

# Create a Monkeydo-compatible JSON
def compile(tasks,name):
	manifest = {
		"tasks": tasks
	}

	with open(f"../still-alive/monkeydo_{name}.json","w") as f:
		json.dump(manifest,f)

# Parse text file with inline events
def create_manifest(track_name,delay = 70):
	track_id = f"#{track_name}"

	# Get lines from file
	f = open(f"{track_name}.txt","r")
	lines = f.readlines()

	track = [] # Will contain each
	track.append([0,"lineFeed",track_id])

	# Add an event task to the track
	def event(key):
		def draw_art(key):
			return [0,"drawArt",key]

		events = {
			"B": [0,"blank",track_id],
			"C": [0,"playCredits"]
		}

		# Get event by key
		if(events.get(key)):
			return events.get(key)
		
		# Or treat as art if no key was found
		return draw_art(int(key))

	# Loop over each line and character in text file
	for line in lines:
		char_iter = iter(line)

		for char in char_iter:
			# Don't add line breaks, they have their own method lineFeed()
			if(char == "\n"):
				continue
			# Hash symbol indicates next character is an event key
			if(char == "#"):
				# Move cursor to the event key and call event()
				track.append(event(next(char_iter,None)))
				continue
			track.append([delay,"textFeed",char,track_id]) # Each char
		track.append([delay,"lineFeed",track_id]) # Each line break

	compile(track,track_name)

create_manifest("credits",70)
create_manifest("lyrics",100)