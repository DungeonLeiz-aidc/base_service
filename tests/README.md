# 🧪 Test Suite - Đảm bảo Chất lượng / Software QA Strategy

**Mục đích / Purpose**: Thư mục này chứa toàn bộ hệ thống kiểm thử đa lớp, là "lưới an toàn" để đảm bảo ứng dụng luôn hoạt động chính xác theo thiết kế. / This directory houses the comprehensive test suite, acting as the system's "Safety Net" to ensure continuous design fidelity.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Xác thực Đúng đắn**: Đảm bảo logic nghiệp vụ luôn cho kết quả chính xác 100%.
2. **Ngăn chặn Lỗi hồi quy**: Đảm bảo code mới không làm hỏng các tính năng cũ.
3. **Tài liệu hóa bằng Ví dụ**: Cung cấp cách sử dụng thực tế nhất cho các linh kiện.
4. **Đo lường Hiệ năng**: Xác định ngưỡng thời gian xử lý và tải của hệ thống.
5. **Kiểm thử Cô lập**: Tạo môi trường sạch để test mà không ảnh hưởng tới dữ liệu thật.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
tests/
├── unit/               # Kiểm thử cô lập từng linh kiện (Domain, App, v.v.).
├── integration/        # Kiểm thử sự phối hợp giữa các linh kiện (Flow test).
├── manual/             # Các kịch bản kiểm thử thủ công và script hỗ trợ.
└── conftest.py         # Cấu hình chung và Fixtures cho Pytest.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Một hệ thống không có test là một hệ thống không thể bảo trì. Bạn không bao giờ dám sửa code vì sợ làm hỏng thứ gì đó.
- **Why Multi-layered Testing?**: Unit test giúp tìm lỗi nhanh ở từng hàm, Integration test giúp đảm bảo toàn bộ bộ máy (DB, Cache, v.v.) hoạt động trơn tru cùng nhau.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Independence**: Các bài test phải hoàn toàn độc lập với nhau.
- **Fast Feedback**: Ưu tiên Unit test chi tiết vì chúng chạy nhanh hơn Integration test.
- **Mocking Strategy**: Phải dùng Mocks cho các dịch vụ ngoại vi (Stripe, RabbitMQ) trong Unit tests.

### 🏛️ Ví dụ thực tế (Examples)
- **Vận hành**: `make test` để chạy toàn bộ suite.
- **Unit**: [test_order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/unit/domain/test_order.py) kiểm tra logic đơn hàng.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Correctness Verification**: Guarantees that business logic remains 100% accurate.
2. **Regression Prevention**: Shields existing features from breakage during updates.
3. **Living Documentation**: Serves as the definitive guide for technical component usage.
4. **Performance Measurement**: Audits processing speeds and load thresholds.
5. **Isolation Verification**: Enables safe testing without polluting production datasets.

### 📂 Directory Layout
```text
tests/
├── unit/               # Isolated component level verification.
├── integration/        # Component synergy and workflow verification.
├── manual/             # Manual test scripts and scenario definitions.
└── conftest.py         # Shared Pytest configurations and fixtures.
```

### 💡 Context & Why
- **Context**: Systems without tests are untrustworthy. Developers become paralyzed by the fear of causing regression failures.
- **Why Multi-layered Testing?**: Unit tests pinpoint local bugs instantly; Integration tests ensure the architectural plumbing (DB, Cache, etc.) functions as a cohesive unit.

### ⚠️ Process & Constraints (CCE Template)
- **Zero Coupling**: Tests must never depend on each other's execution order.
- **Speed Over Depth**: Prioritize Unit tests for rapid developer feedback loops.
- **Mocking Policy**: External integrations must be strictly Mocked in Unit tests to maintain speed and reliability.

### 🏛️ Practical Examples
- **Execution**: `make test` to verify the entire system.
- **Unit**: [test_order.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/unit/domain/test_order.py) auditing the core Order model.
