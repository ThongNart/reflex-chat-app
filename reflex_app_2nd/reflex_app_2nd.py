"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import ui, pages

class State(rx.State):
    """The app state."""

    ...



app = rx.App()
app.add_page(pages.index, route='/')
app.add_page(pages.about_us,route='/about-us')
