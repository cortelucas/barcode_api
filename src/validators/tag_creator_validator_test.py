from .tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    request = MockRequest(json={"product_code": "123"})

    tag_creator_validator(request)

    assert True
