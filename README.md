[![Python application test with Github Actions](https://github.com/mozaloom/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/mozaloom/functions-from-zero/actions/workflows/main.yml)
# Functions From Zero

A Python toolkit demonstrating robust command-line applications with modular code organization. This repository includes tools for calculations, Wikipedia searches, logistics functions, and more.

## Overview

This repository contains Python modules and command-line interfaces that showcase:

- Modular code organization with a reusable library structure
- Command-line interfaces using Click and Fire
- RESTful API implementation using FastAPI
- Testing with pytest
- Docker containerization
- Makefile automation

## Project Structure

- **Core Libraries** (`mylib/`): Reusable Python modules
  - `calc.py`: Mathematical calculation functions
  - `bot.py`: Wikipedia scraping implementation
  - `logistics.py`: Logistics-related functions

- **Command-line Interfaces**:
  - `calcCli.py`: Calculator CLI using Click
  - `fireCli.py`: Wikipedia scraper CLI using Firebase
  - `logisticsCli.py`: Logistics CLI for distance calculations
  - `wikibot.py`: Wikipedia bot CLI

- **API Applications**:
  - `mainLogistics.py`: FastAPI implementation of logistics services

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/functions-from-zero.git
   cd functions-from-zero
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Calculation Tool
```bash
# Add two numbers
python calcCli.py add 5 10

# Subtract two numbers
python calcCli.py sub 10 5
```

### Wikipedia Bot
```bash
python wikibot.py --name "Python programming language"
```

### Logistics CLI
```bash
# List all available cities
python logisticsCli.py list_cities

# Find distance between two cities
python logisticsCli.py distance "New York" "Los Angeles"
```

### Logistics API
```bash
# Start the API server
python mainLogistics.py

# Example API call (using curl):
curl -X POST "http://localhost:8080/distance" \
  -H "Content-Type: application/json" \
  -d '{"city1":"New York", "city2":"Los Angeles"}'
```

### Docker Usage
```bash
# Build the Docker image
docker build -t functions-from-zero .

# Run container
docker run -p 127.0.0.1:8080:8080 <image_id>
```

## Testing

Run tests using pytest:
```bash
pytest
```

Or use the Makefile:
```bash
make test
```

## License

This project is licensed under the terms included in the LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.