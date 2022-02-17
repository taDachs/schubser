import http.client
import urllib


class Pushover:
    def __init__(self, token: str, user: str):
        """
        Constructs a new 'Pushover' object.

        :param token: pushover app token
        :user token: pushover user token
        """
        self.token = token
        self.user = user
        self.conn = http.client.HTTPSConnection("api.pushover.net:443")

    def message(
        self,
        title: str,
        msg: str,
        priority: int = 0,
        retry: int = 30,
        expire: int = 10_000,
        sound: str = "pushover",
        **kwargs,
    ) -> None:
        """
        Push a message to Pushover. For more information regarding the
        parameters see the Pushover API reference.

        :param title: message title
        :param msg: message body
        :param priority: message priority, from -2 to 2
        :param retry: seconds between tries
        :param expire: seconds to expire
        :param sound: name of sound to play

        :raises Exception: on response status code != 200
        """

        if priority > 2 or priority < -2:
            raise f"priority must be between -2 and 2, but was {priority}"

        if retry < 30:
            raise f"retry must be >= 30, but was {retry}"

        if expire > 10_000:
            raise f"expire must be <= 10000, but was {expire}"

        self.conn.request(
            "POST",
            "/1/messages.json",
            urllib.parse.urlencode(
                {
                    "token": self.token,
                    "user": self.user,
                    "title": title,
                    "message": msg,
                    "priority": priority,
                    "retry": retry,
                    "expire": expire,
                    "sound": sound,
                    **kwargs,
                }
            ),
            {"Content-type": "application/x-www-form-urlencoded"},
        )

        response = self.conn.getresponse()

        if response.status != 200:
            raise f"Request failed with error code {response.status}"
