from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewTabUrl:

    TIMEOUT = 5

    @beat('{} examines the url opened in the new tab.')
    def answered_by(self, the_actor: Actor):
        driver = the_actor.ability_to(BrowseTheWeb).browser
        wait = WebDriverWait(driver, self.TIMEOUT)
        wait.until(EC.number_of_windows_to_be(2))
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        url = driver.current_url
        driver.close()
        driver.switch_to.window(windows[0])
        return url
