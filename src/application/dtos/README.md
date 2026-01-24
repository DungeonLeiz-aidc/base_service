# 📦 DTOs - Biên giới Dữ liệu / Data Transfer Boundaries

**Mục đích / Purpose**: DTO là các vật chứa dữ liệu (Containers) dùng để vận chuyển thông tin qua biên giới giữa các tầng, đảm bảo tính bảo mật và cách ly cấu trúc. / DTOs are data containers used to transport information across layer boundaries, ensuring security and structural isolation.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Đóng gói Dữ liệu**: Gom nhóm tham số thành một đối tượng duy nhất để dễ truyền tải.
2. **Lá chắn Bảo vệ**: Cách ly Domain khỏi sự thay đổi JSON cấu trúc của API bên ngoài.
3. **Ẩn giấu Thông tin**: Lọc bỏ các thuộc tính nhạy cảm trước khi trả kết quả cho client.
4. **Xác thực Đầu vào**: Kiểm tra kiểu dữ liệu và định dạng trước khi nạp vào service.
5. **Nguồn cấp Tài liệu**: Cung cấp khuôn mẫu để tự động sinh tài liệu API (Swagger).

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Nếu chúng ta để Frontend làm việc trực tiếp với Domain Entity, một thay đổi nhỏ ở Database (Vd: đổi tên cột `user_id` thành `customer_id`) có thể làm hỏng toàn bộ Frontend.
- **Why DTOs?**: DTO đóng vai trò như một "lớp đệm". Database có thể đổi, nhưng DTO trả về cho khách hàng vẫn giữ nguyên, giúp hệ thống cực kỳ ổn định.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **No Logic**: Tuyệt đối không chứa logic nghiệp vụ hay logic tính toán.
- **Serializable**: Phải dễ dàng chuyển đổi thành JSON hoặc nạp từ Request Schema.
- **Immutable**: Ưu tiên sử dụng `dataclass` hoặc `Pydantic` để dữ liệu không bị thay đổi ngẫu nhiên.

### 🏛️ Ví dụ thực tế (Examples)
- **Schema**: [order_dto.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/dtos/order_dto.py) chứa cấu hình cho yêu cầu đặt hàng.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Data Bundling**: Collects discrete parameters into a single object for transmission.
2. **Boundary Shield**: Decouples the internal Domain from external API JSON changes.
3. **Secure Filtering**: Strips sensitive attributes before returning results to clients.
4. **Ingestion Validation**: Enforces type and format rules before data enters the Service layer.
5. **Schema Documentation**: Acts as the blueprint for automated Swagger/OpenAPI docs.

### 💡 Context & Why
- **Context**: Exposing Domain Entities directly to the Frontend is risky. A DB change (e.g., renaming `user_id` to `customer_id`) would break all client consumers.
- **Why DTOs?**: Acts as a "buffer zone". The database can evolve, but the DTO contract remains stable, ensuring overall system reliability.

### ⚠️ Process & Constraints (CCE Template)
- **Zero Logic**: Strictly prohibited from containing business or calculation logic.
- **Serializability**: Must be easily convertible to/from JSON or Pydantic schemas.
- **Immutability**: Favor `dataclass` or `Pydantic` models to prevent accidental data state mutation.

### 🏛️ Practical Examples
- **Schema**: [order_dto.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/dtos/order_dto.py) for the "Place Order" request payload.
