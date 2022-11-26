from pytest import fixture


@fixture
def pages(env):
    return locals()
