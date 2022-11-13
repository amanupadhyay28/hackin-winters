from decouple import config


TORTOISE_CONF = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": config("DB_HOST"),
                "port": "5432",
                "user": "postgres",
                "password": config("DB_PASSWORD"),
                "database": "hackin_winters",
                "max_cached_statement_lifetime": 0,
                "max_cacheable_statement_size": 0,
            },
        }
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "timezone": "Asia/Kolkata",
}
