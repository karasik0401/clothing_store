from uuid import UUID, uuid4
import asyncio
from fastapi import APIRouter, Depends, HTTPException, Body
from typing import Optional
from app.services.cart_service import CartService
from app.models.cart import Cart, Item


cart_router = APIRouter(prefix='/cart', tags=['Cart'])

@cart_router.get('/')
def get_carts(cart_service: CartService = Depends(CartService)) -> list[Cart]:
    return cart_service.get_carts()

@cart_router.get('/{id}}')
def get_cart_by_id(id: UUID, cart_service: CartService = Depends(CartService)) -> Cart:
    try:
        return cart_service.get_cart_by_id(id)
    except KeyError:
        raise HTTPException(404, f'Cart with id={id} not found')

@cart_router.post('/')
def create_or_update_cart(item: Item, cart_service: CartService = Depends(CartService), id: Optional[UUID] = None) -> Cart:
    try:
        if id and cart_service.get_cart_by_id(id):
            order = cart_service.update_cart(id, item)
            return order.__dict__
        order = cart_service.create_cart(item)
        return order.dict()
    except KeyError:
        raise HTTPException(404, f'Order with {id} not found')