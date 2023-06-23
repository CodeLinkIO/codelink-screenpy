import typing

from screenpy.resolutions import BaseResolution


class EqualToAsListOfDictionaries(BaseResolution):

    line = "2 lists of dictionaries is equal"

    def __init__(
            self,
            list_of_dict_1: typing.List[typing.Dict],
            list_of_dict_2: typing.List[typing.Dict]
    ) -> None:
        super().__init__()
        self.list_of_dict_1 = list_of_dict_1
        self.list_of_dict_2 = list_of_dict_2
        self.compare_two_lists_of_dictionaries()

    def compare_two_lists_of_dictionaries(self):
        assert any(x != y for x, y in zip(self.list_of_dict_1, self.list_of_dict_2))
