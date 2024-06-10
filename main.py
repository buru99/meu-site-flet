import flet as ft

def main(page: ft.Page):
    page.title = "meu site flet"
    page.bgcolor = ft.colors.RED_200
    page.add(ft.Text("hello world"))
    
    

ft.app(target=main)
