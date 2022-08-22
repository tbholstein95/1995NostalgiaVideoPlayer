import vlc
import time
import os
import sys
from tkinter import *


class VideoController:
    def __init__(self):

        self.shows = []
        self.commercials = []
        self.showsDirectory = ""    #Put shows here. This will be replaced with SQL query.
        self.commercialsDirectory = "" #Put commercials here.This will be replaced with SQL query.

    def add_shows(self):
        self.shows = os.listdir(self.showsDirectory)
        print(self.shows)

    def add_commercials(self):
        self.commercials = os.listdir(self.commercialsDirectory)
        print(self.commercials)

    parseReady = 0

    def ParseReceived(event):
        global parseReady
        #set a flag that your data is ready
        parseReady = 1

    def run(self):
        self.mw = Tk()
        self.mw.title('Howdy')
        self.mw.geometry('1280x960')

        self.display=Frame(self.mw, bd=5)
        self.display.place(relwidth=1, relheight=1)



    # def playvideo(self):
    #     media_player = vlc.MediaPlayer()
    #     media = vlc.Media(self.showsDirectory + "/" + self.shows[0])
    #     media_player.set_media(media)
    #     media.parse_with_options(1, 0)
    #     while True:
    #         if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
    #             break
    #         value = media.get_duration()
    #
    #     print(value)
    #     media_player.play()
    #     time.sleep(value/1000)
    #     media_player.stop()

    def playvideo(self):

        player = vlc.Instance()

        media_player = player.media_list_player_new()

        holder = vlc.libvlc_media_list_player_get_media_player(media_player)

        #holder.toggle_fullscreen()


        media_list = player.media_list_new()
        media = player.media_new(self.showsDirectory + "/" + self.shows[0])
        media.add_option('start-time=150.0')
        media.add_option('run-time=15.0')
        media_list.add_media(media)

        holder.set_hwnd(self.display.winfo_id())
        media_player.set_media_list(media_list)

        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break
            value1 = media.get_duration()

        media = player.media_new(self.commercialsDirectory + "/" + self.commercials[0])
        media.add_option('start-time=0.0')
        media.add_option('run-time=15.0')
        media_list.add_media(media)
        media_player.set_media_list(media_list)

        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break
            value2 = media.get_duration()


        media = player.media_new(self.showsDirectory + "/" + self.shows[0])
        media.add_option('start-time=170.0')
        media.add_option('run-time=15.0')
        media_list.add_media(media)
        media_player.set_media_list(media_list)

        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break

        for i in range(len(media_list)):
            print(len(media_list))
            media_player.play_item_at_index(i)
            if(i==0):
                self.mw.mainloop()

            time.sleep(1)
            while media_player.is_playing():
                pass
            print("video")
            if i == len(media_list)-1:
                print("howdy")
                break
            else:
                media_player.next()



