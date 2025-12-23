from api import ma
from ..models import curso_model
from marshmallow import fields

class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso
        load_instance = True
        fields = ("id", "nome", "descricao", "data_publicacao", "_links")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_publicacao = fields.Date(required=True)


    _links = ma.Hyperlinks(
        {
            "get":ma.URLFor("cursodetail", values={"id": "<id>"}),
            "put":ma.URLFor("cursodetail", values={"id": "<id>"}),
            "delete":ma.URLFor("cursodetail", values={"id": "<id>"}),
        }
    )