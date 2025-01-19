from ssrpgif import SSRPGInterface
import time

# Initialize the SSRPGInterface
ssrpgIF = SSRPGInterface()

# Define the test step function
def teststep():
    # Check ?loc.begin
    if ssrpgIF.call("loc.begin"):
        ssrpgIF.y = 0
        # Execute the command to brew tar + wood
        ssrpgIF.call_command("brew", "tar + wood")
    
    # Update y coordinate
    ssrpgIF.y = (ssrpgIF.y + 1) % 30
    
    # Send a command with the y coordinate and current time
    ssrpgIF.call_command(">", "`1," + str(ssrpgIF.y) + "," + "hello python!" + time.ctime())
    
    # Print the foe and its distance
    print("foe:" + ssrpgIF.call("foe"))
    print("foe.distance:" + str(ssrpgIF.call("foe.distance")))
    
    # Equip different items based on the foe type
    if "boss" in ssrpgIF.call("foe"):
        ssrpgIF.call_command("equipR", "sword")
        ssrpgIF.call_command("equipL", "hammer")
    else:
        ssrpgIF.call_command("equip", "arm")
        if ssrpgIF.call("foe.distance") < 8 and ssrpgIF.call("item.CanActivate", "skeleton_arm"):
            ssrpgIF.call_command("activate", "R")
        print(str(ssrpgIF.call("item.GetCooldown", "skeleton_arm")) + " " + str(ssrpgIF.call("item.CanActivate", "skeleton_arm")))


# Assign the test step function to the interface
ssrpgIF.step = teststep

# Run the interface
ssrpgIF.run()