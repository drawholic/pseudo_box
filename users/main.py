from fastapi import Depends, APIRouter
from db.main import get_db
from sqlalchemy.orm import Session
from .crud import get_users, get_user, create_user,  check_user, update_user
from .pd_models import User, UserCreate


router = APIRouter(prefix='/users', tags=['Users'])



@router.get('', response_model=list[User])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.get('/{user_id}', response_model=User)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(user_id, db)
    if user is None:
        return 'No such user'
    return user


@router.post('/', response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    if check_user(user, db):
        return 'username is taken'
    else:
        user = create_user(user, db)
        return user

@router.patch('/{user_id}')
def patch_user(user_id: int, data: dict, db: Session = Depends(get_db)):
    try:
        update_user(user_id, data, db)
        
    except Exception as e:
        print(e)
        return e

