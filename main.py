from fastapi import FastAPI, HTTPException
from iqoptionapi.stable_api import IQ_Option
from models import Trade

app = FastAPI()

@app.get("/")
async def root():
    """" Root Path """
    return {"Hello": "World"}


@app.post("/api/v1/trades")
async def post_trade_on_iqoption(trade: Trade):
    """Connect to iqoption, if connected successfully, then place trade"""

    iq_option = IQ_Option("olamidejubril68@gmail.com", "#Obalola21#")
    connect_success, connection_failed = iq_option.connect()  # connect to iqoption

    if connect_success:
        print("Connected successfully to IQoption")
        print("Trade Data: ", trade)

        Money = trade.money
        ACTIVES = trade.actives
        ACTION = trade.action
        expirations_mode = trade.expirations_mode

        buy_success, trade_id = iq_option.buy(
            Money, ACTIVES, ACTION, expirations_mode)

        if buy_success:
            return {
                "trade_id": trade_id,
                "message": f"Bought {trade.actives}",
                "wallet_balance": f"Your current balance is: {iq_option.get_balance()}"
            }

        raise HTTPException(
            status_code=400,
            detail=f"Buying of {trade.actives} failed"
        )
    raise HTTPException(
        status_code=400,
        detail=f"Connection failed. Reason {connection_failed}"
    )
