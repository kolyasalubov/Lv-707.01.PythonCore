# Here we just ask the user's name

print ("Bot: What's your name buddy?")
user_name = input()

bot_template = "Bot: {0}"
user_template = user_name + " : {0}"

name = "Bot "
weather = 'rainy'
mood = "great"
ukraine = "Ukraine will win"

#Here I create a dictionary with keys as answers and values as different responses

responses = {
"what's your name?": [
"they call me {0}".format(name), 
"Sometimes I referred to as {0}".format(name),
"I can go by {0}".format(name),
"My name is  {0}".format(name)],

"what's the weathear outside?":[
"The weather is {0} :".format(weather),
"It's pretty {0}.".format(weather),
"Let me check the forecast, it looks like {0}".format(weather)],

"Are you a robot?": [ 
"What do you think?", 
"Most likely, yes, but ask Neo first!", 
"Yes, I am a robot with human feelings.", ],

"Do you enjoy politics?": [
"Not really, I'm just a simple-minded bot",
"Politics is dirty business, so not realy",
"No, but I were a human I'd be a commy"],

"Will Ukraine win?": [
"I have no doubt - {0}".format(ukraine),
"It's goona be a tough battle. But at the end of the day no doubt {0}".format(ukraine),
"Russia is a strong state, but {0}".format(ukraine)
],

"Now.Let's talk about your mood.How are you?": [ 
"I am feeling {0}".format(mood), 
"{0}! How about you?".format(mood), 
"I am {0}! How about yourself?".format(mood)
 ],

"": [ 
"Hey! Are you there?", 
"What do you mean by saying nothing?", 
"Sometimes saying nothing tells a lot :)" ],
"default": [
"this is a default message"] }

#Here I create a response function that will randomly respond to the question asked

import random


def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message]) 

    else:
        bot_message = random.choice(responses["default"])

    return bot_message    

# Here is so called relation function. This means if it finds
#the key word in the text it will return the question with this word

def related(text):
    if "name" in text:
        your_text = "what's your name?"
    elif "weather" in text:
        your_text = "what's the weathear outside?"
    elif "robot" in text:
        your_text = "Are you a robot?"
    elif "politics" in text:
        your_text = "Do you enjoy politics?"
    elif "ukraine" in text:
        your_text =  "Will Ukraine win?"
    elif "mood" in text:
        your_text = "Now.Let's talk about your mood.How are you?"   
    else:
        your_text = ""          
  
    return your_text

#Here the conversation in timeline order and response function

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

#Here is the while loop it's kinda our bot is listening to us here

while True:
    my_input = input()
    my_input = my_input.lower()
    related_text = related(my_input)
    send_message(related_text) 

    if my_input == "exit" or my_input == "stop":
        break