# Last.fm-Scrobble-Bot
Um bot simples para enviar "scrobbles"  para a sua conta do Last.fm.


# Last.fm Scrobble Bot

Um bot simples, porém poderoso, para enviar "scrobbles" (registros de músicas ouvidas) para a sua conta do Last.fm. Ideal para registrar aquelas músicas que você ouviu fora de um serviço compatível ou simplesmente para gerenciar seu histórico.

## Funcionalidades Principais

* **Scrobbling Múltiplo**: Envie vários scrobbles de uma única música de uma vez.
* **Gestão de Sessão**: O bot salva sua chave de sessão (`session_key`) em um arquivo `session.txt` após a primeira autorização, agilizando logins futuros.
* **Timestamp Inteligente**: Calcula e escalona o timestamp de cada scrobble para simular que as músicas foram ouvidas em um período de tempo lógico, evitando erros na API do Last.fm.
* **Interativo**: Interface de linha de comando simples e direta para inserir o artista, a música e a quantidade de scrobbles.

## Pré-requisitos

Antes de começar, você precisará de:

1.  **Python 3**: Certifique-se de que o Python esteja instalado em seu sistema.
2.  **Conta no Last.fm**: Você precisa de uma conta de usuário no site [Last.fm](https://www.last.fm).
3.  **API Key e Shared Secret do Last.fm**: Essencial para que o script possa se comunicar com a API do Last.fm.

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <URL-DO-SEU-REPOSITORIO>
    cd <NOME-DO-SEU-REPOSITORIO>
    ```

2.  **Instale as dependências:**
    O projeto utiliza a biblioteca `pylast`. Você pode instalá-la facilmente usando o `pip` e o arquivo `requirements.txt` fornecido.
    ```bash
    pip install -r requirements.txt
    ```

## Configuração: Obtendo sua API do Last.fm

Para que o bot funcione, você precisa autorizá-lo a acessar sua conta do Last.fm. Isso é feito através de uma API Key e um Shared Secret.

1.  **Acesse a página de criação de API do Last.fm**: [https://www.last.fm/api/account/create](https://www.last.fm/api/account/create).
2.  **Preencha o formulário**: Você só precisa preencher o nome da aplicação (pode ser "Bot Scrobblador", por exemplo). Os outros campos não são obrigatórios.
3.  **Pegue suas chaves**: Após enviar o formulário, você será redirecionado para uma página com sua **API Key** e seu **Shared Secret**. Guarde esses dois valores.

## Como Usar

Com tudo instalado e configurado, execute o script principal:

```bash
python bot.py

    Acompanhe o envio em tempo real no terminal.

Para encerrar o programa, basta digitar sair quando ele pedir o nome do artista.
