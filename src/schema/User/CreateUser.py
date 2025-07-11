from dataclasses import dataclass
from enum import auto, Enum

class UserStatus(Enum):
    CREATED = auto()
    EXISTS = auto()
    INVALID = auto()

@dataclass
class CreateUserResult:
    status: UserStatus
    message: str