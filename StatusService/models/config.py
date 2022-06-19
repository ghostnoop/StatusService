from typing import List

from StatusService.settings import settings

TORTOISE_CONFIG = {
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": ["models.main"],
            "default_connection": "default",
        },
    },
}

