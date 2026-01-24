# 🏢 Domain Entities - Thực thể và Bản sắc / Entities & Identity

**Mục đích / Purpose**: Entities là những thành phần quan trọng nhất trong Domain. Chúng mang trong mình bản sắc (identity) và chứa đựng các quy tắc nghiệp vụ bất biến của hệ thống. / Entities are the most critical components of the Domain. They carry an identity and contain the system's invariant business rules.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Định danh (Identity)**: Một Entity được xác định bởi ID của nó, không phải bởi giá trị các thuộc tính. Một người dùng vẫn là người dùng đó ngay cả khi họ đổi tên.
- **Bất biến (Invariants)**: Entity chịu trách nhiệm đảm bảo dữ liệu của nó luôn hợp lệ theo luật nghiệp vụ (ví dụ: số lượng sản phẩm trong đơn hàng không được âm).
- **Vòng đời (Lifecycle)**: Entities có trạng thái thay đổi theo thời gian (ví dụ: Đơn hàng từ `Pending` sang `Shipped`).

### 🏛️ Ví dụ thực tế (Example)
Trong OMS này:
- `Order`: Một Entity phức tạp quản lý danh sách `OrderItem` và tổng giá trị đơn hàng.
- `Product`: Thực thể đại diện cho hàng hóa trong kho với SKU và giá bán.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Identity**: An Entity is identified by its ID, not by its attribute values. A user remains the same user even if they change their name.
- **Invariants**: Entities are responsible for ensuring their data is always valid according to business rules (e.g., product quantity in an order cannot be negative).
- **Lifecycle**: Entities have states that evolve over time (e.g., an Order moving from `Pending` to `Shipped`).

### 🏛️ Practical Example
In this OMS:
- `Order`: A complex Entity managing a list of `OrderItem`s and calculated totals.
- `Product`: Represents warehouse goods with specific SKUs and pricing.
