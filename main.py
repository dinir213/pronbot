from database import start_db
from aiogram.utils import executor
from create_bot import dp, loop
from handlers.start_handler import check_and_send


def register_all_handlers_client(dp):
    from handlers import start_handler, admin
    start_handler.register_handlers_client(dp)
    # from middlewares.middleware import ThrottlingMiddleware
    # dp.middleware.setup(ThrottlingMiddleware())
    admin.register_handlers_client(dp)
async def on_startup(_):
    start_db.db_start()
    register_all_handlers_client(dp)
    loop.create_task(check_and_send())



if __name__ == "__main__":
    # dp.middleware.setup(ThrottlingMiddleware())
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
