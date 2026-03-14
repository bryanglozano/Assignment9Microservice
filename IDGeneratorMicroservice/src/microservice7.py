import json
import time
import re
from pathlib import Path

PIPE_DIR = Path("pipe")
REQ = PIPE_DIR / "id_request.txt"
RES = PIPE_DIR / "id_response.txt"

POLL_SECONDS = 0.1


def IDGenerator(date, title):
    # remove slashes from date
    clean_date = date.replace("/", "")

    # convert title to lowercase
    clean_title = title.lower()

    # replace spaces with underscores
    clean_title = clean_title.replace(" ", "_")

    # remove special characters
    clean_title = re.sub(r'[^a-z0-9_]', '', clean_title)

    return clean_date + clean_title


def process_request():
    raw = REQ.read_text().strip()

    if not raw:
        return

    try:
        request = json.loads(raw)

        date = request.get("date")
        title = request.get("title")

        result = IDGenerator(date, title)

        response = {
            "ok": True,
            "id": result
        }

    except Exception as e:
        response = {
            "ok": False,
            "error": str(e)
        }

    RES.write_text(json.dumps(response))
    REQ.write_text("")


def main():

    PIPE_DIR.mkdir(exist_ok=True)
    REQ.touch(exist_ok=True)
    RES.touch(exist_ok=True)

    print("Microservice 7: ID Generator running...")
    print("Request file:", REQ)
    print("Response file:", RES)

    while True:
        process_request()
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
