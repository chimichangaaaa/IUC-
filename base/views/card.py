import flet as ft


class Card(ft.UserControl):
    def __init__(self, page: ft.Page, id: int, image_index: int):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

        # CLASS VARIABLES
        self.id = id
        self.image_path = f'images/{image_index}.png'

        # Front part of the card (Emoji)
        self.f_bgcolor = '#5db7fc'  # Blue
        self.frontside = self.__create_card_container(self.f_bgcolor,
                                                      self.image_path)

        # Back part of the card
        self.b_bgcolor = '#ff7200'  # Orange
        self.backside = self.__create_card_container(self.b_bgcolor, None)

        # Animator for back side and front side of the card
        self.animator = ft.AnimatedSwitcher(
            content=self.backside,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=500
        )

    # DON´T TOUCH THIS FUNCTION
    def build(self):
        return self.animator

    # TODO: FUNCTION THAT RETURNS THE FRONT OR BACK SIDE OF THE CARD, DEPENDING ON THE bgcolor PARAMETER
    def __create_card_container(self, bgcolor: str, image_path: str = None) -> ft.Control:
        pass

    # TODO: FUNCTION NEEDED FOR THE AnimatedSwitcher TO ANIMATE THE TRANSITION BETWEEN THE FRONT AND THE BACK SIDES OF THE CARD
    def animate_card(self) -> None:
        pass

    # TODO: FUNCTION TO ENABLE THE CARD AND ALLOW IT TO BE PRESSED
    def enable_card(self) -> None:
        pass

    # TODO: FUNCTION TO DISABLE THE CARD AND NOT ALLOW IT TO BE PRESSED
    def disable_card(self) -> None:
        pass

    # TODO: FUNCTION TO CHANGE THE bgcolor OF THE FRONT SIDE OF THE CARD
    def change_fronside_bgcolor(self, bgcolor: str = '#898989') -> None:
        pass
