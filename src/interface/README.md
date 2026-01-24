# 🌐 Interface Layer - Điểm tiếp nhận Yêu cầu / The Entry Points

**Mục đích / Purpose**: Tầng Interface là "mặt tiền" của ứng dụng. Nó chịu trách nhiệm nhận yêu cầu từ bên ngoài (HTTP, CLI, Events), kiểm tra tính hợp lệ và chuyển tiếp chúng vào tầng Application. / The Interface layer is the system's "façade". It receives external requests (HTTP, CLI, Events), validates them, and forwards them to the Application layer.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao không gọi thẳng Service từ Route? Việc tách biệt giúp chúng ta có thể hỗ trợ nhiều loại Interface (Vd: vừa có Web API, vừa có CLI) mà không cần viết lại logic xử lý.
- **Why Global Exception Handling?**: Chúng ta tập trung việc xử lý lỗi ở Middleware để đảm bảo người dùng luôn nhận được phản hồi JSON chuẩn, ngay cả khi có lỗi hệ thống nghiêm trọng.

### ⚠️ Ràng buộc (Constraints)
1. **Request/Response Only**: Chỉ lo việc chuyển đổi dữ liệu (Mapping Pydantic <-> DTO). Không được thực hiện Business Logic ở đây.
2. **Versioning Required**: Luôn sử dụng prefix version (vd: `/v1/`) để đảm bảo tính ổn định.

### 🏛️ Ví dụ thực tế (Examples)
- **API**: [Orders API](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/orders.py) định nghĩa các endpoint REST.
- **Middlewares**: [Global Error Handler](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/error_handler.py) bảo vệ hệ thống.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why separate Routes from Services? This allows supporting multiple interfaces (e.g., both Web API and CLI) without duplicating core logic.
- **Why Global Exception Handling?**: Centralizing error handling in Middleware ensures users always receive standardized JSON responses, even during critical failures.

### ⚠️ Constraints
1. **Request/Response Only**: Handles data translation (Pydantic <-> DTO). Business logic is strictly forbidden here.
2. **Versioning Required**: Always use version prefixes (e.g., `/v1/`) to maintain backward compatibility.

### 🏛️ Practical Examples
- **API**: [Orders API](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/api/v1/orders.py) defines REST endpoints.
- **Middlewares**: [Global Error Handler](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/http/middlewares/error_handler.py) shields the system.
