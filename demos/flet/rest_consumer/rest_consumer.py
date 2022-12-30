import sys

import flet as ft

sys.path.insert(0, "../../..")
import demos_res.rest_mock.rest_mock as rest_mock


def main(page: ft.Page):
    def get_clicked(e):
        progress_ring.visible = True
        page.update()

        response = rest_mock.get_users()
        for user in response["users"]:
            text = user["firstName"] + " " + user["lastName"]
            list_view.controls.append(ft.Text(text))

        progress_ring.visible = False

        page.update()

    title = ft.Text("REST consumer", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    button_get = ft.FilledButton(
        icon=ft.icons.REFRESH, text="Get users", on_click=get_clicked
    )
    progress_ring = ft.ProgressRing(visible=False)
    list_view = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    page.add(title, button_get, progress_ring, list_view)


ft.app(target=main)
