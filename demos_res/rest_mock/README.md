# REST mock

This directory contains a very simple python package mocking a REST API.

Example of usage from a demo app directory:

```python
import sys

sys.path.insert(0, "../../..")
import demos_res.rest_mock.rest_mock as rest_mock

users = rest_mock.get_users()
```
