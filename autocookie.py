import streamlit as st
import requests
import uuid


def join_shopee_session(session_id, generated_uuid, vcookie):
    url2 = f"https://live.shopee.co.id/api/v1/session/{session_id}/join"
    data2 = {
        "uuid": generated_uuid,
        "ver": 1
    }
    headers2 = {
        "Accept": "application/json, text/plain, /",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
        "Client-Info": "os=2;platform=9;scene_id=17",
        "Content-Length": "55",
        "Content-Type": "application/json",
        "Cookie": f"{vcookie}",
        "Sec-Ch-Ua": "Not_A Brand;v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.post(url2, json=data2, headers=headers2)
        response.raise_for_status()
        json_response = response.json()
        if 'data' in json_response and 'usersig' in json_response['data']:
            return json_response['data']['usersig'] + "#" + json_response['data']['session']['chatroom_id'] + "#" + \
                json_response['data']['session']['device_id']
        else:
            print(f"Error joining Shopee session {session_id}: 'usersig' not found in response.")
    except requests.exceptions.RequestException as e:
        print(f"Error joining Shopee session {session_id}: {e}")

    return None


def getCookieShop():
    url = "https://whitelist-bot.com/random.php"
    headers = {'Host': "whitelist-bot.com"}
    response = requests.get(url, headers=headers)
    return response.text.strip()


def main():
    st.title("😎Shopee Bot Bergabung😎")

    id_session_target = st.text_input("Masukkan ID session target (wajib diisi): ")
    jumlah_loop = st.text_input("Masukkan jumlah loop (wajib diisi): ")

    if st.button("Mulai Bot"):
        for _ in range(int(jumlah_loop)):
            random_cookie = getCookieShop()  # Memperbarui cookie setiap kali loop dimulai
            uidinya = str(uuid.uuid4())
            datax = join_shopee_session(id_session_target, f"{uidinya}", random_cookie)


if __name__ == "__main__":
    main()
