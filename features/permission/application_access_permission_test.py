from screenpy import AnActor, given, when
from screenpy_selenium.actions import Open

from features.base_test import BaseTest
from tasks.login import Login


class TestApplicationPermission(BaseTest):

    def test_access_asset_list_game(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).attempts_to(Open.their_browser_on(self.pages['ASSET_LIST_GAME_PAGE'].url))
        when(the_qa_engineer_2).attempts_to(Login('cunguyen', 'forgottenking4tw'))

# TODO: add verify point, figure out a way to pass username and password from commandline
