# 🔗 linkScribe - AI-Powered Web Content Preview

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)](https://docker.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?logo=xgboost&logoColor=white)](https://xgboost.ai)

**Instantly understand web content before clicking!**  
linkScribe uses machine learning to analyze webpages and generate:
- Topic classification
- Content summaries
- Insightful previews


## 🚀 Key Features
- **Intelligent Content Analysis**  
  Classifies webpage subjects using optimized ML models
- **Multi-Model Comparison**  
  Tests 5 classifiers to ensure accurate predictions
- **Instant Preview Generation**  
  Creates concise summaries of web content
- **Dockerized Deployment**  
  Single-command setup for seamless execution
- **API-First Architecture**  
  Fully documented REST endpoints for integration

## 🧩 Tech Stack
### Core Components
| Component       | Technology              |
|-----------------|-------------------------|
| **Frontend**    | Streamlit               |
| **Backend**     | FastAPI + Uvicorn       |
| **ML Framework**| Scikit-learn, XGBoost   |
| **Scraping**    | BeautifulSoup, Requests |
| **Deployment**  | Docker, Docker Compose  |

### Machine Learning Models
| Model                     | Implementation          | 
|---------------------------|-------------------------|
| Support Vector Machine    | `sklearn.svm.SVC`       |
| Decision Tree             | `sklearn.DecisionTreeClassifier` |
| Random Forest             | `sklearn.RandomForestClassifier` | 
| AdaBoost                  | `sklearn.AdaBoostClassifier` |
| XGBoost                   | `xgboost.XGBClassifier` |

## 🛠️ Installation
Prerequisites

    Docker Engine ≥ 20.10

    Docker Compose ≥ 2.17

Setup

# Clone repository
  git clone https://github.com/AIJDprojects/linkScribe.git

  cd linkScribe

# Build and launch containers
docker-compose up --build

## ⚙️ System Architecture
```mermaid
graph TB
    A[User] --> B[Streamlit Frontend]
    B --> C[FastAPI Backend]
    C --> D{Web Scraping}
    D --> E[Content Processing]
    H --> F[ML Classification]
    E --> G[Preview]
    G --> B
    F --> B
    E --> H[Model Service]


