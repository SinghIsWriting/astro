import colorama
from colorama import Fore
colorama.init(autoreset=True)
from datetime import datetime    # datetime module to get current date
import requests   # request library for scrapping the data from NASA website
from gtts import gTTS   # Google-Text-To-Speach library for saving text as audio file
from playsound import playsound   # playsound module for playing audio file

# Include your NASA open API key here, visit https://api.nasa.gov/
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXX"

# Definig a function that takes start and ending dates primarily and extract asteroid information from the NASA website
def astro(start_date, end_date, comment):
	url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
	r = requests.get(url)
	Data = r.json()    # Data json found about asteroids

	try:
		# Extracting info from data json
		total_astroids = Data['element_count']
		close_objects = Data['near_earth_objects']
		print(f"{Fore.YELLOW}\nTotal number of astroids:",total_astroids)
		danger = []
		toSpeak = ""
		for body in close_objects[start_date]:
			id = body['id']
			name = body['name']
			mag = body['absolute_magnitude_h']
			dia = str(body['estimated_diameter']['kilometers']['estimated_diameter_min'])+" - "+str(body['estimated_diameter']['kilometers']['estimated_diameter_min'])+" kilometers"
			haz = body['is_potentially_hazardous_asteroid']
			vel = str(body['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])+" km/hrs"
			orbit = body['close_approach_data'][0]['orbiting_body']
			missd = str(body['close_approach_data'][0]['miss_distance']['miles'])+" miles"
			aptime = body['close_approach_data'][0]['close_approach_date_full']

			magnitude = "Magnitude"
			diameter = "Diameter"
			potential = "Potential Hazardous?"
			velocity = "Relative Velocity"
			orbBody = "Orbiting Body"
			missingDistance = "Missing Distance"

			print(f"{Fore.GREEN}Id:", (id),
				f"{Fore.GREEN}Name:", (name),
				f"{Fore.CYAN}\n\t{magnitude:>25} :", (mag),
				f"{Fore.CYAN}\n\t{diameter:>25} :", (dia),
				f"{Fore.CYAN}\n\t{potential:>25} :", (haz),
				f"{Fore.CYAN}\n\t{velocity:>25} :", (vel),
				f"{Fore.CYAN}\n\t{orbBody:>25} :", (orbit),
				f"{Fore.CYAN}\n\t{missingDistance:>25} :", (missd),
				f"{Fore.CYAN}\n\t Approaching to the Earth :", (aptime))
			print()
			danger.append(str(body['close_approach_data'][0]['miss_distance']['miles']))
		if comment == "today":
			toSpeak = f"There are {total_astroids} asteoids near the Earth {comment}. "+f"The closest astroid approaching to earth is {round(float(min(danger)), 3)} miles away from our earth."
			print(f"{Fore.RED}The Closest approaching astroid is",min(danger),f"{Fore.RED}miles away from earth.")
		else:
			toSpeak = f"There were {total_astroids} asteoids near the Earth {comment}. "+f"The closest astroid approaching to earth was {round(float(min(danger)), 3)} miles away from our earth."
			print(f"{Fore.RED}The Closest approaching astroid was",min(danger),f"{Fore.RED}miles away from earth.")
		
		# Creating an audio file to speak the output in short brief
		sound = gTTS(toSpeak, lang="en")
		sound.save("file.mp3")
		print(f"{Fore.GREEN}Total number of astroids near the earth:", total_astroids)
		print()
		playsound("file.mp3")
	except:
		print(f"{Fore.YELLOW}\nWARNING: Opps, something went wrong!")
		print("[*] Date format is", f"{Fore.CYAN}yyyy-mm-dd", "and there must be max 7 days difference between both dates.\n")

if __name__ == "__main__":
	while(True):
		print("-"*70, "\n\t\t*********", f"{Fore.CYAN}Realtime Asteroid Tracker - NASA", "**********\n")
		print("[1]      Asteroids Today\n[2]      Asteroids in a Time-Interval\n[3]      Exit\n\n[*] Date format is", f"{Fore.CYAN}yyyy-mm-dd", "and there must be max 7 days difference between both dates.\n")
		usr = input("Enter your option: ")
		if usr == "1":
			start_date = datetime.now().strftime("%Y-%m-%d")
			end_date = datetime.now().strftime("%Y-%m-%d")
			astro(start_date, end_date, "today")
		elif usr == "2":
			start_date = input("Enter the start date to get astroids info: ")
			end_date = input("Enter the end date to get astroids info: ")
			astro(start_date, end_date, " in this time interval")
		elif usr == "3":
			print("\nThanks for using this script :)")
			break
		else:
			print(f"{Fore.YELLOW}\nWARNING: Invalid Input!\n")
