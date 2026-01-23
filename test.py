import sys
import json
from typing import Any, Dict, Optional

import httpx


BASE_URL = "http://127.0.0.1:8000"  # change if different


def pretty(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)


def auth_headers(token: str) -> Dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def safe_print_response(resp: httpx.Response):
    print(f"STATUS: {resp.status_code}")
    ct = resp.headers.get("content-type", "")
    if "application/json" in ct:
        try:
            print(pretty(resp.json()))
        except Exception:
            print(resp.text)
    else:
        print(resp.text)


def signup(client: httpx.Client, email: str, username: str, password: str) -> None:
    print("\n=== SIGNUP ===")
    r = client.post(
        f"{BASE_URL}/auth/signup",
        json={"email": email, "username": username, "password": password},
        timeout=20,
    )
    # If user already exists, you'll likely get 400; that's fine.
    safe_print_response(r)


def login(client: httpx.Client, username: str, password: str) -> str:
    print("\n=== LOGIN ===")
    r = client.post(
        f"{BASE_URL}/auth/login",
        json={"username": username, "password": password},
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    data = r.json()
    token = data["access_token"]
    return token


def me(client: httpx.Client, token: str) -> Dict[str, Any]:
    print("\n=== /auth/me ===")
    r = client.get(f"{BASE_URL}/auth/me", headers=auth_headers(token), timeout=20)
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def create_chat(client: httpx.Client, token: str, name: str) -> Dict[str, Any]:
    print("\n=== CREATE CHAT (POST /chats) ===")
    r = client.post(
        f"{BASE_URL}/chats",
        json={"name": name},
        headers=auth_headers(token),
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def list_chats(client: httpx.Client, token: str) -> Any:
    print("\n=== LIST CHATS (GET /chats) ===")
    r = client.get(f"{BASE_URL}/chats", headers=auth_headers(token), timeout=20)
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def add_message(client: httpx.Client, token: str, chat_id: str, role: str, content: str, meta: Optional[dict] = None):
    print("\n=== ADD MESSAGE (POST /chats/{chat_id}/messages) ===")
    payload = {"role": role, "content": content, "meta": meta}
    r = client.post(
        f"{BASE_URL}/chats/{chat_id}/messages",
        json=payload,
        headers=auth_headers(token),
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def get_messages(client: httpx.Client, token: str, chat_id: str, limit: int = 50, offset: int = 0):
    print("\n=== GET MESSAGES (GET /chats/{chat_id}/messages) ===")
    r = client.get(
        f"{BASE_URL}/chats/{chat_id}/messages",
        params={"limit": limit, "offset": offset},
        headers=auth_headers(token),
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def put_context(client: httpx.Client, token: str, chat_id: str, ctx: dict):
    print("\n=== PUT CONTEXT (PUT /chats/{chat_id}/context) ===")
    r = client.put(
        f"{BASE_URL}/chats/{chat_id}/context",
        json=ctx,
        headers=auth_headers(token),
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def get_context(client: httpx.Client, token: str, chat_id: str):
    print("\n=== GET CONTEXT (GET /chats/{chat_id}/context) ===")
    r = client.get(
        f"{BASE_URL}/chats/{chat_id}/context",
        headers=auth_headers(token),
        timeout=20,
    )
    safe_print_response(r)
    r.raise_for_status()
    return r.json()


def main():
    # Change these to your test user
    email = "user@example.com"
    username = "syed"
    password = "Syed@0123"

    # If you already have a token and only want to test chat endpoints,
    # paste it here and set SKIP_LOGIN=True
    EXISTING_TOKEN = ""
    SKIP_LOGIN = False

    with httpx.Client() as client:
        if not SKIP_LOGIN and not EXISTING_TOKEN:
            # optional: try signup (will be 400 if already exists)
            signup(client, email, username, password)
            token = login(client, username, password)
        else:
            token = EXISTING_TOKEN.strip()

        # verify token
        me(client, token)

        # create chat
        chat = create_chat(client, token, name="My First Chat")
        chat_id = chat["id"]
        print(f"\nCreated chat_id: {chat_id}")

        # list chats
        list_chats(client, token)

        # add a message
        add_message(client, token, chat_id, role="user", content="Hello from test script!", meta={"source": "script"})

        # read messages
        get_messages(client, token, chat_id, limit=50, offset=0)

        # context set + get
        put_context(
            client,
            token,
            chat_id,
            {
                "initial_details": "This is a test chat.",
                "ui_details": "Web UI",
                "user_journeys": "Signup -> Create chat -> Message",
                "tech_stack": "FastAPI + Postgres + JWT",
                "extra": {"env": "local"},
            },
        )
        get_context(client, token, chat_id)


if __name__ == "__main__":
    try:
        main()
    except httpx.HTTPStatusError as e:
        print("\n=== HTTP ERROR ===")
        print("Request:", e.request.method, e.request.url)
        print("Response:", e.response.status_code)
        print(e.response.text)
        sys.exit(1)
