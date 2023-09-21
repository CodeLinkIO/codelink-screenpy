from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb


class ClipboardText:

    @beat('{} examines the clipboard.')
    def answered_by(self, the_actor: Actor):
        driver = the_actor.ability_to(BrowseTheWeb).browser
        return driver.execute_script('return navigator.clipboard.readText()')
