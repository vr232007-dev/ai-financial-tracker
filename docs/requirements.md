# Requirements — AI Financial Health & Expense Tracker

## 1. Overview

An all-in-one financial tracker that helps students, young professionals, and
working-class users easily track, understand, and improve their spending,
budgeting, and financial goals — without needing to be a finance expert.

## 2. User Stories (MVP)

1. As a student managing my own and my family's money, I want to log a daily
   expense in just a few taps, so that I capture spending accurately without
   it feeling like a chore.

2. As a student trying to build financial discipline, I want to see a clear
   summary of my spending by category and over time, so that I can recognize
   patterns and make more responsible decisions.

3. (Deferred — post-MVP) As someone who helps manage a family member's
   finances, I want to view and record expenses on behalf of another
   person's account, so that I can help them track spending without them
   needing to use the app themselves.

## 3. Non-Functional Requirements

- Security: passwords hashed (bcrypt/argon2), no secrets in source control
- Performance: API responses under ~500ms for basic CRUD
- Usability: expense entry achievable in under ~15 seconds
- Privacy: no bank credentials stored; minimal data collection

## 4. Feature Prioritization (MoSCoW)

| Feature | Priority |
|---|---|
| Manual expense entry | Must |
| Authentication (login/signup) | Must |
| Multiple accounts | Must |
| Budgeting | Should |
| Charts/analytics | Should |
| Financial goals | Should |
| AI categorization | Could |
| Future expense prediction | Could |
| Fraud/anomaly detection | Could |
| Investment tracking | Could |
| Net worth dashboard | Could |
| Financial education | Could |
| UPI/SMS parsing | Could |
| Indian-language parsing | Won't (for now) |
| Offline-first | Won't (for now) |
| Family/shared finances | Won't (for now) |
| Adaptive/predictive budgets | Won't (for now) |