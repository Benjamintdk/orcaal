from utils.AWSDataHandler import AWSDataHandler
from utils.IDataHandler import IDataHandler
from utils.LocalDataHandler import LocalDataHandler


class DataHandlerConfig:
    @staticmethod
    def get_datahandler(handler_type: str) -> IDataHandler:
        if handler_type == "aws":
            return AWSDataHandler
        elif handler_type == "local":
            return LocalDataHandler
        else:
            raise ValueError(f"Handler type {handler_type} input is invalid")
