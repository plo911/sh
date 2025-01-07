import time
import requests

url = "https://discord.com/api/v9/users/@me/settings"

File = open("Words.txt", "r")
lines = File.readlines()

def ChangeStatus(message):

	header = {
	"authorization": "MTI4MzUzMjgxNzAwNjk4NTIxOA.GDVmoH.Uh11EWhtanDspw7lOgTdodm7K_YrzL6wXJQzlY"
	}

	jsonData = {
	"status": "online",
	"Custom_status": {
		"text": message
		}
	}
	requests = requests.patch(url, headers=header, json=jsonData)

	while True:

		for line in lines:

			ChangeStatus(line.split("\n")[0])
			time.sleep(3)