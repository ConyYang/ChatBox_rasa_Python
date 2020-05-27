
### This is a chatbox implemented using python package rasa

To run this on your computer, follow the following steps: 
Type this in terminal:
 - pip install rasa
 - rasa init
2. cd timezonebot
3. if you want add more features to this chatbox. Change the nlu.md, 
stories.md in data file and domain.yml. Then train the model by typing 
"rasa train" in the terminal. It may takes you a few seconds to finish 
the training.
4. type "/stop" in terminal to end your talk.

This chatbox has the these functions
1. To check up the time zone of a city
2. To give feedback to your mood. If you feel sad, it will send you a photo of tiger.
3. Show you the profile of the most NB person in NTU