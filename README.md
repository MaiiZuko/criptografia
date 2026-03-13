# 🔐 Gerenciador de Criptografia de Arquivos

Um projeto em Python para criptografar e descriptografar arquivos com segurança usando o padrão AES-256-GCM.

## 📋 Sobre

Este projeto oferece duas formas de usar o sistema de criptografia:
- **Interface Gráfica (GUI)** com Tkinter
- **Interface de Linha de Comando (CLI)**

Ambas as versões utilizam os mesmos algoritmos e padrões de segurança para garantir compatibilidade entre elas.

## 🔒 Segurança

- **Algoritmo**: AES-256-GCM (Advanced Encryption Standard com Galois/Counter Mode)
- **Derivação de chave**: PBKDF2-HMAC-SHA256 com 200.000 iterações
- **Salt**: 16 bytes aleatórios
- **Nonce**: 12 bytes aleatórios
- **Tamanho da chave**: 256 bits (32 bytes)

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

## ⚠️ Observações Importantes

- **Senhas fortes**: Use senhas longas e complexas para melhor segurança
- **Backup**: Sempre faça backup dos arquivos originais antes de criptografar
- **Recuperação de senha**: Se esquecer a senha, não há forma de recuperar os dados
- **Integridade**: O modo GCM garante que os dados não foram alterados
- **Compatibilidade**: Arquivos criptografados com uma versão podem ser descriptografados com a outra (GUI ↔ CLI)

## 🛠️ Detalhes Técnicos

### Função `derivar_chave()`
Deriva uma chave AES de 256 bits usando:
- Algoritmo: PBKDF2 com HMAC-SHA256
- Iterações: 200.000
- Salt: 16 bytes aleatórios

### Função `criptografar_arquivo()`
1. Lê o arquivo em bytes
2. Gera salt e nonce aleatórios
3. Deriva a chave da senha
4. Criptografa os dados com AES-256-GCM
5. Salva: `salt + nonce + dados_cifrados` em arquivo `.enc`

### Função `descriptografar_arquivo()`
1. Lê o arquivo `.enc`
2. Extrai salt, nonce e dados cifrados
3. Deriva a chave usando a senha informada
4. Descriptografa e valida autenticação
5. Salva em arquivo `.restaurado`

## 📄 Arquivos do Projeto

```
criptografia/
├── criptografia_arquivos_painel.py      # Interface Gráfica (Tkinter)
├── criptografia_arquivos_terminal.py    # Interface CLI
├── teste.txt                             # Arquivo de teste
└── README.md                             # Este arquivo
```

## 🎨 Interface Gráfica

A interface GUI apresenta um design moderno com tema escuro:
- Cor de fundo: #0a0a0a (preto profundo)
- Cor do texto/botões: #00ff9f (verde neon)
- Font: Consolas
- Layout intuitivo e responsivo

## 🐛 Tratamento de Erros

O programa lida com diversos cenários de erro:
- Arquivo não encontrado
- Arquivo criptografado corrompido
- Senha incorreta
- Arquivo inválido

## 📄 Licença

Este projeto é fornecido como está, sem garantias.

---

**Desenvolvido com segurança em mente** 🔐
