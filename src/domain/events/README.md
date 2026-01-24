# 📣 Domain Events - Tiếng nói của Nghiệp vụ / The Voice of the Domain

**Mục đích / Purpose**: Domain Events ghi lại những sự việc quan trọng vừa xảy ra trong nghiệp vụ, giúp các thành phần trong hệ thống giao tiếp mà không bị ràng buộc (decoupled). / Domain Events record significant business occurrences, enabling decoupled communication between system components.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Ghi lại Sự thật**: Lưu giữ thông tin bất biến về một điều gì đó đã xảy ra (Vd: `OrderPlaced`).
2. **Thông báo Hệ thống**: Truyền tin cho các module khác hoặc hệ thống bên ngoài biết sự thay đổi.
3. **Nới lỏng Phụ thuộc**: Cho phép người gửi (Emit) không cần biết ai là người nhận (Handle).
4. **Đảm bảo Nhất quán**: Kích hoạt chuỗi hành động đồng bộ dữ liệu cần thiết.
5. **Lưu vết Audit**: Đóng vai trò làm bằng chứng lịch sử cho các hoạt động của hệ thống.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Khi đặt hàng thành công, ngoài việc lưu vào DB, ta còn cần gửi email, trừ kho, và tạo hóa đơn. Nếu làm tất cả trong một hàm, mã nguồn sẽ trở nên cực kỳ rắc rối và khó bảo trì.
- **Why Event-Driven?**: Giúp hệ thống "mở rộng" dễ dàng hơn. Sau này nếu cần thêm tính năng "Tích điểm", ta chỉ việc tạo thêm một Handler nghe sự kiện `OrderPlaced` mà không cần sửa dòng code nào của logic đặt hàng.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Bất biến (Immutable)**: Event là thông tin về quá khứ, nội dung của nó không bao giờ được phép thay đổi sau khi tạo.
- **Payload tinh gọn**: Chỉ nên chứa ID và các thông tin thay đổi cốt lõi. Tránh gửi toàn bộ object khổng lồ.
- **Tên theo thì Quá khứ**: Phải đặt tên Event bằng động từ thì quá khứ (Vd: `OrderPaid`, không phải `PayOrder`).

### 🏛️ Ví dụ thực tế (Examples)
- **Events**: Xem [order_events.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/events/order_events.py) để biết các mẫu sự kiện đặt hàng.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Fact Recording**: Captures immutable data about a past occurrence (e.g., `OrderPlaced`).
2. **System Messaging**: Alerts other modules or external systems regarding state changes.
3. **Decoupling**: Allows emitters to remain unaware of specific consumers (Handlers).
4. **Consistency Triggers**: Initiates downstream workflows to ensure eventual data validity.
5. **Audit Trails**: Provides historical evidence of system and user activity.

### 💡 Context & Why
- **Context**: Order success should trigger emails, inventory updates, and invoicing. Tight-coupling these actions within a single function creates brittle, unmaintainable code.
- **Why Event-Driven?**: Facilitates system "extensibility". Adding a new "loyalty points" feature becomes as simple as creating a new listener for `OrderPlaced`.

### ⚠️ Process & Constraints (CCE Template)
- **Immutability**: Since an Event represents the past, its content must never be modified once published.
- **Lean Payloads**: Transmit only essential IDs and change deltas; avoid heavy object transfers.
- **Past Tense Naming**: Use past tense verbs for Event names (e.g., `OrderPaid` instead of `PayOrder`).

### 🏛️ Practical Examples
- **Events**: Refer to [order_events.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/events/order_events.py) for the project's standard order event schemas.
