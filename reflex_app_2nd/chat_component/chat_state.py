import reflex as rx
import asyncio
from typing import List
from . import ai
from reflex_app_2nd.models import Chat as ChatModel

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):

    did_submit: bool = False
    messages: List[ChatMessage] =[]

    @rx.var(cache=True)
    def user_did_submit(self) -> bool:
        return self.did_submit
    

    def on_load(self):
        with rx.session() as session:
            results = session.exec(
                ChatModel.select()
            ).all()

            print(results)

    
    def append_message(self, message, is_bot:bool=False):
        if not is_bot:
            with rx.session() as session:
                obj = ChatModel(
                    title=message,
                )
                session.add(obj)
                session.commit()

        self.messages.append(
                ChatMessage(
                    message = message,
                    is_bot = is_bot
                )
            )

    def get_gpt_messages(self):
        #open ai format
        gpt_messages = [
            {
                "role": "system", 
                "content":"you are a thoughtful companion in life coaching. Response in markdown."
             }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append({
                "role": role,
                "content": chat_message.message
            })
        print("chatgpt messages: ", gpt_messages)
        return gpt_messages


    async def handle_submit(self, form_data:dict):
        print('form data is here: ', form_data)
        user_message = form_data.get('message')
        if user_message:

            self.did_submit = True
            self.append_message(user_message, is_bot=False)

            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)

            # await asyncio.sleep(2) #this can be used for api requests

            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            yield