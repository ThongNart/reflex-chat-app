"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import ui

class State(rx.State):
    """The app state."""

    ...



def about_us() -> rx.Component:
    # About Us page
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("About Us", size="9"),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex ChatGPT !", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index, route='/')
app.add_page(about_us,route='/about-us')
