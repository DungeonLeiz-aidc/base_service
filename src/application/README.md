# 🔄 Application Layer - Tầng Điều Phối / Use Case Orchestration

**Mục đích / Purpose**: Tầng Application đóng vai trò là "người điều phối". Nó không chứa logic nghiệp vụ nhưng biết cách triệu tập các Entity, Repository và Service để hoàn thành một yêu cầu của khách hàng (Use Case). / The Application layer acts as the "orchestrator". It contains no business logic itself but knows how to invoke Entities, Repositories, and Services to fulfill a specific customer request (Use Case).

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tầng này giống như một người quản lý dự án. Nó nhận yêu cầu, kiểm tra tài liệu (DTO), yêu cầu thợ (Entities) làm việc và báo cáo kết quả.
- **Why DTO?**: Chúng ta dùng DTO để đảm bảo rằng nếu tầng Interface (API) thay đổi cấu trúc JSON, chúng ta không cần phải sửa đổi code xử lý bên trong.

### ⚠️ Ràng buộc (Constraints)
1. **No External Tech**: Không chứa code liên quan đến HTTP (FastAPI) hay Database cụ thể (SQL).
2. **Stateless**: Các service nên là không trạng thái để có thể mở rộng dễ dàng.

### 🏛️ Ví dụ thực tế (Examples)
- **Use Case**: [PlaceOrderService](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py) phối hợp luồng đặt hàng.
- **Data Containers**: [OrderDTOs](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/dtos/order_dtos.py) đóng gói dữ liệu truyền tải.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: This layer is like a project manager. It receives a request, checks the paperwork (DTOs), asks the workers (Entities) to perform the task, and reports the outcome.
- **Why DTO?**: We use DTOs to ensure that if the Interface (API) layer changes its JSON structure, the internal processing logic remains unaffected.

### ⚠️ Constraints
1. **No External Tech**: No code related to HTTP (FastAPI) or specific Databases (SQL).
2. **Stateless**: Services should be stateless to allow for easy scaling.

### 🏛️ Practical Examples
- **Use Case**: [PlaceOrderService](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py) coordinates the order flow.
- **Data Containers**: [OrderDTOs](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/dtos/order_dtos.py) package inter-layer data.
