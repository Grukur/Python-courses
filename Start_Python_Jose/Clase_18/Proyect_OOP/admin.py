from Clase_18.Proyect_OOP.user import User


class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

# self.save will be search in Admin
# then in User
# then in Saveable, where it will be found

# self.save uses self.to_dict
# self.to_dict() will be searched in admin, where will be found
