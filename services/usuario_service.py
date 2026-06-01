import email

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.usuario_model import UsuarioModel
from repositories.usuario_repo import UsuarioRepository
from schemas.usuario_schema import UsuarioCreate
from schemas.usuario_schema import UsuarioAtualizarDadosSensiveis

class UsuarioService:

    @staticmethod
    def criar_usuario(db: Session, usuario_data: UsuarioCreate):
        email_existente = UsuarioRepository.buscar_por_email(db, usuario_data.email)
        if email_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail= "E-mail já cadastrado"
            )

        novo_usuario = UsuarioModel(
            nome = usuario_data.nome,
            email = usuario_data.email,
            senha = usuario_data.senha
        )
        return UsuarioRepository.salvar(db, novo_usuario)

    @staticmethod
    def buscar_por_id(db: Session, usuario_id: int):
        usuario = UsuarioRepository.buscar_por_id(db, usuario_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario

    @staticmethod
    def buscar_todos(db: Session):
        return UsuarioRepository.buscar_todos(db)

    @staticmethod
    def atualizar_usuario(db: Session, usuario_id: int, usuario_data: UsuarioCreate):
        usuario = UsuarioService.buscar_por_id(db, usuario_id)

        if usuario.email != usuario_data.email:
            email_existente = UsuarioRepository.buscar_por_email(db, usuario_data.email)
            if email_existente:
                raise HTTPException(status_code=400, detail="Este e-mail já está em uso")

        usuario.nome = usuario_data.nome
        usuario.email = usuario_data.email
        usuario.senha = usuario_data.senha

        return UsuarioRepository.salvar(db, usuario)

    @staticmethod
    def deletar_usuario(db: Session, usuario_id: int):
        usuario = UsuarioService.buscar_por_id(db, usuario_id)
        UsuarioRepository.deletar(db, usuario)
        return {"detail": "Usuário deletado com sucesso"}

    @staticmethod
    def atualizar_credenciais(db: Session, usuario_id: int, dados: UsuarioAtualizarDadosSensiveis):
        usuario = UsuarioService.buscar_por_id(db, usuario_id)
        dados_atualizar = dados.model_dump(exclude_unset=True)

        if not dados_atualizar:
            raise HTTPException(
                status_code=400,
                detail="Nenhum dado informado para atualização.")

        if "email" in dados_atualizar and dados_atualizar["email"] != usuario.email:
            email_existente = UsuarioRepository.buscar_por_email(db, dados_atualizar["email"])
            if email_existente:
                raise HTTPException(
                    status_code=400,
                    detail="Este e-mail já está em uso."
                )

            for chave, valor in dados_atualizar.items():
                setattr(usuario, chave, valor)

            UsuarioRepository.salvar(db, usuario)

        return {"detail": "Credenciais atualizadas com sucesso."}
