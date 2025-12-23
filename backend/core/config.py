from pydantic import BaseSttings

class Settings(BaseSttings):
    DATABASE_URL = ""

settings = Settings() 