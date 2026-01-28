import requests
parameters= {
    "amount": 10,
    "type": "boolean",
}

newresponse=requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean", params=parameters)
newresponse.raise_for_status()
quizdata=newresponse.json()

questiondata=quizdata["results"]
print (questiondata)