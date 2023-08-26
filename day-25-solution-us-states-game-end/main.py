import turtle
import pandas

# Setting up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/benlinn/Python Course/100DaysOfCode/day-25-solution-us-states-game-end/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Use absolute path for the CSV file
csv_path = "/Users/benlinn/Python Course/100DaysOfCode/day-25-solution-us-states-game-end/50_states.csv"
data = pandas.read_csv(csv_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]

        # Also using an absolute path to save the new CSV
        new_csv_path = "/Users/benlinn/Python Course/100DaysOfCode/day-25-solution-us-states-game-end/states_to_learn.csv"
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(new_csv_path)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
