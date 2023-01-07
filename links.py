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
print ("\033[1;90m >> Type example.txt\033[0m\n")
path = input("\033[1;92m[$] Enter the path to the file containing the links: \033[0m")
print("")
path = os.path.expanduser(path)

# How many Links in your list
try:
    # Open the file with the links
    with open(path, 'r') as f:
        # Read the file line by line
        line_num = 0
        for line in f:
            line_num += 1
    print("\033[1;93m  >> This file has {} lines.\033[0m\n".format(line_num))
except FileNotFoundError:
    print("\033[1;91m  >> Error: File not found.\033[0m\n")
    exit()

# Prompt the user to enter the starting line of the links
start_line = input("\033[1;92m[$] Enter the starting line of the links you want to open: \033[0m")

# Prompt the user to enter the ending line of the links
end_line = input("\033[1;92m[$] Enter the ending line of the links you want to open: \033[0m")

# Open the file with the links
with open(path, 'r') as f:
    # Read the file line by line
    line_num = 0
    for line in f:
        line_num += 1
        # If the current line number is within the specified range, open the link
        if line_num >= int(start_line) and line_num <= int(end_line):
            # Strip leading and trailing white space from the line
            line = line.strip()
            # Open the link in Firefox
            # If you want to open links in Chrome, rename Firefox to Google Chrome.
            webbrowser.get('firefox').open(line)
            
print("")
print ("\033[1;93m  >> Links opened successfully!\033[0m\n")
