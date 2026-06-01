from fastapi import FastAPI
from config.database import engine, Base
from controllers import usuario_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Cadastro de Usuários",
    description="API dividida em camadas utilizando FastAPI e MySQL",
    version="1.0"
)

app.include_router(usuario_controller.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )