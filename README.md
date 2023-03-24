# bittensor-delegates

## Update delegates.json process

### 2023-03-23 - First version

1. Execute tooling/generate.py and follow the prompts:
```shell
$ python tooling/generate.py
Your validator's descriptive name (e.g. Opentensor Foundation):
Openτensor Foundaτion

Your validator url (e.g. www.opentensor.org ) [Optional]:
https://opentensor.ai/

A short description for your validator ( e.g. Build, maintain and advance Bittensor):
Founded, maintain and advance Bittensor

The mnemonic of your validator's hotkey ( default location: ~/.bittensor/wallets/<coldkey>/hotkeys/<validator> )
das ist mir wurst
```

2. This will automatically update `public/delegates.json` with your information. You may then 
open a PR with your changes
    1. An example of an [opened PR](https://github.com/opentensor/bittensor-delegates/pull/5) .
3. If all of the checks pass, you may request a review and your delegates will be added to the list.