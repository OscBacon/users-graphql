from typing import Any, Callable, Dict, Optional

import aiohttp
from tartiflette import Directive

@Directive("paginate")
class Paginate():
    async def on_field_execution(
        self,
        directive_args: Dict[str, Any],
        next_resolver: Callable,
        parent_result: Optional[Any],
        args: Dict[str, Any],
        ctx: Optional[Dict[str, Any]],
        info: "Info",
    ) -> Any:
        parent_result["edges"] += [{"node": {"id": 123455}}]
        parent_result["pageInfo"] = {
            "hasNextPage": True,
            "hasPreviousPage": False,
            "startCursor": "cursor1",
            "endCursor": "cursor2"
        }
        return await next_resolver(parent_result, args, ctx, info)
