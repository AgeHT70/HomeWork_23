Для запуска приложения запустите файл run.py

ПРИМЕР ЗАПРОСА:

    {
        "file_name": "apache_logs.txt",
        "queries": 
            [
               {
                    "cmd": "regex",
                    "value": "images/\\S+\\.png"
                }
            ]
    }

    {
        "file_name": "apache_logs.txt",
        "queries": 
            [
                {
                    "cmd": "filter",
                    "value": "POST"
                },
                {
                    "cmd": "limit",
                    "value": "6"
                },
                {
                    "cmd": "map",
                    "value": "0"
                },
                {
                    "cmd": "unique",
                    "value": ""
                },
                {
                    "cmd": "sort",
                    "value": "desc"
                }
            ]
    }