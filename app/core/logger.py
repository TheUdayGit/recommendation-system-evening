import logging

from app.core.config import settings

logger = logging.getLogger("movie-recommender")
logger.setLevel(settings.LOG_LEVEL) # Setting level to info

handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='recommendation_logs.log', encoding='utf-8')
formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formater)
logger.addHandler(handler)
logger.addHandler(file_handler)
