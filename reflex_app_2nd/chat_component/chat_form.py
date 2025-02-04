import reflex as rx

from .chat_state import ChatState

def chat_form() -> rx.Component:

    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='your message',
                required=True,
                width='90%',
            ),
            rx.hstack(
                rx.button('Submit', type="submit"),
                rx.cond(
                    ChatState.user_did_submit,
                    rx.text("Successfully submited!!!!"),
                    rx.fragment()
                    
                )
                
            )
        
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit = True,

    )