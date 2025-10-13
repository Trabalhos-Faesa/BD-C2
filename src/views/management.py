from fastapi import APIRouter


router = APIRouter(prefix='/-', tags=['management'])


@router.get('/health')
async def health_check():
    return {'status': 'healthy'}
