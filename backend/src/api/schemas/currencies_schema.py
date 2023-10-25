from enum import Enum
from pydantic import BaseModel


class AvailableCurrencies(str, Enum):
    AED = "United Arab Emirates Dirham"
    AFN = "Afghan Afghani"
    ALL = "Albanian Lek"
    AMD = "Armenian Dram"
    ANG = "Netherlands Antillean Guilder"
    AOA = "Angolan Kwanza"
    ARS = "Argentine Peso"
    AUD = "Australian Dollar"
    AWG = "Aruban Florin"
    AZN = "Azerbaijani Manat"
    BAM = "Bosnia-Herzegovina Convertible Mark"
    BBD = "Barbadian Dollar"
    BDT = "Bangladeshi Taka"
    BGN = "Bulgarian Lev"
    BHD = "Bahraini Dinar"
    BIF = "Burundian Franc"
    BMD = "Bermudan Dollar"
    BND = "Brunei Dollar"
    BOB = "Bolivian Boliviano"
    BRL = "Brazilian Real"
    BSD = "Bahamian Dollar"
    BTC = "Bitcoin"
    BTN = "Bhutanese Ngultrum"
    BWP = "Botswanan Pula"  
    BYN = "New Belarusian Ruble"
    BYR = "Belarusian Ruble"
    BZD = "Belize Dollar"
    CAD = "Canadian Dollar"
    CDF = "Congolese Franc"
    CHF = "Swiss Franc"
    CLF = "Chilean Unit of Account (UF)"
    CLP = "Chilean Peso"
    CNY = "Chinese Yuan"
    COP = "Colombian Peso"
    CRC = "Costa Rican Colon"
    CUC = "Cuban Convertible Peso"
    CUP = "Cuban Peso"
    CVE = "Cape Verdean Escudo"
    CZK = "Czech Republic Koruna"
    DJF = "Djiboutian Franc"
    DKK = "Danish Krone"
    DOP = "Dominican Peso"
    DZD = "Algerian Dinar"
    EGP = "Egyptian Pound"
    ERN = "Eritrean Nakfa"
    ETB = "Ethiopian Birr"
    EUR = "Euro"
    FJD = "Fijian Dollar"
    FKP = "Falkland Islands Pound"
    GBP = "British Pound Sterling"
    GEL = "Georgian Lari"
    GGP = "Guernsey Pound"
    GHS = "Ghanaian Cedi"
    GIP = "Gibraltar Pound"
    GMD = "Gambian Dalasi"
    GNF = "Guinean Franc"
    GTQ = "Guatemalan Quetzal"
    GYD = "Guyanaese Dollar"
    HKD = "Hong Kong Dollar"
    HNL = "Honduran Lempira"
    HRK = "Croatian Kuna"
    HTG = "Haitian Gourde"
    HUF = "Hungarian Forint"
    IDR = "Indonesian Rupiah"
    ILS = "Israeli New Sheqel"
    IMP = "Manx pound"
    INR = "Indian Rupee"
    IQD = "Iraqi Dinar"
    IRR = "Iranian Rial"
    ISK = "Icelandic Krona"
    JEP = "Jersey Pound"
    JMD = "Jamaican Dollar"
    JOD = "Jordanian Dinar"
    JPY = "Japanese Yen"
    KES = "Kenyan Shilling"
    KGS = "Kyrgystani Som"
    KHR = "Cambodian Riel"
    KMF = "Comorian Franc"
    KPW = "North Korean Won"
    KRW = "South Korean Won"
    KWD = "Kuwaiti Dinar"
    KYD = "Cayman Islands Dollar"
    KZT = "Kazakhstani Tenge"
    LAK = "Laotian Kip"
    LBP = "Lebanese Pound"
    LKR = "Sri Lankan Rupee"
    LRD = "Liberian Dollar"
    LSL = "Lesotho Loti"
    LTL = "Lithuanian Litas"
    LVL = "Latvian Lats"
    LYD = "Libyan Dinar"
    MAD = "Moroccan Dirham"
    MDL = "Moldovan Leu"
    MGA = "Malagasy Ariary"
    MKD = "Macedonian Denar"
    MMK = "Myanma Kyat"
    MNT = "Mongolian Tugrik"
    MOP = "Macanese Pataca"
    MRO = "Mauritanian Ouguiya"
    MUR = "Mauritian Rupee"
    MVR = "Maldivian Rufiyaa"
    MWK = "Malawian Kwacha"
    MXN = "Mexican Peso"
    MYR = "Malaysian Ringgit"
    MZN = "Mozambican Metical"
    NAD = "Namibian Dollar"
    NGN = "Nigerian Naira"
    NIO = "Nicaraguan Cordoba"
    NOK = "Norwegian Krone"
    NPR = "Nepalese Rupee"
    NZD = "New Zealand Dollar"
    OMR = "Omani Rial"
    PAB = "Panamanian Balboa"
    PEN = "Peruvian Nuevo Sol"
    PGK = "Papua New Guinean Kina"
    PHP = "Philippine Peso"
    PKR = "Pakistani Rupee"
    PLN = "Polish Zloty"
    PYG = "Paraguayan Guarani"
    QAR = "Qatari Rial"
    RON = "Romanian Leu"
    RSD = "Serbian Dinar"
    RUB = "Russian Ruble"
    RWF = "Rwandan Franc"
    SAR = "Saudi Riyal"
    SBD = "Solomon Islands Dollar"
    SCR = "Seychellois Rupee"
    SDG = "Sudanese Pound"
    SEK = "Swedish Krona"
    SGD = "Singapore Dollar"
    SHP = "Saint Helena Pound"
    SLE = "Sierra Leonean Leone"
    SLL = "Sierra Leonean Leone"
    SOS = "Somali Shilling"
    SRD = "Surinamese Dollar"
    SSP = "South Sudanese Pound"
    STD = "Sao Tome and Principe Dobra"
    SVC = "Salvadoran Colon"
    SYP = "Syrian Pound"
    SZL = "Swazi Lilangeni"
    THB = "Thai Baht"
    TJS = "Tajikistani Somoni"
    TMT = "Turkmenistani Manat"
    TND = "Tunisian Dinar"
    TOP = "Tongan Pa'anga"
    TRY = "Turkish Lira"
    TTD = "Trinidad and Tobago Dollar"
    TWD = "New Taiwan Dollar"
    TZS = "Tanzanian Shilling"
    UAH = "Ukrainian Hryvnia"
    UGX = "Ugandan Shilling"
    USD = "United States Dollar"
    UYU = "Uruguayan Peso"
    UZS = "Uzbekistan Som"
    VEF = "Venezuelan Bolivar Fuerte"
    VES = "Sovereign Bolivar"
    VND = "Vietnamese Dong"
    VUV = "Vanuatu Vatu"
    WST = "Samoan Tala"
    XAF = "CFA Franc BEAC"
    XAG = "Silver (troy ounce)"
    XAU = "Gold (troy ounce)"
    XCD = "East Caribbean Dollar"
    XDR = "Special Drawing Rights"
    XOF = "CFA Franc BCEAO"
    XPF = "CFP Franc"
    YER = "Yemeni Rial"
    ZAR = "South African Rand"
    ZMK = "Zambian Kwacha (pre-2013)"
    ZMW = "Zambian Kwacha"
    ZWL = "Zimbabwean Dollar"


class Rates(BaseModel):
    AED: int | float
    AFN: int | float
    ALL: int | float
    AMD: int | float
    ANG: int | float
    AOA: int | float
    ARS: int | float
    AUD: int | float
    AWG: int | float
    AZN: int | float
    BAM: int | float
    BBD: int | float
    BDT: int | float
    BGN: int | float
    BHD: int | float
    BIF: int | float
    BMD: int | float
    BND: int | float
    BOB: int | float
    BRL: int | float
    BSD: int | float
    BTC: int | float
    BTN: int | float
    BWP: int | float
    BYN: int | float
    BYR: int | float
    BZD: int | float
    CAD: int | float
    CDF: int | float
    CHF: int | float
    CLF: int | float
    CLP: int | float
    CNY: int | float
    COP: int | float
    CRC: int | float
    CUC: int | float
    CUP: int | float
    CVE: int | float
    CZK: int | float
    DJF: int | float
    DKK: int | float
    DOP: int | float
    DZD: int | float
    EGP: int | float
    ERN: int | float
    ETB: int | float
    EUR: int | float
    FJD: int | float
    FKP: int | float
    GBP: int | float
    GEL: int | float
    GGP: int | float
    GHS: int | float
    GIP: int | float
    GMD: int | float
    GNF: int | float
    GTQ: int | float
    GYD: int | float
    HKD: int | float
    HNL: int | float
    HRK: int | float
    HTG: int | float
    HUF: int | float
    IDR: int | float
    ILS: int | float
    IMP: int | float
    INR: int | float
    IQD: int | float
    IRR: int | float
    ISK: int | float
    JEP: int | float
    JMD: int | float
    JOD: int | float
    JPY: int | float
    KES: int | float
    KGS: int | float
    KHR: int | float
    KMF: int | float
    KPW: int | float
    KRW: int | float
    KWD: int | float
    KYD: int | float
    KZT: int | float
    LAK: int | float
    LBP: int | float
    LKR: int | float
    LRD: int | float
    LSL: int | float
    LTL: int | float
    LVL: int | float
    LYD: int | float
    MAD: int | float
    MDL: int | float
    MGA: int | float
    MKD: int | float
    MMK: int | float
    MNT: int | float
    MOP: int | float
    MRO: int | float
    MUR: int | float
    MVR: int | float
    MWK: int | float
    MXN: int | float
    MYR: int | float
    MZN: int | float
    NAD: int | float
    NGN: int | float
    NIO: int | float
    NOK: int | float
    NPR: int | float
    NZD: int | float
    OMR: int | float
    PAB: int | float
    PEN: int | float
    PGK: int | float
    PHP: int | float
    PKR: int | float
    PLN: int | float
    PYG: int | float
    QAR: int | float
    RON: int | float
    RSD: int | float
    RUB: int | float
    RWF: int | float
    SAR: int | float
    SBD: int | float
    SCR: int | float
    SDG: int | float
    SEK: int | float
    SGD: int | float
    SHP: int | float
    SLE: int | float
    SLL: int | float
    SOS: int | float
    SSP: int | float
    SRD: int | float
    STD: int | float
    SYP: int | float
    SZL: int | float
    THB: int | float
    TJS: int | float
    TMT: int | float
    TND: int | float
    TOP: int | float
    TRY: int | float
    TTD: int | float
    TWD: int | float
    TZS: int | float
    UAH: int | float
    UGX: int | float
    USD: int | float
    UYU: int | float
    UZS: int | float
    VEF: int | float
    VES: int | float
    VND: int | float
    VUV: int | float
    WST: int | float
    XAF: int | float
    XAG: int | float
    XAU: int | float
    XCD: int | float
    XDR: int | float
    XOF: int | float
    XPF: int | float
    YER: int | float
    ZAR: int | float
    ZMK: int | float
    ZMW: int | float
    ZWL: int | float


class CurrencyResponseModel(BaseModel):
    success: bool
    timestamp: int
    base: str
    date: str
    rates: Rates
