import flet as ft

from views import login


def main(page: ft.Page):

    # main configurations for page
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # adding new objets to the page
    page.add(login.login_view)


ft.app(target=main)
