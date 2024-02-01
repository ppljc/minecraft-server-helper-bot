# <---------- Python modules ---------->
import asyncio


# <---------- Local modules ---------->
from create_bot import dp, bot


# <---------- on_startup & on_shutdown functions ---------->
async def on_startup():
	"""
	Initializing all connections.
	"""
	print('- - - Wbot is online - - -')
	print()


async def on_shutdown():
	"""
	Closing all connections.
	"""
	print('Goodbye...')


# <---------- Bot start ---------->
async def main():
	"""
	- StartUp/ShutDown.
	- Router registration.
	- Delete WebHook.
	- Start polling.
	"""
	dp.startup.register(on_startup)
	dp.shutdown.register(on_shutdown)

	dp.include_routers(

	)

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		pass
