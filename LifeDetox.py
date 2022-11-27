import discord
import cohere
import os
from cohere.classify import Example
from replit import db

#For the line below, you must have your own Cohere API key (I removed mine for obvious reasons). You can get started at cohere.ai
co = cohere.Client('')

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)

#Trigger Warning
#Trigger Warning
#Please be mature about this!
#I had to use a lot of very bad words in order to teach the bot what is NOT acceptable to say. 
#Please do not read the examples if you are sensitive to harsh language. I wanted the bot to be effective at filtering out very nasty language.
#I do not condone the use of any of the toxic words below
#The examples had to be rather lengthy and mimic speech due to the nature of the Cohere machine learning algorithm.

examples = [
  Example("You are stupid as fuck", "Toxic"),
  Example("Don't give me that shit", "Toxic"),
  Example("Go to hell man", "Toxic"),
  Example("Give it to me mother fucker", "Toxic"),
  Example("You are a dumb bastard", "Toxic"),
  Example("Don't be a little bitch", "Toxic"),
  Example("Why are you such a cunt?", "Toxic"),
  Example("Kill Yourself", "Toxic"),
  Example("kys", "Toxic"),
  Example("fuck", "Toxic"),
  Example("You are so stupid", "Toxic"),
  Example("You deserve to die", "Toxic"),
  Example("Don't be such a retard", "Toxic"),
  Example("You are retarded", "Toxic"),
  Example("You are a fucking idiot", "Toxic"),
  Example("Damn it man", "Toxic"),
  Example("Fucking crazy man", "Toxic"),
  Example("You're an idiot!", "Toxic"),
  Example("Idiot!", "Toxic"),
  Example("yo how are you", "Benign"),
  Example("I'm curious, how did that happen", "Benign"),
  Example("Try that again", "Benign"),
  Example("Hello everyone, excited to be here", "Benign"),
  Example("I think I saw it first", "Benign"),
  Example("That is an interesting point", "Benign"),
  Example("I love this", "Benign"),
  Example("We should try that sometime", "Benign"),
  Example("You should go for it", "Benign"),
  Example("You are awesome!", "Benign"),
  Example("You aren't stupid!", "Benign"),
  Example("You deserve happiness", "Benign"),
  Example("No that's not true", "Benign"),
  Example("Yes sure, that's ok", "Benign"),
  Example("Yes I agree with that", "Benign"),
  Example("I respectfull disagree", "Benign"),
  Example("XD", "Benign"),
  Example("It's good man", "Benign"),
  Example("Bruh", "Benign"),
  Example("also", "Benign"),
  Example("Exciting!", "Benign"),
  Example("Cool!", "Benign"),
  Example("Hey man", "Benign")
]

if "responding" not in db.keys():
  db["responding"] = True


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if db["responding"]:
    if message.author != client.user:
      messageArray = [message.content]
      response = co.classify(model='large',
                             inputs=messageArray,
                             examples=examples)

      if response.classifications[0].prediction == "Toxic":
        await message.delete()
        await message.channel.send(
          "Your message has been deleted because it was detected to be toxic.")

  if message.content.startswith("$responding"):
    value = message.content.split("$responding ", 1)[1]

    if value.lower() == "on":
      db["responding"] = True
      await message.channel.send("Responding is on.")

    if value.lower() == "off":
      db["responding"] = False
      await message.channel.send("Responding is off.")

#This final line will not work because the Token is hidden in an environment variable on my personal replit. 
#This code is to demonstrate how I made the bot work only. Downloading this code onto your computer and running it will not make your bot work. 
#You have to do a lot of work on the discord developer portal side of things to make everything functional. 
#You can explore that on your own here: https://discord.com/developers/applications
#If you get far enough to make your own token, you can paste all of this code into replit.com and use your own token to create your own bot. 
#Happy coding!
      
client.run(os.getenv('Token'))
