import os
from datetime import datetime, timezone

USERNAME = "haoyuzhou"   

DATA_DIR = "/app/data"

def main() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    fname = f"{USERNAME}_assignment4_{now}.txt"
    fpath = os.path.join(DATA_DIR, fname)

    content = (
        f"username={USERNAME}\n"
        f"utc_time={now}\n"
        "status=ok\n"
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


    print(f"WROTE_FILE={fpath}")
    print(content)

if __name__ == "__main__":
    main()