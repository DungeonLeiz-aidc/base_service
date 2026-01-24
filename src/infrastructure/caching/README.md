# ⚡ Caching & Distribution - Tối ưu Hiệu năng / Performance & Scale

**Mục đích / Purpose**: Sử dụng bộ nhớ RAM (Redis) để tăng tốc độ truy cập dữ liệu và dùng Khóa phân tán để giải quyết tranh chấp tài nguyên trong môi trường đa máy chủ. / Leverages RAM (Redis) for data acceleration and Distributed Locking to resolve resource contention in multi-server environments.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Tăng tốc Truy cập**: Giảm độ trễ bằng cách lưu trữ dữ liệu nóng trên RAM.
2. **Giải quyết Tranh chấp**: Dùng Distributed Lock để ngăn Race Condition (Vd: tránh overselling).
3. **Đảm bảo Nhất quán**: Quản lý vòng đời dữ liệu cache qua chính sách TTL.
4. **Giảm tải Database**: Chặn bớt các truy vấn lặp đi lặp lại vào database chính.
5. **Tính nguyên tử**: Thực hiện các phép toán "Check-then-Set" một cách an toàn.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Hệ thống đặt hàng luôn phải đối mặt với bài toán hàng ngàn người cùng mua 1 món hàng cuối cùng. Database truyền thống thường quá chậm để xử lý khóa (locking) ở quy mô này.
- **Why Redis?**: Redis nổi tiếng với tốc độ xử lý hàng triệu request/giây và hỗ trợ các phép toán Atomic cực mạnh cho việc quản lý kho (Inventory).

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **TTL bắt buộc**: Mọi dữ liệu vào cache đều phải có thời gian hết hạn (Time-To-Live).
- **Graceful Degradation**: Ứng dụng phải vẫn chạy được (dù chậm hơn) nếu Redis gặp sự cố (Cache bypass).
- **Lock Safety**: Luôn sử dụng `try-finally` để đảm bảo Khóa (Lock) luôn được giải phóng.

### 🏛️ Ví dụ thực tế (Examples)
- **Inventory Cache**: [redis_inventory_cache.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) thực hiện khóa để trừ kho.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Performance Acceleration**: Lowers latency by serving high-frequency data from RAM.
2. **Conflict Resolution**: Uses Distributed Locking to prevent Race Conditions (e.g., overselling).
3. **Consistency Management**: Controls cache data freshness via strict TTL policies.
4. **Primary DB Shielding**: Intercepts repetitive read traffic to protect the main Database.
5. **Atomic Operations**: Safely executes critical "Check-then-Set" sequences.

### 💡 Context & Why
- **Context**: Heavy traffic systems must handle concurrent stock deductions. Traditional DB locking is often too slow for peak-load demands.
- **Why Redis?**: Renowned for million-request-per-second speeds and powerful atomic primitives essential for robust inventory management.

### ⚠️ Process & Constraints (CCE Template)
- **Mandatory TTL**: Every cached item must include an expiration policy.
- **Graceful Degradation**: The core app must survive (even at lower speeds) if Redis is unavailable.
- **Lock Safety**: Utilize `try-finally` patterns to guarantee lock release in all scenarios.

### 🏛️ Practical Examples
- **Inventory Cache**: [redis_inventory_cache.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/caching/redis_inventory_cache.py) for thread-safe stock deduction.
