from voluptuous import Schema, Required, ALLOW_EXTRA, Optional

scheme_response_body = Schema({
    Required('challenges'): [{
        Optional('id'): int,
        Optional('name'): str,
        Optional('description'): str,
        Optional('status'): bool,
    }]
})