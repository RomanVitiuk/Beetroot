import re

# change location, country
country_loc_pattern = re.compile(r"""
    (?P<location>
    ([A-Z][a-züö\-]*, [Germany\- ]{7,}(?=$))|
    ([A-Z][a-zö\-]*, [Sweden-]{6,}(?=$))|
    ([A-Z][a-z\-]*, [UK]{2,}(?=$))|
    ([A-Z][a-z\-]*, [Switzer -land]{11,}(?=$))|
    ([A-Z][a-z\-]*, [Iran]{4,}(?=$))|
    ([A-Z][a-z\-]*, [Croatia]{7,}(?=$))|
    ([A-Z][a-zł\-]*,? [Poland]{6,}(?=$))|
    ([A-Z][a-zé\-]*, [Canada-]{6,}(?=$))|
    ([A-Z][a-z\-]*, [USA]{3,}(?=$))|
    ([A-Z][a-z\-]*, [Ireland]{7,}(?=$))|
    ([A-Z][a-z\-]*, [India]{5,}(?=$))|
    ([A-Z][a-z\-]*, [The Netherlands]{11,}(?=$))|
    ([A-Z][a-z\- ]*, [Spain]{5,}(?=$))|
    ([A-Z][a-zé\-]*, [France]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Italy]{5,}(?=$))|
    ([A-Z][a-z\-]*, [Slovakia]{8,}(?=$))|
    ([A-Z][a-z\-]*, [Norway]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Denmark]{7,}(?=$))|
    ([A-Z][a-zø\-]*, [Norway]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Australia]{9,}(?=$))|
    ([A-Z][a-z\-]*, [Austria]{7,}(?=$))|
    ([A-Z][a-z\-]*, [South Korea]{5,}(?=$))|
    ([A-Z][a-z\-]*, [Czech Republic]{14,}(?=$))|
    ([A-Z][a-z\-]*, [Turkey]{6,}(?=$))|
    ([A-Z][a-zé\-]*, [Brazil]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Japan]{5,}(?=$))|
    ([A-Z][a-z\-]*, [Slovenia]{8,}(?=$))|
    ([A-Z][a-z\-]*, [Belgium]{7,}(?=$))|
    ([A-Z][a-z\-]*, [Romania]{7,}(?=$))|
    ([A-Z][a-z\-]*, [Greece]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Taiwan-]{6,}(?=$))|
    ([A-Z][a-z\-]*, [Bosnia and Herzegovina]{22,}(?=$))
    )
""", flags=re.X)

desc_pattern = re.compile(r"""
    (?P<desc>
    (?:^Introduction[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^Psoriasis[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^Background[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^Objective[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^Apremilast[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:(?<=^)TNF[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^We[\w.:()\n\/,≤≥%*­	\-\–^<>=;&\[\]’ ]*)|
    (?:^Dermatology[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)|
    (?:^Many	ancient	texts[\w.:()\n\/,≤≥%*	\-\–^<>=;&\[\]’ ]*)
    )
""", flags=re.DOTALL|re.M|re.X)

location_pattern = re.compile(r"""
    (?P<affiliation_name>
    (?:(1[A-Z][\w,\-\n():.\/&;“”’\– ]*)|
    (University[\w,.\-\n() ]*)|
    (Mayo.*)|(^Mogilev.*)|
    (De[rp][\w.’,\-\n ]*)|
    (Mazandaran.*)|
    (Nasonova.*)|
    (N.A.Nasonova.*)|
    (MetrioPharm.*)|
    (NewLab.*)|
    (State Clinical.*)|
    (Spherix Global.*)|
    (The University.*)|
    (11st[\w.,\"\n\- ]*)|
    (Second Department[\w\n. \-,]*)|
    (Centre.*)|
    (Institute[\w,.’\n& ]*)|
    (Ludwig Maximilian Universit.*)|
    (Peoples' Friendship University.*)|
    (School of Psychology.*)|
    (Brigham and Women.*)|
    (Harvard Medical.*)|
    (State Hospital[\w\-\n,. ]*)|
    (Psoriasisförbundet.*))
    )
""", flags=re.X)

session_topic_pattern = re.compile(r"""
    (?P<session>P\d{3})
    (?P<topic>[A-Z0-9\n\-\–;&@\.\/,\?*:()’“” ­]+(?=[A-Z ]))
""", flags=re.X)

names_pattern = re.compile(r"""
    ((?<=^| )([A-Z][a-z0-9. ]*)*(?=,|\n|$))
""", flags=re.X)

split_location_pattern = re.compile(r"""
    [,]? (?=[0-9])
""", flags=re.X)

topic_pattern = re.compile(r"^P\d{3}(?=\n)")
