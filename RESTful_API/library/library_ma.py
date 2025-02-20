from .extension import ma

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'birth_date', 'gender', 'class_name')

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'page_count', 'author_id', 'category_id')

class BorrowSchema(ma.Schema):
    class Meta:
        fields = ('id', 'book_id', 'student_id', 'borrow_date', 'return_date')

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True, validate=validate.Length(min=1, max=100))
    password = fields.Str(required=True, load_only=True)
    is_active = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
    first_name = fields.Str(validate=validate.Length(min=0, max=100))
    last_name = fields.Str(validate=validate.Length(min=0, max=100))
    is_superuser = fields.Boolean()

    class Meta:
        ordered = True

class LoginAttemptSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    email = fields.Email(required=True, validate=validate.Length(min=1, max=100))
    password = fields.Str(required=True, load_only=True)
    created_at = fields.DateTime(dump_only=True)
    ip_address = fields.Str(validate=validate.Length(min=1, max=100))
    login_status = fields.Str(validate=validate.Length(min=1, max=100))

    class Meta:
        ordered = True


class SessionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    session_id = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    start_time = fields.DateTime(dump_only=True)
    session_status = fields.Str(dump_only=True)

    class Meta:
        ordered = True