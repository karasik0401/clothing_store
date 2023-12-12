from fastapi import FastAPI
from app.endpoints.cart_router import cart_router

app = FastAPI(title='Cart Service')


app.include_router(cart_router)