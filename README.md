# BC Wine AI Agents

AI-powered wine search and recommendation agents for British Columbia wines, built with LangGraph.

## Overview

This project provides intelligent agents that search and analyze BC wine data from [WineAlign](https://www.winealign.com), Canada's leading wine review platform. The agents retrieve wine information including critic scores, tasting notes, pricing, and drink windows to help users discover and evaluate BC wines.

## Features

- **WineAlign Search** - Full-text search across WineAlign's wine database with pagination support
- **Critic Reviews** - Detailed critic reviews including scores, tasting notes, value ratings, and drink windows
- **Session Management** - Automatic login and session handling with cookie-based authentication
- **Auto Re-login** - Transparent session recovery on expiry without interrupting searches
- **LangGraph Integration** - Formatted output designed for LLM consumption in LangGraph agent workflows

## Project Structure

```
BC-wine-ai-agents/
├── winealign_tool.py   # WineAlign search tool with scraping and session management
├── .env                # Environment variables (not tracked in git)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Setup

### Prerequisites

- Python 3.11+
- A WineAlign account (for authenticated search)

### Installation

```bash
# Clone the repository
git clone https://github.com/SUM-AI-ca/BC-wine-ai-agents.git
cd BC-wine-ai-agents

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install httpx beautifulsoup4 pydantic python-dotenv
```

### Environment Variables

Create a `.env` file in the project root:

```
WINEALIGN_EMAIL=your_email@example.com
WINEALIGN_PASSWORD=your_password
```

## Usage

### Standalone Test

```bash
python winealign_tool.py
```

This runs a sample search for "storm haven" and prints formatted results with critic reviews.

### As a LangGraph Tool

```python
from winealign_tool import search_winealign, format_results

# Search with reviews
results = await search_winealign(
    query="pinot noir okanagan",
    max_pages=3,
    include_reviews=True,
)

# Format for LLM consumption
output = format_results(results, "pinot noir okanagan")
```

### API Reference

#### `search_winealign(query, max_pages=3, include_reviews=True)`

Search WineAlign with pagination and optional critic reviews.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | `str` | required | Search term (wine name, winery, varietal) |
| `max_pages` | `int` | `3` | Max pages to fetch (10 results per page) |
| `include_reviews` | `bool` | `True` | Fetch each wine's detail page for critic reviews |

Returns: `list[WineAlignResult]`

#### `get_wine_reviews(wine_url)`

Fetch critic reviews for a single wine by its WineAlign URL.

| Parameter | Type | Description |
|-----------|------|-------------|
| `wine_url` | `str` | Full WineAlign wine detail URL |

Returns: `list[CriticReview]`

### Data Models

#### `WineAlignResult`

| Field | Type | Description |
|-------|------|-------------|
| `wine_name` | `str` | Name of the wine |
| `appellation` | `str \| None` | Wine region/appellation |
| `score` | `str \| None` | Aggregate score from search results |
| `price` | `str \| None` | Listed price |
| `url` | `str \| None` | WineAlign detail page URL |
| `thumbnail_url` | `str \| None` | Bottle thumbnail image URL |
| `critic_reviews` | `list[CriticReview]` | List of critic reviews |

#### `CriticReview`

| Field | Type | Description |
|-------|------|-------------|
| `critic_name` | `str` | Name of the critic |
| `score` | `str \| None` | Critic's score |
| `tasting_notes` | `str \| None` | Detailed tasting notes |
| `value_rating` | `int \| None` | Value rating (0-5 stars) |
| `drink_window` | `str \| None` | Recommended drink window (e.g., "Drink 2025-2032") |

## Tech Stack

- **[httpx](https://www.python-httpx.org/)** - Async HTTP client with cookie/session support
- **[BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/)** - HTML parsing and scraping
- **[Pydantic](https://docs.pydantic.dev/)** - Data validation and serialization
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management
- **[LangGraph](https://langchain-ai.github.io/langgraph/)** - Agent orchestration framework

## License

This project is proprietary to SUM AI.
