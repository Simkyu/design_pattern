from abc import ABC, abstractmethod


class Weapon(ABC):
    range: int
    country: str
    category: str
    def __init__(self, range, country):
        self.range = range
        self.country = country
        self.category = None

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def upgrade(self):
        pass

class Sword(Weapon):
    range: int
    country: str
    category: str
    def __init__(self, range, country):
        super().__init__(range, country)
        self.category = "sword" 
        """
        [chatgpt]
        현재 구조에서 Sword 클래스 안에 "sword"로 박아두는 것도 실용적이지만,
        “순수 추상 팩토리”에서는 팩토리가 category까지 포함한 모든 속성을 결정하는 방식이 더 이상적입니다.
        """

    def attack(self):
        print(f"공격범위 : {self.range}")
        print(f"{self.country} - {self.category} : 공격 개시")

    def upgrade(self):
        print(f"{self.country} - {self.category} : 강화 개시")


class Spear(Weapon):
    range: int
    country: str
    category: str
    def __init__(self, range, country):
        super().__init__(range, country)
        self.category = "spear"

    def attack(self):
        print(f"공격범위 : {self.range}")
        print(f"{self.country} - {self.category} : 공격 개시")

    def upgrade(self):
        print(f"{self.country} - {self.category} : 강화 개시")



class WeaponFactory(ABC):
    country: str
    sword_range: int # dict 나 설정파일로 관리
    spear_range: int
    @abstractmethod
    def make_sword(self) -> Weapon:
        pass

    @abstractmethod
    def make_spear(self) -> Weapon:
        pass


class ChinaWeaponFactory(WeaponFactory):
    def __init__(self) -> None:
        self.country = "china"
        self.sword_range = 1
        self.spear_range = 3

    def make_sword(self) -> Weapon:
        print(f"{self.country}제 검 생산")
        return Sword(self.sword_range, self.country)

    def make_spear(self) -> Weapon:
        print(f"{self.country}제 창 생산")
        return Spear(self.spear_range, self.country)


class EnglandWeaponFactory(WeaponFactory):
    def __init__(self) -> None:
        self.country = "england"
        self.sword_range = 1
        self.spear_range = 4

    def make_sword(self) -> Weapon:
        print(f"{self.country}제 검 생산")
        return Sword(self.sword_range, self.country)


    def make_spear(self) -> Weapon:
        print(f"{self.country}제 창 생산")
        return Spear(self.spear_range, self.country)


def main():
    england_weapon_factory = EnglandWeaponFactory()
    england_sword = england_weapon_factory.make_sword()
    england_spear = england_weapon_factory.make_spear()
    england_sword.attack()
    england_spear.attack()

    china_weapon_factory = ChinaWeaponFactory()
    china_sword = china_weapon_factory.make_sword()
    china_spear = china_weapon_factory.make_spear()
    china_sword.attack()
    china_spear.attack()


if __name__ == "__main__":
    main()