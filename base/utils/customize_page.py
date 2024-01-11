import flet as ft


def customize_page(page: ft.Page, width: int = None, height: int = None,
                   title: str = 'My Page', window_maximizable: bool = False,
                   window_resizable: bool = False, theme_mode: str = 'light',
                   window_focused: bool = True, window_centered: bool = True,
                   auto_scroll: bool = False, scroll: str = None):
    # Initialize page
    page = page
    page.window_width = width
    page.window_height = height
    page.title = title
    page.window_maximizable = window_maximizable
    page.window_resizable = window_resizable
    page.theme_mode = theme_mode
    page.window_focused = window_focused
    page.auto_scroll = auto_scroll
    page.scroll = scroll
    if window_centered:
        page.window_center()
    page.update()
