import reflex as rx
from reflex_app_2nd import ui
from .chat_form import chat_form
from .chat_state import ChatMessage, ChatState

message_style = dict (
    display= "inline-block",
    padding= "1em",
    border_radius = "8px",
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"]
)

def message_box(chat_message: ChatMessage) -> rx.Component:

    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(
                    chat_message.is_bot,
                    rx.color("mauve",4),
                    rx.color("blue",4)
                    ),
                color=rx.cond(chat_message.is_bot, rx.color("crimson", 12), rx.color("cyan",12)),
                **message_style,
            ),
            text_align=rx.cond(chat_message.is_bot, "left", "right"),
            margin_top="1em"
        )
    )


def chat_page():
    return ui.base_layout (
        rx.vstack(
            rx.hstack(
                rx.heading("Chat with AI", size="9"),
                rx.button(" + New Chat", on_click=ChatState.clear_and_start_new)
            ),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width='80%'
            ),
            chat_form(),
            margin="3rem auto", 
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )