import json
from binascii import unhexlify

from bittensor import Keypair

with open("public/delegates.json", "r") as fh:
    information_dict = json.loads(fh.read())

failure_count = 0
for hotkey, delegate_info in information_dict.items():
    if "signature" not in delegate_info.keys():
        raise ValueError(f"No signature found for {delegate_info['name']} ({hotkey=})")

    try:
        keypair = Keypair(ss58_address=hotkey)
        signature_bytes = bytes.fromhex(delegate_info["signature"])

        del delegate_info["signature"]
        information_str = json.dumps({hotkey: delegate_info})

        if not keypair.verify(data=information_str, signature=signature_bytes):
            print(f"Invalid signature for {delegate_info['name']} ({hotkey=})")
            failure_count += 1
    except Exception as e:
        print(f"Error verifying {delegate_info['name']} ({hotkey=}): {e}")
        failure_count += 1

if failure_count > 0:
    print(f"Total failures: {failure_count}")
    exit(1)
else:
    print("All signatures are valid")
    exit(0)
