import os


ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1740287480").split())
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://susantamusic:susantabhan@cluster0.5pwi1py.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Translator-Bot")
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "en")
