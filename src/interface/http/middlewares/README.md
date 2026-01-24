# 🔒 Middlewares - Những "Trạm gác" Trung gian / Request Processing Guards

**Mục đích / Purpose**: Middleware là các thành phần nằm giữa Request và Response. Chúng giúp xử lý các tác vụ chung mà mọi endpoint đều cần như: Ghi log, Xác thực, hoặc Xử lý lỗi tập trung. / Middlewares are components situated between the Request and Response. They handle cross-cutting concerns that every endpoint needs, such as Logging, Authentication, or Centralized Error Handling.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Wrap & Filter**: Middleware bao bọc lấy logic xử lý API. Nó có thể kiểm tra yêu cầu trước khi cho vào (Pre-process) hoặc sửa lại kết quả trước khi gửi đi (Post-process).
- **Separation of Concerns**: Giúp tách biệt logic kỹ thuật (như đo thời gian phản hồi) ra khỏi logic nghiệp vụ của Service.
- **Error Shield**: Đảm bảo rằng dù code có bị lỗi thế nào, người dùng vẫn nhận được một phản hồi JSON chuyên nghiệp thay vì một trang thông báo lỗi "xấu xí".

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `logging_middleware.py`: Tự động ghi lại thông tin về mỗi yêu cầu giúp việc debug trở nên cực kỳ dễ dàng.
- `error_handler.py`: "Bắt" lấy các lỗi đặc thù của Domain (như hết hàng) và biến chúng thành HTTP Status Code 400 phù hợp.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Wrap & Filter**: Middlewares wrap API logic. They can inspect incoming requests (Pre-process) or modify responses (Post-process).
- **Separation of Concerns**: Isolates technical logic (like measuring response time) from the Service's business logic.
- **Error Shield**: Ensures that regardless of code errors, the user receives a professional JSON response instead of a plain error page.

### 🏛️ Practical Example
In this project:
- `logging_middleware.py`: Automatically logs information for every request, making debugging effortless.
- `error_handler.py`: Catches domain-specific exceptions (like out-of-stock) and transforms them into appropriate HTTP 400 status codes.
