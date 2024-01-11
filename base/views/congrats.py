import flet as ft


class Congrats(ft.UserControl):

    def __init__(self, page: ft.Page, matches: int, errors: int):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

        # TODO: WRITE YOUR CLASS VARIABLES HERE

    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE
    def build(self):
        foto = ft.Image(
        src="images/game_over.png",
        height=300,
        width=500
        )

    

        return(foto)
