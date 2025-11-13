import turtle,pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def write_on_map(word, location):
    font = ("Courier", 10, "normal")
    words = turtle.Turtle()
    words.penup()
    words.hideturtle()
    words.goto(location)
    words.write(f"{word}", move=True, align='center', font=font)


guessed = []
score = 0
keep_guessing = bool(score != 50)
#loop to keep guessing
while keep_guessing:
    data = pd.read_csv("50_states.csv")
    total_score = len(data["state"])
    answer_state = screen.textinput(title=f"{score}/{total_score} States Correct", prompt="What's another state's name?").title()

    #want to exit
    if answer_state == "Exit":
        break


    #Check if the guess is among the 50 states
    data = data[data.state == answer_state]

    contain_data = bool(not data.empty)

    data_dict = data.to_dict(orient='list')
    print(data_dict)
    #write correct guesses is among the 50 states
    if contain_data:
        state = data_dict["state"][0]
        x_coordinate = data_dict["x"][0]
        y_coordinate = data_dict["y"][0]
        map_position = (x_coordinate, y_coordinate)

        guessed.append(state)

        score +=1
        write_on_map(state,map_position)


#states to learn, save the un-guessed state
states_to_learn = []

all_data = pd.read_csv("50_states.csv")

#turn our data into lists
all_state = all_data.state.to_list()
#compare guessed into all state list
for state in all_state:

    if state in guessed:
        continue
    #if not already guessed then save it into states to learn list
    else:
        states_to_learn.append(state)


#save the states to learn as a csv file
data_to_learn = {
    "states":states_to_learn,
}

save_data = pd.DataFrame(data_to_learn)
save_data.to_csv("state_to_learn.csv")

print(states_to_learn)
