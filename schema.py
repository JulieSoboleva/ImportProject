from marshmallow import Schema, fields


class InputSchema(Schema):
    number_a = fields.Int(description='Первое число', required=True, example=5)
    number_b = fields.Int(description='Второе число', required=True, example=2)
