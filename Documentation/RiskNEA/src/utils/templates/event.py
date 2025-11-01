from abc import ABC, abstractmethod
from dataclasses import dataclass

class Event(ABC):
    """
    Abstract class for containers with data
    relevant to external objects.
    """
    @abstractmethod
    def __init__(self):
        pass

@dataclass
class ExplicitEvent(Event):
    """
    An event called as a direct result of a player input
    """
    pass

@dataclass
class ImplicitEvent(Event):
    """
    An event called indirectly due to a significant change
    in State
    """

