from screenpy_selenium import Target

from ui.base_page import BasePage


class CompanyPage(BasePage):
    COMPANY_NAME_HEADER = Target.the('Company Name Header').located_by("h1[class*='name']")

    def __init__(self, url):
        super().__init__(url)
        self.company_name = ''

    def of_the_company(self, company_name):
        self.company_name = company_name
        self.url = self.url.format(company_name=company_name.lower())
        return self
