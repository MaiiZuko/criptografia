# 🔐 Gerenciador de Criptografia de Arquivos

Um projeto em Python para criptografar e descriptografar arquivos usando AES-256-GCM. Tem duas versões: uma com interface visual (GUI) e outra por linha de comando (CLI), ambas compatíveis entre si.

## 🔒 Tecnologia

- **Algoritmo**: AES-256-GCM
- **Derivação de chave**: PBKDF2-HMAC-SHA256 (200k iterações)
- **Salt + Nonce**: 28 bytes aleatórios

## 📦 Requisitos

- Python 3.7+
- Biblioteca `cryptography`

## 🚀 Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:

```bash
pip install cryptography
```

## 💻 Como Usar

### Interface Gráfica (GUI)

Execute o script `criptografia_arquivos_painel.py`:

```bash
python criptografia_arquivos_painel.py
```

**Funcionalidades:**
- Selecione um arquivo clicando no botão "Selecionar Arquivo"
- Digite a senha desejada
- Clique em "Criptografar" para criptografar o arquivo (salvo como `.enc`)
- Clique em "Descriptografar" para descriptografar um arquivo `.enc`

### Interface de Linha de Comando (CLI)

Execute o script `criptografia_arquivos_terminal.py`:

```bash
python criptografia_arquivos_terminal.py
```

**Menu interativo:**
```
=== Sistema de Criptografia de Arquivos ===
1 - Criptografar arquivo
2 - Descriptografar arquivo
0 - Sair
```

## 📁 Estrutura dos Arquivos Criptografados

Os arquivos criptografados (`.enc`) possuem a seguinte estrutura binária:

```
┌─────────────────┬──────────────────┬────────────────────┐
│   SALT (16B)    │   NONCE (12B)    │  DADOS CIFRADOS    │
│                 │                  │  (tamanho variável)│
└─────────────────┴──────────────────┴────────────────────┘
```

- **SALT**: Usado para derivar a chave da senha
- **NONCE**: Vetor de inicialização para o modo GCM
- **DADOS CIFRADOS**: Arquivo original criptografado com autenticação

## 📝 Exemplos de Uso

### GUI
1. Inicie a aplicação
2. Clique em "Selecionar Arquivo" e escolha um arquivo
3. Digite uma senha forte
4. Clique em "Criptografar"
5. Um arquivo com extensão `.enc` será criado

Para descriptografar:
1. Selecione o arquivo `.enc`
2. Digite a mesma senha usada para criptografar
3. Clique em "Descriptografar"
4. Um arquivo com extensão `.restaurado` será criado

### CLI
```bash
$ python criptografia_arquivos_terminal.py

=== Sistema de Criptografia de Arquivos ===
1 - Criptografar arquivo
2 - Descriptografar arquivo
0 - Sair
Escolha uma opção: 1
Informe o caminho do arquivo a ser criptografado: documento.pdf
Digite a chave/senha: ****
Arquivo criptografado com sucesso: documento.pdf.enc
```

## ⚠️ Observações

- Se esquecer a senha, não há jeito de recuperar os dados
- Os dois programas são compatíveis entre si (`.enc` gerado por um funciona no outro)



## 📄 Arquivos do Projeto

```
criptografia/
├── criptografia_arquivos_painel.py      # Interface Gráfica (Tkinter)
├── criptografia_arquivos_terminal.py    # Interface CLI
├── teste.txt                             # Arquivo de teste
└── README.md                             # Este arquivo
```

## 🎨 Interface Gráfica

Tema escuro com cores verde neon (bem cyberpunk mesmo 😄)


