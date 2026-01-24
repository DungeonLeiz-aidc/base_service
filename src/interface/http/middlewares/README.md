# 🔒 Middlewares - Những "Trạm gác" Trung gian / Request Processing Guards

**Mục đích / Purpose**: Middleware xử lý các tác vụ chung (Cross-cutting concerns) xuyên suốt các request, đảm bảo tính nhất quán về bảo mật và giám sát hệ thống. / Middlewares handle cross-cutting concerns across all requests, ensuring consistent security and monitoring standards.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Xử lý Tác vụ Chung**: Tự động thực hiện Logging, đo lường Metrics cho mọi request.
2. **Cửa ngõ Bảo mật**: Kiểm tra Authentication và Authorization tập trung.
3. **Bảo vệ Quyền riêng tư**: Tự động che dấu dữ liệu nhạy cảm (PII Masking) trong logs.
4. **Lá chắn Lỗi hệ thống**: Chặn đứng các ngoại lệ không xác định để trả về 500 JSON sạch sẽ.
5. **Giám sát Hiệu năng**: Theo dõi thời gian xử lý và tài nguyên tiêu tốn cho từng yêu cầu.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Bạn không thể viết code kiểm tra quyền truy cập hay ghi log trong từng hàm một. Điều đó sẽ gây ra sự lặp lại khủng khiếp (DRY principle violated).
- **Why Middleware?**: Giúp "canh gác" hệ thống một cách tự động. Mọi request đều phải bước qua các middleware này trước khi chạm tới logic nghiệp vụ.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Tốc độ**: Middleware phải xử lý cực nhanh, không được làm tắc nghẽn luồng request chính.
- **Purity**: Tuyệt đối không được thay đổi logic nghiệp vụ bên trong request.
- **Hệ thống**: Phải luôn có Error Handler ở tầng ngoài cùng để bắt mọi lỗi tiềm ẩn.

### 🏛️ Ví dụ thực tế (Examples)
- **Logging**: [logging_middleware.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/logging_middleware.py) thực hiện việc ghi nhật ký và che thông tin nhạy cảm.
- **Errors**: [error_handler.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/error_handler.py) bảo vệ server.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Cross-cutting Concern Automation**: Handlers generic tasks like Logging and Metrics for every request.
2. **Security Gateway**: Centralized Authentication and Authorization checks.
3. **Privacy Enforcement**: Automated PII Masking of sensitive fields in outbound logs.
4. **Fail-Safe Shielding**: Intercepts unhandled exceptions to prevent server detail leaks (Clean 500s).
5. **Performance Tracking**: Measures latency and resource overhead per HTTP cycle.

### 💡 Context & Why
- **Context**: Manually writing auth or logging logic inside every single function is highly repetitive and error-prone (violates the DRY principle).
- **Why Middleware?**: Provides automated system "guardianship". Every request must clear these checkpoints before reaching core business logic.

### ⚠️ Process & Constraints (CCE Template)
- **Throughput First**: Middleware must execute in milliseconds to avoid bottlenecking the request pipeline.
- **Side-effect Free**: Must never alter the intended business outcome of a request.
- **Safety Net**: A global Error Handler is mandatory at the outermost layer to catch all unhandled states.

### 🏛️ Practical Examples
- **Logging**: [logging_middleware.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/logging_middleware.py) for audit trails and masking.
- **Error Handling**: [error_handler.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/error_handler.py) protecting server integrity.
