import flet as ft

def main(page: ft.Page):
    page.title = "Ejercicio 4-Pablo Martinez Conde "
    page.window_width= 1200
    page.window_height= 800
    page.theme_mode = "light"
    page.window_maximizable = False
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft. CrossAxisAlignment.CENTER
    
    def cambio(i):
       page.window_center()
       page.update() 

    # TODO: WRITE YOUR CONTROLS STRUCTURE HERE
    img = ft.Image(
        src="C:/Users/pablo/OneDrive/Escritorio/IUC/base/assets/images/cover.png",
         width=400,
         height=400,
         fit=ft.ImageFit.FILL,
        )
    
    boton = ft.Container(
        bgcolor= ft.colors.ORANGE_800, 
        border_radius= 10,
        border=ft.border.all(5, ft.colors.BLACK),
        height= 110, 
        width=200, 
        on_click=cambio,
        alignment= ft.alignment.center,
        content= ft.Text("Jugar", size=60, weight=ft.FontWeight.W_700))
        

    page.add(img,boton)
    page.update()

    


ft.app(target=main, view=ft.AppView.FLET_APP)
