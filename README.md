# 🎓 Clean Architecture & DDD Boilerplate (Python)

**Mục tiêu / Mission**: Dự án này không chỉ là một ứng dụng Quản lý Đơn hàng (OMS), mà là một giáo trình thực hành về **Clean Architecture** và **Domain-Driven Design (DDD)** trong môi trường Python hiện đại. / This project is not just an Order Management System (OMS), but a practical curriculum for **Clean Architecture** and **Domain-Driven Design (DDD)** in a modern Python environment.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📖 Tại sao dự án này tồn tại?
Dự án được thiết kế để giải quyết sự phức tạp của phần mềm bằng cách tách biệt logic nghiệp vụ khỏi các ràng buộc về công nghệ (database, framework, external services). Đây là nền tảng để bạn học cách xây dựng các hệ thống Microservices bền vững và dễ kiểm thử.

### 🏛️ Trụ cột kiến trúc (The Pillars)
| Layer | Trách nhiệm | Ví dụ trong OMS |
| :--- | :--- | :--- |
| **Domain** | Chứa logic nghiệp vụ cốt lõi, không phụ thuộc framework. | `Order`, `Product`, `OrderPlaced` event. |
| **Application** | Điều phối các luồng xử lý (Use Cases). | `PlaceOrderService`. |
| **Infrastructure** | Triển khai kỹ thuật (DB, Redis, Messaging). | `SQLAlchemy Repository`, `Redis Cache`. |
| **Interface** | Cổng giao tiếp với thế giới bên ngoài. | `FastAPI Routes`, `Typer CLI`. |

### 🛠️ Công nghệ & Lý do lựa chọn
- **FastAPI**: Tận dụng sức mạnh của `asyncio` và `pydantic` cho hiệu năng và tính an toàn kiểu dữ liệu.
- **Redis**: Giải quyết vấn đề **Concurrency** (overselling) bằng Distributed Locking.
- **RabbitMQ**: Demo mô hình **Event-driven**, giúp hệ thống mở rộng và giảm tải (decoupling).

### 🚀 Lộ trình học (How to learn)
1. Đọc tầng **Domain** để hiểu luật chơi.
2. Xem tầng **Application** để thấy cách luật chơi được thực thi qua Use Cases.
3. Khám phá **Infrastructure** để thấy cách kết nối với thế giới thực.
4. Chạy **Manual Tests** để thấy toàn bộ hệ thống phối hợp.

---

## 🇺🇸 English Version

### 📖 Why does this project exist?
This project is designed to tackle software complexity by isolating business logic from technological constraints (databases, frameworks, external services). It serves as a foundation for learning how to build sustainable, testable Microservices.

### 🏛️ Architectural Pillars
| Layer | Responsibility | Example in OMS |
| :--- | :--- | :--- |
| **Domain** | Pure business logic, framework-independent. | `Order`, `Product`, `OrderPlaced` event. |
| **Application** | Orchestrates workflows (Use Cases). | `PlaceOrderService`. |
| **Infrastructure** | Technical implementations (DB, Redis, Messaging). | `SQLAlchemy Repository`, `Redis Cache`. |
| **Interface** | Gateways to the outside world. | `FastAPI Routes`, `Typer CLI`. |

### 🛠️ Technology Stack & Rationale
- **FastAPI**: Leverages `asyncio` and `pydantic` for high performance and type safety.
- **Redis**: Handles **Concurrency** issues (overselling) using Distributed Locking.
- **RabbitMQ**: Demonstrates an **Event-driven** model for system scalability and decoupling.

### 🚀 Learning Path
1. Read the **Domain** layer to understand the rules of the game.
2. Check the **Application** layer to see how rules are executed via Use Cases.
3. Explore **Infrastructure** to see how the system interacts with the real world.
4. Run **Manual Tests** to observe the entire system in harmony.
