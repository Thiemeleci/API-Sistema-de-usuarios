from sqlalchemy.orm import Session
from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioCreate

class UsuarioRepository:

    @staticmethod
    def buscar_por_id(db: Session, usuario_id: int) -> UsuarioModel:
        return db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    @staticmethod
    def buscar_por_email(db: Session, email:str) -> UsuarioModel:
        return db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    @staticmethod
    def buscar_todos(db: Session, skip: int = 0, limit: int = 100):
        return db.query(UsuarioModel).offset(skip).limit(limit).all()

    @staticmethod
    def salvar(db: Session, usuario: UsuarioModel) -> UsuarioModel:
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario

    @staticmethod
    def deletar(db: Session, usuario: UsuarioModel):
        db.delete(usuario)
        db.commit()