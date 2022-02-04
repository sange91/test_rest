from fastapi import APIRouter
from webapi.lib.models.transaction import Transaction
from webapi.lib.routes import get_root_route

transaction_route = '{}/transaction'.format(get_root_route())
router = APIRouter(prefix=transaction_route)


@router.get('', response_model=Transaction)
@router.get('/{id}', response_model=Transaction)
def get_transaction(transaction_id: int = None):
    return {'test': 'hi'}


@router.post('')
def create_transaction(request: Transaction):
    return {}
