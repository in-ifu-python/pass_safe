from config import db


class Passw(object):

    @staticmethod
    def get_all_passw() -> list:
        result = db.passw.find()
        passwords = [x for x in result]
        return passwords

    @staticmethod
    def create_passw(new_passw) -> None:
        passwords = db.passw
        passwords.insert_one(new_passw)
