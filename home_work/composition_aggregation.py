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
        self.os = [Linux('Ubuntu'), Windows('7')]


    def __str__(self):
        return f'{self.__class__.__name__} installed {len(self.os)} os: {", ".join(map(lambda x: f"{x.__class__.__name__}", self.os))} '


class Linux:  #ubuntu
    def __init__(self,  distribution):
        self.os_name = distribution


class Windows: # 7
    def __init__(self, version):
        self.version = version






if __name__ == '__main__':
    # classic = Melody(['♩', '♪', '♫', '♬', '♭', '♮', '♯', '♩', '♪', '♫', '♬', '♭', '♮', '♯'], 'Robert B. Weide')
    # play_music = Guitar(classic)
    # print(play_music.play_melody)

    lp = Laptop('User')
    print(lp)
