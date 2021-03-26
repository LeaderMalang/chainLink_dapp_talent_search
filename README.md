# Chainlink Python  External Adapter 

This template shows a basic usecase of an external adapter written in Python for the CryptoCompare API. It can be ran locally.

## Install

```
pipenv install
```

## Test

```
pipenv run pytest
```

##run 
````
python app.py
````

##curl request to test 
``````
curl -X POST \
  http://0.0.0.0:8060/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 16ce459e-1fb1-f864-5e1e-f144bfa24357' \
  -d '{"id": "dada", "data": {"base": "ETH", "quote": "USD"}}
  '
``````
