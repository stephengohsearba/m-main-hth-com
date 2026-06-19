import json
from datetime import datetime

SITE_DATA = {
    "hth": {
        "url": "https://m-main-hth.com",
        "tags": ["sports", "entertainment", "mobile"],
        "description": "HTH is a mobile-first platform offering sports and entertainment content.",
        "keywords": ["hth", "mobile", "sports", "entertainment"],
        "category": "entertainment",
        "region": "global",
        "language": "en"
    },
    "hth_wap": {
        "url": "https://m-main-hth.com/wap",
        "tags": ["mobile", "wap", "hth"],
        "description": "WAP version of HTH platform for low-bandwidth environments.",
        "keywords": ["hth wap", "mobile site", "hth"],
        "category": "entertainment",
        "region": "global",
        "language": "en"
    },
    "hth_live": {
        "url": "https://m-main-hth.com/live",
        "tags": ["live", "streaming", "hth"],
        "description": "Live streaming section of HTH, covering events and matches.",
        "keywords": ["hth live", "streaming", "live events"],
        "category": "live",
        "region": "global",
        "language": "en"
    }
}

DEFAULT_SITE = "hth"

def generate_summary(site_key):
    if site_key not in SITE_DATA:
        site_key = DEFAULT_SITE
    site = SITE_DATA[site_key]
    summary_parts = [
        f"Site Identifier: {site_key}",
        f"URL: {site['url']}",
        f"Tags: {', '.join(site['tags'])}",
        f"Keywords: {', '.join(site['keywords'])}",
        f"Category: {site['category']}",
        f"Region: {site['region']}",
        f"Language: {site['language']}",
        f"Description: {site['description']}"
    ]
    return "\n".join(summary_parts)

def structured_summary(site_key, as_dict=False):
    if site_key not in SITE_DATA:
        site_key = DEFAULT_SITE
    site = SITE_DATA[site_key]
    record = {
        "site": site_key,
        "url": site["url"],
        "tags": site["tags"],
        "keywords": site["keywords"],
        "description": site["description"],
        "category": site["category"],
        "region": site["region"],
        "language": site["language"],
        "generated_at": datetime.utcnow().isoformat()
    }
    if as_dict:
        return record
    return json.dumps(record, indent=2)

def list_all_sites():
    return list(SITE_DATA.keys())

def print_summary_for(site_key=None):
    if site_key is None:
        site_key = DEFAULT_SITE
    print("=== Structured Summary ===")
    print(generate_summary(site_key))
    print()
    print("=== JSON Summary ===")
    print(structured_summary(site_key))
    print()
    print(f"Available sites: {', '.join(list_all_sites())}")

if __name__ == "__main__":
    print_summary_for("hth")
    print("---")
    print_summary_for("hth_live")