# 🧪 Manual Tests - Kiểm thử Thực tế & Đặc biệt / Exploratory & Edge-case Testing

**Mục đích / Purpose**: Manual Tests cho phép lập trình viên kiểm tra các tình huống phức tạp khó mô phỏng tự động, hoặc để trực quan hóa hành vi hệ thống trong môi trường thực tế. / Manual Tests allow developers to verify complex scenarios difficult to automate or to visualize system behavior in real-world environments.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Kiểm thử Tranh chấp (Concurrency)**: Kiểm tra các lỗi xảy ra khi có hàng ngàn yêu cầu cùng lúc (Vd: tranh mua món hàng cuối).
2. **Xác thực UX/DX**: Đảm bảo các thông báo lỗi và tài liệu Swagger dễ hiểu với người sử dụng.
3. **Khám phá Lỗi (Exploratory)**: Tìm kiếm các lỗi tiềm ẩn thông qua việc thử nghiệm tự do không theo kịch bản cứng.
4. **Kiểm tra Vận hành**: Chạy thực tế các script Seed dữ liệu và các tool CLI của hệ thống.
5. **Xác minh Resilience**: Chủ động tắt Database/Redis để xem hệ thống hồi phục như thế nào.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Có những kịch bản (như Race Condition) cực kỳ khó viết automation test một cách ổn định. Việc viết script "bắn phá" (Stress test) thủ công đôi khi hiệu quả hơn.
- **Why Manual Scripts?**: Cung cấp một bộ công cụ cho lập trình viên để "sờ tận tay, thấy tận mắt" các linh kiện bảo vệ (Vd: Distributed Lock) đang hoạt động.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Môi trường riêng**: Chỉ được chạy các script này trong môi trường Dev/Local. Cấm chạy trên Prod.
- **Dữ liệu mẫu**: Sử dụng bộ dữ liệu tại `seed/` để tạo môi trường giả lập giàu thông tin.
- **Log Review**: Phải theo dõi `logs/` trong lúc chạy để phát hiện các lỗi ngầm.

### 🏛️ Ví dụ thực tế (Examples)
- **Concurrency Test**: [test_concurrency.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/manual/test_concurrency.py) chứng minh cơ chế chòng Overselling.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Contention Testing (Concurrency)**: Verifies behavior under high load (e.g., race for the last stock item).
2. **UX/DX Validation**: Ensures that API responses and documentation (Swagger) remain intuitive.
3. **Exploratory Testing**: Identifies hidden system bugs through unscripted, creative trial.
4. **Operational Verification**: Validates high-impact scripts like Data Seeding and CLI tools.
5. **Resilience Verification**: Proactively downs DB/Redis instances to monitor system recovery patterns.

### 💡 Context & Why
- **Context**: Some scenarios (like deep race conditions) are notoriously unstable to automate. Specialized "stress" scripts are often more insightful.
- **Why Manual Scripts?**: Empowers developers to manually witness and verify protection mechanisms like Distributed Locks in action.

### ⚠️ Process & Constraints (CCE Template)
- **Environment Isolation**: These scripts are strictly for Dev/Local environments. Execution on Production is forbidden.
- **Rich Seed Data**: Leverage the `seed/` scripts to generate realistic test scenarios.
- **Real-time Monitoring**: Continuous log inspection (monitoring `logs/`) is mandatory during manual runs.

### 🏛️ Practical Examples
- **Concurrency Test**: [test_concurrency.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/manual/test_concurrency.py) proving overselling prevention.
