# ⚡ Caching & Distribution - Tối ưu Hiệu năng và Đồng bộ / Performance & Consistency

**Mục đích / Purpose**: Danh mục này tập trung vào việc sử dụng bộ nhớ đệm (Cache) để giảm tải cho database và cơ chế Khóa phân tán (Distributed Lock) để đảm bảo tính toàn vẹn dữ liệu trong môi trường nhiều người dùng. / This directory focuses on using Caching to reduce database load and Distributed Locking to ensure data integrity in concurrent user environments.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Caching**: Lưu trữ các kết quả tính toán hoặc truy vấn nặng vào bộ nhớ tốc độ cao (Redis). Thay vì hỏi Database (chậm), chúng ta hỏi Redis (nhanh).
- **Distributed Lock**: Trong hệ thống phân tán, nhiều server có thể cùng xử lý một mặt hàng. Khóa giúp đảm bảo chỉ có một server được phép thay đổi số lượng tồn kho tại một thời điểm, tránh việc bán quá số lượng (Overselling).
- **Time-to-Live (TTL)**: Dữ liệu trong cache không tồn tại mãi mãi. Chúng ta đặt thời hạn để dữ liệu tự động bị xóa, đảm bảo tính cập nhật.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `redis_inventory_cache.py`: Triển khai logic khóa để "giữ hàng" khi khách đang thanh toán, đảm bảo không ai khác có thể mua mất món hàng đó trong vài phút.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Caching**: Stores heavy query results or calculations in high-speed memory (Redis). We query Redis (fast) instead of the Database (slower).
- **Distributed Lock**: In a distributed system, multiple servers might process the same item simultaneously. A lock ensures only one server updates inventory at a time, preventing overselling.
- **Time-to-Live (TTL)**: Cache data shouldn't live forever. We set expiration times to ensure data remains fresh.

### 🏛️ Practical Example
In this project:
- `redis_inventory_cache.py`: Implements locking logic to "reserve" items during checkout, ensuring no other customer can buy the same item for a few minutes.
