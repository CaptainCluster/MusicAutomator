#Github: CaptainCluster | https://github.com/CaptainCluster

from settings import SETTINGS 
import modules.endtimer as endtimer
import os
import vlc
import keyboard
import time

#The user can interact with the music player via keyboard inputs (determined by the user)
#Parameters: mediaPlayer (media player of the VLC instance), settings (object), song number (integer)

def userInteractions(mediaPlayer, settings, songNumber):
    try:
        #This while-loop will run, as long as the song hasn't ended...
        #and if the user has chosen not to change the song manually.
        while mediaPlayer.get_state() != vlc.State.Ended:
            if(settings.endTimeEnabled):
                endtimer.checkEndTimer() #Due to the way this loop iterates, we check the endtimer over here
            if(settings.skipEnabled):
                if keyboard.is_pressed(settings.skipInput):
                    break
            #If the user wants to go back, we need to adjust the song's position to be the one before 
            #the one that was player right before the current song. This means that instead of -1, we
            #do -2. This is because we will add +1 at the end of the 2nd while-loop at playMusic function
            if(settings.goBackEnabled):
                if keyboard.is_pressed(settings.goBackInput):
                    if songNumber != 0:
                        songNumber = songNumber - 2 #Adjusted to -1... the 2nd while-loop at playMusic function
                    else:
                        songNumber = -1 #Adjusted to 0... the 2nd while-loop at playMusic function
                    break
        return songNumber
    
    except Exception:
        print("An error has occurred in the process.")


def playMusic():
    try:
        settings = SETTINGS() #A settings object to access a set of fixed values
        if(settings.endTimeEnabled):
            endtimer.createSchedule()

        directoryContent = os.listdir(settings.directory) 
        vlcInstance = vlc.Instance()
        mediaPlayer = vlcInstance.media_player_new()

        songNumber = 0 

        #The music player will run in this while-loop (each iteration is done when the song changes).
        while True:
            musicFile = directoryContent[songNumber] 
            time.sleep(0.5) #A delay to avoid issues (for instance, skipping more than one song at a time)
            musicFilePath = os.path.join(settings.directory, musicFile) #Merging the directory with the file name 
            #Next we will handle the media for the vlc and play the song
            vlcMedia = vlcInstance.media_new(musicFilePath) 
            mediaPlayer.set_media(vlcMedia)
            mediaPlayer.play()

            #Now that the song should be playing, we will handle the possible interactions following that.
            if(settings.notifyPlay):
                print("Now playing " + musicFile)
            songNumber = userInteractions(mediaPlayer, settings, songNumber)      
            mediaPlayer.stop()

            songNumber = songNumber + 1 #Increading the value by one to, on default, move onto the next file on the directory (playlist)

    except Exception:
        print("An error has occurred in the process.")
