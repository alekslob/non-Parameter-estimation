from loguru import logger

logger.catch(
    Exception,
    message='Ошибка инициализации',
    level="DEBUG",
    reraise=True
)
from .interface import init
def start():
    try:
        init()
    except KeyboardInterrupt:
        pass