import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        result.value = str(bin(int(number.value)))
        page.update()

    def clear_clicked(e):
        number.value = ""
        result.value = ""
        page.update()

    title = ft.Text("Convert decimal to binary", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    number = ft.TextField(hint_text="Number to convert")
    button_convert = ft.FilledButton(
        icon=ft.icons.REFRESH, text="Convert", on_click=add_clicked
    )
    button_clear = ft.OutlinedButton(text="Clear", on_click=clear_clicked)
    result = ft.Text()
    convert_row = ft.Row([number, button_convert, button_clear])

    page.add(title, convert_row, result)


ft.app(target=main)
