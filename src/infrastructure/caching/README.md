# ⚡ Caching & Distribution - Tối ưu Hiệu năng / Performance & Scale

**Mục đích / Purpose**: Danh mục này tập trung vào việc sử dụng Redis để tăng tốc độ truy cập dữ liệu và cơ chế Khóa phân tán (Distributed Lock). Đây là thành phần then chốt để giải quyết bài toán Concurrency (Tranh chấp tài nguyên). / This directory focuses on using Redis for data acceleration and Distributed Locking—a critical component for solving resource contention (Concurrency).

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong hệ thống thương mại điện tử, hàng nghìn người có thể cùng mua một món hàng. Nếu chỉ dùng Database, việc kiểm tra tồn kho sẽ rất chậm và dễ bị lỗi tranh chấp (Race Condition).
- **Why Distributed Lock?**: Chúng ta dùng Redis Lock để đảm bảo tại một thời điểm, chỉ có một luồng xử lý được quyền "giữ" hàng cho khách, ngăn chặn tuyệt đối tình trạng Bán quá số lượng (Overselling).

### ⚠️ Ràng buộc & Cấu trúc (CCE Template)
- **Constraints**: 
    1. **TTL (Time-To-Live)**: Mọi Lock phải có thời hạn tự động giải phóng (default: 30s) để tránh treo hệ thống (Deadlock).
    2. **Atomic Operation**: Việc kiểm tra tồn kho và trừ kho phải là một hoạt động nguyên tử trong Lock.
- **Workflow**: 
    1. Yêu cầu Lock theo `product_id`.
    2. Nếu có Lock: Kiểm tra Redis Cache -> Trừ kho ảo -> Trả kết quả.
    3. Giải phóng Lock sớm nhất có thể.

### 🏛️ Ví dụ thực tế (Examples)
- **InventoryLock**: [Redis implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) thực hiện việc giữ hàng trong 30 giây khi khách đang thanh toán.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: In high-traffic e-commerce, thousands of concurrent users might target the same item. Relying solely on a Relational Database for stock checks is slow and vulnerable to Race Conditions.
- **Why Distributed Lock?**: Redis Locks ensure only one execution thread "reserves" stock at any time, eliminating the risk of Overselling.

### ⚠️ Constraints & Workflow
- **Constraints**: 
    1. **TTL (Time-To-Live)**: All locks must have an expiration (default: 30s) to prevent permanent deadlocks if a server crashes.
    2. **Atomic Operation**: Inventory checks and deductions must remain atomic within the lock context.
- **Workflow**: 
    1. Request Lock using `product_id`.
    2. If Acquired: Check Redis Cache -> Deduct virtual stock -> Return result.
    3. Release Lock ASAP.

### 🏛️ Practical Examples
- **InventoryLock**: [Redis implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) reserves stock for 30s during the checkout lifecycle.
