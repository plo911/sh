import time
import requests

url = "https://discord.com/api/v9/users/1283532817006985218/profile" 

File = open("Words.txt", "r")
lines = File.readlines()

def ChangeStatus(message):

	header = {
	Authorization?: "MTI4MzUzMjgxNzAwNjk4NTIxOA.G632vv.2I9MHd0pdKHXhFWuF8lAI5HUgONr6n212eNRz8";
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
