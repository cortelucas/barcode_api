from src.views.http_types import HttpRequest, HttpResponse


class TagCreatorView:
    """
    responsability for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body["product_code"]

        # lógica de regra de negócio
        print("Estou na view")
        print(http_request)

        return HttpResponse(200, {"message": "Tag created"})
