from starlite import Starlite, Provide
import uvicorn
from src.plugins import SQLA_PLUG, SQLA_CONF
from src.models import Base

# Routers
# End Routers


async def on_startup() -> None:
    """Initialize the database."""
    async with SQLA_CONF.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = Starlite(
    route_handlers=[
    ],
    plugins=[
        SQLA_PLUG
    ],
    on_startup=[on_startup]
)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        log_level="debug",
        port=80,
        timeout_keep_alive=0,
    )