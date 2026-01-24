# 🥇 API v1 - Phiên bản Đầu tiên / Initial API Version

**Mục đích / Purpose**: Danh mục `v1/` chứa các triển khai cụ thể cho phiên bản API đầu tiên của hệ thống. Đây là nơi tập trung các logic về Endpoint, Schema và logic xử lý Request/Response cho người dùng. / The `v1/` directory contains specific implementations for the system's first API version, focusing on Endpoints, Schemas, and Request/Response handling.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Stability Guarantee**: Một khi API v1 đã được công khai, chúng ta cam kết không thay đổi cấu trúc dữ liệu để tránh làm lỗi Client. Nếu muốn thay đổi lớn, chúng ta sẽ tạo `v2`.
- **Granular Schemas**: Ở đây chúng ta sử dụng các Pydantic Schemas rất chi tiết để đảm bảo dữ liệu khách gửi lên là hoàn hảo (ví dụ: SKU không được trống).
- **Service Injection**: Tầng này sẽ "nhờ" các Application Services thực hiện công việc nặng nhọc, nó chỉ lo việc nhận và trả dữ liệu.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `orders.py`: Định nghĩa các endpoint `/api/v1/orders`. Nó nhận input, validate bằng Pydantic, gọi `PlaceOrderService` và trả về JSON chuẩn.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Stability Guarantee**: Once API v1 is public, we commit to maintaining its data structure to avoid breaking clients. Major changes would necessitate a `v2`.
- **Granular Schemas**: We use detailed Pydantic Schemas here to ensure incoming data is perfect (e.g., SKU must not be empty).
- **Service Injection**: This layer delegates heavy lifting to Application Services, focusing solely on data ingestion and response delivery.

### 🏛️ Practical Example
In this project:
- `orders.py`: Defines the `/api/v1/orders` endpoints. It ingest input, validates via Pydantic, invokes `PlaceOrderService`, and returns standardized JSON.
