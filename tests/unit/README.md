# 🧪 Unit Tests - Kiểm thử Đơn vị / Isolated Component Testing

**Mục đích / Purpose**: Unit Tests giúp xác minh tính đúng đắn của từng hàm, từng class một cách cô lập. Chúng rất nhanh và không cần bất kỳ hạ tầng nào (Database/Network) để chạy. / Unit Tests verify the correctness of individual functions or classes in isolation. They are extremely fast and require no infrastructure (Database/Network) to run.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Mocking**: Thay thế các thành phần bên ngoài (như Database) bằng các đối tượng giả để kiểm soát dữ liệu đầu vào.
- **Tập trung vào Logic**: Unit tests tập trung vào việc kiểm tra các quy quy tắc nghiệp vụ (invariants) trong Entities hoặc Services.
- **Fail Fast**: Vì chạy rất nhanh, Unit tests là lớp bảo vệ đầu tiên giúp phát hiện lỗi ngay khi vừa sửa code.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `tests/unit/domain/`: Kiểm tra các luật của `Order` và `Product` mà không cần DB.
- `tests/unit/infrastructure/`: Kiểm tra cách `Redis client` xử lý logic (sử dụng `unittest.mock`).

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Mocking**: Replaces external components (like Databases) with fake objects to control input data.
- **Logic-Focused**: Unit tests focus on verifying business invariants within Entities or Services.
- **Fail Fast**: Being high-speed, Unit tests are the first line of defense to detect errors immediately after code changes.

### 🏛️ Practical Example
In this project:
- `tests/unit/domain/`: Tests `Order` and `Product` rules without a database.
- `tests/unit/infrastructure/`: Tests how the `Redis client` handles logic (using `unittest.mock`).
