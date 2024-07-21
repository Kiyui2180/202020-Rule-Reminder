from datetime import datetime, timedelta # for accessing the datetime functions
import time
import os # for getting terminal features functions
from plyer import notification # for acessing notification function of the library
import winsound # for accessing sounds

def exit_script(): # function for exiting the script, 
    print("- Exiting ...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('- Script disabled')
    time.sleep(1)
    exit()

def decision_continue():
     while True:
        decision = str(input("- Continue (yes or no [abort]): "))

        if decision == "yes" or decision == "y":
            main()
            break
        elif decision == "no" or decision == "n":
            exit_script()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("- Invalid input, only enter inputs 'yes' or 'no'")

def notify(): # funtion for the body of the notification
    computer_name = os.environ.get("COMPUTERNAME", "User") # COMPUTERNAME = user's computer name, else User if not found
    duration = 1500
    freq = 440
    winsound.Beep(freq, duration)

    time.sleep(1)
    notification.notify(
        title = f"Time to Rest your Eyes, {computer_name}!",
        message = "20 minutes is up! Make sure to look 20ft (~6 meters) away outside for 20 seconds.",
        timeout = 1
    )

def timer_tillNotify(): # function for the timer comparison
    n = 20 # assinged int minutes for timer to add to the initiated_time
    initiated_time = datetime.now()
    while True:
        current_time = datetime.now()
        final_time = initiated_time + timedelta(minutes=n)
        # initiated_time is when the timer stamps the current time and is fixed, current_time changes for user feedback,
        # final_time is the calculated time when the timer will alarm

        os.system('cls' if os.name == 'nt' else 'clear')

        # the time format for printing
        current_time_str = current_time.strftime("%H:%M:%S")
        final_time_str = final_time.strftime("%H:%M:%S")

        print(f"- {current_time_str}/ {final_time_str}") # printing the time

        if current_time >= final_time: # when the time reaches 20 minutes or more, this if-else will work
            print("- Notifying ...")
            time.sleep(1)
            notify()

            os.system('cls' if os.name == 'nt' else 'clear')
            decision_continue()
           
        time.sleep(1) # adding a second to replicate a second in time

def main():
    os.system('cls' if os.name == 'nt' else 'clear') # clearing the terminal for a cleaner look
    exit_key_words = ["quit", "exit", "0"]

    startTimer = str(input("- Please enter any key to start the 20-20-20 Rule (to exit, enter: '0'): "))

    if startTimer in exit_key_words:
        exit_script()
    else:
        print("- Starting, please wait ...")
        time.sleep(1)
        timer_tillNotify()
            
if __name__ == "__main__":
    main()
