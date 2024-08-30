from fastapi import APIRouter, Query

from samurai.application.schemas.samurai_schema import (
    SamuraiSchema,
    SamuraiCreateSchema,
    SamuraiResponseSchema
)

router = APIRouter(
    prefix='/samurai',
    tags=['Samurai'],
)


@router.get('/')
async def ola_samurai():
    return {'message': 'olá samurai'}


@router.post('/new', response_model=SamuraiResponseSchema)
async def new_samurai(samurai: SamuraiCreateSchema, name: str = Query(None)):
    return {
        "name": "string",
        "age": 1,
        "family": "Tokugawa",
        "power": {
            "name": "string",
            "force": 1
        },
        "id": 1
    }