# 🌐 HTTP Interface - Giao thức Web / Web Communication Layer

**Mục đích / Purpose**: Đây là "Mặt tiền" chính của ứng dụng, nơi tiếp nhận các yêu cầu từ trình duyệt, ứng dụng di động hoặc các Microservices khác thông qua giao thức HTTP. / This is the primary "Storefront" of the application, receiving requests from browsers, mobile apps, or other Microservices via the HTTP protocol.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **RESTful API**: Chúng tôi tuân thủ các nguyên tắc REST để đảm bảo API dễ hiểu, có tính nhất quán và dễ tích hợp.
- **Request Cycle**: Mỗi yêu cầu đi qua: Router -> Middleware -> Schema Validation -> Service.
- **Async Execution**: Tận dụng triệt để sức mạnh của FastAPI để xử lý hàng ngàn kết nối cùng lúc mà không làm treo hệ thống.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- Thư mục `http/` quản lý toàn bộ vòng đời của một request web, từ khi nhận vào cho đến khi trả về JSON cho khách hàng.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **RESTful API**: We adhere to REST principles to ensure the API is intuitive, consistent, and easy to integrate.
- **Request Cycle**: Every request flows through: Router -> Middleware -> Schema Validation -> Service.
- **Async Execution**: Fully utilizes FastAPI to handle thousands of concurrent connections without blocking the system.

### 🏛️ Practical Example
In this project:
- The `http/` directory manages the entire lifecycle of a web request, from ingestion to returning JSON responses to the client.
