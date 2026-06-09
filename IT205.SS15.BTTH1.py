# PHÂN TÍCH VÀ THIẾT KẾ 

# 1. Phân tích biến Global và Local
#
# Biến Global:
# - inventory_stock:
#   + Được khai báo ngoài hàm.
#   + Dùng để lưu số lượng sản phẩm tồn kho hiện tại.
#   + Được nhiều chức năng sử dụng và cập nhật.
#
# - total_revenue:
#   + Được khai báo ngoài hàm.
#   + Dùng để lưu tổng doanh thu toàn hệ thống.
#   + Được cập nhật sau mỗi lần bán hàng thành công.
#
# - is_run_true:
#   + Điều khiển vòng lặp chạy menu chương trình.
#
#
# Biến Local:
# - choice:
#   + Chỉ tồn tại trong hàm check_input_selection().
#   + Lưu lựa chọn menu của người dùng.
#
# - quantity:
#   + Chỉ tồn tại trong hàm check_quantity().
#   + Lưu số lượng sản phẩm nhập vào.
#
# - price:
#   + Chỉ tồn tại trong hàm check_price().
#   + Lưu giá bán sản phẩm.
#
# - temporary_total_amount:
#   + Chỉ tồn tại trong hàm processed_into_money().
#   + Lưu tổng tiền tạm tính trước giảm giá và VAT.
#
# - discount:
#   + Biến cục bộ dùng để xác định mức giảm giá.
#
# - vat:
#   + Biến cục bộ dùng để tính thuế VAT.
#
# - final_total:
#   + Chỉ dùng trong chức năng bán hàng.
#   + Lưu tổng tiền cuối cùng khách phải thanh toán.
#
#
# 2. Thiết kế luồng xử lý chương trình
#
# Chức năng 1: Nhập thêm hàng
# - Người dùng nhập số lượng hàng cần thêm.
# - Kiểm tra dữ liệu hợp lệ:
#   + Phải là số nguyên.
#   + Phải lớn hơn 0.
# - Gọi hàm import_more_goods().
# - Cập nhật inventory_stock.
# - In thông báo nhập hàng thành công.
#
#
# Chức năng 2: Bán hàng
# - Người dùng nhập:
#   + Số lượng sản phẩm muốn mua.
#   + Giá bán sản phẩm.
#
# - Kiểm tra:
#   + Dữ liệu phải là số hợp lệ.
#   + Giá và số lượng phải lớn hơn 0.
#   + Không được vượt quá tồn kho.
#
# - Nếu hợp lệ:
#   + Gọi hàm processed_into_money().
#   + Tính:
#       temporary_total_amount = quantity * price
#       discount = 10% nếu hóa đơn >= 1000
#       vat = 8%
#       final_total = sau giảm giá + VAT
#
# - Sau đó:
#   + Trừ tồn kho.
#   + Cộng doanh thu vào total_revenue.
#   + In hóa đơn chi tiết.
#
#
# Chức năng 3: Báo cáo tổng quan
# - Gọi hàm print_report().
# - Hiển thị:
#   + Tồn kho hiện tại.
#   + Tổng doanh thu.
#
#
# Chức năng 4: Thoát chương trình
# - Đổi is_run_true = False.
# - Kết thúc vòng lặp while.
#
#
# 3. Xử lý Edge Cases
#
# Edge Case 1:
# - Người dùng nhập số âm hoặc bằng 0.
# - Hệ thống báo:
#   "Dữ liệu nhập vào phải lớn hơn 0."
#
#
# Edge Case 2:
# - Người dùng nhập chữ thay vì số.
# - Hệ thống dùng try-except để bắt lỗi ValueError.
#
#
# Edge Case 3:
# - Người dùng mua vượt quá tồn kho.
# - Hệ thống báo:
#   "Không đủ hàng trong kho."
#
#
# Edge Case 4:
# - Người dùng chọn menu ngoài phạm vi 1-4.
# - Hệ thống yêu cầu nhập lại.
#
#
# 4. Thiết kế hàm
#
# check_input_selection()
# - Kiểm tra lựa chọn menu.
# - Trả về lựa chọn hợp lệ.
#
# check_quantity(content)
# - Kiểm tra số lượng nhập vào.
# - Trả về số lượng hợp lệ.
#
# check_price()
# - Kiểm tra giá bán.
# - Trả về giá hợp lệ.
#
# import_more_goods(stock, quantity)
# - Cộng thêm hàng vào kho.
# - Trả về tồn kho mới.
#
# processed_into_money(quantity, price)
# - Tính:
#   + Tạm tính
#   + Giảm giá
#   + VAT
# - Trả về các giá trị hóa đơn.
#
# print_report()
# - In báo cáo doanh thu và tồn kho.

# Hệ Thống Quản Lý Kho Hàng & Doanh Thu (TechStore Inventory)

inventory_stock = 100
total_revenue = 0.0
is_run_true = True


def check_input_selection():
    """
    Kiểm tra lựa chọn menu hợp lệ.
    """

    while True:
        try:
            choice = int(input("Chọn chức năng (1-4): "))

            if choice not in (1, 2, 3, 4):
                print("Lựa chọn của bạn không tồn tại!")
                continue

            return choice

        except ValueError:
            print("Vui lòng nhập số nguyên!")


def check_quantity(content):
    """
    Kiểm tra số lượng nhập vào hợp lệ.
    """

    while True:
        try:
            quantity = int(input(f"Số lượng hàng {content}: "))

            if quantity <= 0:
                print("Số lượng hàng hóa phải lớn hơn 0!")
                continue

            return quantity

        except ValueError:
            print("Vui lòng nhập số nguyên!")


def check_price():
    """
    Kiểm tra giá bán hợp lệ.
    """

    while True:
        try:
            price = int(input("Giá bán: "))

            if price <= 0:
                print("Giá bán phải lớn hơn 0!")
                continue

            return price

        except ValueError:
            print("Vui lòng nhập số nguyên!")


def add_stock(stock, quantity):
    """
    Thêm hàng vào kho.
    """

    stock += quantity
    return stock


def calculate_final_price(quantity, price):
    """
    Tính hóa đơn cuối cùng.
    """

    temporary_total_amount = quantity * price

    discount = 0.1 if temporary_total_amount >= 1000 else 0

    discount_amount = temporary_total_amount * discount

    vat = (temporary_total_amount - discount_amount) * 0.08

    final_total = (
        temporary_total_amount
        - discount_amount
        + vat
    )

    return (
        temporary_total_amount,
        discount_amount,
        vat,
        final_total
    )


def process_sale(stock, revenue, quantity, final_total):
    """
    Xử lý bán hàng:
    - Trừ tồn kho
    - Cập nhật doanh thu
    """

    stock -= quantity
    revenue += final_total

    return stock, revenue


def print_report():
    """
    Hiển thị báo cáo hệ thống.
    """

    print("\n" + " BÁO CÁO KINH DOANH ".center(50, "="))
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.1f}")


while is_run_true:

    print("\n" + " TECHSTORE MANAGEMENT SYSTEM ".center(50, "="))
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print("=" * 50)

    choice = check_input_selection()

    match choice:

        case 1:

            content = "muốn thêm vào kho"

            add_quantity = check_quantity(content)

            inventory_stock = add_stock(
                inventory_stock,
                add_quantity
            )

            print(f"Đã nhập thành công: {add_quantity} sản phẩm")
            print(f"Tồn kho hiện tại: {inventory_stock}")

        case 2:

            print("\n" + " BÁN HÀNG ".center(50, "="))

            content = "muốn mua"

            buy_quantity = check_quantity(content)

            if buy_quantity > inventory_stock:
                print(
                    f"Không đủ hàng trong kho! "
                    f"Tồn kho hiện tại: {inventory_stock}"
                )
                continue

            price = check_price()

            (
                temporary_total_amount,
                discount_amount,
                vat,
                final_total
            ) = calculate_final_price(
                buy_quantity,
                price
            )

            inventory_stock, total_revenue = process_sale(
                inventory_stock,
                total_revenue,
                buy_quantity,
                final_total
            )

            print("\n-> Hóa đơn chi tiết:")
            print(f"Số lượng: {buy_quantity}")
            print(f"Đơn giá: ${price:.1f}")
            print(f"Tạm tính: ${temporary_total_amount:.1f}")
            print(f"Giảm giá: ${discount_amount:.1f}")
            print(f"VAT (8%): ${vat:.1f}")
            print("-" * 50)
            print(f"Tổng thanh toán: ${final_total:.1f}")
            print("Đã bán thành công!")

        case 3:

            print_report()

        case 4:

            print("Thoát chương trình...")
            is_run_true = False

