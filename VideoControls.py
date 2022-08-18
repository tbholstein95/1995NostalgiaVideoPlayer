import vlc
import time
import os


class VideoController:
    def __init__(self):

        self.shows = []
        self.commercials = []
        self.showsDirectory = "C:/Users/tbhol/codingstuff/1995NostalgiaVideoPlayer/1995NostalgiaVideoPlayer/shows"
        self.commercialsDirectory = "C:/Users/tbhol/codingstuff/1995NostalgiaVideoPlayer/1995NostalgiaVideoPlayer/commercials"

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
        media_player = vlc.MediaListPlayer()
        player = vlc.Instance()
        media_list = player.media_list_new()
        media = player.media_new(self.showsDirectory + "/" + self.shows[0])
        media_list.add_media(media)
        media_player.set_media_list(media_list)

        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break
            value1 = media.get_duration()

        media = player.media_new(self.commercialsDirectory + "/" + self.commercials[0])
        media_list.add_media(media)
        media_player.set_media_list(media_list)

        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break
            value2 = media.get_duration()



        media_player.play_item_at_index(0)
        time.sleep(value1)
        media_player.next()
        time.sleep(value2)

