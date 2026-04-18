from fastapi.testclient import TestClient

from server.app.main import app

client = TestClient(app)

def test_login_and_me():
    # Perform login with any credentials
    response = client.post(
        "/auth/login",
        data={"username": "alice", "password": "secret"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 200
    data = response.json()
    token = data.get("access_token")
    assert token

    # Use the token to call the protected endpoint
    auth_header = {"Authorization": f"Bearer {token}"}
    me_resp = client.get("/auth/me", headers=auth_header)
    assert me_resp.status_code == 200
    me_data = me_resp.json()
    assert me_data.get("username") == "alice"
