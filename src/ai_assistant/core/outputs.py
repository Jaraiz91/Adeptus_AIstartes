from pydantic import BaseModel, Field
from typing import Literal


class router_atrtibutes(BaseModel):
    tipo_pregunta : Literal['General', 'Especifica', 'Otro'] = Field(description="Indica si la pregunta es de caracter general si pregunta un resumen sobre las reglas de warhammer 40k o específica si es una pregunta concreta. En caso de ser otra cosa nada relacionada con las reglas identificalo como 'otro'")
    workflow: Literal['audio', 'texto'] = Field(description="Indica si debe responder en texto o en audio")
    pregunta: str = Field(description="pregunta del usuario")