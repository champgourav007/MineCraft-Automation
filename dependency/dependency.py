import subprocess
from sys import stderr
import colorama
import time
from numpy import greater
import regex as re
import decimal

YES_NO_COLOR = colorama.Fore.GREEN + "[Y]" + " " + colorama.Fore.RED + "[N] : " + colorama.Back.CYAN + colorama.Style.RESET_ALL

RED_COLOR = colorama.Fore.RED
GREEN_COLOR = colorama.Fore.GREEN
RESET_COLOR = colorama.Style.RESET_ALL

def check_decorator(str, t = 5):
    for x in range (0,t):  
        b = str + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    print()

def install_java(dependency):
    try:
        subprocess.run(["sudo", "apt", "install", dependency])
        print(GREEN_COLOR + f"{dependency} is installed Successfull!")
        isDone = True
    except:
        print(RED_COLOR + "Some Error Occured while installing Java!")
        isDone = False
    return isDone

def install_rclone():
    try:
        subprocess.run(["sudo", "-v", ";", "curl", "https://rclone.org/install.sh", "|", "sudo", "bash"])
        isDone = True
    except:
        isDone = False
    return isDone

def not_found_decorator(dependency):
    print(RED_COLOR + f"{dependency} is not Installed!")



# check for java version installed in the system
def check_java():
    isDone = False
    try:
        check_decorator("Checking Java Version", 5)
        version = str(subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)).split('\\n')
        openjdk_version = version[0].split(" ")[2]
        print("Your Java OpenJDK version : ",GREEN_COLOR + openjdk_version)
        major_version = openjdk_version[1:len(openjdk_version)-2].split(".")[0]
        
        if int(major_version) >= 19:
            print(f"Java version : {openjdk_version}",u'\N{check mark}')
        else:
            print(RED_COLOR + "Incompatable Java Version : ", RED_COLOR + openjdk_version)
            while True:
                choice = input("Do you want to update JAVA : " + YES_NO_COLOR)

                if choice.upper()[0] == "Y":
                    check_decorator("Updating Java")
                    print(f"{major_version} -> 18")
                    isDone = install_java("openjdk-17-jre")
                    break
                elif choice.upper()[0] == "N":
                    break
                else:
                    print("Invalid Input!")
                    continue
    except:
        not_found_decorator("Java")
        while True:
            choice = input("Do you want to install Java" + YES_NO_COLOR)
            if choice.upper()[0] == "Y":
                isDone = install_java("openjdk-18-jre")
                break
            elif choice.upper()[0] == "N":
                break
            else:
                print("Invalid Input!")

    return isDone

def check_rclone():
    isDone = False
    check_decorator(colorama.Style.RESET_ALL + "Checking rclone Version", 5)

    try:
        version = str(subprocess.check_output(['rclone', '--version'], stderr=subprocess.STDOUT)).split('\\n')
        start = re.search("v", version[0]).start()
        rclone_version = version[0][start:]
        print("Installed rclone version : ", GREEN_COLOR + rclone_version)
        if decimal.Decimal(rclone_version[1:5]) <= 1.50:
            check_decorator("Updating rclone")
            isDone = install_rclone()
        else:
            print(GREEN_COLOR + "rclone version is Verified : ", rclone_version)
    except:
        not_found_decorator("rclone")
        while True:
            choice = input("Do you want to install rclone " + YES_NO_COLOR)
            if choice.upper()[0] == "Y":
                isDone = install_rclone()
                break
            elif choice.upper()[0] == "N":
                break
            else:
                print("Enter valid input!")

    # while True:
    #     choice = input("Do you want to configure "+ YES_NO_COLOR)
    #     if choice.upper()[0] == "Y":
    #         subprocess.run(["rclone", "config"], stderr=subprocess.STDOUT)
    #         break
    #     else:
    #         print("Invalid Input!")
    #         continue
            
    return isDone


if __name__ == "__main__":
    pass