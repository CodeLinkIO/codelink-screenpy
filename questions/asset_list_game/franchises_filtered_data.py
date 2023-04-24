import typing

from screenpy import Actor
from screenpy.pacing import beat


class FranchisesFilteredData:

    def __init__(
            self,
            franchises: dict,
            titles: dict,
            only_active_titles: bool = False,
            only_ea_titles: bool = False,
            additional_content: bool = False
    ) -> None:
        self.franchises: list = franchises.get("franchises")
        self.titles: list = titles.get("titles")
        self.only_active_titles = only_active_titles
        self.only_ea_titles = only_ea_titles
        self.additional_content = additional_content

    @beat("{} examines the franchises list.")
    def answered_by(self, the_actor: Actor) -> typing.List[str]:
        the_actor.cleans_up_ordered_tasks()
        desired_franchise_ids = []
        if self.only_active_titles:
            desired_franchise_ids += set([item['franchiseId'] for item in self.titles if item['isActive']])
        if self.only_ea_titles:
            desired_franchise_ids += set([item['franchiseId'] for item in self.titles if item['isEAGame']])
        if self.additional_content:
            desired_franchise_ids += set([item['franchiseId'] for item in self.titles if item['gameObjectType'] == 'base-game'])
        if desired_franchise_ids:
            desired_franchises = list(filter(lambda franchise: franchise['id'] in set(desired_franchise_ids), self.franchises))
        else:
            valid_franchise_ids = set([item['franchiseId'] for item in self.titles])
            desired_franchises = [item for item in self.franchises if item['id'] in valid_franchise_ids]
        return [item['name'] for item in desired_franchises]
