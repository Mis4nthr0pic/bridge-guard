import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

RPC_L1_ENDPOINT = os.getenv("HTTP_RPC_HH")
RPC_L1_NAME = os.getenv("WS_RPC_L1_NAME")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

def load_helper_abi():
    with open("src/abi.json") as abi_file:
        abi = json.load(abi_file)

    if(abi is None):
        self.logger.error("Helper abi not found for contract")  

    return abi