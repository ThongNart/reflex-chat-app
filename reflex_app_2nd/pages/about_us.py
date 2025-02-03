import reflex as rx
from reflex_app_2nd import ui

def about_us() -> rx.Component:
    # About Us page
    return ui.base_layout(
        rx.color_mode.button(position="bottom-right"),
        rx.vstack(
            rx.heading("About Us", size="9"),
            
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )