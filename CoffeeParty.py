<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd
#Reading data from public online google sheets collecting responses from google forms
df= pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTt2zTAl0BKc4VO8SZwexi2sHjAwryHhxEvgTHDpqYaZRFULG4ykJuiwTXSk9xEEJ4eWlpmRxBT_GrW/pub?output=xlsx')
#Creating new variables from headers
name="What is your name?"
email="What is your email?"
=======
=======
>>>>>>> fa80f54c3b6bb3554c0b8e9a96adeacda9b036de

#This function uses the lists with the participants, coversation_starters, and jokes to create random coffee drink groups\n",
# with a random joke and conversation starter\n",

import random #To use the random package\n",

def group_allocation(people, conversation_starters, jokes):
    
    min_group_size = 2  #To prevent people and up allone
    max_group_size = 5  #max size of the coffee group
    group_num = 1       #Starting number of the group key

    groups = {}         #dictonary to store the data

    while len(people) > 0:  #Loops until everybody is allocated to a group
        group_value =[]     #List that refreshes each round where the people, coverstation starter and joke is stored for a specific group

        #Chooses for each round a random number for the size of the group between the set min and max size
        group_size = random.randint(min_group_size, max_group_size) 


        #Checks how many people are left after the random group size is choosen 
        group_left = len(people) - group_size

        #If the group size chooses a number that resulted in somebody being left out, the loops starts again to create a new groupsize
        if group_left == 1:
            continue

        # If there are not enough people left to form a group of the chosen size, 
        # set the group size to the remaining number of people    

        if len(people) < group_size:
            group_size = len(people)


        # Take the first group_size people from the list of people and add them to a new group
        group = people[:group_size]

        # Remove the people in the group from the list of people
        people = people[group_size:]

        # Add the group to the list of group
        group_value.append(group)

        selected_starter = random.choice(conversation_starters) #picks an random conversation starter
        selected_joke = random.choice(jokes) # picks an random joke

        group_value.append(selected_starter) # adds the conversation starter to the group
        group_value.append(selected_joke) # adds joke to group

        group_key = "Group " + str(group_num) #Creates the name of the dictonary key for example \"Group 1\"
 
        groups[group_key] = group_value #Combines the key with its value

        group_num += 1 #Increases the group number with one
  
    return groups #Returns the dictonary with the selected group, conversation starter, and joke


   
#import random #To use the random package

#List of participants\n",
people = ["name 1","name 2","name 3","name 4","name 5","name 6","name 7","name 8",
          "name 9","name 10","name 11","name 12",
           "name 13","name 14","name 15","name 16"]

#List of conversaton starter\n",
conversation_starters = ["Start 1", "Start 2", "Start 3", "Start 4",
                         "Start 5", "Start 6", "Start 7", "Start 8"]

#List of jokes\n",
jokes = ["joke 1", "joke 2","joke 3","joke 4","joke 5","joke 6",
         "joke 7","joke 8","joke 9","joke 10","joke 11","joke 12" ] 

#Shuffels the list of participants to a random order
random.shuffle(people)

#Calls the function that randomly allocates the coffee drinkers with a joke and conversation starter\n",
groups = group_allocation(people,conversation_starters, jokes)

#part laila

import random

# define conversation starters file(s)
questions_file = 'questions.txt'
jokes_file = 'jokes.txt'
activity_file = 'activity.txt'

# Open the conversation starters file and read the lines
with open(questions_file, 'r') as file:
    questions = file.readlines()

# Open the jokes file and read the lines
with open(jokes_file, 'r', encoding='utf-8') as file:
    jokes = file.readlines()

# Open the activities file and read the lines
with open(activity_file, 'r') as file:
    activity = file.readlines()

# Shuffle the conversation starters
random.shuffle(questions)
random.shuffle(jokes)
random.shuffle(activity)

# Random conversation starter
random_question = random.choice(questions).strip()
random_joke = random.choice(jokes).strip()
random_activity = random.choice(activity).strip()

# Construct the message
message = "Hello everyone!\n\n"
message += "We are excited to let you know that you have been matched for a meeting.\n\n"
message += f"Here's your conversation starter:\n{random_question}\n\n"
message += f"And here's a joke to lighten the mood:\n{random_joke}\n\n"
message += f"Lastly, we thought you might enjoy doing this activity together:\n{random_activity}\n"

print(message)

### 8. The program generates messages to all groups which address the participants by name, inform
## them about having been matched for a meeting, and include the conversation starter. It saves these
## messages in one or multiple text files.

introtext = ""
for group in group_names:
    introduction = "Hey"
    for person in group:
        introduction += " " +person

    introduction += ", you have been matched for a meeting. To get the conversation started use X. \n \n"
    introtext += introduction



with open("introduction.txt", "wb") as file:
    file.write(introtext.encode("utf8"))

#prints the group dictionary in a nice order   

for i, group in enumerate(groups):
    print(f"Group {i+1}: {groups[group]}"),
 