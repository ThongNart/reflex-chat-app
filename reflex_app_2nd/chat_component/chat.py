import reflex as rx

from reflex_app_2nd import ui

def chat_page():
    return ui.base_layout (
        rx.vstack(
            rx.heading("Chat with AI", size="9"),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )