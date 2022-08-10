from sqlite3 import Row
import flet
from flet import (
    AppBar,
    Icon,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    colors,
    icons,
    Container,
    margin,
    Column,
    Divider,
    border_radius,
    padding,
    border,
    alignment,
    Theme
)

def main(page: Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()
    print(page.height)
    page.bgcolor = colors.WHITE
    page.padding = 0
    page.title = "Lebsy Tools"
    page.appbar = AppBar(
        leading=Icon(icons.SHOPPING_CART,color=colors.BLACK),
        leading_width=40,
        title=Text("Lebsy Shopping",weight="bold",color=colors.BLACK),
        center_title=False,
        bgcolor=colors.WHITE,
        # elevation=5,
        actions=[
            Container(
                content=Text("Beta",color=colors.WHITE),
                border_radius=border_radius.all(25),
                bgcolor="#ADDEFF",
                height=20,
                width=100,
                alignment=alignment.center,
                # padding=padding.all(10)
                margin=margin.all(10)
            )
        ],
    )
    page.add(
        Divider(height=0.5,thickness=0.5),
        Container(
            height=page.height,
            # bgcolor=colors.BLACK
            padding=20,
        )
    )

flet.app(target=main, view=flet.WEB_BROWSER,assets_dir="images")