# Attention Task

Web based cognitive task for children created with the Cognitive Development Laboratory at CMU

URL for the website: https://gcwhitfield.github.io/AttentionTask/

## What it does
1. Researcher and child open up attention task in web browser
2. Researcher and child connects to python server. Server will wait for both the researcher 
and child to connect. Server sends message back confirming that everyone is connected
3. The child will see the book, the researcher will see the comprehension questions
4. After the reading attention task has ended, researcher and child send message to the server
The sever waits for both child and researcher to confirm before proceeding to the 
red smiley part
5. Child sees the smile identification task, researcher sees screen showing # of 
tasks completed
6. At the end of the task, child sends info to server and server sends info to a secure
database

## File descriptions
* python - contains server for attention task and test code
* unity-files - WebGL build from Unity
* index.html - html for the attention task website
* css - css files for attention task website

# How to run the python code (MacOS)
I'm using `pipenv` to manage my python virtual environment. You need to install `pipenv` first

## Installing pipenv
1. You need to install Homebrew first. Follow the directions on https://brew.sh/
2. type `brew install pipenv`

## Running the code inside of the virtual environment.
1. Move into the AttentionTask/python folder and type `pipenv shell`. This will activate the environment. Now you should be able to run the python scripts in AttentionTask/python
2. To exit the environment, type `exit`
