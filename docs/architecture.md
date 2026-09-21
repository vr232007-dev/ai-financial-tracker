# System Architecture

## 1. Purpose

This document describes the high-level architecture of the AI-Powered Personal Financial Health & Expense Tracker.

The architecture defines the major components of the system, their responsibilities, and how they communicate with each other.

The system follows a layered architecture consisting primarily of:

- React + Vite frontend
- FastAPI backend
- PostgreSQL database
- ML/Data Science layer
- Authentication and security mechanisms
- External services where required

The architecture is designed to keep the system modular, secure, understandable, and suitable for incremental development.

---

## 2. High-Level Architecture

```text
                          ┌─────────────────────┐
                          │        USER         │
                          └──────────┬──────────┘
                                     │
                                     │ interacts through browser
                                     ▼
                          ┌─────────────────────┐
                          │   REACT + VITE      │
                          │      FRONTEND       │
                          │                     │
                          │ UI, forms, charts,  │
                          │ dashboards          │
                          └──────────┬──────────┘
                                     │
                                     │ HTTP requests / JSON
                                     │
                                     ▼
                    ┌─────────────────────────────────┐
                    │        FASTAPI BACKEND          │
                    │                                 │
                    │ Authentication / Authorization  │
                    │ Input Validation                │
                    │ Business Logic                  │
                    │ API Routes                       │
                    │                                 │
                    │ Routes requests to DB / ML      │
                    └──────────────┬──────────┬───────┘
                                   │          │
                         SQL / ORM │          │ ML function calls
                                   │          │
                                   ▼          ▼
                    ┌──────────────────┐  ┌─────────────────────┐
                    │    POSTGRESQL    │  │   ML / DATA-SCIENCE │
                    │     DATABASE     │  │       LAYER         │
                    │                  │  │                     │
                    │ Users            │  │ Categorization      │
                    │ Accounts         │  │ Prediction          │
                    │ Transactions     │  │ Anomaly Detection  │
                    │ Budgets          │  │                     │
                    │ Goals            │  │ Future ML modules   │
                    │ Investments      │  │                     │
                    └──────────────────┘  └─────────────────────┘
                                   ▲
                                   │
                                   │
                    ┌──────────────┴───────────────┐
                    │      EXTERNAL SERVICES       │
                    │                              │
                    │ Future market data, external │
                    │ integrations, etc.           │
                    └──────────────────────────────┘
```

### Core architectural rule

The frontend does **not** connect directly to PostgreSQL.

All requests go through the FastAPI backend.

The backend is responsible for authentication, authorization, validation, business rules, database access, and communication with the ML layer.

---

## 3. Component Responsibilities

| Component | Responsibility |
|---|---|
| React + Vite Frontend | Provides the user interface, forms, dashboards, charts, and user interactions |
| FastAPI Backend | Provides APIs, authentication, authorization, validation, business logic, and coordination between components |
| PostgreSQL Database | Stores persistent application data such as users, accounts, transactions, budgets, goals, and investments |
| ML/Data Science Layer | Provides machine-learning functionality such as transaction categorization, prediction, and anomaly detection |
| Authentication/Security | Protects user accounts and ensures users can access only authorized financial information |
| External Services | Provide information or functionality that may come from outside the application, such as future market-data integrations |

---

## 4. Why the Frontend Does Not Connect Directly to the Database

The frontend runs in the user's browser, so database credentials and unrestricted database access must not be exposed to it.

Instead, the frontend communicates with the FastAPI backend.

The backend can then:

1. Authenticate the user.
2. Check authorization.
3. Validate incoming data.
4. Apply business rules.
5. Access the database securely.
6. Return only the required information to the frontend.

This provides better security and control over financial data.

---

## 5. Example Request Flow: Adding an Expense

Consider a user entering an expense of ₹250 under the Food category.

### Step 1 — User

The user enters:

```text
Amount: ₹250
Category: Food
Date: 2026-09-19
```

and clicks **Add Expense**.

### Step 2 — Frontend

The React application collects the form information and sends an HTTP `POST` request to the backend.

Example JSON:

```json
{
  "amount": 250,
  "category": "Food",
  "date": "2026-09-19"
}
```

The frontend performs basic UI checks, but the backend performs the actual validation.

### Step 3 — Backend

FastAPI receives the request.

The backend performs:

- Authentication check
- Authorization check
- Input validation
- Business logic

For example, it verifies that the amount is positive and that the request belongs to the authenticated user.

If budgeting is implemented, the backend may also determine whether this expense affects the user's current budget.

### Step 4 — Database

After successful validation, the backend sends the appropriate database operation to PostgreSQL.

The transaction is stored and associated with the correct user and financial account.

### Step 5 — Database Response

PostgreSQL confirms that the transaction was successfully created and returns the stored record information to the backend.

### Step 6 — Backend Response

The backend sends a JSON response to the frontend.

Example:

```json
{
  "id": 42,
  "amount": 250,
  "category": "Food",
  "date": "2026-09-19"
}
```

### Step 7 — Frontend Update

The React application receives the response and updates the transaction list.

The user can see the new expense without manually refreshing the page.

---

## 6. Where the ML Layer Fits

Machine learning is not required for every operation in the application.

During the initial MVP, users can manually select expense categories and the backend can use normal business logic.

Later, the backend can call ML functionality when required.

For example:

```text
User enters transaction
        ↓
React Frontend
        ↓
FastAPI Backend
        ↓
ML categorization function
        ↓
Predicted category
        ↓
Backend validation/business logic
        ↓
PostgreSQL
```

The ML layer is therefore available as a specialized component rather than being involved in every request.

---

## 7. Mapping Major Features to the Architecture

| Feature | Main Component(s) | Initial Approach |
|---|---|---|
| Manual expense entry | Frontend + Backend + Database | Standard CRUD operation |
| AI transaction categorization | Backend + ML | ML prediction called by backend |
| SMS/UPI parsing | Backend + ML | Parse transaction information and classify when required |
| Budgeting | Backend + Database | Business rules and calculations |
| Adaptive budget recommendations | Backend + ML/Data Analysis | Analyze historical spending and recommend budgets |
| Future expense prediction | Backend + ML + Database | Use historical transactions for prediction |
| Anomaly detection | Backend + ML + Database | Detect unusual transactions and store anomaly information |
| Financial goals | Frontend + Backend + Database | Goal tracking and calculations |
| Investment tracking | Frontend + Backend + Database | Store and manage investment information |
| Net-worth dashboard | Backend + Database + Frontend | Aggregate assets and liabilities |
| Financial education | Backend + Frontend | Provide relevant educational content |
| Family/shared finances | Backend + Database + Authentication | Requires authorization and shared-access rules |
| Offline mode | Frontend + Local Storage | Support local data handling and later synchronization |
| Privacy controls | Backend + Authentication + Database | Protect and restrict financial data |

---

## 8. Data Flow Principle

The general data flow of the application is:

```text
User
  ↓
Frontend
  ↓
Backend/API
  ↓
Validation + Authentication + Business Logic
  ↓
Database / ML / External Services
  ↓
Backend
  ↓
Frontend
  ↓
User
```

The backend acts as the central coordination layer.

---

## 9. Architectural Decisions

### No Direct Frontend-to-Database Connection

The frontend communicates with the backend rather than directly accessing PostgreSQL.

This protects database credentials and allows the backend to enforce authorization, validation, and business rules.

### No Microservices for the Initial Project

The project will initially use a modular backend rather than multiple independently deployed services.

A microservices architecture would introduce additional complexity such as service-to-service communication, deployment management, and monitoring.

For a student project of this scale, a modular monolithic backend is sufficient.

### No Message Queue Initially

Technologies such as Kafka or RabbitMQ are not required for the initial implementation.

Direct function calls are sufficient for the expected scale of this project.

If the system were later deployed at significantly larger scale, these technologies could be reconsidered.

### ML Is Added Incrementally

The ML layer will not be required for the initial MVP.

Manual categorization and rule-based functionality can be implemented first.

ML functionality can then be added to the architecture when the required transaction data becomes available.

---

## 10. Architecture and Project Development

The architecture supports incremental development.

The initial system can begin with:

```text
React
  ↓
FastAPI
  ↓
PostgreSQL
```

Then additional capabilities can be added:

```text
React
  ↓
FastAPI
  ├── PostgreSQL
  ├── ML/Data Science
  └── External Services
```

This allows the project to remain manageable while gradually adding advanced financial intelligence.

---

## 11. Summary

The system follows a layered and modular architecture.

The frontend is responsible for user interaction, the backend is responsible for APIs and business logic, PostgreSQL is responsible for persistent data storage, and the ML layer provides specialized predictive and classification capabilities.

The backend acts as the central coordination layer between these components.

This architecture provides a clear separation of responsibilities and allows the application to evolve from a basic financial tracker into an AI-powered financial intelligence platform without unnecessarily complicating the initial implementation.