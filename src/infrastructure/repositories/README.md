# 🏆 Repository Pattern - Trừu tượng hóa Dữ liệu / Data Access Abstraction

**Mục đích / Purpose**: Repository đóng vai trò như một bộ sưu tập (collection) các đối tượng Domain trong bộ nhớ. Nó ẩn đi sự phức tạp của việc truy vấn SQL và chuyển đổi dữ liệu. / The Repository pattern acts as an in-memory collection of Domain objects, hiding the complexities of SQL queries and data mapping.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao không dùng thẳng `session.query()` trong Service? Vì nếu làm vậy, Service sẽ bị "dính chặt" vào SQLAlchemy. Repository giúp Service chỉ cần nói "Cho tôi đơn hàng 123", còn lấy như thế nào là việc của Infrastructure.
- **Why Mapping?**: Đây là nơi chúng ta biến những hàng (rows) khô khan của database thành những đối tượng Domain mạnh mẽ, sẵn sàng cho nghiệp vụ.

### ⚠️ Ràng buộc (Constraints)
1. **Contract Fulfillment**: Phải triển khai chính xác các Interface đã định nghĩa tại `src/domain/interfaces/`.
2. **No Business Logic**: Repository không được ra quyết định nghiệp vụ (vd: tính tiền), nó chỉ lo việc lưu và lấy.

### 🏛️ Ví dụ thực tế (Examples)
- **OrderRepository**: [Implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) sử dụng `AsyncSession` để ghi dữ liệu xuống Postgres.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why not use `session.query()` directly in the Service? Doing so tightly couples the Service to SQLAlchemy. Repositories allow the Service to simply ask for "Order 123", leaving the "how" to the Infrastructure layer.
- **Why Mapping?**: This is where dry database rows are transformed into rich Domain objects ready for business logic.

### ⚠️ Constraints
1. **Contract Fulfillment**: Must strictly implement interfaces defined in `src/domain/interfaces/`.
2. **No Business Logic**: Repositories must not make business decisions (e.g., pricing); their sole responsibility is persistence and retrieval.

### 🏛️ Practical Examples
- **OrderRepository**: [Implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) uses `AsyncSession` to persist data to Postgres.
