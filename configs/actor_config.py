from typing import Generator
from pytest import fixture
from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb


@fixture
def the_qa_engineer(driver) -> Generator:
    the_actor = Actor.named('The QA Engineer').who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit()


@fixture(scope='class')
def the_qa_engineer(driver) -> Generator:
    the_actor = Actor.named('The QA Engineer').who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit()
