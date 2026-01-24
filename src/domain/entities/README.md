# 🎭 Domain Entities - Bản sắc của Nghiệp vụ / Core Business Identity

**Mục đích / Purpose**: Entities là những đối tượng có định danh (Identity) duy nhất và vòng đời dài hạn. Chúng chứa đựng các quy tắc nghiệp vụ cốt lõi và đảm bảo tính nhất quán của dữ liệu. / Entities are objects with a unique identity and a long-term lifecycle. They encapsulate core business rules and ensure data consistency.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao không dùng dictionary? Vì Entity có "hành vi" (behavior). Ví dụ: Một Đơn hàng biết cách tự tính tổng số tiền và kiểm tra xem nó có thể chuyển trạng thái hay không.
- **Why Invariants?**: Các phương thức trong Entity giúp bảo vệ các "bất biến" (Invariants). Bạn không thể thay đổi giá sản phẩm thành số âm vì Entity sẽ ngăn chặn điều đó ngay lập tức.

### ⚠️ Ràng buộc (Constraints)
1. **Rich Domain Model**: Ưu tiên đưa logic vào Entity thay vì để Service xử lý (tránh Anemic Domain Model).
2. **Identification**: Luôn xác định thực thể bằng ID hoặc SKU, không phải bằng thuộc tính ngẫu nhiên.

### 🏛️ Ví dụ thực tế (Examples)
- **Order Entity**: Chứa danh sách `OrderItem` và logic chuyển trạng thái `confirm()`, `cancel()`.
- **Product Entity**: Quản lý `stock_quantity` và đảm bảo không bao giờ bị âm.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why not use simple dictionaries? Entities have "behavior". For instance, an Order knows how to calculate its total and validate its own state transitions.
- **Why Invariants?**: Entity methods protect business "Invariants". You cannot set a negative price because the Entity will immediately block such an invalid state.

### ⚠️ Constraints
1. **Rich Domain Model**: Prefer logic within Entities over Services (avoiding the Anemic Domain Model anti-pattern).
2. **Identification**: Always identify entities by ID or SKU, never by transient attributes.

### 🏛️ Practical Examples
- **Order Entity**: Contains `OrderItem` list and logic for `confirm()` and `cancel()` transitions.
- **Product Entity**: Manages `stock_quantity` and ensures it never drops below zero.
