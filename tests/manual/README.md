# 🧪 Manual Tests - Kiểm thử Thực tế & Đặc biệt / Exploratory & Edge-case Testing

**Mục đích / Purpose**: Manual Tests cho phép lập trình viên kiểm tra các tình huống phức tạp khó mô phỏng bằng auto-test, hoặc để trực quan hóa hành vi hệ thống trong môi trường thực tế. / Manual Tests allow developers to check complex scenarios difficult to automate or to visualize system behavior in a real-world environment.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Concurrency Testing**: Kiểm tra các lỗi xảy ra khi có nhiều yêu cầu cùng lúc (như tranh chấp kho hàng).
- **UX Verification**: Đảm bảo các thông báo lỗi và phản hồi API dễ hiểu với người dùng cuối.
- **Edge-case Discovery**: Tìm kiếm các lỗi tiềm ẩn thông qua việc thử nghiệm tự do (Exploratory testing).

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `test_concurrency.py`: Một script Python đặc biệt bắn hàng loạt request cùng lúc để chứng minh Redis Distributed Lock đang hoạt động hiệu quả để chống Overselling.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Concurrency Testing**: Verifies behavior under simultaneous requests (like inventory contention).
- **UX Verification**: Ensures error messages and API responses are intuitive for end-users.
- **Edge-case Discovery**: Identifies hidden bugs through freedom of trial (Exploratory testing).

### 🏛️ Practical Example
In this project:
- `test_concurrency.py`: A specialized Python script firing concurrent requests to prove that the Redis Distributed Lock is effectively preventing Overselling.
