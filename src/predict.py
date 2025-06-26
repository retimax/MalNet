def get_malicious_process(df, y_pred_proba, threshold=0.9, le_dict=None):
    print("\n---------------------Results-------------------------")

    df = df.copy()
    df["malicious_prob"] = y_pred_proba

    suspicious = df[df["malicious_prob"] >= threshold]
    suspicious = suspicious.sort_values("malicious_prob", ascending=False)

    if le_dict and "ImageFileName" in le_dict:
        suspicious["ImageFileName"] = le_dict[
            "ImageFileName"
        ].inverse_transform(suspicious["ImageFileName"])

    print("Most suspicious processes:")
    print(suspicious[["ImageFileName", "malicious_prob"]].head(10))

    return suspicious
