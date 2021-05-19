import hashlib
import getpass

# Criando uma lista vazia chamada “usuários”

usuarios = []


# Criando um usuário como dicionário com name, username e password

usuario = {

    "name": "Clark Kent",

    "username": "kent",

    "password": "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"

}
# Inclui este usuário na lista usuários

usuarios.append(usuario)


# Criando um usuário como dicionário com name, username e password
usuario = {

    "name": "Bruce Wayne",

    "username": "wayne",

    "password": "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"

}

# Inclui este usuário na lista usuários

usuarios.append(usuario)


# Criando um usuário como dicionário com name, username e password
usuario = {

    "name": "Christopher Walker",

    "username": "walker",

    "password": "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"

}

# Inclui este usuário na lista usuários

usuarios.append(usuario)


print("Digite seu usuário:")
usuario = input()
senha = hashlib.sha256(getpass.getpass('Digite sua senha":') .encode('utf-8')).hexdigest()
logou = 0

for user in usuarios:
    if user["username"] == usuario:
        if user["password"] == senha:
            print(f"{user['name']} Logado!")
            logou = 1

if not bool(logou):
    print("Usuário/senha inválidos.")