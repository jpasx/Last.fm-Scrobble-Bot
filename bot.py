import pylast
import os
import time
from datetime import datetime, timedelta

SESSION_FILE = "session.txt"


def get_lastfm_network():
    print("Bot Scrobblador — Last.fm (Session Key Edition)\n")

    API_KEY = input("API Key do Last.fm: ").strip()
    API_SECRET = input("Secret Key: ").strip()

    session_key = None

    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            session_key = f.read().strip()
        print("Sessão encontrada! Usando session_key salva.\n")
        return pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, session_key=session_key)

    print("Nenhuma sessão encontrada.")
    print("Acesse o link abaixo para autorizar o app:")

    network_temp = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
    sg = pylast.SessionKeyGenerator(network_temp)
    url = sg.get_web_auth_url()

    print(f"\n{url}\n")
    input("Pressione ENTER depois de autorizar o app no navegador...")

    try:
        session_key = sg.get_web_auth_session_key(url)
        with open(SESSION_FILE, "w") as f:
            f.write(session_key)
        print("\nSessão criada e salva com sucesso!\n")
    except Exception as e:
        print("Erro ao gerar session key:", e)
        exit(1)

    return pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, session_key=session_key)


def main():
    network = get_lastfm_network()
    user = network.get_authenticated_user()
    print(f"Conectado como {user.get_name()}\n")

    while True:
        artist = input("Artista (ou 'sair' para encerrar): ").strip()
        if artist.lower() == "sair":
            print("\nEncerrado.")
            break

        title = input("Música: ").strip()
        try:
            num_scrobbles = int(input("Quantos scrobbles deseja enviar? ").strip())
        except ValueError:
            num_scrobbles = 1

        print(f"\nEnviando {num_scrobbles} scrobble(s) de '{title}'...\n")

        for i in range(num_scrobbles):
            timestamp = int((datetime.now() - timedelta(minutes=(num_scrobbles - i) * 4)).timestamp())
            try:
                network.scrobble(artist=artist, title=title, timestamp=timestamp)
                print(f"({i+1}/{num_scrobbles}) {artist} - {title}")
                time.sleep(1)
            except Exception as e:
                print(f"Erro no scrobble {i+1}: {e}")
                break

        print("\nTodos os scrobbles enviados!\n")


if __name__ == "__main__":
    main()
