from pydantic import BaseModel


class BaseAPIModel(BaseModel):
    @classmethod
    def meta(cls):
        return {
            "description": cls.description(),
            "requestBody": {
                "description": cls.request_body_description(),
                "required": True,
                "content": {
                    "application/json": {
                        "schema": cls.schema(),
                        "examples": {
                            "Schema": {}
                        },
                    }
                }
            }
        }

    @classmethod
    def description(cls):
        return '### Description\n' + getattr(cls.Config, 'description', '')

    @classmethod
    def request_body_description(cls):
        table_body_format = "|{key}|{description}|{type}|{required}|\n"
        properties = cls.schema().get('properties')
        required_fields = cls.schema().get('required')

        table_header = "\n" \
                       "\n| Key               | Description                                                   | Type      | Required|" \
                       "\n|-------------------|---------------------------------------------------------------|-----------|-------|\n"
        table_body = ""

        for filed, value in properties.items():
            description = value.get('description', '')
            required = 'True' if filed in required_fields else ''

            table_body += table_body_format.format(key=filed, description=description, type=value.get('type'),
                                                   required=required)

        table_description = table_header + table_body
        return table_description
