from pydantic import BaseModel


class BaseAPIModel(BaseModel):
    @classmethod
    def meta(cls):
        return {
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": cls.schema()
                    }
                }
            }
        }
