"""
WARNING: The file needs to be in the same directory as the SSRPGInterface folder. 
"""

from SSRPGInterface.commands import *
import SSRPGInterface
import time

# Define the test step function
y = 0
def teststep():
    global y
    # Check ?loc.begin
    if loc.begin():
        y = 0
        # Execute the command to brew tar + wood
        command.Brew("tar + wood")
    
    # Update y coordinate
    y = (y + 1) % 30
    
    # Send a command with the y coordinate and current time
    command.Print(f"`1,{y},hello python!{time.ctime()}")
    
    
    # Print the foe and its distance
    print(f"foe:{foe()}")
    print(f"foe.distance:{foe.distance()}")
    
    # Equip different items based on the foe type
    if "boss" in foe():
        command.equipR("sword")
        command.equipL("hammer")
    else:
        command.equip("arm")
        if foe.distance() < 8 and item.CanActivate("skeleton_arm"):
            command.Activate("R")
        print(f"{item.GetCooldown("skeleton_arm")} {item.CanActivate("skeleton_arm")}")

def battle_test():
    if item.left.state() == 3:
        command.EquipL("sword")
    if item.right.state() == 3:
        command.EquipR("shield")
    
    if foe.distance() < 24:
        command.Equip("arm")
    else:
        command.EquipL("trisk")
        command.EquipR("compound")

    print(f"\r{hp()}/{maxhp()} {armor()}/{maxarmor()} {item.left.state()} {item.right.state()} {totaltime()}", end="")

num = 0
fl = []
start_time = 0
end_time = 0
finish_time = 0
avg_time = 0
def connect_callback_speed_test():
    global num, start_time, end_time, finish_time, avg_time
    from time import time_ns
    num = num + 1
    start_time = time_ns()
    #tt = totaltime()
    for i1 in range(100):
        for i2 in range(100):
            #if tt == -1:
            if totaltime() == -1:
                return
    end_time = time_ns()
    finish_time = end_time - start_time
    fl.append(finish_time)
    print(f"Connect Callback Speed Test {num}:\t{finish_time / 1000000}ms\t{finish_time}ns")
    if num >= 20:
        for f in fl:
            avg_time += f
        avg_time /= len(fl)
        print(f"average time is {avg_time / 1000000}ms\t{avg_time}ns")
        loc.Pause()
        exit()

def item_name_length_test():
    left_item = item.left()
    right_item = item.right()
    print(f"\rleft len:{len(left_item)} name:{left_item}\t\tright len:{len(right_item)} name:{right_item}\t\t\t\t\t", end="")


if __name__ == "__main__":
    # Run the interface
    run_script(teststep)