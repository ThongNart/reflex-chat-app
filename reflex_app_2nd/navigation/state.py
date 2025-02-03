import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        """
        on_click event
        """
        print('clicked')
        return rx.redirect(routes.HOME_ROUTE)