from uuid import UUID
from archery_secret import Secret
from archery_auth.sql import Session
from archery_auth.sql.models.roles import Role as RoleModel


class Role:
    __secret = Secret()
    __session = Session()

    def add(
        self: object,
        name: str,
        description: str
    ) -> bool:
        self.__session.add(
            RoleModel(
                name=name,
                description=description
            )
        )
        self.__session.commit()
        return True

    @property
    def roles(
        self: object
    ) -> list:
        db_return = self.__session.query(
            RoleModel
        )
        roles = []
        [
            roles.append(
                {
                    'name': role.name,
                    'description': role.description
                }
            ) for role in db_return
        ]
        return roles

    def show_id(
        self: object,
        name: str
    ) -> str:
        role = self.__session.query(
            RoleModel
        ).filter(
            RoleModel.name == name
        ).one()
        return self.__secret.encrypt(
            role.id
        )

    def remove(
        self: object,
        id: str
    ) -> bool:
        role = self.__session.query(
            RoleModel
        ).filter(
            RoleModel.id == UUID(id)
        ).one()
        self.__session.delete(
            role
        )
        self.__session.commit()
        return True
