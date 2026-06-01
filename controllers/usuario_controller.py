from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services.usuario_service import UsuarioService
from typing import List
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioAtualizarDadosSensiveis


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService.criar_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioResponse])
def listar_todos(db: Session = Depends(get_db)):
    return UsuarioService.buscar_todos(db)

@router.get("/{id}", response_model=UsuarioResponse)
def buscar_por_id(id: int, db: Session = Depends(get_db)):
    return UsuarioService.buscar_por_id(db, id)

@router.put("/{id}", response_model=UsuarioResponse)
def atualizar(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService.atualizar_usuario(db, id, usuario)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deletar(id: int, db: Session = Depends(get_db)):
    return UsuarioService.deletar_usuario(db, id)

@router.patch("/{id}/credenciais", status_code=status.HTTP_200_OK)
def atualizar_credenciais(id: int, dados: UsuarioAtualizarDadosSensiveis, db: Session = Depends(get_db)):
    return UsuarioService.atualizar_credenciais(db, id, dados)


