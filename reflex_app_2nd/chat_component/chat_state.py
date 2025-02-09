import reflex as rx
import asyncio
from typing import List
from . import ai
from reflex_app_2nd.models import ChatSession, ChatSessionMessageModel

class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    chat_session: ChatSession = None
    did_submit: bool = False
    messages: List[ChatMessage] =[]

    @rx.var (cache=True)
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def create_new_chat_session(self):
        with rx.session() as db_session:
                obj = ChatSession()
                db_session.add(obj)
                db_session.commit()
                db_session.refresh(obj)
                #print("\nPrint out the chat session object and id: ", obj, obj.id)
                self.chat_session= obj

    def clear_and_start_new(self):
        self.chat_session = None
        self.create_new_chat_session()
        self.messages = []
        yield

    def on_load(self):
        
        # with rx.session() as session:
        #     results = session.exec(
        #         ChatModel.select()
        #     ).all()

        #     print(results)
        print("running on load")
        if self.chat_session is None:
            self.create_new_chat_session()

    def insert_message_to_db (self, content, role='unknown'):
        print("running insert message data to db ")
        if self.chat_session is None:
            return
        if not isinstance(self.chat_session, ChatSession):
            return
        with rx.session() as db_session:
            data = {
                "session_id": self.chat_session.id,
                "content": content,
                "role": role

            }
            obj = ChatSessionMessageModel(**data)
            db_session.add(obj)
            db_session.commit()
            #print("\nPrint out the chat session object and id: ", obj, obj.id)


    
    def append_message_to_ui(self, message, is_bot:bool=False):

        # if not is_bot:
        #     with rx.session() as session:
        #         obj = ChatModel(
        #             title=message,
        #         )
        #         session.add(obj)
        #         session.commit()

        if self.chat_session is not None:
            # print (self.chat_session.id)
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
        # print("chatgpt messages: ", gpt_messages)
        return gpt_messages


    async def handle_submit(self, form_data:dict):
        # print('form data is here: ', form_data)

        user_message = form_data.get('message')

        if user_message:

            self.did_submit = True
            self.append_message_to_ui(user_message, is_bot=False)
            self.insert_message_to_db(user_message, role='user')

            yield
            gpt_messages = self.get_gpt_messages()
            bot_response = ai.get_llm_response(gpt_messages)

            # await asyncio.sleep(2) #this can be used for api requests

            self.did_submit = False
            self.append_message_to_ui(bot_response, is_bot=True)
            self.insert_message_to_db(bot_response, role='system')
            yield