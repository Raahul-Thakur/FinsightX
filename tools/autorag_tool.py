import json
from pathlib import Path
from typing import List, Optional

from embeddings.embedder import get_embedding
from embeddings.vector_store import add_to_db, count_documents, query

# Paths for offline corpora
BASE_DIR = Path(__file__).resolve().parent.parent
FILINGS_DIR = BASE_DIR / "data" / "filings"
PRIVATE_DATA_PATH = BASE_DIR / "data" / "private_companies.json"

_bootstrapped = False


def _load_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def _bootstrap_financial_docs():
    global _bootstrapped
    if _bootstrapped or count_documents() > 0:
        _bootstrapped = True
        return

    filings: List[tuple[str, str, dict]] = []
    for txt in FILINGS_DIR.glob("*.txt"):
        text = _load_text_file(txt)
        parts = txt.stem.split("__")
        company = parts[0]
        doc_type = parts[1] if len(parts) > 1 else "filing"
        filings.append(
            (
                txt.stem,
                text,
                {"company": company.lower(), "doc_type": doc_type, "source": "filing"},
            )
        )

    private_cases: List[tuple[str, str, dict]] = []
    if PRIVATE_DATA_PATH.exists():
        data = json.loads(PRIVATE_DATA_PATH.read_text(encoding="utf-8"))
        for entry in data:
            doc_id = f"private__{entry['name'].lower().replace(' ', '_')}"
            text = (
                f"Company: {entry['name']} | Sector: {entry['sector']} | Stage: {entry['stage']} | "
                f"ARR: {entry['arr']} | Growth: {entry['growth']}% | Notes: {entry['notes']}"
            )
            private_cases.append(
                (
                    doc_id,
                    text,
                    {
                        "company": entry["name"].lower(),
                        "doc_type": "vc_case",
                        "source": "private_market",
                    },
                )
            )

    for doc_id, text, metadata in filings + private_cases:
        add_to_db(doc_id=doc_id, text=text, embedding=get_embedding(text), metadata=metadata)

    _bootstrapped = True


def query_equity_kb(text: str, company: Optional[str] = None, doc_types: Optional[List[str]] = None) -> str:
    """Query the financial corpus with optional filters and return stitched context."""
    _bootstrap_financial_docs()
    where = {}
    if company:
        where["company"] = company.lower()
    if doc_types:
        where["doc_type"] = {"$in": doc_types}

    results = query(text, get_embedding, where=where)
    documents = results.get("documents") or []
    metadatas = results.get("metadatas") or []

    stitched = []
    for idx, doc_list in enumerate(documents):
        meta = metadatas[idx][0] if idx < len(metadatas) and metadatas[idx] else {}
        label = f"{meta.get('source', 'kb')}::{meta.get('doc_type', 'doc')}"
        stitched.append(f"[{label}] {doc_list[0]}")

    return "\n".join(stitched) if stitched else ""
