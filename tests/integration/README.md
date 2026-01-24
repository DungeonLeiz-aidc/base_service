# 🧪 Integration Tests - Kiểm thử Tích hợp / Component Coordination

**Mục đích / Purpose**: Integration Tests xác minh rằng các thành phần khác nhau của hệ thống có thể "nói chuyện" với nhau chính xác. Chúng kiểm tra sự phối hợp giữa API, Service và Database. / Integration Tests verify that different system components interact correctly, testing the coordination between API, Services, and actual Databases.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Xác thực Luồng (Workflow Validation)**: Kiểm tra một kịch bản người dùng trọn vẹn (Vd: nhận yêu cầu -> lưu DB -> bắn sự kiện).
2. **Kiểm tra Kết nối (Wiring Check)**: Đảm bảo các cấu hình Dependency Injection và kết nối hạ tầng hoạt động đúng.
3. **Đảm bảo Nhất quán Dữ liệu**: Xác minh dữ liệu được lưu vào Database thực khớp chính xác với yêu cầu đầu vào.
4. **Phát hiện Lỗi Biên (Edge Integration)**: Tìm các lỗi phát sinh tại ranh giới giữa hai hệ thống (Vd: API Schema không khớp Service DTO).
5. **Môi trường Kiểm soát**: Chạy trên các database test tạm thời để đảm bảo không rác dữ liệu production.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Ngay cả khi từng "viên gạch" (Unit) hoạt động tốt, "ngôi nhà" (Hệ thống) vẫn có thể đổ nếu xi măng (Kết nối) không chắc.
- **Why Integration Tests?**: Đây là lớp quan trọng nhất để chứng minh rằng toàn bộ "bộ máy" kỹ thuật đã được lắp ráp đúng quy trình.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **DB Clean-up**: Mọi dữ liệu tạo ra trong quá trình test phải được dọn sạch sau khi kết thúc.
- **Mock External**: Chỉ Mock các dịch vụ bên ngoài (Stripe, Email), còn DB, Cache nội bộ phải dùng hàng thật (hoặc bản Test thực).
- **Setup Reality**: Phải nạp đầy đủ các cấu hình (Settings) như lúc chạy thật.

### 🏛️ Ví dụ thực tế (Examples)
- **Flow Test**: [test_order_flow.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/integration/test_order_flow.py) mô phỏng một lần đặt hàng thật từ API xuống DB.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Workflow Validation**: Verifies end-to-end user scenarios (e.g., Request -> Persistence -> Notification).
2. **Wiring Check**: Ensures Dependency Injection and infrastructure wiring are correctly configured.
3. **Data Integrity Assurance**: Verifies that live database state accurately reflects incoming business requests.
4. **Edge Integration Detection**: Identifies failures at the boundaries between layers (e.g., Schema vs. DTO mismatches).
5. **Controlled Environment**: Executes against temporary test databases to prevent production data pollution.

### 💡 Context & Why
- **Context**: Even if every "brick" (Unit) is perfect, the "house" (System) collapses if the mortar (Connections) is weak.
- **Why Integration Tests?**: The definitive proof that the entire technical "engine" has been assembled according to architectural rules.

### ⚠️ Process & Constraints (CCE Template)
- **Mandatory Clean-up**: All experimental data must be purged from the test database post-execution.
- **Selective Mocking**: Mock only external providers (Stripe, Mail); internal infra (DB, Cache) must be real test instances.
- **Real Settings**: Tests must leverage the actual configuration loader for environment setup.

### 🏛️ Practical Examples
- **Flow Test**: [test_order_flow.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/tests/integration/test_order_flow.py) simulating a live order trajectory from API to DB.
