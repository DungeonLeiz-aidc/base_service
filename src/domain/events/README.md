# 📣 Domain Events - Tiếng nói của Nghiệp vụ / The Voice of the Domain

**Mục đích / Purpose**: Domain Events ghi lại những sự kiện quan trọng vừa xảy ra trong nghiệp vụ. Chúng cho phép các thành phần khác nhau của hệ thống giao tiếp mà không cần phụ thuộc trực tiếp vào nhau. / Domain Events record significant business occurrences, enabling decoupled communication between different system components.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Khi một đơn hàng được đặt, nhiều việc cần xảy ra: Gửi mail, Trừ kho, Sinh hóa đơn. Nếu gom tất cả vào một Service, code sẽ trở nên khổng lồ và khó bảo trì.
- **Why Async Events?**: Sử dụng Event giúp chúng ta tách biệt các hành động này. Service đặt hàng chỉ việc "bắn" ra một sự kiện, còn ai làm gì tiếp theo là việc của các Worker khác.

### ⚠️ Ràng buộc (Constraints)
1. **Immutable**: Sự kiện đại diện cho quá khứ, không bao giờ được phép thay đổi dữ liệu bên trong sự kiện.
2. **Minimal Payload**: Chỉ nên chứa những thông tin thiết yếu (Vd: ID Đơn hàng), không nên chứa cả object khổng lồ.

### 🏛️ Ví dụ thực tế (Examples)
- **OrderPlaced**: Chứa `order_id` và timestamp. Đây là "ngòi nổ" cho chuỗi xử lý sau bán hàng.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: When an order is placed, several actions should follow: emailing the customer, deducting stock, generating invoices. Combining these into a single Service leads to bloated, unmaintainable code.
- **Why Async Events?**: Events allow us to decouple these actions. The Order Service simply "fires" an event, and background workers handle the subsequent tasks independently.

### ⚠️ Constraints
1. **Immutable**: Events represent the past; their internal data must never be altered.
2. **Minimal Payload**: Should only carry essential information (e.g., Order ID) rather than large, complex objects.

### 🏛️ Practical Examples
- **OrderPlaced**: Carries `order_id` and timestamp. It acts as the "trigger" for post-sale processing workflows.
