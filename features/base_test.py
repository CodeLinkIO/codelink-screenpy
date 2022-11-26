from pytest import fixture


class BaseTest:
    @fixture(autouse=True)
    def injector(self, env, pages):
        self.env = env
        self.pages = pages
