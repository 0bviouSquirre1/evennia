"""
Random tables - adopted from _Knave_.

"""

# Character generation tables

character_generation = {
    "physique": [
        "athletic",
        "brawny",
        "corpulent",
        "delicate",
        "gaunt",
        "hulking",
        "lanky",
        "ripped",
        "rugged",
        "scrawny",
        "short",
        "sinewy",
        "slender",
        "flabby",
        "statuesque",
        "stout",
        "tiny",
        "towering",
        "willowy",
        "wiry",
    ],
    "face": [
        "bloated",
        "blunt",
        "bony",
        "chiseled",
        "delicate",
        "elongated",
        "patrician",
        "pinched",
        "hawkish",
        "broken",
        "impish",
        "narrow",
        "ratlike",
        "round",
        "sunken",
        "sharp",
        "soft",
        "square",
        "wide",
        "wolfish",
    ],
    "skin": [
        "battle scar",
        "birthmark",
        "burn scar",
        "dark",
        "makeup",
        "oily",
        "pale",
        "perfect",
        "pierced",
        "pockmarked",
        "reeking",
        "tattooed",
        "rosy",
        "rough",
        "sallow",
        "sunburned",
        "tanned",
        "war paint",
        "weathered",
        "whip scar",
    ],
    "hair": [
        "bald",
        "braided",
        "bristly",
        "cropped",
        "curly",
        "disheveled",
        "dreadlocks",
        "filthy",
        "frizzy",
        "greased",
        "limp",
        "long",
        "luxurious",
        "mohawk",
        "oily",
        "ponytail",
        "silky",
        "topknot",
        "wavy",
        "wispy",
    ],
    "clothing": [
        "antique",
        "bloody",
        "ceremonial",
        "decorated",
        "eccentric",
        "elegant",
        "fashionable",
        "filthy",
        "flamboyant",
        "stained",
        "foreign",
        "frayed",
        "frumpy",
        "livery",
        "oversized",
        "patched",
        "perfumed",
        "rancid",
        "torn",
        "undersized",
    ],
    "virtue": [
        "ambitious",
        "cautious",
        "courageous",
        "courteous",
        "curious",
        "disciplined",
        "focused",
        "generous",
        "gregarious",
        "honest",
        "honorable",
        "humble",
        "idealistic",
        "just",
        "loyal",
        "merciful",
        "righteous",
        "serene",
        "stoic",
        "tolerant",
    ],
    "vice": [
        "aggressive",
        "arrogant",
        "bitter",
        "cowardly",
        "cruel",
        "deceitful",
        "flippant",
        "gluttonous",
        "greedy",
        "irascible",
        "lazy",
        "nervous",
        "prejudiced",
        "reckless",
        "rude",
        "suspicious",
        "vain",
        "vengeful",
        "wasteful",
        "whiny",
    ],
    "speech": [
        "blunt",
        "booming",
        "breathy",
        "cryptic",
        "drawling",
        "droning",
        "flowery",
        "formal",
        "gravelly",
        "hoarse",
        "mumbling",
        "precise",
        "quaint",
        "rambling",
        "rapid-fire",
        "dialect",
        "slow",
        "squeaky",
        "stuttering",
        "whispery",
    ],
    "background": [
        "alchemist",
        "beggar",
        "butcher",
        "burglar",
        "charlatan",
        "cleric",
        "cook",
        "cultist",
        "gambler",
        "herbalist",
        "magician",
        "mariner",
        "mercenary",
        "merchant",
        "outlaw",
        "performer",
        "pickpocket",
        "smuggler",
        "student",
        "tracker",
    ],
    "misfortune": [
        "abandoned",
        "addicted",
        "blackmailed",
        "condemned",
        "cursed",
        "defrauded",
        "demoted",
        "discredited",
        "disowned",
        "exiled",
        "framed",
        "haunted",
        "kidnapped",
        "mutilated",
        "poor",
        "pursued",
        "rejected",
        "replaced",
        "robbed",
        "suspected",
    ],
    "alignment": [
        ("1-5", "law"),
        ("6-15", "neutrality"),
        ("16-20", "chaos"),
    ],
    "armor": [
        ("1-3", "no armor"),
        ("4-14", "gambeson"),
        ("15-19", "brigandine"),
        ("20", "chain"),
    ],
    "helmets and shields": [
        ("1-13", "no helmet or shield"),
        ("14-16", "helmet"),
        ("17-19", "shield"),
        ("20", "helmet and shield"),
    ],
    "starting weapon": [  # note: these are all d6 dmg weapons
        ("1-7", "dagger"),
        ("8-13", "club"),
        ("14-20", "staff"),
    ],
    "dungeoning gear": [
        "rope, 50ft",
        "pulleys",
        "candles, 5",
        "chain, 10ft",
        "chalk, 10",
        "crowbar",
        "tinderbox",
        "grap. hook",
        "hammer",
        "waterskin",
        "lantern",
        "lamp oil",
        "padlock",
        "manacles",
        "mirror",
        "pole, 10ft",
        "sack",
        "tent",
        "spikes, 5",
        "torches, 5",
    ],
    "general gear 1": [
        "air bladder",
        "bear trap",
        "shovel",
        "bellows",
        "grease",
        "saw",
        "bucket",
        "caltrops",
        "chisel",
        "drill",
        "fish. rod",
        "marbles",
        "glue",
        "pick",
        "hourglass",
        "net",
        "tongs",
        "lockpicks",
        "metal file",
        "nails",
    ],
    "general gear 2": [
        "incense",
        "sponge",
        "lens",
        "perfume",
        "horn",
        "bottle",
        "soap",
        "spyglass",
        "tar pot",
        "twine",
        "fake jewels",
        "blank book",
        "card deck",
        "dice set",
        "cook pots",
        "face paint",
        "whistle",
        "instrument",
        "quill & ink",
        "small bell",
    ],
    "name": [
        "Abbo",
        "Adelaide",
        "Ellis",
        "Eleanor",
        "Lief",
        "Luanda",
        "Ablerus",
        "Agatha",
        "Eneto",
        "Elizabeth",
        "Luke",
        "Lyra",
        "Acot",
        "Aleida",
        "Enio",
        "Elspeth",
        "Martin",
        "Mabel",
        "Alexander",
        "Alexia",
        "Eral",
        "Emeline",
        "Merrick",
        "Maerwynn",
        "Almanzor",
        "Alianor",
        "Erasmus",
        "Emma",
        "Mortimer",
        "Malkyn",
        "Althalos",
        "Aline",
        "Eustace",
        "Emmony",
        "Ogden",
        "Margaret",
        "Ancelot",
        "Alma",
        "Everard",
        "Enna",
        "Oliver",
        "Margery",
        "Asher",
        "Alys",
        "Faustus",
        "Enndolynn",
        "Orion",
        "Maria",
        "Aster",
        "Amabel",
        "Favian",
        "Eve",
        "Oswald",
        "Marion",
        "Balan",
        "Amice",
        "Fendrel",
        "Evita",
        "Pelagon",
        "Matilda",
        "Balthazar",
        "Anastas",
        "Finn",
        "Felice",
        "Pello",
        "Millicent",
        "Barat",
        "Angmar",
        "Florian",
        "Fern",
        "Peyton",
        "Mirabelle",
        "Bartholomew",
        "Annabel",
        "Francis",
        "Floria",
        "Philip",
        "Muriel",
        "Basil",
        "Arabella",
        "Frederick",
        "Fredegonde",
        "Poeas",
        "Nabarne",
        "Benedict",
        "Ariana",
        "Gaidon",
        "Gillian",
        "Quinn",
        "Nell",
        "Berinon",
        "Ayleth",
        "Gavin",
        "Gloriana",
        "Ralph",
        "Nesea",
        "Bertram",
        "Barberry",
        "Geoffrey",
        "Godeleva",
        "Randolph",
        "Niree",
        "Beves",
        "Barsaba",
        "Gerard",
        "Godiva",
        "Reginald",
        "Odette",
        "Bilmer",
        "Basilia",
        "Gervase",
        "Gunnilda",
        "Reynold",
        "Odila",
        "Blanko",
        "Beatrix",
        "Gilbert",
        "Gussalen",
        "Richard",
        "Oria",
        "Bodo",
        "Benevolence",
        "Giles",
        "Gwendolynn",
        "Robert",
        "Osanna",
        "Borin",
        "Bess",
        "Godfrey",
        "Hawise",
        "Robin",
        "Ostrythe",
        "Bryce",
        "Brangian",
        "Gregory",
        "Helena",
        "Roger",
        "Ottilia",
        "Carac",
        "Brigida",
        "Gringoire",
        "Helewise",
        "Ronald",
        "Panope",
        "Caspar",
        "Brunhild",
        "Gunthar",
        "Hester",
        "Rowan",
        "Paternain",
        "Cassius",
        "Camilla",
        "Guy",
        "Hildegard",
        "Rulf",
        "Pechel",
        "Cedric",
        "Canace",
        "Gyras",
        "Idony",
        "Sabin",
        "Pepper",
        "Cephalos",
        "Cecily",
        "Hadrian",
        "Isabella",
        "Sevrin",
        "Petronilla",
        "Chadwick",
        "Cedany",
        "Hedelf",
        "Iseult",
        "Silas",
        "Phrowenia",
        "Charillos",
        "Christina",
        "Hewelin",
        "Isolde",
        "Simon",
        "Poppy",
        "Charles",
        "Claramunda",
        "Hilderith",
        "Jacquelyn",
        "Solomon",
        "Quenell",
        "Chermon",
        "Clarice",
        "Humbert",
        "Jasmine",
        "Stephen",
        "Raisa",
        "Clement",
        "Clover",
        "Hyllus",
        "Jessamine",
        "Terrowin",
        "Reyna",
        "Clifton",
        "Collette",
        "Ianto",
        "Josselyn",
        "Thomas",
        "Rixende",
        "Clovis",
        "Constance",
        "Ibykos",
        "Juliana",
        "Tristan",
        "Rosamund",
        "Cyon",
        "Damaris",
        "Inigo",
        "Karitate",
        "Tybalt",
        "Rose",
        "Dain",
        "Daphne",
        "Itylus",
        "Katelyn",
        "Ulric",
        "Ryia",
        "Dalmas",
        "Demona",
        "James",
        "Katja",
        "Walter",
        "Sarah",
        "Danor",
        "Dimia",
        "Jasper",
        "Katrina",
        "Wander",
        "Seraphina",
        "Destrian",
        "Dione",
        "Jiles",
        "Kaylein",
        "Warin",
        "Thea",
        "Domeka",
        "Dorothea",
        "Joffridus",
        "Kinna",
        "Waverly",
        "Trillby",
        "Donald",
        "Douce",
        "Jordan",
        "Krea",
        "Willahelm",
        "Wendel",
        "Doran",
        "Duraina",
        "Joris",
        "Kypris",
        "William",
        "Wilberga",
        "Dumphey",
        "Dyota",
        "Josef",
        "Landerra",
        "Wimarc",
        "Winifred",
        "Eadmund",
        "Eberhild",
        "Laurence",
        "Larraza",
        "Wystan",
        "Wofled",
        "Eckardus",
        "Edelot",
        "Leofrick",
        "Linet",
        "Xalvador",
        "Wymarc",
        "Edward",
        "Edyva",
        "Letholdus",
        "Loreena",
        "Zane",
        "Ysmay",
    ],
}


reactions = [
    ("2", "Hostile"),
    ("3-5", "Unfriendly"),
    ("6-8", "Unsure"),
    ("9-11", "Talkative"),
    ("12", "Helpful"),
]

initiative = [
    ("1-3", "Enemy acts first"),
    ("4-6", "PC acts first"),
]


death_and_dismemberment = [
    "dead",
    "dead",  # original says 'dismemberment' here, we don't simulate this
    "weakened",  # -1d4 STR
    "unsteady",  # -1d4 DEX
    "sickly",  # -1d4 CON
    "addled",  # -1d4 INT
    "rattled",  # -1d4 WIS
    "disfigured",  # -1d4 CHA
]
