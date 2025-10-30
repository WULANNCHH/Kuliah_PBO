class Hero:
    __jumlah = 0   # private class variable untuk menghitung jumlah hero

    def __init__(self, name, health, attPower, armor):
        # semua atribut bersifat private
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        # atribut dinamis yang bergantung pada level
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        # health awal sama dengan health max
        self.__health = self.__healthMax

        # setiap kali objek dibuat, jumlah hero bertambah
        Hero.__jumlah += 1

    # getter untuk info jumlah hero
    @classmethod
    def getJumlah(cls):
        return cls.__jumlah

    # property untuk mendapatkan info hero
    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n" \
               f"health = {self.__health}/{self.__healthMax}\n" \
               f"attack = {self.__attPower}\n" \
               f"armor = {self.__armor}"

    # property gainEXP (setter dan getter)
    @property
    def gainEXP(self):
        pass  # hanya agar setter bisa dipakai

    @gainEXP.setter
    def gainEXP(self, addExp):
        self.__exp += addExp
        print(f"{self.__name} mendapatkan {addExp} exp")

        # perulangan level up
        while self.__exp >= 100:
            print(f"{self.__name} level up!")
            self.__level += 1
            self.__exp -= 100

            # hitung ulang atribut dinamis berdasarkan level baru
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax  # reset darah saat naik level

    # method attack
    def attack(self, musuh):
        print(f"{self.__name} menyerang {musuh.__name}")
        self.gainEXP = 50


# TEST CASE
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)
