FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV RUNNER_VERSION=2.311.0
ENV RUNNER_ALLOW_RUNASROOT=1

# Switch to root to install packages
USER root

# Install essential packages
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    jq \
    iputils-ping \
    net-tools \
    sudo \
    unzip \
    wget \
    zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
    && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
    && apt-get update && apt-get install -y terraform \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user if not exists and add to sudoers
RUN id -u vscode &>/dev/null || (useradd -m -s /bin/bash -u 1000 vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode)

# Set up the GitHub Actions Runner for the vscode user
WORKDIR /home/vscode
USER vscode

# Create actions-runner directory
RUN mkdir -p /home/vscode/actions-runner && cd /home/vscode/actions-runner

# Download the GitHub Actions runner
RUN cd /home/vscode/actions-runner \
    && curl -o actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && rm actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz

# Create start script that will be executed by postStartCommand
RUN echo '#!/bin/bash\n\
cd /home/vscode/actions-runner\n\
\n\
# Wait for configuration\n\
while [ ! -f ".credentials" ] && [ ! -f ".runner" ]; do\n\
  echo "Waiting for runner configuration..."\n\
  sleep 5\n\
done\n\
\n\
# Start the runner\n\
./run.sh\n\
' > /home/vscode/actions-runner/start.sh \
    && chmod +x /home/vscode/actions-runner/start.sh

# Switch back to root for any remaining operations
USER root

# Add a note about configuration
RUN echo "GitHub Actions Runner installed. Configure with: ./config.sh --url <REPO_URL> --token <TOKEN>" > /home/vscode/actions-runner/README.txt

# Set permissions
RUN chown -R vscode:vscode /home/vscode/actions-runner

# Configure environment for VS Code extensions
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to vscode user for default operations
USER vscode
WORKDIR /home/vscode

# Note: The extensions and features specified in devcontainer.json will be installed by VS Code
# when the container starts. This Dockerfile just ensures the prerequisites are available.