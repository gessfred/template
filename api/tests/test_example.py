from fastapi.testclient import TestClient
from main import app
from routers.playbyplay import playbyplayv2
from unittest import mock
from dependencies import get_db
from tests.utils import get_docker_engine
import pandas as pd

app.dependency_overrides[get_db] = get_docker_engine

client = TestClient(app)

def mock_playbyplay():
    return []

def test_player_timeline_nocache(postgres_db):
    pbp = mock.MagicMock()
    """eventnum as event_num,
            coalesce(
                homedescription,
                neutraldescription,
                visitordescription
            ) as play_description,
            period as quarter_num,
            pctimestring as shot_clock,
            wctimestring as real_time,
            score
    """
    pbp.get_data_frames.return_value = [pd.read_csv("./tests/data/playbyplay_test_001.csv")]
    with mock.patch.object(playbyplayv2, "PlayByPlayV2", return_value=pbp):
        response = client.get("/player-timeline", params={"player": "Giannis", "game_id": "0022300002"})

        assert response.status_code == 200

        data = response.json()

        assert len(data) == 7, type(data)

# def test_player_timeline_cached():
#     response = client.get("/player-timeline")
#     assert response.status_code == 200

# def test_player_timeline_nogame():
#     response = client.get("/player-timeline")
#     assert response.status_code == 200

# def test_player_timeline_noplayer():
#     response = client.get("/player-timeline")
#     assert response.status_code == 200

# def test_player_timeline_noplay():
#     """
#         Test that the calculation does not fail if the player is never subbed in
#     """
#     response = client.get("/player-timeline")
#     assert response.status_code == 200