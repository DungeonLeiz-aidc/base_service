# 🔄 Application Layer - Người Điều Phối / Use Case Orchestrator

**Mục đích / Purpose**: Tầng Application đóng vai trò như một "nhà điều hành", kết nối giữa yêu cầu của người dùng và các quy tắc nghiệp vụ trong Domain. Nó không chứa logic nghiệp vụ cốt lõi nhưng biết cách điều phối chúng để hoàn thành một công việc cụ thể (Use Case). / The Application layer acts as an "operator", bridging user requests and domain business rules. It doesn't contain core business logic but knows how to orchestrate it to complete a specific task (Use Case).

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Services (Use Cases)**: Các lớp chứa quy trình thực hiện một công việc (ví dụ: `Đặt hàng`). Nó sẽ gọi Repository để lấy dữ liệu, gọi Domain để kiểm tra luật, và gọi Publisher để thông báo kết quả.
- **DTOs (Data Transfer Objects)**: Các đối tượng dùng để đóng gói dữ liệu khi di chuyển giữa các lớp (In/Out). Giúp bảo vệ tầng Domain khỏi các thay đổi của API Schema.
- **Interfaces**: Các bản hợp đồng (Protocols) mà tầng Infrastructure phải tuân thủ.

### 🏛️ Ví dụ thực tế (Example)
- `PlaceOrderService`: Điều phối việc kiểm tra kho (Redis), lưu đơn hàng (PostgreSQL) và bắn sự kiện (RabbitMQ).
- `src/application/dtos/`: Nơi định nghĩa các yêu cầu đầu vào (`Request`) và kết quả trả về (`Response`) cho người dùng.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Services (Use Cases)**: Classes containing the workflow for a specific task (e.g., `Place Order`). It calls Repositories for data, Domain for rules, and Publishers for notifications.
- **DTOs (Data Transfer Objects)**: Objects used to package data moving between layers (In/Out). They protect the Domain layer from changes in the API schemas.
- **Interfaces**: Contracts (Protocols) that the Infrastructure layer must implement.

### 🏛️ Practical Example
- `PlaceOrderService`: Orchestrates stock checking (Redis), order persistence (PostgreSQL), and event publishing (RabbitMQ).
- `src/application/dtos/`: Defines input requirements (`Request`) and expected results (`Response`) for the user.
