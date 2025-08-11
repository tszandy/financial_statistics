# set up python environment
python -m venv financial_py

# activate python environment
source financial_py/bin/activate

# install requirement
pip install -r requirements.txt

# export requirement
pip freeze > requirements.txt

# run list all stock
python src/list_all_stock.py

yf.Ticker("ticker")

https://www.google.com/finance/quote/ABBV:NYSE

# important field to look at
trailingPE
forwardPE
dividendRate
trailingAnnualDividendRate

regularMarketPrice

input_path=output/output_2025_06_26.json
output_path=output/output_2025_06_26_partial_data.json
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
