from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PRIVATE_DATA_PATH = BASE_DIR / "data" / "private_companies.json"

PUBLIC_CANONICAL = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "TSLA": "Tesla",
    "GOOGL": "Alphabet",
    "AMZN": "Amazon",
}


@dataclass
class CompanyResolution:
    company: str | None
    ticker: str | None
    is_public: bool
    source: str


def _load_private_names() -> list[str]:
    if not PRIVATE_DATA_PATH.exists():
        return []
    data = json.loads(PRIVATE_DATA_PATH.read_text(encoding="utf-8"))
    return [entry["name"].lower() for entry in data]


PRIVATE_NAMES = _load_private_names()


def resolve_company(user_text: str) -> CompanyResolution:
    tokens = re.findall(r"[A-Za-z]{1,6}", user_text.upper())
    for token in tokens:
        if token in PUBLIC_CANONICAL:
            return CompanyResolution(company=PUBLIC_CANONICAL[token], ticker=token, is_public=True, source="symbol_map")
        if len(token) <= 5 and token.isalpha():
            return CompanyResolution(company=None, ticker=token, is_public=True, source="heuristic")

    lowered = user_text.lower()
    for name in PRIVATE_NAMES:
        if name in lowered:
            return CompanyResolution(company=name.title(), ticker=None, is_public=False, source="private_case_base")

    return CompanyResolution(company=None, ticker=None, is_public=False, source="unknown")
