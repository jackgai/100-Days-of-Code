import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

correct_answer = []
answer_len = data.shape[0]

while len(correct_answer) < answer_len:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/{answer_len} States Correct.",
                                    prompt="What's another state name?")
    answer_title_case = answer_state.title()
    if answer_title_case == "Exit":
        break

    state = data[data["state"] == answer_title_case]
    if state.empty:
        continue

    state_arr = state.values
    state_name = state_arr[0][0]
    x = state_arr[0][1]
    y = state_arr[0][2]

    state_label = turtle.Turtle()
    state_label.color("black")
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(x=x, y=y)
    state_label.write(f"{state_name}", align="center", font=FONT)

    correct_answer.append(answer_title_case)

learning_list = [state for state in data["state"].tolist() if state not in correct_answer]

df = pandas.DataFrame(learning_list, columns=["States"])
df.to_csv("states_leaning_list.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
