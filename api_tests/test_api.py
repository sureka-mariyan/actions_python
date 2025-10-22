import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            ignore_https_errors=True,
            extra_http_headers={
                "x-api-key": "reqres-free-v1"  # Just example header, JSONPlaceholder doesn't require it
            }
        )
        yield request_context
        request_context.dispose()

# ✅ GET request test
def test_get_post(api_request_context):
    response = api_request_context.get("/posts/1")
    assert response.ok
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    print("GET Response:", data)

# ✅ POST request test
def test_create_post(api_request_context):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = api_request_context.post("/posts", data=payload)
    assert response.status == 201
    data = response.json()
    assert data["title"] == "foo"
    print("POST Response:", data)

# ✅ PUT request test
def test_update_post(api_request_context):
    payload = {"id": 1, "title": "updated", "body": "new content", "userId": 1}
    response = api_request_context.put("/posts/1", data=payload)
    assert response.ok
    data = response.json()
    assert data["title"] == "updated"
    print("PUT Response:", data)

# ✅ DELETE request test
def test_delete_post(api_request_context):
    response = api_request_context.delete("/posts/1")
    assert response.status in [200, 204]
    print("DELETE Response:", response.text())
