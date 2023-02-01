class HandledExceptions(Exception):
    """Base class for other exceptions"""
    pass


class InvalidInput(HandledExceptions):
    """Raised when No file is uploaded"""
    def __init__(self,error) -> None:
        self.message="Invalid Input : "+error
        super().__init__(self.message)
