tags = (
    'All', 'Title', 'Abstract', 'Date', 'Author', 'Affiliation', 'Pages', 
    'Chemical', 'Conference', 'Document type', 'Publication stage', 'DOI', 
    'Other IDs', 'Editor', 'Exact source title', 'Funding', 'Index terms', 
    'Issue', 'Keywords', 'Language', 'Manufacturer', 'Publisher', 'References', 
    'Sequence bank', 'Source', 'Subject area', 'Title/Abstract/Keyword', 
    'Title/Abstract/Keyword/Author', 'Tradename', 'Volume', 'Website'
    )

radios = {
    'Affiliation': ('Affiliation', 'Affiliation city', 'Affiliation country', 'Affiliation organization'),
    'Author': ('Author', 'Author name', 'Author first initial', 'Author last name', 'Collaboration author', 'Author keywords', 'First author'), #Boolean operators cannot be used in the AU-ID field
    'Chemical': ('Chemical', 'Chemical name', 'CAS registry number'),
    'Conference': ('Conference information', 'Conference name', 'Conference location', 'Conference sponsors'),
    'Editor': ('Editor', 'Editor first name', 'Editor last name'),
    'Funding': ('Funding sponsor', 'Funding sponsor acronym', 'Funding grant number'),
    'Other IDs': ('Article number', 'Code', 'EISSN', 'ISBN', 'ISSNP', 'PubMed ID'),
    'Pages': ('Pages', 'First page', 'Last page'),
    'References': ('References', 'Reference authors', 'Reference title', 'Reference source title', 'Reference year', 'Article number', 'Reference page numbers', 'Reference first page'),
    'Sequence bank': ('Sequence bank', 'Accession number'),
    'Source': ('Source title', 'Source type')
}

selects = {
    'Document type': {
        'Article': 'ar',
        'Abstract report': 'ab',
        'Book': 'bk',
        'Business article': 'bz',
        'Book chapter': 'ch',
        'Conference paper': 'cp',
        'Conference review': 'cr',
        'Editorial': 'ed',
        'Erratum': 'er',
        'Letter': 'le',
        'Note': 'no',
        'Press release': 'pr',
        'Review': 're',
        'Short survey': 'sh'
        },

    'Publication stage': {
        'Article in press': 'aip',
        'Final document': 'final',
        },

    'Source type': {
        'Journal': 'j',
        'Book': 'b',
        'Book series': 'k',
        'Conference proceeding': 'p',
        'Report': 'r',
        'Trade publication': 'd',
        },

    'Subject area': {
        'Agricultural and biological sciences': 'AGRI',
        'Arts and humanities': 'ARTS',
        'Biochemistry, genetics and molecular Biology': 'BIOC',
        'Business, management and accounting': 'BUSI',
        'Chemical engineering': 'CENG',
        'Chemistry': 'CHEM',
        'Computer science': 'COMP',
        'Decision sciences': 'DECI',
        'Dentistry': 'DENT',
        'Earth and planetary sciences': 'EART',
        'Economics, econometrics and finance': 'ECON',
        'Energy': 'ENER',
        'Engineering': 'ENGI',
        'Environmental science': 'ENVI',
        'Health professions': 'HEAL',
        'Immunology and microbiology': 'IMMU',
        'Materials science': 'MATE',
        'Mathematics': 'MATH',
        'Medicine': 'MEDI',
        'Neuroscience': 'NEUR',
        'Nursing': 'NURS',
        'Pharmacology, toxicology and pharmaceutics': 'PHAR',
        'Physics and astronomy': 'PHYS',
        'Psychology': 'PSYC',
        'Social sciences': 'SOCI',
        'Veterinary': 'VETE',
        'Multidisciplinary': 'MULT'                        
        }
}



field = {
        # FIELD RESTRICTION
        'All': 'ALL',
        'Abstract': 'ABS',
        'Affiliation ID': 'AF-ID',
        'Affiliation': 'AFFIL',
        'Affiliation city': 'AFFILCITY',
        'Affiliation country': 'AFFILCOUNTRY',
        'Affiliation organization': 'AFFILORG',
        'Article number': 'ARTNUM',
        'Author ID': 'AU-ID',
        'Author name': 'AUTHOR-NAME',
        'Author': 'AUTH',
        'Author first initial': 'AUTHFIRST',
        'Author last name': 'AUTHLASTNAME',
        'Collaboration author': 'AUTHCOLLAB',
        'Author keywords': 'AUTHKEY',
        'CAS registry number': 'CASREGNUMBER',
        'Chemical': 'CHEM',
        'Chemical name': 'CHEMNAME',
        'Code': 'CODEN',
        'Conference information': 'CONF',
        'Conference location': 'CONFLOC',
        'Conference name': 'CONFNAME',
        'Conference sponsors': 'CONFSPONSORS',
        'Document type': 'DOCTYPE',
        'Publication stage': 'PUBSTAGE',
        'DOI': 'DOI',
        'Editor first name': 'EDFIRST',
        'Editor': 'EDITOR',
        'Editor last name': 'EDLASTNAME',
        'EISSN': 'EISSN',
        'Exact source title': 'EXACTSRCTITLE',
        'First author': 'FIRSTAUTH',
        'Funding sponsor': 'FUND-SPONSOR',
        'Funding sponsor acronym': 'FUND-ACR',
        'Funding grant number': 'FUND-NO',
        'Index terms': 'INDEXTERMS',
        'ISBN': 'ISBN',
        'ISSN': 'ISSN',
        'ISSNP': 'ISSNP',
        'Issue': 'ISSUE',
        'Keywords': 'KEY',
        'Language': 'LANGUAGE',
        'Manufacturer': 'MANUFACTURER',
        'Open access': 'OPENACCESS',
        'First page': 'PAGEFIRST',
        'Last page': 'PAGELAST',
        'Pages': 'PAGES',
        'PubMed ID': 'PMID',
        'Publisher': 'PUBLISHER',
        'Date': 'PUBYEAR',
        'References': 'REF',
        'Reference authors': 'REFAUTH',
        'Reference title': 'REFTITLE',
        'Reference source title': 'REFSRCTITLE',
        'Reference publication year': 'REFPUBYEAR',
        'Reference article number': 'REFARTNUM',
        'Reference page numbers': 'REFPAGE',
        'Reference first page': 'REFPAGEFIRST',
        'Sequence bank': 'SEQBANK',
        'Accession number': 'SEQNUMBER',
        'Source title': 'SRCTITLE',
        'Source type': 'SRCTYPE',
        'Subject area': 'SUBJAREA',
        'Title': 'TITLE',
        'Title/Abstract/Keyword': 'TITLE-ABS-KEY',
        'Title/Abstract/Keyword/Author': 'TITLE-ABS-KEY-AUTH',
        'Tradename': 'TRADENAME',
        'Volume': 'VOLUME',
        'Website': 'WEBSITE',
        }

non_boolean = ['Affiliation ID', 'Author ID', 'Collaboration author', 'DOI', 'Editor', 'Editor first name', 'Editor last name']