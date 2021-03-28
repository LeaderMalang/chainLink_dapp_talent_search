
# Chainlink Fun
CCNdfBaV9z6/dG7vPjZ5uFjvddJs6rxN
> Learn about chainlink by working through basic examples.

## Deploy Chainlink Node

### Run with Docker

#### Requirements
- Install [Docker](https://docs.docker.com/get-docker/)
- Install [Postgres](https://www.postgresql.org/)
- Create an [Infura](https://infura.io/) account
  - Click the `Projects` section and create a new project.
  - In the `KEYS` section you will see a list of different credentials. Under `ENDPOINTS` tab change the select to `Ropsten`.
  - Underneath this you will have two links. Notice the `wss://ropsten.infura.io/ws/v3/...` link. You will need this in a second

#### Running the Node
- Run `cd run-node`
- Open the .env file and where `ETH_URL=INFURA_ROPSTEN_LINK_HERE` is paste your infura link.

- Create `$PATH_TO_DIR/chainlink-volume` directory
- Create `$PATH_TO_DIR/chainlink-volume/password.txt` - Password used within Chainlink node for access
Add the following:
```
secret
```
- Create `$PATH_TO_DIR/chainlink-volume/apicredentials.txt` - Credientials to login into the Chainlink UI
Add the following:
```
test@test.tech
chainlinkPassword
```

- Add shared paths to Docker
  - Docker -> Preferences -> Resources -> File Sharing
  - Add `$PATH_TO_DIR/chainlink-volume`
  - Add `$PATH_TO_POSTGRES_DATA`
- Run `docker-compose up` - This will run our docker-compose.yml and spin up a Postgres/Chainlink node instance.
- This will run our Postgres instance but fail when starting the Chainlink node because there is no `chainlink` postgres database created. We can solve this by entering the CLI of our Postgres(`pg_chainlink`) instance inside Docker.
- Open the Docker dashboard and click on `chainlink-ropsten` then open the CLI for `chainlink-ropsten_database_1`.
- Enter the Postgres console by typing: `psql -U postgres -h localhost`
- Now create the database: `CREATE DATABASE chainlink;`
- Run `docker-compose up` once again and your Chainlink node should be running as expected.
- Goto: `http://localhost:6688` and you will be greeted with a login page.
- Type in the credentials specified in your `apicredentials.txt` file and boom! You are logged into your locally running Chainlink node.
- You can locate your account address by clicking on the `Configuration` tab in the top right corner and locating the ACCOUNT_ADDRESS key variable.
- From here you should fund your address LINK and ETH. You can do that by copying your account address and going to the [LINK ropsten faucet](https://ropsten.chain.link/) and [ETH ropsten faucet](https://faucet.ropsten.be/).
=======
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
