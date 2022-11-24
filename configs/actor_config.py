from typing import Generator
import pytest
from screenpy import Actor
from screenpy_selenium.abilities import BrowseTheWeb


@pytest.fixture
def the_qa_engineer(driver) -> Generator:
    the_actor = Actor.named('The QA Engineer').who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit()
