# Attention Task

Web based cognitive task for children created with the Cognitive Development Laboratory at CMU

URL for the website: https://gcwhitfield.github.io/AttentionTask/

## What it does
1. Researcher and child open up attention task in web browser
2. Researcher and child connects to python server. Server will wait for both the researcher 
and child to connect. Server sends message back confirming that everyone is connected
3. The child will see the book, the researcher will see the comprehension questions
4. After the reading attention task has ended, researcher and child send message to the server.
The sever waits for both child and researcher to confirm before proceeding to the 
red smiley part.
5. Child sees the smile identification task, researcher sees screen showing # of 
tasks completed
6. At the end of the task, child sends info to server and server sends info to a secure
database.

## File descriptions
* python - contains server for attention task and test code
* unity-files - WebGL build from Unity
* index.html - html for the attention task website
* css - css files for attention task website