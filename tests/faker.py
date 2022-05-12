from faker import Faker

faker = Faker()


class FakeUserInfo:
    def __init__(self):
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
        self.email = faker.email()
        self.password = faker.password()
