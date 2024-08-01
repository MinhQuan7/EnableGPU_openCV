import cv2

def main():
    # Mở kết nối tới camera USB (thường là device 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Không thể mở camera")
        return

    print("Camera đã được mở thành công")

    while True:
        # Đọc frame từ camera
        ret, frame = cap.read()

        if not ret:
            print("Không thể nhận frame (stream kết thúc?). Exiting ...")
            break

        # In kích thước frame để kiểm tra
        print("Frame size:", frame.shape)

        # Hiển thị frame
        cv2.imshow('USB Camera', frame)

        # Thoát khi nhấn phím 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
