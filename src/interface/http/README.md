# 🌐 HTTP Gateway - Cổng giao tiếp Web / Web Communication Gateway

**Mục đích / Purpose**: Thư mục này tập trung vào việc quản lý các kết nối qua giao thức HTTP, bao gồm định nghĩa các điểm cuối (Endpoints) và các bộ lọc trung gian (Middlewares). / This directory manages HTTP-based communications, including the definition of API Endpoints and cross-cutting Middlewares.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Quản lý Endpoints**: Định nghĩa các đường dẫn (Routes) để Client có thể truy cập tài nguyên.
2. **Thực thi Middlewares**: Áp dụng các bộ lọc chung (Auth, Logging, Error Handling) cho mọi request.
3. **Cấu hình Server**: Thiết lập các tham số vận hành cho web framework (FastAPI).
4. **Xử lý Giao thức**: Đảm bảo việc nhận và gửi dữ liệu tuân thủ chuẩn HTTP/JSON.
5. **Kiểm soát Truy cập**: Đảm bảo chỉ những yêu cầu hợp lệ mới được đi sâu vào hệ thống.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
http/
├── api/                # Định nghĩa các Route và logic điều hướng API.
├── middlewares/        # Các bộ canh gác (Logging, Security, Error Handlers).
└── __init__.py         # Khởi tạo mô-đun HTTP.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: HTTP là giao thức phổ biến nhất hiện nay. Việc tách biệt logic HTTP giúp chúng ta dễ dàng thay đổi thư viện (Vd: từ FastAPI sang Starlette) mà không ảnh hưởng tới các linh kiện khác.
- **Why Fastapi?**: Tối ưu cho hiệu suất bất đồng bộ (Async), cực kỳ phù hợp cho các hệ thống cần độ trễ thấp.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **No Persistence**: Cấm tuyệt đối việc gọi trực tiếp Database tại tầng này. Phải qua Application Service.
- **Input Validation**: Mọi dữ liệu vào phải được kiểm tra kiểu qua Pydantic Schemas.
- **Error Shielding**: Mọi lỗi phải được bắt và trả về định dạng JSON chuẩn.

### 🏛️ Ví dụ thực tế (Examples)
- **API**: Xem [api/v1/router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/router.py).
- **Middleware**: [logging_middleware.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/logging_middleware.py) canh gác dữ liệu.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Endpoint Management**: Defines the resource paths available to external clients.
2. **Middleware Execution**: Applies global filters (Auth, Logging, Error Handling) to every request lifecycle.
3. **Server Configuration**: Sets the operational parameters for the underlying web framework.
4. **Protocol Handling**: Ensures all data transmissions strictly adhere to HTTP/JSON standards.
5. **Access Control**: Guarantees that only structurally valid requests penetrate deeper layers.

### 📂 Directory Layout
```text
http/
├── api/                # API Route definitions and navigation logic.
├── middlewares/        # Guards for logging, security, and global errors.
└── __init__.py         # HTTP module initialization.
```

### 💡 Context & Why
- **Context**: HTTP is the dominant protocol today. Decoupling HTTP logic allows for easier framework transitions without disrupting core business.
- **Why FastAPI?**: Built for asynchronous performance, making it the ideal choice for low-latency service requirements.

### ⚠️ Process & Constraints (CCE Template)
- **Zero Persistence**: Strictly prohibits direct database calls; interaction must flow through Application Services.
- **Input Validation**: All incoming data must undergo strict type-checking via Pydantic Schemas.
- **Error Shielding**: All exceptions must be caught and returned as standardized JSON responses.

### 🏛️ Practical Examples
- **API**: Refer to [api/v1/router.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/router.py).
- **Middleware**: [logging_middleware.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/logging_middleware.py).
