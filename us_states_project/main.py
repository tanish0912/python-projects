from turtle import Turtle,Screen
import pandas as pd
tim = Turtle()
tim.hideturtle()

screen = Screen()
screen.title("US-States Game")
screen.setup(width=725,height=491)
screen.register_shape("blank_states_img.gif")
screen.bgpic("blank_states_img.gif")


game_is_on = True
input_list = []
count = 0
while game_is_on:

  user_input = screen.textinput(f"Score {count}/50.", "Enter something:")
  find_state = user_input.title()
  file = pd.read_csv("50_states.csv")
  list_of_states = file.state.tolist()
  if user_input == "Exit":
      missing_states = [state for state in list_of_states if state not in input_list]
      new_data = pd.DataFrame(missing_states)
      new_data.to_csv("states_to_learn.csv")
      break

  state_data = file[file.state == find_state]

  if find_state in list_of_states:
       tim.penup()
       tim.goto(int(state_data.x),int(state_data.y))
       if find_state in input_list:
           pass
       else:
          tim.write(f"{find_state}", align="center", font=("Arial", 8, "normal"))
          input_list.append(find_state)
          count += 1

screen.exitonclick()


