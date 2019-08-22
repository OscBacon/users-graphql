from datetime import date

from tartiflette import Resolver
from users import version


@Resolver("Query.version")
async def get_version(parent, args, ctx, info):
    return version


@Resolver("Query.users")
async def get_users(parent, args, ctx, info):
    firstname = "Mark"
    lastname = "Toto"
    birthdate = date.today()

    edges = [
        {
            "node": {
                "id": _id,
                "firstname": firstname,
                "lastname": lastname,
                "birthdate": birthdate,
            }
        }
        for _id in range(1, 4)
    ]
    print(edges)

    return {"edges": edges}
