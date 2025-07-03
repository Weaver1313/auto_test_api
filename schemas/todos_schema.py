from voluptuous import Schema, Required, ALLOW_EXTRA, Optional


schema_response_body = Schema({
    Required("todos"): [{
        Optional("id"): int,
        Optional("title"): str,
        Optional("doneStatus"): bool,
        Optional("description"): str
    }]
})