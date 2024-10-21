import time
from sty import ef,fg,rs

while True:
    try:
        name=input(f"{fg.black}{ef.b}Enter Your Name: {rs.all}")
        age=int(input(f"{fg.black}{ef.b}Enter Your Age: {rs.all}"))
        if age >=10 and age<=60:
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(2)
            print(f"{fg.cyan}{ef.i}WellCome To Adventure Game!{rs.all}")
            break
        else:
            print(f"{fg.cyan}{ef.i}You are not playing{fg.rs}{fg.da_blue}\nSorry!{rs.all}")  
    except ValueError:
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(2)
        print(f"{fg.cyan}{ef.i}Invalid Statement!{rs.all}")
try:
    path=input(f"{fg.cyan}{ef.i}You have two ways.{rs.all}{fg.black}{ef.b}\nChose one (left or right): {rs.all}")
    if path.lower().strip()=="left":
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(2)
        print(f"{fg.cyan}{ef.i}WellCome to the long road.\nNow you are looking a bike and a car.{rs.all}")
        ride=input(f"{fg.black}{ef.b}Which vechicle you will chose form both: {rs.all}")
        if ride.lower().strip()=="bike":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(2)
            print(f"{fg.cyan}{ef.i}You are driving, and cool air was touching your face.\nyou are enjoing your trip,\
 Suddenly a truck has come in front of you{rs.all}")
            ride2=input(f"{fg.black}{ef.b}Which side you will turn (left or right): {rs.all}")
            if ride2.lower().strip()=="left":
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(2)
                print(f"{fg.cyan}{ef.i}You are saved.\nyour speed of bike will be slow, and finally you will enjoy your way.\nGood luck{rs.all}")
            elif ride2.lower().strip()=="right":
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(2)
                print(f"{fg.cyan}{ef.i}The left side a car was coming,and you has been hited the car\nThe reason of accident you are near to the death.\nBefore of coming rescue you has been lost your breath.{rs.all}")
        elif ride.lower().strip()=="car":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(2)
            print(f"{fg.cyan}{ef.i}You are enjoying a music.\nYou are saved in the car.\nFinally you have been reached on your target.{rs.all}")
    elif path.lower().strip()=="right":
        print(f"{fg.green}{ef.i}Loding...{rs.all}")
        time.sleep(2)
        print(f"{fg.cyan}{ef.i}WellCome to the jungle zoo.{rs.all}")
        path2=input(f"{fg.cyan}{ef.i}Front of you have two paths (left or right).{rs.all}{fg.black}{ef.b}\nchose one: {rs.all}")
        if path2.lower().strip()=="left":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(2)
            print(f"{fg.cyan}{ef.i}Suddenly, a lion has been come in front of you\nThe lion attacked on you.\nYou will be die must.{rs.all}")
        elif path2.lower().strip()=="right":
            print(f"{fg.green}{ef.i}Loding...{rs.all}")
            time.sleep(2)
            print(f"{fg.cyan}{ef.i}You are looking a river, and climate is rany.{rs.all}")
            path3=input(f"{fg.black}{ef.b}Will you jump or come back: {rs.all}")
            if path3.lower().strip()=="jump":
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(2)
                print(f"{fg.cyan}{ef.i}The river was too depth.\nyou can't take breath under the river\nYou are dying and flow of the river was too fast.{rs.all}")
            elif path3.lower().strip()=="come back" or path3.lower().strip()=="back":
                print(f"{fg.green}{ef.i}Loding...{rs.all}")
                time.sleep(2)
                print(f"{fg.cyan}{ef.i}behaind of you a bear was looking you.\nThe bear attacked on you, and you are near to the death\nyou has been died\n the game has been ended{rs.all}")
except ValueError:
    print(f"{fg.red}{ef.b}Error{rs.all}")        
