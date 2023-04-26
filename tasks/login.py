from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Click

from ui import LoginPage


class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @beat("{} logs in with username '{username}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Enter.the_text(self.username).into_the(LoginPage.USERNAME_INPUT),
            Enter.the_password(self.password).into_the(LoginPage.PASSWORD_INPUT),
            Click.on_the(LoginPage.LOG_IN_BUTTON)
        )
