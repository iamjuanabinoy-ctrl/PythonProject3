import random
import time

# Introduction
print(" Welcome to Barbie's Dream Adventure! ")
time.sleep(1)
print("Barbie is exploring Dream World, full of magic, fashion, and surprises!")
time.sleep(1)

# Player stats
energy = 100
inventory = []
style_points = 0

events = ["fashion challenge", "magical creature", "shopping spree", "mystery gift"]


def encounter(event):
    global energy, inventory, style_points
    print(f"\n✨ You encounter a {event}! ✨")

    if event == "fashion challenge":
        action = input("Do you want to (D)ress up or (S)kip? ").lower()
        if action == "d":
            points = random.randint(5, 20)
            style_points += points
            print(f"You nailed the challenge and earned {points} style points! Total: {style_points}")
            return True
        elif action == "s":
            print("You skipped the challenge. No style points gained.")
            return True
        else:
            print("Invalid choice. You lose a little energy for hesitation.")
            energy -= 5
            return True

    elif event == "magical creature":
        action = input("Do you want to (F)riend it or (R)un away? ").lower()
        if action == "f":
            found_item = random.choice(["sparkly wand", "magic tiara", "rainbow boots"])
            print(f"The creature gifts you a {found_item}!")
            inventory.append(found_item)
            return True
        elif action == "r":
            lost_energy = random.randint(5, 15)
            energy -= lost_energy
            print(f"You run away, losing {lost_energy} energy. Current energy: {energy}")
            return True
        else:
            print("Invalid choice. The creature playfully scares you. Lose 5 energy.")
            energy -= 5
            return True

    elif event == "shopping spree":
        found_gold = random.randint(10, 50)
        print(f"You find {found_gold} shiny coins to spend on accessories!")
        style_points += found_gold // 2
        return True

    elif event == "mystery gift":
        item = random.choice(["glitter backpack", "fancy necklace", "magic pet"])
        print(f"You open a mystery gift and receive a {item}!")
        inventory.append(item)
        return True


while True:
    print(f"\n💖 Energy: {energy}, Style Points: {style_points}, Inventory: {inventory}")
    choice = input("Do you want to (E)xplore Dream World, (R)est, or (Q)uit? ").lower()

    if choice == "e":
        event = random.choice(events)
        encounter(event)
        if energy <= 0:
            print("Oh no! Barbie is too tired to continue... GAME OVER 💔")
            break

    elif choice == "r":
        healed = random.randint(10, 30)
        energy += healed
        if energy > 100:
            energy = 100
        print(f"You rest at the Dream Castle Spa and recover {healed} energy. Current energy: {energy}")

    elif choice == "q":
        print(f"\nYou leave Dream World with {style_points} style points and items: {inventory}.")
        print("Thanks for playing Barbie's Dream Adventure!")
        break

    else:
        print("Invalid choice. Choose E, R, or Q.")