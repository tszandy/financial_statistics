# set up python environment
python -m venv financial_py

# activate python environment
## mac
source financial_py/bin/activate
## windows
.\financial_py\Scripts\Activate.ps1

# install requirement
pip install -r requirements.txt
npm install

# export requirement
pip freeze > requirements.txt

# run list all stock
mkdir output
python src/list_all_stock.py

yf.Ticker("ticker")

https://www.google.com/finance/quote/ABBV:NYSE

# important field to look at
trailingPE
forwardPE
dividendRate
trailingAnnualDividendRate

regularMarketPrice

# analyze data
## mac
time_stamp=2025_08_14
input_path=output/output_${time_stamp}.json
output_path=output/output_${time_stamp}_partial_data.json
node src/filter_data.js -i $input_path -o $output_path -f trailingPE,forwardPE,dividendYield,trailingAnnualDividendYield

## windows
$time_stamp = "2025_08_15"
$input_path = "output/output_${time_stamp}.json"
$output_path = "output/output_${time_stamp}_partial_data.json"
node src/filter_data.js -i $input_path -o $output_path -f trailingPE,forwardPE,dividendYield,trailingAnnualDividendYield


Good Stock
    AES
    SYF
    DVN
    EIX
    CMCSA
    FANG

Bad Stock
    GM
    UAL
    F
    CNC
    HAL
    DAL
    MO

Don't know
    SYF
    PHM
    APA
    LEN
    HPE
    DHI
    ACGL
    GL
    NTRS
    VZ

TAP
HPQ
BG
OMC
EMN
UHS
EOG
RF
FOX
USB
NCLH
DFS
STT
TROW
APTV
TGT
MRK
NEM
CHTR
TRMB
FOXA
GIS
C
COP
BIIB
SLB
HBAN
MTB
VICI
FITB
PNC
IVZ
KHC
HIG
JPM
CF












# install direnv to turn on python environment when enter folder
brew install direnv

# Hook it into your shell
Add this to your ~/.bashrc or ~/.zshrc:
```
eval "$(direnv hook bash)"   # for bash
eval "$(direnv hook zsh)"
```

# Allow direnv to run it:
```
direnv allow
```

