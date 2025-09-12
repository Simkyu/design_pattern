from abc import ABC, abstractmethod


class SpawnUnitFactory(ABC):
    @abstractmethod
    def spawn_unit(self, unit_name: str):
        pass

    def operation(self, unit_name: str):
        unit = self.spawn_unit(unit_name)
        print(f"{unit_name} spawn complete!")
        unit.spawned()


class Barrack(SpawnUnitFactory):
    def spawn_unit(self, unit_name: str):
        if unit_name == "marine":
            return Marine(unit_name, "You want a piece of me, boy?")
        elif unit_name == "medic":
            return Medic(unit_name, "Please state the nature of your medical emergency.")

class Starport(SpawnUnitFactory):
    def spawn_unit(self, unit_name: str):
        if unit_name == "wraith":
            return Wraith(unit_name, "Wraith awaiting launch orders!")


class Unit(ABC):
    def __init__(self, unit_name:str, spawning_phrase: str):
        self.unit_name = unit_name
        self.spawning_phrase = spawning_phrase

    @abstractmethod
    def spawned(self):
        pass

class Marine(Unit):
    def spawned(self):
        print(f"{self.spawning_phrase}. go.")

class Medic(Unit):
    def spawned(self):
        print(f"{self.spawning_phrase}. stop.")

class Wraith(Unit):
    def spawned(self):
        print(f"{self.spawning_phrase}. wingwing.")


if __name__ == "__main__":
    barrack = Barrack()
    starport = Starport()
    barrack.operation("marine")
    barrack.operation("marine")
    barrack.operation("medic")
    starport.operation("wraith")

