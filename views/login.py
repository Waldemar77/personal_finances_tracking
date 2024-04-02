import flet as ft


login_view = ft.Container(
    # adding new components
    ft.Column(
        [
            ft.Container(
                ft.Text(
                    "LOGIN", text_align="center", size=30, width=320, weight="w900"
                ),
                padding=ft.padding.only(20, 20),
            ),
            ft.Container(
                ft.TextField(
                    width=250,
                    height=60,
                    hint_text="Email",
                    # border="underline",
                    border_color="white",
                    prefix_icon=ft.icons.EMAIL_ROUNDED,
                ),
                padding=ft.padding.only(20, 20),
            ),
            ft.Container(
                ft.TextField(
                    width=250,
                    height=60,
                    hint_text="Password",
                    # border="underline",
                    border_color="white",
                    prefix_icon=ft.icons.KEY,
                    password=True,
                    can_reveal_password=True,
                ),
                padding=ft.padding.only(20, 20),
            ),
            ft.Container(
                ft.TextButton(
                    text="Forgot your password?",
                ),
                padding=ft.padding.only(60),
            ),
            ft.Container(
                ft.TextButton(text="Create a new account"), padding=ft.padding.only(60)
            ),
            ft.Container(
                ft.ElevatedButton(
                    text="LOGIN",
                    width=250,
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.BLACK,
                ),
                padding=ft.padding.only(20, 20),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    # main features about this container
    border_radius=20,
    width=300,
    height=600,
    gradient=ft.LinearGradient(
        [ft.colors.AMBER_200, ft.colors.PURPLE_200, ft.colors.PINK_100]
    ),
)


def main(page: ft.Page):

    # main configurations for page
    page.bgcolor = ft.colors.BLACK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # adding new objets to the page
    page.add(login_view)


ft.app(target=main)
