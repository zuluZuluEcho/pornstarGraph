from pydantic_settings import BaseSettings


class Constants(BaseSettings):
    PATH_PORNSTAR_FILE: str
    PATH_FILE_FREQUENCY_PER_PORNSTAR: str
    PATH_FILE_FREQUENCY_PER_PORNSTAR_PAIR: str
    PATH_FILENAME_FOR_CPP: str

    class Config:
        env_file: str = ".env"


constants: Constants = Constants()
