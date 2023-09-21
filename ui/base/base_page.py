from screenpy_selenium import Target


class BasePage:

    SMALL_LOADING_ICON = Target.the('Small Loading Icon').located_by("[class^='SmallLoader']")

    def __init__(self, url):
        self.url = url
