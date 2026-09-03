"""Fetch arXiv metadata (title + abstract + authors) from the public arXiv API.

arXiv distributes its metadata, abstracts included, under CC0 1.0.  We keep only
what the measurement needs and never report anything person-specific: the
`first_author` string is used purely as a grouping key and no per-author result
is written out.
"""

import json
import os
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "arxiv_raw.jsonl")
API = "http://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom"}
CATS = ["cs.LG", "cs.CV", "cs.CL", "stat.ML"]
PER_PAGE = 500
PAGES = 10  # per category -> up to 20k records


def fetch(cat, start):
    q = urllib.parse.urlencode({
        "search_query": f"cat:{cat}",
        "start": start,
        "max_results": PER_PAGE,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })
    req = urllib.request.Request(API + q, headers={"User-Agent": "infpriv-research/0.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def main():
    t0 = time.time()
    seen, n = set(), 0
    with open(OUT, "w") as f:
        for cat in CATS:
            for p in range(PAGES):
                for attempt in range(3):
                    try:
                        raw = fetch(cat, p * PER_PAGE)
                        break
                    except Exception as e:
                        print("retry", cat, p, e)
                        time.sleep(5)
                else:
                    continue
                root = ET.fromstring(raw)
                entries = root.findall("a:entry", NS)
                if not entries:
                    break
                for e in entries:
                    eid = e.findtext("a:id", default="", namespaces=NS)
                    if eid in seen:
                        continue
                    seen.add(eid)
                    authors = [a.findtext("a:name", default="", namespaces=NS)
                               for a in e.findall("a:author", NS)]
                    if not authors:
                        continue
                    f.write(json.dumps({
                        "id": eid,
                        "first_author": authors[0].strip(),
                        "n_authors": len(authors),
                        "abstract": " ".join(
                            e.findtext("a:summary", default="", namespaces=NS).split()),
                    }) + "\n")
                    n += 1
                print(f"{cat} page {p}: total {n}  ({time.time()-t0:.0f}s)", flush=True)
                time.sleep(3.1)  # arXiv API courtesy rate limit
    print(f"wrote {n} records to {OUT} in {time.time()-t0:.0f}s "
          f"({os.path.getsize(OUT)/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
