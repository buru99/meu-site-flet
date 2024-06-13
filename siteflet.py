import flet as ft

def main(page: ft.Page):
    
    def botao(e):
        # Adiciona o texto "olá" na página
        page.add(ft.Text("olá"))
        page.update()
    
    button = ft.TextButton("link", on_click=botao)
    
    # Adiciona o botão à página
    page.add(button)

ft.app(main)
