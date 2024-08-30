from sqlalchemy.orm import Session

from abc import ABC, abstractmethod


class DataSource(ABC):

    @property
    @abstractmethod
    def session(self) -> Session:
        raise NotImplementedError

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError
