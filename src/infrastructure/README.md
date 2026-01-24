# 🏗️ Infrastructure Layer - Chi tiết Kỹ thuật / Technical Implementation

**Mục đích / Purpose**: Tầng Infrastructure hiện thực hóa các "bản hợp đồng" từ Domain, quản lý mọi kết nối ra thế giới bên ngoài (DB, Cache, Network). / The Infrastructure layer implements Domain contracts, managing all external connections (DB, Cache, Network).

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Hiện thực hóa Hợp đồng**: Triển khai mã nguồn thực tế cho các Interface đã định nghĩa tại Domain.
2. **Cách ly Công nghệ**: Ngăn chặn thư viện bên thứ ba làm "ô nhiễm" mã nguồn nghiệp vụ.
3. **Xây dựng Tính bền vững**: Thiết lập các cơ chế bảo vệ hệ thống như Retry và Circuit Breaker.
4. **Quản lý Tài nguyên**: Tối ưu hóa việc sử dụng kết nối (Pool) và bộ nhớ cho dịch vụ ngoại vi.
5. **Ánh xạ Dữ liệu**: Chuyển đổi dữ liệu từ định dạng kỹ thuật sang đối tượng Domain và ngược lại.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
infrastructure/
├── models/             # Cấu trúc bảng DB vật lý (SQLAlchemy).
├── repositories/       # Triển khai các bộ sưu tập dữ liệu (Postgres).
├── caching/            # Tăng tốc và khóa phân tán (Redis).
├── messaging/          # Giao tiếp bất đồng bộ (RabbitMQ).
├── clients/            # Kết nối dịch vụ bên thứ ba (Stripe, Email).
└── migrations/         # Cấu hình "dây dợ" cho việc tiến hóa database.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Nghiệp vụ (Domain) không nên quan tâm bạn dùng Postgres hay MySQL. Những chi tiết này nên được giấu kỹ ở tầng Infrastructure.
- **Why Hexagonal Architecture?**: Giúp dễ dàng thay thế "linh kiện" kỹ thuật. Bạn có thể đổi từ RabbitMQ sang Kafka mà không cần chạm vào lõi nghiệp vụ.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Không nghiệp vụ**: Tuyệt đối không đưa logic quyết định nghiệp vụ vào đây.
- **Dependency Only**: Chỉ được phụ thuộc vào Domain và Application layer.
- **Async First**: Ưu tiên xử lý bất đồng bộ để đạt hiệu năng tối đa.

### 🏛️ Ví dụ thực tế (Examples)
- **Repositories**: [Data persistence](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/README.md).
- **Messaging**: [RabbitMQ Publisher](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/README.md).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Contract Implementation**: Provides concrete source code for Domain-defined Interfaces.
2. **Framework Isolation**: Prevents technical libraries from "polluting" business logic.
3. **Resilience Engineering**: Implements system protections like Retry and Circuit Breaker logic.
4. **Resource Management**: Optimizes connection pooling and memory for external services.
5. **Data Mapping**: Translates between technical records and rich Domain objects.

### 📂 Directory Layout
```text
infrastructure/
├── models/             # Physical database schemas (SQLAlchemy).
├── repositories/       # Concrete data collection implementations (Postgres).
├── caching/            # Acceleration and distributed locking (Redis).
├── messaging/          # Asynchronous communication (RabbitMQ).
├── clients/            # Third-party integration clients (Stripe, Email).
└── migrations/         # Wiring logic for database schema evolution.
```

### 💡 Context & Why
- **Context**: Business logic (the Domain) should remain agnostic of specific database or broker choices.
- **Why Hexagonal Architecture?**: Facilitates seamless "component swapping", enabling tech stack migrations without core business disruption.

### ⚠️ Process & Constraints (CCE Template)
- **No Business Logic**: Never make business-critical decisions within this layer.
- **Directional Dependency**: Only allow dependencies pointing towards the Domain or Application layers.
- **Async First**: Prioritize asynchronous I/O for peak performance results.

### 🏛️ Practical Examples
- **Repositories**: [Data persistence](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/README.md).
- **Messaging**: [RabbitMQ implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/README.md).
