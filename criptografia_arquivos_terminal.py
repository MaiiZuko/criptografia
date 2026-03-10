import os
import sys
import getpass
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32  # 256 bits
PBKDF2_ITERATIONS = 200_000


def derivar_chave(senha: str, salt: bytes) -> bytes:
    """
    Deriva uma chave AES de 256 bits a partir da senha informada pelo usuário.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    return kdf.derive(senha.encode("utf-8"))


def criptografar_arquivo(caminho_entrada: str, senha: str) -> str:
    """
    Criptografa um arquivo com AES-GCM e salva com extensão .enc
    Estrutura do arquivo salvo: [salt][nonce][dados_cifrados]
    """
    caminho = Path(caminho_entrada)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    dados = caminho.read_bytes()

    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)
    chave = derivar_chave(senha, salt)

    aesgcm = AESGCM(chave)
    dados_cifrados = aesgcm.encrypt(nonce, dados, None)

    caminho_saida = caminho.with_suffix(caminho.suffix + ".enc")
    caminho_saida.write_bytes(salt + nonce + dados_cifrados)

    return str(caminho_saida)


def descriptografar_arquivo(caminho_entrada: str, senha: str) -> str:
    """
    Descriptografa um arquivo .enc gerado pelo programa.
    """
    caminho = Path(caminho_entrada)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    conteudo = caminho.read_bytes()

    if len(conteudo) < SALT_SIZE + NONCE_SIZE:
        raise ValueError("Arquivo criptografado inválido ou corrompido.")

    salt = conteudo[:SALT_SIZE]
    nonce = conteudo[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    dados_cifrados = conteudo[SALT_SIZE + NONCE_SIZE:]

    chave = derivar_chave(senha, salt)
    aesgcm = AESGCM(chave)

    try:
        dados_originais = aesgcm.decrypt(nonce, dados_cifrados, None)
    except Exception:
        raise ValueError("Senha incorreta ou arquivo alterado/corrompido.")

    if caminho.suffix != ".enc":
        raise ValueError("O arquivo informado deve possuir extensão .enc")

    caminho_saida = caminho.with_suffix("")
    caminho_restaurado = Path(str(caminho_saida) + ".restaurado")
    caminho_restaurado.write_bytes(dados_originais)

    return str(caminho_restaurado)


def menu():
    print("\n=== Sistema de Criptografia de Arquivos ===")
    print("1 - Criptografar arquivo")
    print("2 - Descriptografar arquivo")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            caminho = input("Informe o caminho do arquivo a ser criptografado: ").strip()
            senha = getpass.getpass("Digite a chave/senha: ")

            try:
                saida = criptografar_arquivo(caminho, senha)
                print(f"Arquivo criptografado com sucesso: {saida}")
            except Exception as e:
                print(f"Erro ao criptografar: {e}")

        elif opcao == "2":
            caminho = input("Informe o caminho do arquivo .enc: ").strip()
            senha = getpass.getpass("Digite a chave/senha: ")

            try:
                saida = descriptografar_arquivo(caminho, senha)
                print(f"Arquivo descriptografado com sucesso: {saida}")
            except Exception as e:
                print(f"Erro ao descriptografar: {e}")

        elif opcao == "0":
            print("Encerrando...")
            sys.exit(0)

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()