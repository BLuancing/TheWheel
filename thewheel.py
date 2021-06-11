import pandas
import numpy
import os

# CONSTANTS & GLOBALS
DEFAULT_FILE_NAME = "movies.csv"

def GetMovieFilePath():
    sMoviePath = DEFAULT_FILE_NAME

    print("Searching for default movies files '" + DEFAULT_FILE_NAME + "'...")

    # Check if default movie path exsits in current directory
    if os.path.exists(DEFAULT_FILE_NAME) == False:
        print("Could not locate default movie file '" + DEFAULT_FILE_NAME + "'!")

        while True:
            newPath = input("Enter a new path to a movie file, or type 'no' to exit: ")

            #If 'no' or any variation...
            if newPath.lower() == "no":
                print("Terminating program...")
                exit(0)

            #Check if the new path exists
            if os.path.exists(newPath) == False:
                print("No such file located at '" + newPath + "'!")
            else:
                print("That file exists!")
                return newPath



    return sMoviePath

def LoadMovieFile(sMovieFilePath):
    print("Attempting to load movie file located at '" + sMovieFilePath + "'...")

    try:
        file = pandas.read_csv(sMovieFilePath)
    except Exception as err:
        print("Failed to properly load movie file: {0}\nTerminating program...".format(err))
        exit(-1)
    return file

def ReadMovieFile(file):
    #Construct a pandas array with genre tags
    return

def MainMenuLoop():
    bContinueMenu = True

    # Load the file and display summary of info about it
    sMoviePath = GetMovieFilePath()
    fMovieFile =  LoadMovieFile(sMoviePath)

    #Read the movie file

    while (bContinueMenu):
        DisplayOptions()
        cMenuSelection = input("What would you like to do? ->")
            # Prompt for filename


def DisplayOptions():
    return

if __name__ == "__main__":
    print('''****************************************************************************
    _________          _______                      _______  _______  _       
    \__   __/|\     /|(  ____ \  |\     /||\     /|(  ____ \(  ____ \( \      
       ) (   | )   ( || (    \/  | )   ( || )   ( || (    \/| (    \/| (      
       | |   | (___) || (__      | | _ | || (___) || (__    | (__    | |      
       | |   |  ___  ||  __)     | |( )| ||  ___  ||  __)   |  __)   | |      
       | |   | (   ) || (        | || || || (   ) || (      | (      | |      
       | |   | )   ( || (____/\  | () () || )   ( || (____/\| (____/\| (____/\   
       )_(   |/     \|(_______/  (_______)|/     \|(_______/(_______/(_______/

    ****************************************************************************
        ''')

    print("\nWelcome to The Wheel!")

    sMoviePath = GetMovieFilePath()

    MainMenuLoop()

