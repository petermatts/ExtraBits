from abc import ABC, abstractmethod


class Database(ABC):
    bool_val = True

    def __init_subclass__(cls):
        super().__init_subclass__()

        # Ensure subclass overrides __init__
        if cls.__init__ is Database.__init__:
            raise TypeError(
                f"{cls.__name__} must override __init__ and set a default `_locations`."
            )

        # Wrap the subclass's __init__ to check AFTER construction
        orig_init = cls.__init__

        def wrapped_init(self, *args, **kwargs):
            orig_init(self, *args, **kwargs)
            if not hasattr(self, "_locations"):
                raise TypeError(
                    f"{cls.__name__}.__init__ must set a default `_locations`."
                )
        cls.__init__ = wrapped_init

    def __init__(self):
        self.steps = 1

    @property
    def server_locations(self):
        return self._locations

    @server_locations.setter
    def server_locations(self, locations):
        self._locations = locations

    def __str__(self) -> str:
        msg = ""
        for l in self.server_locations:
            msg += f"{l}\n"
        return msg


class DB1(Database):
    def __init__(self):
        super().__init__()
        self._locations = ["Boston"]


if __name__ == "__main__":
    DB = DB1()
    DB.server_locations = ['New York']
    print(DB)
    print(DB.steps)
    print(DB.bool_val)
