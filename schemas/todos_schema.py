from voluptuous import Schema, Required, ALLOW_EXTRA, Optional


schema_response_body = Schema({
    Required("todos"): [{
        Optional("id"): int,
        Optional("title"): str,
        Optional("doneStatus"): bool,
        Optional("description"): str
    }]
})

schema_create_todos = Schema({
    Required('id'): int,
    Required('title'): str,
    Required('doneStatus'): bool,
    Required('description'): str
})