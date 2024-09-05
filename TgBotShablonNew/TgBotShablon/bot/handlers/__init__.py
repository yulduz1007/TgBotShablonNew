from bot.dispatcher import dp
from bot.handlers.main import main_router

dp.include_routers(*[
    main_router
])