#!/bin/bash
KROKI_VERSION=0.5.0

wget -O /tmp/kroki.tar.gz https://github.com/yuzutech/kroki-cli/releases/download/v${KROKI_VERSION}/kroki-cli_${KROKI_VERSION}_linux_amd64.tar.gz
tar -xvzf /tmp/kroki.tar.gz
chmod +x kroki