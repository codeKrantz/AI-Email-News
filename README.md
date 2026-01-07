# AI Email News

A daily personalized email service that delivers curated news and updates based on user interests, powered by OpenAI's language models.

## Overview

AI Email News automatically compiles and sends personalized daily emails featuring news, articles, and updates tailored to your interests—including sports, hobbies, tech, business, and any other topics you care about. The service uses AI to intelligently curate and summarize content, delivering a concise, engaging digest straight to your inbox.

## Features

- **Personalized Content**: Customize your interests and preferences to receive relevant news
- **Daily Digests**: Automated daily email delivery at your preferred time
- **AI-Powered Summaries**: Smart content curation using OpenAI's language models
- **Multiple Interest Categories**: Support for sports, technology, business, entertainment, and more
- **Easy Setup**: Simple configuration with environment variables

## Tech Stack

- **Python 3.12+**: Core programming language
- **OpenAI API**: LLM for content generation and curation
- **SMTP/Gmail**: Email delivery service
- **python-dotenv**: Environment configuration management

## Installation

### Prerequisites

- Python 3.12 or higher
- Gmail account with app-specific password (for SMTP)
- OpenAI API key

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Email-News