from screenpy import AnActor, given, when, then
from screenpy.actions import See
from screenpy.resolutions import IsEqual, Equals
from screenpy_selenium.actions import Open
from screenpy_selenium.questions import Text, BrowserURL

from features.base_test import BaseTest
from tasks.Example.search_on_homepage import SearchOnHomePage
from ui.Example.company_page import CompanyPage
from ui.Example.homepage import HomePage


class TestITViec(BaseTest):

    def test_goto_itviec(self, the_qa_engineer: AnActor):
        given(the_qa_engineer).attempts_to(Open.their_browser_on(self.pages['homepage'].url))
        then(the_qa_engineer).should(
            See.the(BrowserURL(), Equals(self.pages['homepage'].url))
        )

    def test_search_for_codelink(self, the_qa_engineer: AnActor):
        given(the_qa_engineer).attempts_to(Open.their_browser_on(self.pages['homepage'].url))
        when(the_qa_engineer).attempts_to(SearchOnHomePage("codelink"))
        company_page: CompanyPage = self.pages['company_page'].of_the_company('CodeLink')
        then(the_qa_engineer).should(
            See.the(BrowserURL(), Equals(company_page.url)),
            See.the(Text.of_the(CompanyPage.COMPANY_NAME_HEADER), Equals("CodeLink"))
        )


