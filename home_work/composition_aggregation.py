import random
import time


class Guitar:
    def __init__(self, melody):
        self.melody = melody
        self.n_note = 0

    def __repr__(self):
        return f'Compositor: {self.melody.compositor}.'

    def __iter__(self):
        return self

    def __next__(self):
        if self.n_note >= len(self.melody):
            raise StopIteration
        else:
            note = random.choice(self.melody._note)
            self.n_note += 1
            return note

    @property
    def play_melody(self):
        for music in self:
            time.sleep(0.3)
            print(music)
        return f'Directed by {self.melody.compositor}...'


class Melody:
    def __init__(self, note, compositor):
        self._note = note
        self.compositor = compositor

    def __len__(self):
        return len(self._note)


class Laptop:
    def __init__(self, user_name):
        self.user_name = user_name
        self.linux = OperatingSystem('linux', 'Telegram', 'Viber', 'PyCharm',
                                     'Atom', 'Google Chrome')
        self.windows = OperatingSystem('Windows 10', 'Zoom', 'Skype', 'Telegram', 'Viber',
                                       'PyCharm', 'Atom', 'Google Chrome')

    def __str__(self):
        return f'{self.__class__.__name__} installed os:' \
               f' {self.linux.os_name}, {self.windows.os_name}\n' \
               f'Manual installed programs on os linux :' \
               f' {len(self.linux.programs)} -> {", ".join(self.linux.programs)}.\n' \
               f'Manual installed programs on os windows 10 :' \
               f' {len(self.windows.programs)} -> {", ".join(self.linux.programs)}.'


class OperatingSystem:
    def __init__(self, os_name, *programs):
        self.os_name = os_name
        self.programs = programs


if __name__ == '__main__':
    classic = Melody(['♩', '♪', '♫', '♬', '♭', '♮', '♯', '♩', '♪', '♫', '♬', '♭', '♮', '♯'], 'Robert B. Weide')
    play_music = Guitar(classic)
    print(play_music.play_melody)

    lp = Laptop('User')
    print(lp)
