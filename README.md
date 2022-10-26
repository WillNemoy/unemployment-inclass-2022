# unemployment-inclass-2022
In class exercise for OPIM 244 on 10/24/2022



## Setup

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```



## Usage

Run an example script report:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python app/unemployment.py

#or pass API key from the command line
ALPHAVANTAGE_API_KEY="_______" python app/unemployment.py
```