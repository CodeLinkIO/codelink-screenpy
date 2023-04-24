from screenpy import Actor

from libraries.api_client import ApiClient


class CallAnApi:
    """Enable an Actor to work with APIs.

    Examples::

        the_actor.can(CallAnApi())
    """

    def __init__(
            self,
            the_actor: Actor,
            base_url: str = None
    ):
        self.the_actor = the_actor
        self.base_url = base_url
        self.api = ApiClient(the_actor, base_url)

    @staticmethod
    def using(
            the_actor: Actor,
            base_url: str = None
    ) -> "ApiClient":
        """Provide an API Client to use to work with APIs."""
        return ApiClient(the_actor, base_url)
