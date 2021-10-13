#a121_catch_a_turtle.py
#-----import statements----
import turtle 
import random as rand
from typing import Mapping
import leaderboard as lb

#----game configuration----
turtle_color = ["red", "green", "blue", "orange", "yellow", "Purple", "black"]
turtle_size=5
turtle_shape = ["turtle", "circle", "triangle" ]
score = 0
font_setup=("Arial", 20, "normal")
timer = 5
counter_interval = 1000
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
lrader_names_list = []
leader_scores_list = []
player_name = input("Enter your name:")

#-----initialize turtle-----
MrTurtle=turtle.Turtle()
MrTurtle.fillcolor(rand.choice(turtle_color))
MrTurtle.shape(rand.choice(turtle_shape))
MrTurtle.shapesize(turtle_size)
MrTurtle.penup()
score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(-200,200)
score_writer.hideturtle()
counter=turtle.Turtle()
counter.penup()
counter.goto(200,200)
counter.hideturtle()

#-----game functions-----
#print("Mr.Turtle was clicked")

def turtle_clicked(x,y):
    
    if timer_up == True:
        MrTurtle.hideturtle()
    else:
        update_score()
        MrTurtle.hideturtle()
        MrTurtle.fillcolor(rand.choice(turtle_color))
        MrTurtle.shape(rand.choice(turtle_shape))
        change_position()
        MrTurtle.showturtle()

def change_position():
    new_xpos = rand.randint(-175,175)
    new_ypos = rand.randint(-175,175)
    MrTurtle.hideturtle()
    MrTurtle.goto(new_xpos,new_ypos)
    MrTurtle.showturtle()
    

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)
    print(score)

def countdown():
    global timer, timer_up
    counter.clear()
    if (timer <= 0):
        counter.write("time's up", font = font_setup)
        timer_up = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1 
        counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)



#-----events-----
MrTurtle.onclick(turtle_clicked)


wn=turtle.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()