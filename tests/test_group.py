from faker import Faker
from database.models import User, Group
from database.database import session

faker = Faker()


class TestGroup:
    def create_user(self):
        """helper func: to create a user"""
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()

        new_user_id = User.create(email=email,
                                  first_name=first_name,
                                  last_name=last_name,
                                  password=password)

        new_user = session.query(User).filter_by(id=new_user_id).first()
        return new_user

    def test_create_group(self, test_db):
        """
        create a group object
        get new object id from database
        check that group exists
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        new_group_id = Group.create(name=name,
                                    owned_by_user=owned_by_user)

        new_group = session.query(Group).filter_by(id=new_group_id).first()

        assert new_group
        assert new_group.name == name
        assert new_group.owned_by_user == owned_by_user
        assert new_group.time_created
        assert not new_group.users

    def test_group_exists(self, test_db):
        """
        create group object
        check that group exists
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        assert Group.exists(group.id)

    def test_group_not_exist(self, test_db):
        """
        check that group_id 5000 does not exist
        """
        id = 5000

        assert not Group.exists(id)

    def test_get_group(self, test_db):
        """
        create group and test that it can be retrieved via get
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        retrieved_group = Group.get(id=group.id)
        assert retrieved_group.name == name
        assert retrieved_group.owned_by_user == owned_by_user

    def test_get_all_groups(self, test_db):
        """
        delete all rows in Group table
        create num_groups and then get them all from db.
        passes if the correct number of groups is returned
        """
        session.query(Group).delete()
        session.commit()

        num_groups = 10
        for i in range(num_groups):
            user = self.create_user()

            name = faker.user_name()
            owned_by_user = user.id

            group = Group(name=name, owned_by_user=owned_by_user)

            session.add(group)
            session.commit()

        groups = Group.get_all()

        assert len(groups) == num_groups

    def test_update_group_1(self, test_db):
        """
        create group, update the group to new val, and then retrieve it from the db.
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        new_name = faker.user_name()
        new_group = {'name': new_name}

        updated_group = Group.update(id=group.id, **new_group)

        assert updated_group.name == new_name
        assert updated_group.owned_by_user == owned_by_user

    def test_update_group_2(self, test_db):
        """
        create group, update the group to new val, and then retrieve it from the db.
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        new_user = self.create_user()
        new_name = faker.user_name()
        new_owned_by_user = new_user.id
        new_group = {'name': new_name, 'owned_by_user': new_owned_by_user}

        updated_group = Group.update(id=group.id, **new_group)

        assert updated_group.name == new_name
        assert updated_group.owned_by_user == new_owned_by_user

    def test_delete_group(self, test_db):
        """
        create group, delete it, & test that it does not exist
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        Group.delete(group)

        assert not bool(session.query(Group).filter_by(id=group.id).first())

    def test_group_member_exists(self, test_db):
        """
        create group object, add user to group
        check that group exists
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        user2 = self.create_user()
        group.users.append(user2)
        group.save()

        assert user2 in group.users

    def test_group_member_exists2(self, test_db):
        """
        create group object, add user to group
        check that group exists
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        user2 = self.create_user()
        group.users.append(user2)
        group.save()

        user3 = self.create_user()
        group.users.append(user3)
        group.save()

        user4 = self.create_user()

        assert user2 in group.users
        assert user3 in group.users
        assert user4 not in group.users

    def test_group_member_delete(self, test_db):
        """
        create group object, add user to group
        check that group exists
        """
        user = self.create_user()

        name = faker.user_name()
        owned_by_user = user.id

        group = Group(name=name, owned_by_user=owned_by_user)

        session.add(group)
        session.commit()

        user2 = self.create_user()
        group.users.append(user2)
        group.save()

        user3 = self.create_user()
        group.users.append(user3)
        group.save()

        group.users.remove(user2)
        group.users.remove(user3)
        group.save()

        assert user2 not in group.users
        assert user3 not in group.users
