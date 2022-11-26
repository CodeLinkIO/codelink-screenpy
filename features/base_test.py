import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, env):
        self.env = env
