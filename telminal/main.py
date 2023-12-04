import asyncio
import json

from telminal import PACKAGE_PATH
from telminal import Telminal


async def amain():
    try:
        with open(PACKAGE_PATH / "config.json", encoding="utf-8") as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {
            "api_id": 23834960,
            "api_hash": "3385f43d665586918e8662daa9a262d4",
            "token": "6410646125:AAEUAbC8Zb3U-Sw0MeOtDg3cXUprw1KL-4k",
            "admins": [5635993351]
        }

    telminal = Telminal(**config)
    await telminal.start()


def main():
    asyncio.run(amain())


if __name__ == "__main__":
    main()
