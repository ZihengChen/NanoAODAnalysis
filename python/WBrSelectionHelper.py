

def get_config(year, isData):
    if year == "2016":
        cfg = {
            "elTrg": "Ele27_WPTight_Gsf",
            "muTrg": "IsoMu24",
            "cutEl1Pt":30, "cutEl2Pt":20, 
            "cutMu1Pt":25, "cutMu2Pt":10,
            "cutDeepCSVL": 0.2217,
            "cutDeepCSVM": 0.6321,
            "cutDeepCSVT": 0.8953,
            }

    elif year == "2017":
        cfg = {
            "elTrg": "Ele35_WPTight_Gsf",
            "muTrg": "IsoMu27",
            "cutEl1Pt":38, "cutEl2Pt":20, 
            "cutMu1Pt":30, "cutMu2Pt":10,
            "cutDeepCSVL": 0.1522,
            "cutDeepCSVM": 0.4941,
            "cutDeepCSVT": 0.8001,
            }

    elif year == "2018":
        cfg = {
            "elTrg": "Ele32_WPTight_Gsf",
            "muTrg": "IsoMu24",
            "cutEl1Pt":35, "cutEl2Pt":20, 
            "cutMu1Pt":25, "cutMu2Pt":10,
            "cutDeepCSVL": 0.1241,
            "cutDeepCSVM": 0.4184,
            "cutDeepCSVT": 0.7527,
            }
    return cfg