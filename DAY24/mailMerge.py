PLACEHOLDER="[name]"

with open("DAY24/Mail_Merge/Input/Names/invited_names.txt") as file:
    names=file.readlines()
    
with open("DAY24/Mail_Merge/Input/Letters/strating_letter.txt") as letter:
    content=letter.read()
    for name in names:
        new_name=name.strip()
        new_letter=content.replace(PLACEHOLDER, new_name)
        with open(f"DAY24/Mail_Merge/Output/ready_2_send/letter_for_{new_name}.docx", mode="w")as completed_letter:
            completed_letter.write(new_letter)
