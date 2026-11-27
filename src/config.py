import string

# 1. ВОЗМОЖНЫЕ ЗНАЧЕНИЯ ДЛЯ ГЕНЕРАЦИИ

DIGITS = string.digits
HEX_DIGITS = "0123456789abcdefABCDEF"
HEX_DIGITS_LOWER = "0123456789abcdef"
BOTH_CASES_LETTERS = string.ascii_letters
BOTH_CASE_LETTERS_DIGITS = BOTH_CASES_LETTERS + DIGITS
ONLY_UPPER = string.ascii_uppercase
ONLY_LOWER = string.ascii_lowercase

# 2. МЕНЮ

EXIT_OPTION = "Выход"
MAIN_MENU_OPTIONS = ("Сгенерировать .env", EXIT_OPTION)

# 3. ВОЗМОЖНЫЕ ДАННЫЕ ДЛЯ ГЕНЕРАЦИИ

# Словарь типа {"TOKEN": {"startswith": "TOKEN_", "available_symbols": "0123456789", "count": 10}}
# Где:
#    1) Ключ: название секрета в .env
#    2) startswith: с чего начинается
#    3) available_symbols: доступные символы
#    4) count: количество этих самых символов

DOTENV_KEYS = {
    "AWS_ACCESS_KEY_ID": {"startswith": "AKIA", "available_symbols": ONLY_UPPER + DIGITS, "count": 16},
    "AWS_SECRET_ACCESS_KEY": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "/+=", "count": 40},
    "AWS_SESSION_TOKEN": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "/+=", "count": 200},
    "AZURE_CLIENT_SECRET": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "~-_.", "count": 40},
    "DIGITALOCEAN_TOKEN": {"startswith": "dop_v1_", "available_symbols": HEX_DIGITS_LOWER, "count": 64},
    "CLOUDFLARE_API_TOKEN": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 40},
    "OPENAI_API_KEY": {"startswith": "sk-", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 51},
    "OPENAI_PROJECT_KEY": {"startswith": "sk-proj-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 130},
    "ANTHROPIC_API_KEY": {"startswith": "sk-ant-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "-", "count": 50},
    "HUGGINGFACE_TOKEN": {"startswith": "hf_", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 34},
    "GROQ_API_KEY": {"startswith": "gsk_", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 50},
    "OPENROUTER_API_KEY": {"startswith": "sk-or-v1-", "available_symbols": HEX_DIGITS_LOWER, "count": 70},
    "GITHUB_TOKEN": {"startswith": "ghp_", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 36},
    "GITHUB_FINE_GRAINED_TOKEN": {"startswith": "github_pat_", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_", "count": 82},
    "JWT_SECRET": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "!@#", "count": 32},
    "DJANGO_KEY": {"startswith": "django-insecure-", "available_symbols": ONLY_LOWER + DIGITS + "!@#$%^&*(-_=+)", "count": 50},
    "MAILGUN_API_KEY": {"startswith": "key-", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 32},
    "PAYPAL_CLIENT_SECRET": {"startswith": "E", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 80},
    "GOOGLE_CLIENT_SECRET": {"startswith": "GOCSPX-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "-", "count": 28},
    "SLACK_BOT_TOKEN": {"startswith": "xoxb-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "-", "count": 50},
    "FIREBASE_API_KEY": {"startswith": "AIza", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 35},
    "BINANCE_SECRET_KEY": {"startswith": "", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 64},
    "GITLAB_TOKEN": {"startswith": "glpat-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 20},
    "NPM_TOKEN": {"startswith": "npm_", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 36},
    "PYPI_API_TOKEN": {"startswith": "pypi-", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 150},
    "DOCKER_HUB_TOKEN": {"startswith": "dckr_pat_", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-", "count": 27},
    "NOTION_SECRET": {"startswith": "ntn_", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 46},
    "XAI_API_TOKEN": {"startswith": "xai-", "available_symbols": BOTH_CASE_LETTERS_DIGITS, "count": 80},
    "JIRA_API_TOKEN": {"startswith": "ATATT3xFfGF0", "available_symbols": BOTH_CASE_LETTERS_DIGITS + "_-=", "count": 180}
}

FAKE_COMMENTS = ("# DO NOT COMMIT THIS FILE TO VERSION CONTROL",
                 "# WARNING: NEVER COMMIT THIS FILE TO THE REPOSITORY!",
                 "# THIS FILE CONTAINS SENSITIVE CREDENTIALS. DO NOT COMMIT!",
                 "# ONLY FOR LOCAL DEVELOPMENT. ADD TO .GITIGNORE",
                 "# SECURITY NOTICE: KEEP THIS FILE OUT OF GIT",
                 "# ATTENTION: CONTAINS PRODUCTION SECRETS",
                 "# RESTRICTED: SECRET INFORMATION. COMMITTING IS PROHIBITED!",
                 "# CONFIDENTIAL: DO NOT COMMIT!",
                 "# SECRET INSIDE! MAKE SURE THIS IS IN .GITIGNORE",
                 "# STOP! DO NOT COMMIT THIS FILE. ONLY FOR LOCAL DEV. CONTAINS REAL SECRETS!",
                 "# ALERT: THIS FILE CONTAINS REAL, CONFIDENTIAL INFORMATION. DO NOT SHARE AND DO NOT COMMIT!",
                 "Свой вариант")

AVAILABLE_CASES = ("использовать нижний регистр",
                   "ИСПОЛЬЗОВАТЬ ВЕРХНИЙ РЕГИСТР",
                   "Использовать Регистр, Где Каждое Слово С Большой Буквы",
                   "Использовать регистр как в предложениях",
                   "Не менять регистр")
