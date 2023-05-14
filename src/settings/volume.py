import sqlite3
import pygame as pg
from gameobjects.menu.text import Text

REDUCE_CONSTANT = 1000


class VolumeObject():

    """Database management object for volume settings; can be expanded to
       include other settings quite easily."""
    
    # The idea with storing volume into a database is just to gain points;
    # Really there's no need at all to use a database solution in a project
    # like this, so I hope this suffices for those points. It would be quite
    # easy to store anything (leaderboards, gamehistory, game configurations 
    # if added) into a mere csv or a simpler storage system, but this database
    # is an alternative solution that will hopefully increase my grade. 

    def __init__(self, initial_vol_music: int, volume_text: Text):
        """

        Initial volume is an integer between 0-100.
        """
        pg.init()
        self.__conn = sqlite3.connect('src/settings/volumeDB')
        self.create_table()

        # this first block modifies initial_vol if it is present
        # from a previous run
        result = self.__conn.execute("SELECT * FROM VOLUME")
        vol = result.fetchone()
        if bool(vol):
            initial_vol_music = vol[0]

        # set values
        self.__vol_music = initial_vol_music
        self.__volume_text = volume_text
        self.__volume_text.text = str(self.__vol_music)

        # start pygame
        pg.mixer.music.set_volume(initial_vol_music / REDUCE_CONSTANT)
        pg.mixer.music.load('src/assets/sound/music/Menu_soundtrack.wav')
        pg.mixer.music.play(-1)

        # no need to guard against injections because values possible to
        # add are controlled
        self.__conn.execute(
            f'''INSERT INTO VOLUME(MUSIC) VALUES ({initial_vol_music})''')

    def change_vol(self, new_vol_music: int) -> str:
        """
        Change volume between 0-100

            Args:
                new_vol: integer, 0-100

            Returns:
                empty string for main loop
        """
        new_vol_music = self.__vol_music + new_vol_music

        if 0 > new_vol_music:
            new_vol_music = 0
        elif 100 < new_vol_music:
            new_vol_music = 100

        pg.mixer.music.set_volume(new_vol_music / REDUCE_CONSTANT)
        self.__vol_music = new_vol_music
        self.__conn.execute('DELETE FROM VOLUME')
        self.__conn.execute(
            f'''INSERT INTO VOLUME(MUSIC) VALUES ({new_vol_music})''')
        self.__volume_text.text = str(self.__vol_music)

        self.__conn.commit()

        return ""

    def create_table(self):
        """
        Creates the tables used by the class if necessary
        """
        table_name = 'VOLUME'

        # Execute the query to check if the table exists
        result = self.__conn.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        )
        comp = result.fetchone()
        if not bool(comp):
            self.__conn.execute('''CREATE TABLE VOLUME(MUSIC FLOAT)''')

        self.__conn.commit()
