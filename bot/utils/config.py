import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class that reads environment variables to set various settings.
    """

    def __init__(self):
        self.API_ID: int = int(os.environ.get("API_ID", 0))
        self.API_HASH: str = os.environ.get("API_HASH", "")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
        self.OWNER_ID: int = int(os.environ.get("OWNER_ID", 0))
        self.MONGODB_URL: str = os.environ.get("MONGODB_URL", "")
        self.DATABASE_CHAT_ID: int = int(os.environ.get("DATABASE_CHAT_ID", 0))
        self.OWNER_USERNAME: str = "IlhamTag"

        # Perform validation
        self._validate()

    def _validate(self):
        """
        Validate environment variables to ensure they are correct.
        """
        if not self.API_ID:
            raise ValueError("API_ID: Missed")
        if not self.API_HASH:
            raise ValueError("API_HASH: Missed")
        if not self.BOT_TOKEN:
            raise ValueError("BOT_TOKEN: Missed")
        if not self.OWNER_ID:
            raise ValueError("OWNER_ID: Missed")
        if not self.MONGODB_URL:
            raise ValueError("MONGODB_URL: Missed")
        if not self.DATABASE_CHAT_ID:
            raise ValueError("DATABASE_CHAT_ID: Missed")


config: Config = Config()
