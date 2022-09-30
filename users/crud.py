from db.models import User



def get_users(db):
    return db.query(User).all()


def get_user(id:int, db):
    return db.query(User).filter(User.id==id).first()

def check_user(user, db):
    user = db.query(User).filter(User.username==user.username).first()
    if user is None:
        return False
    return True


def create_user(user, db):
    password = hash(user.password)
    user_db = User(username=user.username, password=password)
    db.add(user_db)
    db.commit()
    return user_db

def update_user(user_id, data, db):
    user = db.query(User).filter(User.id==user_id).first()
    for key in data:
        setattr(user, key, data[key])
    db.commit()
    return user
