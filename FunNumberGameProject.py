import random
import os

def cls():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def rng():
    return random.randint(1, 10)

def calc(h):
    return sum(h)

def run():
    # Welcome banner
    print("\n" + "*"*45)
    print("      WELCOME TO THE FUN NUMBER GAME      ")
    print("          (Try to hit 21!)       ")
    print("*"*45)
    print("   RULES:                                    ")
    print("   1. Try to get as close to 21 as possible. ")
    print("   2. If you go over 21, you lose.           ")
    print("   3. Computer plays alongside you.          ")
    print("   4. Computer must hit until it reaches 17. ")
    print("   5. If Computer hits 21, it wins instantly ")
    print("      (unless you also have 21 -> Draw).     ")
    print("*"*45 + "\n")

    # Initial deal
    p = [rng(), rng()]
    cpu = [rng(), rng()]
    
    active = True

    while active:
        ps = calc(p)
        cs = calc(cpu)

        print(f"\nYour Hand:     {p}  (Score: {ps})")
        print(f"Computer Hand: {cpu}  (Score: {cs})")

        # Check instant win/loss
        if ps > 21:
            print("\n>>> You went over 21! BUST! You lose.")
            return
        
        if cs > 21:
            print("\n>>> Computer went over 21! You win!")
            return

        if cs == 21:
            if ps == 21:
                print("\n>>> Wow! Both got 21. It's a Draw!")
            else:
                print("\n>>> Computer hit 21! Computer wins.")
            return

        if ps == 21:
            print("\n>>> You hit 21! Nice job!")
            # Computer catches up
            while calc(cpu) < 17:
                print("Computer is drawing to catch up...")
                cpu.append(rng())
                
                if calc(cpu) == 21:
                    print(f"Computer Hand: {cpu} -> 21")
                    print("Computer matched your 21! It's a Draw.")
                    return
            break 

        # Player turn
        cmd = input("\nType 'Hit' for another number, or 'Stand' to stop: ").strip().lower()

        if cmd == 'hit':
            n = rng()
            print(f"You drew a {n}!")
            p.append(n)

            # Computer turn
            if calc(cpu) < 17:
                cn = rng()
                print(f"Computer decides to hit... and gets {cn}")
                cpu.append(cn)
            else:
                print("Computer is staying safe.")
            
        elif cmd == 'stand':
            print("\nYou chose to Stand.")
            # Finish computer turn
            while calc(cpu) < 17:
                print("Computer needs to hit (under 17)...")
                n = rng()
                print(f"Computer drew a {n}")
                cpu.append(n)
                
                # Check computer 21
                if calc(cpu) == 21:
                    print(f"\nComputer Hand: {cpu} -> 21")
                    print("Computer hit 21! Computer wins!")
                    return
            
            active = False
        else:
            print("I didn't understand that. Please type 'Hit' or 'Stand'.")

    # Results
    pf = calc(p)
    cf = calc(cpu)

    # Results header
    print("\n" + "="*35)
    print("           FINAL RESULTS")
    print("=" * 35)
    print(f"You:      {pf}")
    print(f"Computer: {cf}")

    if cf > 21:
        print("Computer busted! You win!")
    elif cf > pf:
        print("Computer has a higher score. Computer wins.")
    elif pf > cf:
        print("You have a higher score! You win!")
    else:
        print("It's a tie!")
    
    # Footer
    print("_" * 35)

if __name__ == "__main__":
    cls()
    while True:
        run()
        again = input("\nPlay again? (y/n): ").lower()
            
        if again != 'y':
            print("Thanks for playing! Bye!")
            break
        cls()
