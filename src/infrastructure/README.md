# 🔌 Infrastructure Layer - Tầng Thực Thi Kỹ Thuật / Technical Implementation

**Mục đích / Purpose**: Tầng Infrastructure là nơi hiện thực hóa các ý tưởng của tầng Application bằng các công nghệ cụ thể. Đây là nơi code của bạn tương tác với thế giới bên ngoài như Database, Mail Server, hoặc Message Broker. / The Infrastructure layer provides concrete technical implementations for the ideas defined in the Application layer. This is where your code interacts with the outside world, such as Databases, Mail Servers, or Message Brokers.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Persistence (Repositories)**: Triển khai việc lưu trữ dữ liệu vào database thực (PostgreSQL). Nó cụ thể hóa các interface đã định nghĩa trong domain.
- **Adapters / Clients**: Các lớp bao bọc lấy các thư viện bên ngoài (Redis client, RabbitMQ client) để cung cấp bộ API đơn giản cho hệ thống.
- **Data Models**: Các lớp định nghĩa cấu trúc bảng cho ORM (SQLAlchemy). Khác với Domain Entities, Models tập trung vào cách dữ liệu được lưu trữ.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `repositories/`: Sử dụng SQLAlchemy Async để truy vấn PostgreSQL.
- `clients/`: Chứa các bộ điều khiển cho Redis (quản lý kho) và RabbitMQ (bắn sự kiện).
- `models/`: Chứa định nghĩa schema cho database.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Persistence (Repositories)**: Implements data storage in the actual database (PostgreSQL). It realizes the interfaces defined in the domain.
- **Adapters / Clients**: Classes that wrap external libraries (Redis client, RabbitMQ client) to provide a simplified API for the system.
- **Data Models**: Classes defining table structures for the ORM (SQLAlchemy). Unlike Domain Entities, Models focus on how data is stored.

### 🏛️ Practical Example
In this project:
- `repositories/`: Uses SQLAlchemy Async to query PostgreSQL.
- `clients/`: Contains controllers for Redis (inventory management) and RabbitMQ (event publishing).
- `models/`: Contains database schema definitions.
