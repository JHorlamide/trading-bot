""" Trading Model"""
from enum import Enum
from pydantic import BaseModel

class ActivesTypes(str, Enum):
    """ Available Active Types on IQ Option"""
    EURUSD = "EURUSD"
    EURGBP = "EURGBP"


class ActionTypes(str, Enum):
    """ Available Action Types on IQ Option"""
    CALL = "call"
    PUT = "put"


class Trade(BaseModel):
    """ Trading Data """
    money: int
    expirations_mode: int
    actives: str
    action: str
