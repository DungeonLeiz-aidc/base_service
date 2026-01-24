# 📜 Scripts - Công cụ và Tự động hóa / Automation Utilities

**Mục đích / Purpose**: Thư mục này chứa các kịch bản phụ trợ dùng để kiểm tra, bảo trì hoặc thực hiện các tác vụ quản trị hệ thống một cách nhanh chóng mà không cần qua API. / This directory contains utility scripts for checking, maintaining, or performing administrative tasks quickly without going through the API.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **SRE & DevOps**: Trong thực tế, lập trình viên cần các công cụ để kiểm tra nhanh trạng thái hạ tầng (Health Check) hoặc thực hiện các thao tác dữ liệu hàng loạt.
- **Tính độc lập**: Các script ở đây thường chạy độc lập với server API nhưng có thể dùng chung cấu hình (`settings`).

### 🏛️ Ví dụ thực tế (Example)
- `check_services.py`: Kiểm tra sự sẵn sàng của PostgreSQL, Redis và RabbitMQ. Đây là ví dụ về cách tự động hóa việc kiểm tra điều kiện tiên quyết trước khi chạy app.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **SRE & DevOps**: In reality, developers need tools to quickly check infrastructure health or perform bulk data operations.
- **Independence**: Scripts here usually run independently of the API server but may share the same configuration (`settings`).

### 🏛️ Practical Example
- `check_services.py`: Verifies the availability of PostgreSQL, Redis, and RabbitMQ. This is an example of automating prerequisite checks before starting the application.
