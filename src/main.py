from model import train_model
from predict import get_malicious_process
from preprocess import label_encoder, load_and_tag


def main():
    df = load_and_tag("data/clean.json", "data/malware.json")
    df, le_dict = label_encoder(df)
    history, model, y_pred_proba = train_model(df)
    get_malicious_process(df, y_pred_proba, threshold=0.9, le_dict=le_dict)


if __name__ == "__main__":
    main()
