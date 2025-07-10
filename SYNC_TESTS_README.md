# Sync Logic Test Scripts

This directory contains test scripts for validating the auto-patch deploy workflow sync logic without executing actual API calls.

## Scripts

### test_sync_logic.py
Comprehensive test suite that validates all components of the sync workflow:
- JSON configuration loading
- Base64 encoding of private information
- GitHub API branch creation command construction
- GitHub API file upload command construction
- Subprocess call mocking to prevent actual execution

### sync_test.py  
Simplified test script that closely mirrors the original sync logic format while preventing actual API execution through mocking.

## Usage

Both scripts run silently and execute without output as requested:

```bash
# Run comprehensive test suite
python3 test_sync_logic.py

# Run simplified test
python3 sync_test.py

# Both can also be run as executables
./test_sync_logic.py
./sync_test.py
```

## Features

- **No actual API calls**: All subprocess calls are mocked to prevent real GitHub API interactions
- **Silent execution**: Scripts run without producing any log output
- **Comprehensive testing**: Validates all aspects of the sync workflow
- **Safe testing**: Uses temporary files and proper cleanup

## Security

The scripts use mock data and do not require actual security.json files. The .gitignore file excludes security.json to prevent accidental commits of sensitive information.