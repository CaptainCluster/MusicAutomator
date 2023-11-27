#Github: CaptainCluster | https://github.com/CaptainCluster


class SETTINGS:
    """A bunch of  different values into one place to keep them maintainable
    """
    def __init__(self) -> None:

        self.directory = "" #PASTE YOUR DIRECTORY OVER HERE

        #Different features that can be enabled/disabled
        self.notifyPlay     = True
        self.skipEnabled    = True
        self.endTimeEnabled = True
        self.goBackEnabled  = True
        self.pauseEnabled   = True

        #Determine the inputs for the actions you have enabled
        #Example: 'alt + v' is a valid string
        self.skipInput      = ""      
        self.goBackInput    = ""    
        self.pauseInput     = "" #Works as both Pause and Resume

        #The time the program will end automatically on (%h:%m)
        self.endTime = ""
        