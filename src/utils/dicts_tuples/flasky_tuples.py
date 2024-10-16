# BASIC
tags = [
    ("ALL", "All Fields"),
    ("TITLE", "Title"),
    ("ABS", "Abstract"),
    ("AUTH", "Author"),
]


# ADVANCED
pubmed_tags = [
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

elsevier_tags = [
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

scielo_tags = [
    ("", "All areas"),
    ("year_cluster", "Publication Year"),
    ("au", "Author"),
    ("sponsor", "Sponsor"),
    ("ta", "Journal"),
    ("ab", "Abstract"),
    ("ti", "Title"), 
]

pprint_tags = [
    ("abstract", "Abstract"),
    ("title", "Title"),
    ("doi", "DOI"),
    ("date", "Date"),
    ("authors", "Authors"),
    ("journal", "Journal"),
]

# PubMed Filters
pubmed_filters = {
    "abstract": "fha",
    "free_full_text": "ffrft",
    "full_text": "fft",
    "booksdocs": "pubt.booksdocs",
    "clinicaltrial": "pubt.clinicaltrial",
    "meta_analysis": "pubt.meta-analysis",
    "randomizedcontrolledtrial": "pubt.randomizedcontrolledtrial",
    "review": "pubt.review",
    "systematicreview": "pubt.systematicreview",
    "humans": "hum_ani.humans",
    "animal": "hum_ani.animal",
    "male": "sex.male",
    "female": "sex.female",
    "english": "lang.english",
    "portuguese": "lang.portuguese",
    "spanish": "lang.spanish",
    "data": "articleattr.data",
    "excludepreprints": "other.excludepreprints",
    "medline": "other.medline",
}

# en_ner_bionlp13cg_md Labels
scispacy = [
    (None, "None"),
    ("AMINO_ACID", "Amino acid"),
    ("ANATOMICAL_SYSTEM", "Anatomical system"),
    ("CANCER", "Cancer"),
    ("CELL", "Cell"),
    ("CELLULAR_COMPONENT", "Cellular component"),
    ("DEVELOPING_ANATOMICAL_STRUCTURE", "Developing anatomical structure"),
    ("GENE_OR_GENE_PRODUCT", "Gene or gene product"),
    ("IMMATERIAL_ANATOMICAL_ENTITY", "Immaterial anatomical entity"),
    ("MULTI-TISSUE_STRUCTURE", "Multi-tissue structure"),
    ("ORGAN", "Organ"),
    ("ORGANISM", "Organism"),
    ("ORGANISM_SUBDIVISION", "Organism subdivision"),
    ("ORGANISM_SUBSTANCE", "Organism substance"),
    ("PATHOLOGICAL_FORMATION", "Pathological formation"),
    ("SIMPLE_CHEMICAL", "Simple chemical"),
    ("TISSUE", "Tissue"),
]


# DICTS
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

to_scielo = {
    "TITLE": "ti",
    "ABS": "ab",
    "AUTH": "au",
}

to_pprint = {
    "TITLE": "title",
    "ABS": "abstract",
    "AUTH": "authors",
}

