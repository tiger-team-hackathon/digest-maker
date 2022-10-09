from fastapi import Depends, APIRouter, Request


news_router = r = APIRouter()


@r.get("/get_news_for_role/", status_code=200, response_model=dict)
def get_news_for_role(request: Request, role: str, page: int) -> dict:
    if role == 'accountant':
        digest = request.app.state.matcher.get_digest_for_role(role, page)

        res = {'news': digest}

        return res
    else:
        return {'error': 'No such role'}


@r.get("/get_trend/", status_code=200, response_model=dict)
def get_trend(request: Request, role: str) -> dict:
    res = {'trend': '',
           'insight': ''}

    return res
