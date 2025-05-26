# Scalable Chat System

A production-ready, scalable chat system built with Python (FastAPI), PostgreSQL, Redis, and Amazon S3. Designed for millions of users, with separate REST and WebSocket services for optimal performance and scalability.

---

## **Architecture Overview**

### **Core Components**

- **REST API Service:** Handles all HTTP requests (user management, sending/fetching messages, chat room management, media URL generation).
- **WebSocket Gateway:** Manages persistent WebSocket connections for real-time message delivery and notifications.
- **PostgreSQL:** Stores all persistent data (users, messages, chat rooms, media references).
- **Redis:** Used for Pub/Sub (real-time message propagation), caching, and ephemeral data (presence, typing status).
- **Amazon S3:** Stores media files (images, videos, attachments) and serves them via pre-signed URLs.
- **Worker Service (optional):** Handles background jobs (media processing, notifications, analytics).
- **Load Balancers:** Layer 7 (API Gateway) for REST, Layer 4 (TCP) for WebSocket.

---

## **Data Access Pattern**

Below is a diagram and explanation of how data flows from the client to all backend components.

```
+-------------------+         +-------------------+         +-------------------+
|                   |  HTTP   |                   |  SQL    |                   |
|      Client       +-------->+   REST API        +-------->+   PostgreSQL      |
|  (Web/Mobile)     |         |   Service         |         |   (Database)      |
|                   |         |                   |         |                   |
+-------------------+         +-------------------+         +-------------------+
         |                            |   ^                          ^
         |                            |   |                          |
         |                            |   |                          |
         |                            v   |                          |
         |                        +-------------------+              |
         |                        |                   |              |
         |                        |      Redis        |<-------------+
         |                        |   (Pub/Sub,       |
         |                        |    Cache,         |
         |                        |    Presence)      |
         |                        +-------------------+
         |                            ^
         |                            |
         |   WebSocket                |
         +--------------------------> |
                                      |
                             +-------------------+
                             |                   |
                             | WebSocket Gateway |
                             |   Service         |
                             +-------------------+
                                      |
                                      v
                             +-------------------+
                             |                   |
                             |   Amazon S3       |
                             | (Media Storage)   |
                             +-------------------+
```

---

### **Data Flow Explanation**

- **REST API Service**
  - Handles all HTTP requests (user registration, login, sending messages, fetching chat history, generating S3 URLs).
  - Reads/writes persistent data to PostgreSQL.
  - Publishes new messages/events to Redis for real-time delivery.

- **WebSocket Gateway**
  - Maintains persistent WebSocket connections with clients.
  - Subscribes to Redis Pub/Sub channels to receive new messages/events.
  - Pushes real-time updates (messages, notifications, presence) to connected clients.

- **Redis**
  - Acts as a message broker (Pub/Sub) between REST API and WebSocket services.
  - Optionally caches frequently accessed data and stores ephemeral state (e.g., online users, typing status).

- **PostgreSQL**
  - Stores all persistent data: users, messages, chat rooms, media references (S3 URLs).

- **Amazon S3**
  - Stores all media files.
  - REST API generates pre-signed URLs for clients to upload/download media directly from S3.

---

## **Key Features**

- **Scalable:** Designed for millions of users with independent scaling of REST and WebSocket services.
- **Reliable:** All critical operations available via HTTP; WebSocket used for real-time enhancements.
- **Extensible:** Modular architecture for easy addition of new features (e.g., bots, analytics).
- **Secure:** Media access via pre-signed S3 URLs; authentication handled by REST API.

---

## **Getting Started**

1. **Clone the repository**
2. **Configure environment variables** (PostgreSQL, Redis, S3 credentials)
3. **Run with Docker Compose**
4. **Access REST API and WebSocket endpoints**

---

## **Planned Components**

- [ ] REST API Service (FastAPI)
- [ ] WebSocket Gateway (FastAPI/Starlette)
- [ ] PostgreSQL Database
- [ ] Redis (Pub/Sub, cache)
- [ ] Amazon S3 integration
- [ ] Worker Service (optional)
- [ ] Docker Compose setup

---

## **Contact**

For questions or contributions, please open an issue or pull request. # Chat-System
