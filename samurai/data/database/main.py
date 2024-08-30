from samurai.infra import env

class Sqlite:
    
    def connect(self, url: str = env.DATABASE_URL):
        ...