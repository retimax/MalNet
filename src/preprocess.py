import json
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_json(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return [data]
            else:
                print(f"[!] Formato no reconocido en: {path}")
                return []
    except FileNotFoundError:
        print(f"[!] Archivo no encontrado: {path}")
        return []
    except json.JSONDecodeError:
        print(f"[!] JSON inválido: {path}")
        return []


def load_and_tag(clean_path, malware_path):
    clean = load_json(clean_path)
    malware = load_json(malware_path)

    for item in clean:
        item["infested"] = 0
    for item in malware:
        item["infested"] = 1

    all_data = clean + malware
    return pd.DataFrame(all_data)


def label_encoder(df):
    label_columns = [
        "ExitTime",
        "File output",
        "Handles",
        "ImageFileName",
        "Wow64",
        "__children",
        "CreateTime",
        "SessionId",
    ]

    le_dict = {}

    for col in label_columns:
        if col in df.columns:
            df[col] = df[col].astype(str)
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            le_dict[col] = le

    return df, le_dict
