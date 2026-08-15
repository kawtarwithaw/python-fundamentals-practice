#Extract all email addresses from a .txt file and save them to another file
import re
file=input("Enter the name of the text file: ")
new_file=input("Enter the name of the other text file: ")
emails=re.findall(r'[\w.-]+@[\w.-]+', open(file).read())
with open(new_file,'w') as f:
    for email in emails:
        f.write(email+'\n')
    
        

        
            