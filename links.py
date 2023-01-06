import webbrowser, os

logo="""\033[1;91m
 _     _  _      _  __ ____ 
/ \   / \/ \  /|/ |/ // ___\.
| |   | || |\ |||   / |    \.
| |_/\| || | \|||   \ \___ |
\____/\_/\_/  \|\_|\_\\____/\033[0m"""
print (logo)
print ("\033[95mFB/sharifansari00")
print ("")

# Prompt the user to enter the path to the file
path = input("\033[1;92m[$] Enter the path to the file containing the links: \033[0m")
path = os.path.expanduser(path)

# Open the file with the links
with open(path, 'r') as f:
    # Read the file line by line
    for line in f:
        # Strip leading and trailing white space from the line
        line = line.strip()
        # Open the link in Firefox
        webbrowser.get('firefox').open(line)
print ("")
print ("\033[1;93mProcess Complete")
