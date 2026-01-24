# 🧪 Test Suite - Đảm bảo Chất lượng Phần mềm / Quality Assurance Hub

**Mục đích / Purpose**: Thư mục `tests/` là nơi chứa "Lưới an toàn" của dự án. Nó giúp các developer tự tin thay đổi code mà không sợ làm hỏng các tính năng cũ thông qua việc tự động hóa kiểm tra. / The `tests/` directory serves as the project's "Safety Net", allowing developers to modify code confidently without breaking existing features through automated verification.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Test-Driven Mentality**: Một mã nguồn tốt luôn đi kèm với các bài kiểm tra. Nếu không có test, code đó là "Legacy code" ngay khi vừa viết xong.
- **Pytest Framework**: Chúng tôi sử dụng Pytest vì tính linh hoạt, hỗ trợ async và khả năng viết code test cực kỳ súc tích.
- **Coverage**: Chúng tôi đặt mục tiêu kiểm thử mọi ngóc ngách của hệ thống, từ logic domain nhỏ nhất đến luồng xử lý phức tạp của API.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `unit/`: Kiểm tra logic thuần túy (không cần DB).
- `integration/`: Kiểm tra cách các mảnh ghép khớp với nhau (có dùng DB tạm).
- `manual/`: Các script kiểm tra đặc thù như Concurrency (tranh chấp kho hàng).

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Test-Driven Mentality**: High-quality source code is inseparable from its tests. Without tests, code is effectively "Legacy" the moment it's written.
- **Pytest Framework**: We utilize Pytest for its flexibility, native async support, and concise testing syntax.
- **Coverage**: We aim to test every corner of the system, from the smallest domain logic to complex API workflows.

### 🏛️ Practical Example
In this project:
- `unit/`: Verifies pure logic (no database required).
- `integration/`: Checks how components fit together (using temporary databases).
- `manual/`: Specialized scripts for edge cases like Concurrency and inventory contention.
