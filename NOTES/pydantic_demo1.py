from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float


external_data = {"count": 11, "size": 5.5}
foo = Foo(**external_data)

print(foo)

breakpoint()