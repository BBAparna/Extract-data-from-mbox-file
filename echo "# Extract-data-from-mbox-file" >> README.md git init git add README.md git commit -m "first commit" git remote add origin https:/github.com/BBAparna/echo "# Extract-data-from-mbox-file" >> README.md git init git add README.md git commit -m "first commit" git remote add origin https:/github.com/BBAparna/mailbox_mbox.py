import mailbox
 import re
 
for message in mailbox.mbox('path.mbox'):  # give the path where mbox file is saved
    mbox_string = message.as_string()   # save the extracted messages 
    # print(mbox_string)
# regex to extract emails from the mbox     
regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
match = re.findall(regex, mbox_string) # reading  email ids from the extracted messages
for m in match:
    print(m)
    
 
