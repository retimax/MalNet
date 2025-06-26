# MalNet

**MalNet** is a neural network-based malware detection system that classifies potentially malicious processes based on behavioral JSON data.

Built with [Tensorflow](https://github.com/tensorflow/tensorflow) and [scikit-learn](https://github.com/scikit-learn/scikit-learn), this project provides a simple yet effective baseline for analyzing process metadata and identifying anomalies.

## Features
- Binary classification of processes: benign vs. malicious
- Input format: structured JSON logs
- Uses LabelEncoder + StandardScaler + Fully Connected Neural Net
- Outputs suspicious processes with probability scores
- Modular structure, easy to extend and reuse

## Getting Started
### 1. Clone this repository to your local machine:
```
git clone https://github.com/retimax/MalNet.git
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your data
Place your files under `data/`:
- `clean.json`: contains legitimate process entries.
- `malware.json`: contains malicious process entries.
- Each file should contain a list of dictionaies describing individual processes.

You can get this files with multiple tools, i recommend you to use [Volatility3](https://github.com/volatilityfoundation/volatility3), just have to get a memory dump in raw format and pass it through Volatility3 to get the needed JSON file.
```
vol -f <memdump.raw> -r json windows.pslist > /path/to/data/malware/clean.json
```

### 4. Running the model
Train from scratch:
```
python src/main.py
```
**Output:**
- A trained model saved to `models/malware_model.keras`
- Console output with top suspicious processes

#### Sample output
```
---------------------Results-------------------------
Most suspicious processes:
      ImageFileName  malicious_prob
197  GoogleCrashHan        0.984778
222  GoogleUpdate.e        0.978224
214     firefox.exe        0.962982
187     audiodg.exe        0.961986
182  VBoxService.ex        0.961883
210    WmiApSrv.exe        0.958958
180         lsm.exe        0.958238
178    services.exe        0.955485
211    WmiPrvSE.exe        0.955432
177    winlogon.exe        0.951079
```

## Contributing
If you want to contribute to this project, please open an issue or create a pull request.
