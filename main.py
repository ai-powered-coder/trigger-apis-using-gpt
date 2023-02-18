import openai
import requests
import json

def lights_on():
    print("Lights on")

def lights_off():
    print("Lights off")

def do_not_disturb():
    print("Do not disturb")

def bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['bpi']['USD']['rate_float']

def main():
    commands = ['lights_on', 'lights_off', 'do_not_disturb', 'bitcoin_price']
    commandsWithDashInFront = [f'-{command}' for command in commands]
    commandsAsString = '\n'.join(commandsWithDashInFront)

    statement = input(f'What would you like to do?')

    prompt = f'''
Statement:
{statement}
----
Choose a command that matches the statement from the list below: 
{commandsAsString}

You can choose "nothing" if there is no match.
-----
Chosen command:

'''
    
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)

    if completion.choices[0].text == 'lights_on':
        lights_on()
    elif completion.choices[0].text == 'lights_off':
        lights_off()
    elif completion.choices[0].text == 'do_not_disturb':
        do_not_disturb()
    elif completion.choices[0].text == 'bitcoin_price':
        print(bitcoin_price())
    elif completion.choices[0].text == 'nothing':
        print('No command matched')

main()
