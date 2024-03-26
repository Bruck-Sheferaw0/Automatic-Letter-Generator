names_list = []

with open("./Input/Names/invited_names.txt") as names:
    contents = names.read()
    names_list += contents.split('\n')
    print(names_list)


content = ""
with open("./Input/Letters/starting_letter.txt",'r') as template:
    content += template.read()


for i in names_list:
    letter_name = "letter_for_"+i
    with open(f"./Output/ReadyToSend/{letter_name}", 'w') as final_letter:
        final_letter.write(content.replace("[name],",i+","))












