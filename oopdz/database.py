class DataBase:
    def __init__(self, path):
        self.path = path

    def authentication(self, email, password):
        with open(self.path, "r") as db:
            for lines in db.readlines():
                mail, pas = lines.split()
                if mail == email and pas == password:
                    print("Вы авторизовались")
                    break
            else:
                print("Неверный логин или пароль")

    def new_user(self, email, password):
        with open(self.path, "r") as db:   #проверка на отсутствие идентичной почты в базе
            for lines in db.readlines():
                mail, pas = lines.split()
                if mail == email:
                    print("Пользователь с таким логином уже зарегестрирован")
                    break
            else:
                with open(self.path, "a") as db:
                    db.write(f"\n{email} {password}")                                # переносы строк зависят от того, будет ли в конце файла перенос, я взял случай, когда в конце данного файла нет переноса строки
                    print("Пользователь успешно зарегестрирован")

    def change_pas(self, email, password):
        with open(self.path, "r+") as db:
            lines = db.readlines()
            for i in range(len(lines)):
                if email in lines[i]:
                    lines[i] = f"{email} {password}\n"
                    db.seek(0)
                    db.writelines(lines)
                    print("Пароль успешно изменён")
                    break
            else:
                print("В базе нет пользователя с таким логином")

db = DataBase("text.txt")
db.authentication("pythonmaster@yandex.ru", "wherRHrh")
db.new_user("adghdra@mail.ru", "123df45")
db.change_pas("ivanov46@gmail.com", "123dhdrh")