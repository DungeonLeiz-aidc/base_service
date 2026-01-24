# 🧪 Integration Tests - Kiểm thử Tích hợp / Component Coordination

**Mục đích / Purpose**: Integration Tests xác minh rằng các thành phần khác nhau của hệ thống có thể "nói chuyện" với nhau một cách chính xác. Chúng kiểm tra sự phối hợp giữa API, Service và Database thực. / Integration Tests verify that different system components interact correctly. They test the coordination between the API, Services, and actual Databases.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Real-world Scenarios**: Kiểm tra một luồng xử lý trọn vẹn từ lúc nhận Request đến khi dữ liệu được lưu vào Database.
- **Test Database**: Thường sử dụng một database tạm thời (như SQLite in-memory) để đảm bảo môi trường sạch cho mỗi lần chạy.
- **Wiring**: Đảm bảo việc cấu hình Dependency Injection (DI) hoạt động chính xác.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `test_order_flow.py`: Giả lập một tiến trình đặt hàng hoàn chỉnh: Gọi API -> Service xử lý -> Lưu Postgres -> Bắn sự kiện (Mocked).

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Real-world Scenarios**: Tests a complete workflow from receiving a Request to data being persisted in the Database.
- **Test Database**: Usually uses a temporary database (like SQLite in-memory) to ensure a clean environment for each run.
- **Wiring**: Ensures that Dependency Injection (DI) configurations are working correctly.

### 🏛️ Practical Example
In this project:
- `test_order_flow.py`: Simulates a full ordering process: API Call -> Service Processing -> Postgres Persistence -> Event Publishing (Mocked).
