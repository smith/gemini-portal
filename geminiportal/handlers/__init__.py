from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geminiportal.protocols.base import BaseResponse

from geminiportal.handlers.audio import AudioHandler
from geminiportal.handlers.base import BaseHandler
from geminiportal.handlers.file import FileHandler
from geminiportal.handlers.gemini import GeminiHandler
from geminiportal.handlers.gopher import GopherHandler
from geminiportal.handlers.gopherplus import GopherPlusHandler
from geminiportal.handlers.image import ImageHandler
from geminiportal.handlers.nex import NexHandler
from geminiportal.handlers.text import TextHandler


def get_handler_class(response: BaseResponse) -> type[BaseHandler]:
    handler_class: type[BaseHandler]

    if response.mimetype is None:
        handler_class = FileHandler
    elif response.mimetype.startswith("image/"):
        handler_class = ImageHandler
    elif response.mimetype.startswith("audio/"):
        handler_class = AudioHandler
    elif response.mimetype.startswith("text/plain"):
        if response.url.scheme == "text":
            handler_class = NexHandler
        else:
            handler_class = TextHandler
    elif response.mimetype.startswith("text/gemini"):
        handler_class = GeminiHandler
    elif response.mimetype.startswith("text/"):
        handler_class = TextHandler
    elif response.mimetype.startswith("application/nex"):
        handler_class = NexHandler
    elif response.mimetype.startswith(("application/gopher-menu", "application/gopher+-menu")):
        handler_class = GopherHandler
    elif response.mimetype.startswith("application/gopher+-attributes"):
        handler_class = GopherPlusHandler
    else:
        handler_class = FileHandler

    return handler_class
