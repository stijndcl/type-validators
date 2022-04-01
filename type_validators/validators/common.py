from abc import ABC, abstractmethod


class Validator(ABC):
    """Main validator base class that all other validators inherit from"""
    @abstractmethod
    def validate(self, value) -> bool:
        """Validate the value passed to this argument"""
