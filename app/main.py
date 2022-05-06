from randomname import get_name

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

NUMBER_OF_RANDOM_WORDS=13
templates = Jinja2Templates(directory="app/templates")

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("2/second")
async def root(request: Request):
    random_words = get_random_words(NUMBER_OF_RANDOM_WORDS)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "random_words": random_words
    })

def get_random_words(n):
    words = [get_name().replace('-', ' ').title() for _ in range(0,n)]
    return words

