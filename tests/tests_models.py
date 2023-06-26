from .conftest import User


def test_is_instance_user(user: User):
    assert isinstance(user, User)


def test_user_attributes(user: User):
    assert user.first_name == 'peter'
    assert user.last_name == 'parker'
    assert user.email == 'spider@icloud.com'


def test_user_return_str(user: User):
    assert user.__str__() == 'peter'
