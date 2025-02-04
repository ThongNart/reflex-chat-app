import reflex as rx
from rxconfig import config
from reflex_app_2nd import ui
from reflex_app_2nd.chat_component.chat_state import ChatState

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        #x.color_mode.button(position="top-right"),
        rx.vstack(

            rx.color_mode.button(position="bottom-right"),


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


            rx.hstack(
                rx.button(
                    "Decrement",
                    color_scheme="ruby",
                    on_click=State.decrement,
                ),
                rx.heading(State.count, font_size="2em"),
                rx.button(
                    "Increment",
                    color_scheme="grass",
                    on_click=State.increment,
                ),
                spacing="4",
            ),


            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
