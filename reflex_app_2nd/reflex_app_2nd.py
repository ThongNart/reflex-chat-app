"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import ui, pages, navigation, chat_component

class State(rx.State):
    """The app state."""

    ...

app = rx.App()
app.add_page(pages.index, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us,route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(
    chat_component.chat_page,route=navigation.routes.CHAT_ROUTE,
    on_load = chat_component.chat_state.ChatState.on_load()
    )
