# bittensor-delegates

## Update delegates.json process

### 2023-03-23 - First version

1. Execute tooling/generate.py
1. Update public/delegates.json file
1. Open a PR with your changes
    1. An example of an [opened PR](https://github.com/opentensor/bittensor/pull/1211) with a signature created by `tooling/generate.py`.
    1. At this point the output of the script is commented in the PR as follows:
    ```
    Verified True
    Validator information: 
    {
        "5DnWFhKfeu6gXMydzrv8bkwxFegAC6bMWsC4Z2XtaotAeB6S": 
        {
            "name": "Bittensor Greece", 
            "url": "", 
            "description": "The Greek / Cypriot validator supporting the development of decentralised AI"
        }
    }
    Validator signature: ee8df5360eb641bd91a38da9d8b6dda36a39302c9bba7babf5d7eb16f6e9f73321aeb6f8adb30e0f511d64c1f35caa15215dd280fb2ed3f8f5b09d783cc9958f
    ```
1. Reviewers will verify the added information with `tooling/verify.py` and specially they will verify validator's signature.