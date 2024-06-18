import turtle as t
import pandas as p

screen=t.Screen()
screen.title("U.S. State Game")
image="DAY25/US state Game/blank_states_img.gif"
screen.addshape(image)
t.shape(image)


data=p.read_csv("DAY25/US state Game/50_states.csv")
all_states=data.state.to_list()

guessed=[]

while len(guessed)<50:
    answer=screen.textinput(title=f"{len(guessed)}/50 State Correct",prompt="What's another state's name?").title()

# if answer state is one of the states in all states from csv file
    if answer=="Exit":
        missing=[]
        for state in all_states:
            if state not in guessed:
                missing.append(state)
        new_data=p.DataFrame(missing)
        new_data.to_csv("DAY25/US state Game/mssing_state.csv")
        break
    if answer in all_states:
        guessed.append(answer)
        a=t.Turtle()
        a.hideturtle()
        a.penup()
        state_data=data[data.state==answer]
        a.goto(int(state_data.x),int(state_data.y))
        a.write(answer)




