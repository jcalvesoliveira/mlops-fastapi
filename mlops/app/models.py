from pydantic import BaseModel

class House(BaseModel):
    square_meters: float
    year_built: int
    garage_cars: int

    def to_list(self) -> list:
        return [self.square_meters, self.year_built, self.garage_cars]