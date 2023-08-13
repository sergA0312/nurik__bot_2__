create_user_table = ("\n"
                     "        CREATE TABLE IF NOT EXISTS telegram_users\n"
                     "        (Id INTEGER PRIMARY KEY,\n"
                     "        Telegram_id INTEGER,\n"
                     "        Username CHAR(50),\n"
                     "        Firstname CHAR(50),\n"
                     "        Lastname CHAR(50),\n"
                     "        UNIQUE (Telegram_id))\n")
create_ban_table = ('\n'
                    '        CREATE TABLE IF NOT EXISTS users_ban\n'
                    '        (Id INTEGER PRIMARY KEY,\n'
                    '        Telegram_id INTEGER,\n'
                    '        BanCount INTEGER,\n'
                    '        FOREIGN KEY (Telegram_id) REFERENCES telegram_users(Telegram_id))\n')