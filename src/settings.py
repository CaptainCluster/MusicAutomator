#Github: CaptainCluster | https://github.com/CaptainCluster

#This class gathers a bunch of different values into one place to keep them maintainable
class SETTINGS:
    def __init__(self):

        self.directory = "" #PASTE YOUR DIRECTORY OVER HERE

        self.notifyPlay = True
        self.skipEnabled = True
        self.skipInput = "" #TYPE THE INPUT YOU WANT TO USE TO SKIP A SONG
        self.goBackEnabled = True
        self.goBackInput = "" #TYPE THE INPUT YOU WANT TO USE TO GO BACK TO THE PREVIOUS SONG
        self.endTimeEnabled = True
        self.endTime = "" #TYPE THE TIME YOU WANT TO END THE PROGRAM AUTOMATICALLY (%h:%m)
        