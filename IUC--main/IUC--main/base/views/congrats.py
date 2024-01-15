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


        f = ft.Image(
            src="images/game_over.png",
            height=500,
            width=700

        )

        foto=ft.Row(
            controls=[f],
            alignment= ft.MainAxisAlignment.CENTER)

        # Estadísticas del juego
        stats_text = ft.Text("Matches: 10",size=30,weight=ft.FontWeight.BOLD,color=ft.colors.GREEN)
        stats_tex2 = ft.Text("|",size=30,weight=ft.FontWeight.BOLD)
        stats_tex3 = ft.Text("Errors: 21",size=30,weight=ft.FontWeight.BOLD,color=ft.colors.RED)

        text_row = ft.Row(
            controls=[stats_text, stats_tex2, stats_tex3],
            alignment=ft.MainAxisAlignment.CENTER)



        game=ft.Column(
            controls=[foto,text_row],
            alignment= ft.MainAxisAlignment.CENTER)
        


        divider = ft.Divider(height=5, thickness= 5)


        # Botones de control del juego
        go_home_btn = ft.IconButton(
            icon=ft.icons.HOME,
            on_click=lambda _: self.page.go("/"),
            icon_size=70,
            icon_color=ft.colors.GREEN
        )
        restart_game_btn = ft.IconButton(
            icon=ft.icons.REFRESH,
            on_click=lambda _: self.page.go("/game"),
            icon_size=70,
            icon_color=ft.colors.ORANGE
        )
        end_game_btn = ft.IconButton(
            icon=ft.icons.POWER_SETTINGS_NEW,
            on_click=lambda _:self.page.window_close(),
            icon_size=70,
            icon_color=ft.colors.RED
        )
        
        thome= ft.Text("Go home", size=30, weight=ft.FontWeight.BOLD)
        trestart= ft.Text("Restart", size=30, weight=ft.FontWeight.BOLD)
        tend= ft.Text("End game", size=30, weight=ft.FontWeight.BOLD)

        # Organizar botones en una fila
        buttons_row = ft.Row(
            controls=[go_home_btn,thome, restart_game_btn, trestart,end_game_btn,tend],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
        buttons_colum = ft.Column(
            controls=[game,divider,buttons_row],
           
        )


        return(buttons_colum)
