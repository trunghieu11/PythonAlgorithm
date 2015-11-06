#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'trunghieu11'

BUSINESSANDINDUSTRY = ["sản phẩm","cung cấp","hàng","giá","sỉ","loại","lotte","bán","thế giới","toàn quốc","khách hàng","cinema","liên hệ","cửa hàng","tiêu dùng","mua","kinh doanh","online","bán lẻ","dịch vụ","mặt hàng","công ty","siêu thị",]
ENTERTAINMENT = ["cung","ca sĩ","ngày","việt","giải trí","cười","truyện","giải","thích","tên","nhạc","hoàng đạo","thông tin","thuộc","fc","bình","cuộc thi","góc","cập nhật","bảo","chòm sao","chào mừng","truyện cười","blog","truyện ngắn","âm nhạc","cộng đồng","bói","nổi tiếng","hài","kênh","dj","thơ","truyền thuyết","nhật ký","nhật kí","manga","anime"]
FAMILYANDRELATIONSHIPS = ["tình yêu","stt","cảm xúc","cuộc sống","status","chia sẻ","yêu","tâm trạng","yêu thương","ý nghĩa","con","tâm sự","lời","hội","dòng","câu","đểu","chất","hạnh phúc","trái tim","câu chuyện","tim","đọc","viết","nhớ","radio","cha","ba","mẹ","sẻ chia","độc thân","tình bạn","lgbt","cưới","em","anh","tớ","cậu","gia đình","phụ nữ"]
FINESSANDWELLNESS = ["giảm cân","nữ","bí quyết","hiệu quả","kinh nghiệm","mặc","sức khỏe","thuốc","lishou","mỡ","hãng","bưởi","kiến thức","trái","sakura","sắc đẹp","cơ địa","tích luỹ","chăm sóc","y học","dược sĩ","thân hình","y khoa","chị em","điều dưỡng","tác dụng","điều trị"]
FOODANDDRINK = ["cà phê","café","cafe","nhà hàng","trà","quán xá","món","ăn","uống","thương hiệu","mcdonald","tea","coffee","leaf","bean","ra đời","quán ăn","quán","nhu cầu","thưởng thức","coca","tụ điểm","đáp ứng","bánh","thực khách","cola","cầu nối","thức ăn","pizza","donuts","ẩm thực","món ngon"]
HOBBIESANDACTIVITIES = ["tiếng nhật","tiếng anh","tiếng trung","tiếng hàn","học","yêu thích","hát","fan","bài","ca khúc","diễn viên","rap","ráp","đam mê","thần tượng","nghệ thuật","chính phủ","ielts","toefl","ảnh","vẽ","overlays","overlay","xe"]
SHOPPINGANDFASHION = ["thời trang","shop","da","quần","mỹ phẩm","đẹp","làm đẹp","phụ kiện","mụn","chất lượng","giày","túi xách","nắng","váy","dép","parkson","trị","bác sĩ","fashion","tư vấn","noir","áo","trang sức","con gái","uy tín","mua sắm","đầm","kem","vnxk","thẩm mỹ viện","tóc","jewelry","trang điểm","tết tóc","sẹo","xinh","nước hoa"]
SPORTSANDOUTDOORS = ["bóng đá","hâm mộ","scores","cầu","phạt góc","fcvn","thẻ vàng","đăng ký","live","tải","utd","trận","bảng","cristiano","xếp hạng","đội hình","ronaldo","sút","nhận","manchester","fans","cr","hâm","thẻ đỏ","bóng","thống kê"]
TECHNOLOGY = ["asus","công nghệ","số","hệ thống","điện thoại","di động","phát triển","phân phối","thegioididong","com","mỹ","toàn cầu","điện tử","phục vụ","thị trường","trung tâm","quyền lợi","châu á","thương mại","góp phần","máy tính xách tay","laptop","smartphone","smartwatch"]

def match(keyWords, description):
    for s in keyWords:
        if s in description:
            print s
    print "---------------------------------"

def main():
    description = raw_input()
    print "BUISINESS: "
    match(BUSINESSANDINDUSTRY, description)
    print "ENTERTAINMENT: "
    match(ENTERTAINMENT, description)
    print "FAMILY: "
    match(FAMILYANDRELATIONSHIPS, description)
    print "FINESS: "
    match(FINESSANDWELLNESS, description)
    print "FOOD: "
    match(FOODANDDRINK, description)
    print "HOBBIES: "
    match(HOBBIESANDACTIVITIES, description)
    print "SHOPPING: "
    match(SHOPPINGANDFASHION, description)
    print "SPORTS: "
    match(SPORTSANDOUTDOORS, description)
    print "TECHNOLOGY: "
    match(TECHNOLOGY, description)

if __name__ == '__main__':
    main()