from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwitchToNewTab:

    TIMEOUT = 5

    @beat("{} switches to new tab.")
    def perform_as(self, the_actor: Actor) -> None:
        driver = the_actor.ability_to(BrowseTheWeb).browser
        wait = WebDriverWait(driver, self.TIMEOUT)
        wait.until(EC.number_of_windows_to_be(2))
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
