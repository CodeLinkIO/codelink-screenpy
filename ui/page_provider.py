from pytest import fixture

from ui.Example.company_page import CompanyPage
from ui.Example.homepage import HomePage
from utils.json_reader import deep_get


@fixture
def pages(env, env_data):
    base_url = get_path(env, env_data, 'base_url')

    homepage = HomePage(base_url)
    company_page = CompanyPage(f"{base_url}{get_path(env, env_data, 'paths.companies')}")

    return locals()


def get_path(env, env_data, path):
    return deep_get(
        env_data,
        f'{env}.{path}',
        deep_get(env_data, f'default.{path}')
    )
