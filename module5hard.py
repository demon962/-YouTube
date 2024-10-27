import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def verify_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

class Video:
    def __init__(self, title, description, age_limit=0):
        self.title = title
        self.description = description
        self.age_limit = age_limit

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.verify_password(password):
                self.current_user = user
                return f"Пользователь {nickname} успешно вошёл в систему."
        return "Ошибка: Неверное имя пользователя или пароль."

    def log_out(self):
        if self.current_user:
            current_nickname = self.current_user.nickname
            self.current_user = None
            return f"Пользователь {current_nickname} вышел из системы."
        return "Ошибка: Пользователь не авторизован."

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            return f"Пользователь {nickname} уже существует."
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)  # Регистрируем пользователя
            return f"Пользователь {nickname} зарегистрирован."

    def add(self, *videos):
        messages = []
        for video in videos:
            if not any(v.title.lower() == video.title.lower() for v in self.videos):
                self.videos.append(video)
                messages.append(f"Видео '{video.title}' добавлено.")
            else:
                messages.append(f"Ошибка: Видео '{video.title}' уже существует.")
        return messages

    def watch_video(self, title):
        if not self.current_user:
            return "Войдите в аккаунт, чтобы смотреть видео."

        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            return "Ошибка: Видео не найдено."

        if self.current_user.age < video.age_limit:
            return "Вам нет 18 лет, пожалуйста, покиньте страницу."

        output = [f"Воспроизведение видео: {video.title}"]
        for second in range(1, 11):
            output.append(str(second))
            time.sleep(1)
        output.append("Конец видео")
        return output


if __name__ == "__main__":
    urtube = UrTube()


    print("\n".join(urtube.add(Video('Лучший язык программирования 2024 года', 'Обзор языка.', age_limit=18),
                                Video('Для чего девушкам парень программист?', 'Обсуждаем преимущества.'))))

    print(urtube.register('vasya_pupkin', 'password123', age=20))
    print(urtube.register('urban_pythonist', 'mypassword', age=17))

    print(urtube.watch_video('Лучший язык программирования 2024 года'))

    print(urtube.log_in('urban_pythonist', 'mypassword'))

    print(urtube.watch_video('Лучший язык программирования 2024 года'))
