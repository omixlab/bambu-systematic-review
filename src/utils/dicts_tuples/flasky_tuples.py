boolean_operators = [("AND", "AND"), ("OR", "OR"), ("NOT", "NOT")]

# BASIC
tags = [
    ('ALL', "All Fields"),
    ('TITLE', "Title"),
    ('ABS', "Abstract"),
    ('AUTH', "Author"),
    ('AFFIL', "Affiliation"),
    ('PAGES', "Pages"),
    ('VOLUME', "Volume"),
    ('LANGUAGE', "Language"),
    ('DOCTYPE', "Publication Type"),
    ('PUBLISHER', "Publisher"),
]

to_pubmed = {
    "ALL": "",
    "Date": "[Date Publication]",
    "TITLE": "[Title]",
    "ABS": "[Title/Abstract]",
    "AUTH": "[Author]",
    "AFFIL": "[Affiliation]",
    "PAGES": "[Pagination]",
    "VOLUME": "[Volume]",
    "LANGUAGE": "[Language]",
    "DOCTYPE": "[Publication Type]",
    "PUBLISHER": "[Publisher]",
}


# ADVANCED
pm_tags = [
    ("", "All Fields"),
    ("[Date]", "Date"),
    ("[Author]", "Author"),
    ("[Affiliation]", "Affiliation"),
    ("[Book]", "Book"),
    ("[Journal]", "Journal"),
    ("[Volume]", "Volume"),
    ("[Pagination]", "Pagination"),
    ("[Title]", "Title"),
    ("[Title/Abstract]", "Title/Abstract"),
    ("[Transliterated Title]", "Transliterated Title"),
    ("[Text Word]", "Text Word"),
    ("[Language]", "Language"),
    ("[MeSH]", "MeSH"),
    ("[Pharmacological Action]", "Pharmacological Action"),
    ("[Conflict of Interest Statements]", "Conflict of Interest Statements"),
    ("[EC/RN Number]", "EC/RN Number"),
    ("[Grant Number]", "Grant Number"),
    ("[ISBN]", "ISBN"),
    ("[Investigator]", "Investigator"),
    ("[Issue]", "Issue"),
    ("[Location ID]", "Location ID"),
    ("[Secondary Source ID]", "Secondary Source ID"),
    ("[Other Term]", "Other Term"),
    ("[Publication Type]", "Publication Type"),
    ("[Publisher]", "Publisher"),
    ("[Subject - Personal Name]", "Subject - Personal Name"),
    ("[Supplementary Concept]", "Supplementary Concept"),
]

els_tags = [
    ("ALL", "All"),
    ("ABS", "Abstract"),
    ("AF-ID", "Affiliation ID"),
    ("AFFIL", "Affiliation"),
    ("AFFILCITY", "Affiliation city"),
    ("AFFILCOUNTRY", "Affiliation country"),
    ("AFFILORG", "Affiliation organization"),
    ("ARTNUM", "Article number"),
    ("AU-ID", "Author ID"),
    ("AUTHOR-NAME", "Author name"),
    ("AUTH", "Author"),
    ("AUTHFIRST", "Author first initial"),
    ("AUTHLASTNAME", "Author last name"),
    ("AUTHCOLLAB", "Collaboration author"),
    ("AUTHKEY", "Author keywords"),
    ("CASREGNUMBER", "CAS registry number"),
    ("CHEM", "Chemical"),
    ("CHEMNAME", "Chemical name"),
    ("CODEN", "Code"),
    ("CONF", "Conference information"),
    ("CONFLOC", "Conference location"),
    ("CONFNAME", "Conference name"),
    ("CONFSPONSORS", "Conference sponsors"),
    ("DOCTYPE", "Document type"),
    ("PUBSTAGE", "Publication stage"),
    ("DOI", "DOI"),
    ("EDFIRST", "Editor first name"),
    ("EDITOR", "Editor"),
    ("EDLASTNAME", "Editor last name"),
    ("EISSN", "EISSN"),
    ("EXACTSRCTITLE", "Exact source title"),
    ("FIRSTAUTH", "First author"),
    ("FUND-SPONSOR", "Funding sponsor"),
    ("FUND-ACR", "Funding sponsor acronym"),
    ("FUND-NO", "Funding grant number"),
    ("INDEXTERMS", "Index terms"),
    ("ISBN", "ISBN"),
    ("ISSN", "ISSN"),
    ("ISSNP", "ISSNP"),
    ("ISSUE", "Issue"),
    ("KEY", "Keywords"),
    ("LANGUAGE", "Language"),
    ("MANUFACTURER", "Manufacturer"),
    ("OPENACCESS", "Open access"),
    ("PAGEFIRST", "First page"),
    ("PAGELAST", "Last page"),
    ("PAGES", "Pages"),
    ("PMID", "PubMed ID"),
    ("PUBLISHER", "Publisher"),
    ("PUBYEAR", "Date"),
    ("REF", "References"),
    ("REFAUTH", "Reference authors"),
    ("REFTITLE", "Reference title"),
    ("REFSRCTITLE", "Reference source title"),
    ("REFPUBYEAR", "Reference publication year"),
    ("REFARTNUM", "Reference article number"),
    ("REFPAGE", "Reference page numbers"),
    ("REFPAGEFIRST", "Reference first page"),
    ("SEQBANK", "Sequence bank"),
    ("SEQNUMBER", "Accession number"),
    ("SRCTITLE", "Source title"),
    ("SRCTYPE", "Source type"),
    ("SUBJAREA", "Subject area"),
    ("TITLE", "Title"),
    ("TITLE-ABS-KEY", "Title/Abstract/Keyword"),
    ("TITLE-ABS-KEY-AUTH", "Title/Abstract/Keyword/Author"),
    ("TRADENAME", "Tradename"),
    ("VOLUME", "Volume"),
    ("WEBSITE", "Website"),
]