# Archery Auth
Persons authorization information manager.

[Github](https://github.com/archeryhq/archery-auth)

## Environment

Before using the module, it is necessary to create the following environment variables:

* ARCHERY_PERSON_SECRET - This key must be 32 url-safe base64-encoded bytes.
* ARCHERY_PERSON_SQL_URI - PostgreSQL URL.

These variables can be stored within an .env file.

## How to use

There are two related tables:

* Roles - Authorization levels.

* Auth - Responsible from personal data.

Show the [notebook](https://github.com/archeryhq/archery-auth/Tests.ipynb)!*