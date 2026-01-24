# 🧪 Unit Testing - Kiểm thử Cô lập / Component Level Verification

**Mục đích / Purpose**: Thư mục này chứa các bài kiểm thử đơn vị (Unit Tests), tập trung vào việc xác minh tính đúng đắn của từng lớp, từng hàm một cách cô lập hoàn toàn. / This directory houses Unit Tests, focusing on the isolated verification of individual classes and functions.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Kiểm thử Cô lập**: Đảm bảo từng linh kiện hoạt động đúng mà không cần đến database hay network thật.
2. **Thực thi Biên độ (Edge Case Testing)**: Kiểm tra các giá trị biên (Vd: số lượng bằng 0, giá tiền âm).
3. **Mô phỏng Phụ thuộc (Mocking/Faking)**: Thay thế các dịch vụ thật bằng các đối tượng giả để kiểm soát kết quả.
4. **Phản hồi Tức thì**: Phải chạy cực nhanh (dưới 1 giây) để lập trình viên có thể kiểm tra liên tục.
5. **Đảm bảo Tính hợp nhất**: Phát hiện sớm các thay đổi logic làm sai lệch hợp đồng giữa các tầng.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
unit/
├── domain/             # Kiểm thử thực thể và logic lõi (Order, Product).
├── application/        # Kiểm thử luồng điều phối (Service, Business scenarios).
├── infrastructure/     # Kiểm thử các logic kỹ thuật (Cache keys, Mappers).
└── interface/          # Kiểm thử logic giao tiếp (Schemas, Redaction).
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Nếu bạn cần một database thật để test logic tính tiền, bài test đó sẽ rất chậm và khó thiết lập. Cô lập (Unit testing) giải quyết triệt để vấn đề này.
- **Why Unit Tests First?**: Đây là lớp phòng thủ đầu tiên. Nó giúp bạn tự tin rằng "viên gạch" của mình đã vững chắc trước khi xây cả ngôi nhà.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Pure Isolation**: Cấm tuyệt đối việc gọi database, redis hay rabbitmq thật tại đây.
- **Single Assert**: Mỗi bài test nên tập trung xác minh một hành vi duy nhất.
- **Speed**: Tổng thời gian chạy unit test cho toàn dự án nên giữ ở mức vài giây.

### 🏛️ Ví dụ thực tế (Examples)
- **Domain Test**: [test_order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/unit/domain/test_order.py) kiểm tra logic tính toán mà không cần DB.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Isolated Verification**: Ensures components function correctly without requiring live DBs or Network calls.
2. **Edge Case Validation**: Rigorously tests boundary values (e.g., zero quantity, negative prices).
3. **Mocking & Faking**: Swaps real infrastructure for controlled Mock objects.
4. **Instant Feedback**: Optimized for speed (sub-second execution) for developer efficiency.
5. **Contract Integrity**: Detects logic regressions that break inter-layer communication rules.

### 📂 Directory Layout
```text
unit/
├── domain/             # Testing core entities and behaviors (Order, Product).
├── application/        # Testing use-case orchestration and scenarios.
├── infrastructure/     # Testing technical mappers, cache keys, and clients.
└── interface/          # Testing communication schemas and redaction logic.
```

### 💡 Context & Why
- **Context**: Testing pricing logic should not require a live database. Unit testing solves this setup overhead by isolating the logic.
- **Why Unit Tests First?**: The first line of defense. Ensures each "brick" is solid before assembling the entire structure.

### ⚠️ Process & Constraints (CCE Template)
- **Absolute Purity**: Real-world infrastructure (Postgres, Redis, RabbitMQ) is strictly prohibited here.
- **Single Assertion**: Focus each test case on one specific behavior or outcome.
- **Speed Threshold**: The entire unit suite should complete within a few seconds.

### 🏛️ Practical Examples
- **Domain Test**: [test_order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/unit/domain/test_order.py) verifying calculations in total isolation.
