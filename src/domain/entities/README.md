# 🎭 Domain Entities - Bản sắc của Nghiệp vụ / Core Business Identity

**Mục đích / Purpose**: Entities là những đối tượng có định danh duy nhất (ID), chứa đựng hành vi và bảo vệ tính đúng đắn của dữ liệu nghiệp vụ. / Entities are objects with unique identities (IDs) that encapsulate business behaviors and enforce data integrity.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Quản lý Định danh**: Đảm bảo mỗi thực thể luôn có một ID duy nhất trong suốt vòng đời.
2. **Bảo vệ Bất biến**: Thực thi quy tắc nghiệp vụ nội bộ (Vd: số lượng hàng phải dương).
3. **Quản lý Trạng thái**: Kiểm soát các bước chuyển trạng thái (Vd: Pending -> Confirmed).
4. **Sinh Sự kiện Domain**: Tạo thông báo khi có thay đổi nghiệp vụ quan trọng vừa xảy ra.
5. **Tự xác thực (Self-Validation)**: Tự chịu trách nhiệm về tính hợp lệ ngay khi khởi tạo.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Một Đơn hàng (Order) dù có thay đổi địa chỉ hay sản phẩm thì nó vẫn là *chính nó*. Định danh (ID) giúp chúng ta phân biệt nó với hàng ngàn đơn hàng khác.
- **Why Identity over Attributes?**: Trái ngược với Value Object, Entity được định nghĩa bởi ID. Hai đơn hàng giống hệt nhau về sản phẩm và khách hàng nhưng có ID khác nhau thì vẫn là hai đơn hàng riêng biệt.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Behavior-Rich**: Tuyệt đối không để Entity chỉ chứa toàn data (Getters/Setters). Nó phải có các phương thức thực thi hành động (Vd: `confirm()`, `add_item()`).
- **Always Valid**: Entity không được phép tồn tại ở trạng thái không hợp lệ (Vd: Order không có items).
- **Encapsulated State**: Thuộc tính bên trong nên được bảo vệ, chỉ thay đổi qua các phương thức nghiệp vụ.

### 🏛️ Ví dụ thực tế (Examples)
- **Order Entity**: [order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/entities/order.py) quản lý luồng trạng thái của một đơn hàng thực tế.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Identity Management**: Ensures unique entity identification throughout its entire lifecycle.
2. **Invariant Protection**: Enforces business rules (e.g., non-negative quantities).
3. **State Transitions**: Governs valid progression of business states (e.g., Pending to Confirmed).
4. **Domain Event Emission**: Triggers notifications for high-value business occurrences.
5. **Self-Validation**: Assumes responsibility for data integrity from the moment of initialization.

### 💡 Context & Why
- **Context**: An Order remains the same entity even if its delivery address changes. Its unique ID distinguishes it from all other orders.
- **Why Identity over Attributes?**: Unlike Value Objects, Entities are defined by ID. Two identical orders with different IDs are fundamentally different business units.

### ⚠️ Process & Constraints (CCE Template)
- **Behavior-Rich**: Entities must avoid being "dumb" data containers. They should feature actionable methods (e.g., `confirm()`, `add_item()`).
- **Stay Valid**: Entities must never be allowed to exist in an invalid state.
- **State Encapsulation**: Internal attributes should only be modified through controlled, validated business methods.

### 🏛️ Practical Examples
- **Order Entity**: [order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/entities/order.py) managing the lifecycle of an actual customer order.
