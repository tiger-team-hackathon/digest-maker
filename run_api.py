import pickle
import os

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from matcher import Matcher
from api.news import news_router


def load_roles():
    roles = dict()

    for file_name in os.listdir('roles'):
        role_name = file_name.split('.')[0]
        with open(file_name, 'rb') as handle:
            app.state.roles['role_name'] = pickle.load(handle)

    return


def create_app():
    app = FastAPI(title="News for people")

    origins = "*"
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.state.matcher = Matcher(init_roles(app))
    app.include_router(news_router)

    return app


if __name__ == '__main__':
    gl_app = create_app()
    uvicorn.run(gl_app, host="0.0.0.0", port=8000)
