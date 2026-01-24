# ⚡ Caching & Distribution - Tối ưu Hiệu năng / Performance & Scale

**Mục đích / Purpose**: Danh mục này tập trung vào việc sử dụng Redis để tăng tốc độ truy cập dữ liệu và cơ chế Khóa phân tán (Distributed Lock) để đảm bảo tính nhất quán trong môi trường nhiều server. / This directory focuses on using Redis to accelerate data access and Distributed Locking to ensure consistency across multiple server instances.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong hệ thống thương mại điện tử, hàng nghìn người có thể cùng mua một món hàng. Nếu chỉ dùng Database, việc kiểm tra tồn kho sẽ rất chậm và dễ bị lỗi tranh chấp (Race Condition).
- **Why Distributed Lock?**: Chúng ta dùng Redis Lock để đảm bảo tại một thời điểm, chỉ có một luồng xử lý được quyền "giữ" hàng cho khách, ngăn chặn tuyệt đối tình trạng Bán quá số lượng (Overselling).

### ⚠️ Ràng buộc (Constraints)
1. **Timeout Sensitive**: Lock phải luôn có thời hạn (TTL) để tránh việc hệ thống bị treo vĩnh viễn nếu một server bị sập khi đang giữ lock.
2. **Fail-Safe**: Hệ thống phải hoạt động bình thường (hoặc fallback) nếu Redis gặp sự cố tạm thời.

### 🏛️ Ví dụ thực tế (Examples)
- **InventoryLock**: [Redis implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) thực hiện việc giữ hàng trong 30 giây khi khách đang thanh toán.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: In e-commerce, thousands of users might buy the same item simultaneously. Relying solely on the Database for stock checks is slow and prone to race conditions.
- **Why Distributed Lock?**: We use Redis Locks to ensure that only one process can "reserve" stock at any given time, strictly preventing Overselling.

### ⚠️ Constraints
1. **Timeout Sensitive**: Locks must always have a Time-to-Live (TTL) to prevent permanent system deadlocks if a server crashes while holding a lock.
2. **Fail-Safe**: The system should handle Redis downtime gracefully (e.g., via fallbacks).

### 🏛️ Practical Examples
- **InventoryLock**: [Redis implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) reserves items for 30 seconds during the checkout phase.
