import random
import time
import threading

import flet as ft

from .card import Card


class Game(ft.UserControl):
    def __init__(self, page: ft.Page):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

        # CLASS VARIABLES
        self.n_pairs = 10  # Number of card pairs (int)
        self.card_images_indexes = []  # List of indexes of card images (list)
        self.cards = []  # List of Cards (list)

        self.matches = None  # Number of matches between cards (int)
        self.errors = None  # Number of errors during the game (int)

        self.selected_card = None  # First card selected from the pair (Card)
        # List of identifiers for those pairs of cards already found (list)
        self.cards_ids_matched = []

        self.__initialize_game()

    # DON´T TOUCH THIS FUNCTION
    def did_mount(self):
        self.running = True
        self.th = threading.Thread(
            target=self.__game_logic, args=(), daemon=True)
        self.th.start()

    # DON´T TOUCH THIS FUNCTION
    def will_unmount(self):
        self.running = False

    # DON´T TOUCH THIS FUNCTION
    def __game_logic(self) -> None:
        # Loop inside while the number of found matches is different to the
        # total number of pairs
        while self.matches != self.n_pairs and self.running:
            for card in self.cards:
                if card.animator.content == card.frontside:
                    self.__is_a_match(card)

        # The game is over
        self.running = False
        print('Game Over!')
        time.sleep(1)

        # Go to Congrats view
        self.page.go(f'/congrats/{self.matches}/{self.errors}')

    # TODO: FUNCTION TO INITIALIZE THE CLASS VARIABLES OF THE GAME
    def __initialize_game(self):
        pass

    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE
    def build(self):
        pass

    # TODO: FUNCTION TO UPDATE THE VALUES OF THE NUMBER OF MATCHES AND ERRORS
    def __update_texts(self) -> None:
        pass

    # TODO: FUNCTION TO CHECK IF EXISTS A MATCH BETWEEN THE PREVIOUS SELECTED CARD AND THE NEW SELECTION
    def __is_a_match(self, card: Card) -> None:
        pass

    # DON´T TOUCH THIS FUNCTION
    def __game_logic(self) -> None:
        # Loop inside while the number of found matches is different to the
        # total number of pairs
        while self.matches != self.n_pairs and self.running:
            for card in self.cards:
                if card.animator.content == card.frontside:
                    self.__is_a_match(card)

        # The game is over
        self.running = False
        print('Game Over!')
        time.sleep(1)

        # Go to Congrats view
        self.page.go(f'/congrats/{self.matches}/{self.errors}')
