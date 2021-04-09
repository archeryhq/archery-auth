from uuid import UUID
from archery_secret import Secret
from archery_auth.sql import Session
from archery_auth.sql.models.persons import Person
from archery_auth.sql.models.roles import Role
from archery_auth.parsers.auths.emails import check_email
from archery_auth.parsers.auths.passwords import check_password
from archery_auth.parsers.auths.usernames import check_username
from archery_auth.exceptions import LogInError


class Auth:
    """
        Responsible for communicating with the database, managing users.

    """
    __secret = Secret()
    __session = Session()

    def create(
        self: object,
        username: str,
        email: str,
        password: str
    ) -> bool:
        self.__session.add(
            Person(
                username=check_username(username),
                email=check_email(email),
                password=self.__secret.generate(
                    check_password(password)
                )
            )
        )
        self.__session.commit()
        return True

    def login(
        self: object,
        username: str,
        password: str
    ) -> str:
        person = self.__show(
            username
        )
        if self.__secret.verify(
            person.password,
            password
        ) is True:
            self.id = self.__secret.encrypt(person.id)
            self.username = person.username
            self.email = person.email
            self.role = person.role
            self.enabled = person.enabled
            return {
                'id': self.id,
                'username': self.username,
                'email': self.email,
                'role': self.role,
                'enabled': self.enabled
            }
        else:
            raise LogInError(username)

    def __show(
        self: object,
        username: str
    ) -> dict:
        person = self.__session.query(
            Person
        ).filter_by(
            username=username
        ).first()
        return person

    def change_password(
        self: object,
        password: str
    ) -> bool:
        person = self.__session.query(
            Person
        ).filter_by(
            username=self.username
        ).first()
        person.password = self.__secret.generate(
            check_password(
                password
            )
        ) if str(
            person.id
        ) == self.__secret.decrypt(
            self.id
        ) else False
        self.__session.commit()
        return True

    def change_email(
        self: object,
        email: str
    ) -> bool:
        person = self.__session.query(
            Person
        ).filter_by(
            username=self.username
        ).first()
        if str(
            person.id
        ) == self.__secret.decrypt(self.id):
            person.email = check_email(
                email
            )
            self.email = person.email
            self.__session.commit()
        return True

    def enable(
        self: object,
        id: str,
        enabled: bool = False
    ) -> bool:
        """
            Enable person. Necessary know real person id.
        """
        person = self.__session.query(
            Person
        ).filter_by(
            id=id
        ).first()
        person.enabled = enabled
        self.__session.commit()
        return True

    def change_role(
        self: object,
        person_id: str,
        role_id: str
    ) -> bool:
        person = self.__session.query(
            Person
        ).filter_by(
            id=person_id
        ).first()
        role = self.__session.query(
            Role
        ).filter(
            Role.id == UUID(
                role_id
            )
        ).one()
        person.role = self.__secret.encrypt(
            role.id
        )
        return True

    def remove(
        self: object,
        id: str
    ) -> bool:
        person = self.__session.query(
            Person
        ).filter(
            Person.id == UUID(
                id
            )
        ).one()
        self.__session.delete(
            person
        )
        self.__session.commit()
        return True
