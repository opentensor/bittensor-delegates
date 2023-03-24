import json
from binascii import unhexlify

from bittensor import Keypair

with open("public/delegates.json", "r") as fh:
    information_dict = json.loads(fh.read())

for hotkey, delegate_info in information_dict.items():
    if "signature" not in delegate_info.keys():
        raise ValueError(f"No signature found for {delegate_info['name']} ({hotkey=})")

    keypair = Keypair(ss58_address=hotkey)
    signature = delegate_info["signature"].encode()

    del delegate_info["signature"]
    information_str = json.dumps({hotkey:delegate_info})

    if not keypair.verify( data = information_str, signature = unhexlify( signature ) ):
        raise ValueError(f"Invalid signature for {delegate_info['name']} ({hotkey=})")
