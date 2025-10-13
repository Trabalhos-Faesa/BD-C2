from fastapi.testclient import TestClient


def test_root_path_return(client: TestClient) -> None:
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {
        'rows': [],
        'rowcount': -1,
        'status': 'success',
        'msg': 'Welcome!',
    }
