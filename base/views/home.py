import flet as ft


class Home(ft.UserControl):

    def __init__(self, page: ft.Page):
        # Call super constructor
        super().__init__()

        # Save page as class variable
        self.page = page

    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE
    def build(self):
        c1 = ft.Image(
        src="images/cover.png",
        height=400,
        width=400,
        fit=ft.ImageFit.FILL
 )
        boton = ft.Container(
            bgcolor= ft.colors.ORANGE_800, 
            border_radius= 10,
            border=ft.border.all(5, ft.colors.BLACK),
            height= 110, 
            width=200, 
            alignment= ft.alignment.center,
            on_click=lambda _: self.page.go("/congrats/:matches/:errors"),
            content= ft.Text("Jugar", size=60, weight=ft.FontWeight.W_700))
        
        row=ft.Row(
            controls=[c1],
            alignment= ft.MainAxisAlignment.CENTER

        )
        row2=ft.Row(
            controls=[boton],
            alignment= ft.MainAxisAlignment.CENTER

        )
        columna= ft.Column(
            controls=[row,row2]
            )
        
        return(columna)
        
       