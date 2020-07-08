from django.urls import resolve
from django.contrib import messages
import re


def is_singular_url(request):
    # https://stackoverflow.com/questions/2491605/how-to-get-the-current-url-name-using-django
    url_name = resolve(request.path_info).url_name
    return re.search("singular$", url_name)


def singular_url_logger(request, requesting):
    if is_singular_url(request):
        pass
        # TODO: Create a logger
        # log(f"{requesting} requested {requested} which is in singular format.")
        messages.warning(
            request,
            f"The requested url {request.build_absolute_uri()} contains an depreciated"
            " style using singular notation. Please make requests using plural notation"
            " such as group -> groups and option -> options. Beginning in the next major"
            " release singular notation will no longer be accepted."
        )
    return

# Api hits a singular url
# Requests normal view
# View calls singular_logger function
# singular_logger handles all things if it is singular
# Logged into a file or the database (or could make api call somewhere to log)
# Normal information returned to requester
