from turtle import Turtle,Screen
import pandas
turtle=Turtle()
text=Turtle()
text.penup()
screen = Screen()
screen.title("US STATE GAME")
img="blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

answer=screen.textinput(title="Guess the state",
                 prompt="guess a state's name?")

data = pandas.read_csv("50_states.csv")
game=True
score=0
guessed_state=[]
while game:

    for i in range(len(data)):
        j = data.state[i]
        if answer.casefold() == j.casefold():
            guessed_state.append(j)
            xocr=data.x[i]
            ycor=data.y[i]
            text.goto(xocr,ycor)
            text.write(j)
            score += 1
            answer = screen.textinput(title=f"Guess the state {score}/50",
                                      prompt="guess another state's name?")
        elif answer.casefold() == "exit":
                game = False
                break
    else:
        answer = screen.textinput(title=f"Guess the state {score}/50",
                                  prompt="Wrong, try guessing another state's name?")
        continue

misssedout_states=[]

for i in data.state:
    if i not in guessed_state:
        misssedout_states.append(i)

df = pandas.DataFrame(misssedout_states)
df.to_csv('Missed_states.csv')





# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()



