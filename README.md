# Bittensor Delegates
***
This repository maintains and tracks a list of delegates for the Bittensor network.

### Update delegates.json process
Note: This is a separate repository from bittensor and you must execute the scripts from here
(that is, *not* from the bittensor repository.)

For general guidance on how to clone and submit your changes see Github's official documentation:

* [How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
* [How to submit a PR from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

### 2023-03-23 - First version
***

1. From this repository, execute tooling/generate.py and follow the prompts:
```
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
open a PR with your changes:
    1. An example of an [opened PR](https://github.com/opentensor/bittensor-delegates/pull/5) .
3. If all of the checks pass, you may request a review and your delegates will be added to the list.
