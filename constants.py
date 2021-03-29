CLI_NAME = "passme"
CLI_DESCRIPTION = "passme - A terminal local encrypted password manager cli tool"
INIT_CLI_DESCRIPTION = "Initializes passme with master password"
ADD_CLI_DESCRIPTION = "Add to existing password vault"
GET_CLI_DESCRIPTION = "Get password for given key from password vault"
KEY_CLI_DESCRIPTION = "Key/Identifier for the the corresponding password. Ex: myEmail"
PASSWORD_CLI_DESCRIPTION = "Password to be stored in password vault"
MASTER_PASSWORD_PROMPT = "Please enter Master Password:"
KEY_LENGTH_IN_BYTES = 32
HASH_SALT = "H9LfdQKRHk+eo3Dy0FatfSW/8oqUWhJ8TGvURHgZZBg="
HASH_ITERATIONS = 1000000
BASE_FILE_PATH = '/var/lib/passme/'
INTI_ALREADY_DONE_ERROR = "Passme is initialized already. Use -f to force.\nWarning: Password stored in previous vault will be erased"
FORCE_CLI_DESCRIPTION = "Force initialize passme"
INCORRECT_MASTER_PASSWORD = "Master password entered is incorrect"
KEY_NOT_EXISTS = "Key not exists in vault"