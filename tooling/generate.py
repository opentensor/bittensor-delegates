import json

from bittensor import Keypair

name = input("Your validator's descriptive name (e.g. Opentensor Foundation):\n")
url = input("Your validator url (e.g. www.opentensor.org ) [Optional]:\n")
description = input(
    "A short description for your validator ( e.g. Build, maintain and advance Bittensor):\n"
)
mnemonic = input(
    "The mnemonic of your validator's hotkey "
    "( default location: ~/.bittensor/wallets/<coldkey>/hotkeys/<validator> )\n"
)

keypair = Keypair.create_from_mnemonic(mnemonic)
delegates_entry = dict()
delegates_entry[keypair.ss58_address] = {
    "name": name,
    "url": url,
    "description": description,
}

message = json.dumps(delegates_entry)
signature = keypair.sign(data=message)
delegates_entry[keypair.ss58_address]["signature"] = signature.hex()

print(f"Adding entry: {delegates_entry}")
with open("public/delegates.json", "r") as fh:
    delegates = json.loads(fh.read())

delegates.update(delegates_entry)

with open("public/delegates.json", "w") as fh:
    fh.write(json.dumps(delegates))
print("Success. Submit these changes as PR at https://github.com/opentensor/bittensor-delegates")
