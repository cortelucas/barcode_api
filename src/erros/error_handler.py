from src.views.http_types import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntity):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server Error", "detail": str(error)}]},
    )