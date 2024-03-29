from src.utils.dicts_tuples.flasky_tuples import to_pubmed


def basic(pm_query, els_query, tag, keyword, boolean, open_access):
    # PubMed query
    if not pm_query:
        pm_query = f"({keyword}{to_pubmed[tag]})"
    else:
        pm_query += f" {boolean} ({keyword}{to_pubmed[tag]})"

    # Elsevier query
    if not els_query:
        els_query = f"{tag}({keyword})"
    else:
        els_query += f" {boolean} {tag}({keyword})"

    # Filter
    if open_access and "ffrft[Filter]" not in pm_query:
        pm_query += " AND (ffrft[Filter])"
    if open_access and "OPENACCESS(1)" not in els_query:
        els_query += " AND OPENACCESS(1)"

    return pm_query, els_query


def pubmed(pm_query, tag, keyword, boolean):
    if not pm_query:
        pm_query = f"({keyword}{tag})"
    else:
        pm_query += f" {boolean} ({keyword}{tag})"
    return pm_query

def pubmed_filters(pm_query, filters):
    for filter in filters:
        if not pm_query:
            pm_query = f"({filter}[Filter])"
        else:
            if f"{filter}" not in pm_query:
                pm_query += f" AND ({filter}[Filter])"
    return pm_query


def elsevier(els_query, tag, keyword, boolean, open_access):
    if not els_query:
        els_query = f"{tag}({keyword})"
    else:
        els_query += f" {boolean} {tag}({keyword})"

    if open_access and "OPENACCESS(1)" not in els_query:
        els_query += " AND OPENACCESS(1)"

    return els_query

def preprints(ppr_query, keyword):
    if not ppr_query:
        ppr_query = f'{keyword}'
    else:
        ppr_query += f', {keyword}'

    return ppr_query
