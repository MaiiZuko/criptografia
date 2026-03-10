import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32
PBKDF2_ITERATIONS = 200000

arquivo_selecionado = None


def derivar_chave(senha, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    return kdf.derive(senha.encode())


def selecionar_arquivo():
    global arquivo_selecionado
    arquivo_selecionado = filedialog.askopenfilename()
    if arquivo_selecionado:
        label_arquivo.config(text=f"Arquivo: {arquivo_selecionado}")


def criptografar():
    global arquivo_selecionado

    if not arquivo_selecionado:
        messagebox.showerror("Erro", "Selecione um arquivo primeiro.")
        return

    senha = entrada_senha.get()

    if not senha:
        messagebox.showerror("Erro", "Digite uma senha.")
        return

    try:
        with open(arquivo_selecionado, "rb") as f:
            dados = f.read()

        salt = os.urandom(SALT_SIZE)
        nonce = os.urandom(NONCE_SIZE)

        chave = derivar_chave(senha, salt)

        aesgcm = AESGCM(chave)
        cifrado = aesgcm.encrypt(nonce, dados, None)

        saida = arquivo_selecionado + ".enc"

        with open(saida, "wb") as f:
            f.write(salt + nonce + cifrado)

        messagebox.showinfo("Sucesso", f"Arquivo criptografado:\n{saida}")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


def descriptografar():
    global arquivo_selecionado

    if not arquivo_selecionado:
        messagebox.showerror("Erro", "Selecione um arquivo primeiro.")
        return

    senha = entrada_senha.get()

    if not senha:
        messagebox.showerror("Erro", "Digite a senha.")
        return

    try:
        with open(arquivo_selecionado, "rb") as f:
            conteudo = f.read()

        salt = conteudo[:SALT_SIZE]
        nonce = conteudo[SALT_SIZE:SALT_SIZE+NONCE_SIZE]
        dados = conteudo[SALT_SIZE+NONCE_SIZE:]

        chave = derivar_chave(senha, salt)

        aesgcm = AESGCM(chave)
        original = aesgcm.decrypt(nonce, dados, None)

        saida = arquivo_selecionado.replace(".enc", "") + ".restaurado"

        with open(saida, "wb") as f:
            f.write(original)

        messagebox.showinfo("Sucesso", f"Arquivo restaurado:\n{saida}")

    except Exception:
        messagebox.showerror("Erro", "Senha incorreta ou arquivo inválido.")


# Interface gráfica

janela = tk.Tk()
janela.title("Gerenciador de Criptografia")
janela.geometry("600x350")
janela.configure(bg="#0a0a0a")

titulo = tk.Label(
    janela,
    text="Gerenciador de Criptografia de Arquivos",
    fg="#00ff9f",
    bg="#0a0a0a",
    font=("Consolas", 18, "bold")
)
titulo.pack(pady=20)

botao_arquivo = tk.Button(
    janela,
    text="Selecionar Arquivo",
    command=selecionar_arquivo,
    bg="#111",
    fg="#00ff9f",
    font=("Consolas", 12),
    width=20
)
botao_arquivo.pack(pady=10)

label_arquivo = tk.Label(
    janela,
    text="Nenhum arquivo selecionado",
    fg="#00ffaa",
    bg="#0a0a0a",
    font=("Consolas", 10)
)
label_arquivo.pack(pady=5)

label_senha = tk.Label(
    janela,
    text="Insira a senha:",
    fg="#00ff9f",
    bg="#0a0a0a",
    font=("Consolas", 12, "bold")
)
label_senha.pack(pady=(15, 5))

entrada_senha = tk.Entry(
    janela,
    show="*",
    width=30,
    font=("Consolas", 12),
    bg="#111",
    fg="#00ff9f",
    insertbackground="#00ff9f"
)
entrada_senha.pack(pady=10)

entrada_senha.insert(0, "")

botao_cript = tk.Button(
    janela,
    text="Criptografar",
    command=criptografar,
    bg="#002b36",
    fg="#00ff9f",
    font=("Consolas", 12),
    width=20
)
botao_cript.pack(pady=8)

botao_decript = tk.Button(
    janela,
    text="Descriptografar",
    command=descriptografar,
    bg="#002b36",
    fg="#00ff9f",
    font=("Consolas", 12),
    width=20
)
botao_decript.pack(pady=8)

janela.mainloop()