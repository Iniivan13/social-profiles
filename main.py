import os
import webbrowser
import requests
from bs4 import BeautifulSoup

SOCIAL_MEDIA_DOMAINS = [
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "youtube.com",
    "pinterest.com",
    "tiktok.com",
    "snapchat.com",
    "github.com",
    "tumblr.com",
    "flickr.com",
    "vimeo.com",
    "reddit.com",
    "medium.com",
    "dribbble.com",
    "behance.net",
    "soundcloud.com",
    "spotify.com",
    "quora.com",
    "stackoverflow.com",
    "dev.to",
    "goodreads.com",
    "twitch.tv",
    "bitchute.com",
    "dailymotion.com",
    "weibo.com",
    "vk.com",
    "myspace.com",
    "gaiaonline.com",
    "plurk.com",
    "gab.com",
    "mastodon.social",
    "mix.com",
    "imgur.com",
]

SEARCH_ENGINE_URLS = [
    "https://www.google.com/search?q=",
    "https://www.bing.com/search?q=",
    "https://search.yahoo.com/search?p=",
    "https://duckduckgo.com/?q=",
    "https://www.ask.com/web?q=",
    "https://search.aol.com/aol/search?q=",
    "https://www.baido.com/s?q=",
    "https://www.yandex.com/search/?text=",
    "https://searx.be/search?q=",
    "https://startpage.com/do/search?q=",
    "https://swisscows.com/web?query=",
    "https://meta.search.io/search?q=",
    "https://www.ecosia.org/search?q=",
    "https://www.qwant.com/?q=",
    "https://www.wolframalpha.com/input/?i=",
    "https://www.blekko.com/ws/?q=",
    "https://www.mojeek.com/search?q=",
    "https://www.exalead.com/search?q=",
    "https://www.gibiru.com/results.html?q=",
    "https://www.infinitysearch.co/search?q=",
]

HEADERS = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:89.0) Gecko/20100101 Firefox/89.0"},
    {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"},
    {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},
    {"User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0"},
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0; rv:89.0) Gecko/20100101 Firefox/89.0"},
    {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"},
    {"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"},
    {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"},
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("\033[36m")
    print("===================================================")
    print("                       Iniivan13       ")
    print("                 Social Profiles Tool   ")
    print("===================================================")
    print("\033[0m")

def menu():
    print("\033[33m")
    print("1. Cari Profil Sosial Media")
    print("2. Keluar")
    print("\033[0m")

def open_instagram():
    print("\033[32m[*] Membuka halaman Instagram pembuat...\033[0m")
    webbrowser.open("https://www.instagram.com/lampungcysec/")

def search_similar_profiles(username):
    search_query = f"{username} " + " OR ".join([f"site:{domain}" for domain in SOCIAL_MEDIA_DOMAINS])

    for search_engine_url in SEARCH_ENGINE_URLS:
        try:
            headers = HEADERS[SEARCH_ENGINE_URLS.index(search_engine_url) % len(HEADERS)]
            search_url = f"{search_engine_url}{requests.utils.quote(search_query)}"
            response = requests.get(search_url, headers=headers)
            if response.status_code == 200:
                return response.text
        except requests.RequestException as error:
            print(f"\033[31m[!] Terjadi kesalahan saat permintaan ke {search_engine_url}: {error}\033[0m")
    return ""

def parse_search_results(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    profiles = set()

    for link in soup.find_all("a", href=True):
        url = link["href"]

        # Filter khusus untuk Facebook
        if "facebook.com" in url:
            if url.startswith("https://www.facebook.com/"):
                profiles.add(url)
        # Filter untuk platform lainnya
        elif any(domain in url for domain in SOCIAL_MEDIA_DOMAINS) and url.startswith("http"):
            profiles.add(url)

    return list(profiles)

def save_profiles_to_file(profiles, username):
    if not os.path.exists("results"):
        os.makedirs("results")
    file_path = os.path.join("results", f"{username}_profiles.txt")

    with open(file_path, "w") as file:
        for profile_url in profiles:
            platform = next((domain.split(".")[0].upper() for domain in SOCIAL_MEDIA_DOMAINS if domain in profile_url), "Unknown")
            file.write(f"Platform: {platform}, URL: {profile_url}\n")

def display_social_media_profiles(profiles):
    print("\033[36m\nProfil Media Sosial yang Ditemukan:\033[0m")
    print("\033[32m")

    if profiles:
        for idx, profile_url in enumerate(profiles, start=1):
            platform = next((domain.split(".")[0].upper() for domain in SOCIAL_MEDIA_DOMAINS if domain in profile_url), "Unknown")
            print(f"{idx}. Platform: {platform}, URL: {profile_url}")
    else:
        print("Tidak ditemukan profil media sosial yang mirip.")

    print("\033[0m")

def main():
    open_instagram()
    while True:
        clear_screen()
        banner()
        menu()

        choice = input("\033[33mPilih opsi: \033[0m")
        if choice == "1":
            username = input("\033[34mMasukkan nama pengguna untuk mencari profil yang mirip: \033[0m")

            print("\033[37m[*] Mohon tunggu, pencarian sedang berlangsung...\033[0m")
            print(f"[*] Mencari profil media sosial yang mirip dengan: {username}")

            html_content = search_similar_profiles(username)
            profiles = parse_search_results(html_content)
            display_social_media_profiles(profiles)
            save_profiles_to_file(profiles, username)

            print("\033[32m[+] Hasil pencarian telah disimpan di folder 'results'.\033[0m")
            input("\033[33mTekan Enter untuk kembali ke menu utama...\033[0m")

        elif choice == "2":
            print("\033[32m[*] Keluar dari program. Sampai jumpa!\033[0m")
            break
        else:
            print("\033[31m[!] Pilihan tidak valid, coba lagi.\033[0m")
            input("\033[33mTekan Enter untuk kembali ke menu utama...\033[0m")

if __name__ == "__main__":
    main()
