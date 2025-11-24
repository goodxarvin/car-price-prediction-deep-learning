from hazm import word_tokenize


# excess and unuseful data

adjectives = ['آماده‌',
              'تمیز', 'سالم', 'نو', 'کم کار', 'کمکار', 'بی رنگ', 'بی‌رنگ', 'بینظیر', 'فول', 'فول آپشن',
              'فول‌اپشن', 'فولاپشن', 'لاکچری', 'زیره پا نخورده', 'عروس', 'فابریک', 'کارکرده', 'بی‌خط', 'بی خط',
              'در', 'حد', 'صفر', 'درحدصفر', 'درحد', 'بینقص', 'سفارشی', 'دوگانه', 'تک گانه', 'دورنگ', 'بیمه دار',
              'آماده تحویل', 'تمیز و مرتب', 'فنی سالم', 'خوش رکاب', 'بدون', 'رنگ', 'بدون خط و خش', 'آماده', 'سفر', 'تک‌', 'برگ', 'مدل', 'دوگانه سوز', 'سوز', '،', 'حواله', 'بی',
              'خرج', 'سیلندر', 'توربو', 'شارژ', 'خانگی', 'تازه', 'شده', 'کامل', 'موتور', 'جدید', 'استثنایی', 'ارتقا', 'یافته', 'فلز', 'اپشنال', 'آپشنال', 'شرط', 'به', 'اسفند', 'سفارشی',
              'تعمیر', 'انژکتور', 'صفر', 'خشک', 'واقعی', 'فروش', 'معاوضه', 'و', 'خونگی', 'بیرنگ', 'کولر', 'شرکتی', 'جدید', 'بورسی', 'طلا', 'جدید', 'سندآزاد', 'سند', 'آزاد', 'ازاد'
              ]
docs_words = [
    'تک برگ', 'سند تک برگ', 'سند', 'کارکرد', 'بیمه', 'برگه', 'کارشناسی', 'برگه', 'قولنامه', 'مالک',
    'مدارک کامل', 'برگه کمپانی', 'تخفیف بیمه', 'سال تخفیف', 'بدون خلافی', 'پلاک ملی', 'بنزینی',
    'دوگانه سوز', 'دوگانه‌سوز', 'دوگانه', 'حواله', 'مدرک', 'مدارک', 'جزییات', 'اسقاطی', 'کاربراتور', 'کاربرات',
    'آبشنال', 'کیلومتر', '(', ')', 'زیمنس', 'هرمزگان ', 'بندرلنگه', 'گاز', 'گولر', 'بیمه', ',', 'Lx,بیمه', '**', '*',
    'اقساط', 'اقساطی', 'نقد', 'و', 'آپشن', 'وترمز', 'ترمز', 'گانه', 'رینگ', 'کارخانه', 'خودرو', 'سوز', 'تومن', 'تومان', 'هزار', 'عالی',
    'رین', 'فوری', 'عروسک', 'سال', 'تحویل', 'کم', 'نمایندگی', 'با', 'مانیتور', 'پایین', 'قالپاق', 'گازوئیل', 'کارمندی', 'کارمند',
    'گازسوزکارخانه', 'قابل', 'وقابل', 'فروشی', 'صفرخشک', 'پایدار', 'پایداری', 'ثالث', 'شخص', 'بدنه', 'دارد', 'تمام', 'بدون‌رنگ', 'فنی',
    'پر', 'کلاغی', 'پرکلاغی', 'تک', 'لاکاغذی', 'سواری', 'مونتاژ', 'وارداتی', 'واردات', 'یخچال', 'کاپوت', 'فقط', 'شرایط', 'تا', 'درصدنقدمابقی',
    'ماه', 'پارسال', 'فوق', 'سلامت', 'اخر', 'آخر', 'اراک', 'ساده', 'سالم', 'دارم', 'روز', 'ارتقاء', 'سود', 'شما', 'برج', 'برای', 'بسیار',
    'یی'
]
colors = [
    'سفید', 'مشکی', 'طوسی', 'نقره‌ای', 'خاکستری', 'آبی', 'قرمز', 'زرشکی', 'سبز', 'بژ',
    'زرد', 'نارنجی', 'قهوه‌ای', 'طلایی', 'موکا', 'یخی', 'نوک‌مدادی', 'دلفینی', 'سیمی',
    'white', 'black', 'gray', 'grey', 'blue', 'red', 'green', 'silver', 'gold', 'orange', 'brown'
]
years = [y for y in range(1370, 1406)] + [y for y in range(1990, 2026)] + \
    [y for y in range(50, 100)] + [y for y in range(400, 404)]

models = [y for y in range(400)]


unuseful_words = adjectives + docs_words + colors + years


def filter_unuseful_words(name):
    token = word_tokenize(name)
    for word in token.copy():
        try:
            int_word = int(word)
            if int_word in years:
                token.remove(word)

            elif int_word in models:
                for i, num in enumerate(token):
                    if word == num:
                        token[i] = str(int_word)

        except:
            if word in unuseful_words:
                token.remove(word)

    delete_star = " ".join(token).replace("*", "")
    delete_p_s = delete_star.replace("(", "")
    delete_p_e = delete_p_s.replace(")", "")
    delete_mines = delete_p_e.replace("-", "")
    delete_ = delete_mines.replace('_', '')
    delete_slash = delete_.replace("/", "")
    delete_b_slash = delete_slash.replace("\\", "")
    delete_in = delete_b_slash.replace("»", "")
    delete_out = delete_in.replace("«", "")
    delete_percent = delete_out.replace("٪", "")
    delete_en_percent = delete_percent.replace("%", "")
    delete_in_start = delete_en_percent.replace("<", "")
    delete_out_end = delete_in_start.replace(">", "")
    delete_semi_colon = delete_out_end.replace(";", "")
    delete_colon = delete_semi_colon.replace(":", "")
    delete_nbsp = delete_colon.replace("&nbsp", "")
    delete_nbsp_more = delete_nbsp.replace("&nbsp;&nbsp;", "")
    delete_plus = delete_nbsp_more.replace("+", "")
    delete_dot = delete_plus.replace(".", "")
    rep_h = delete_dot.replace("اچ", "h")
    delete_silver = rep_h.replace("نقره ای", "")
    delete_es = delete_silver.replace("اص", "")
    delete_white = delete_es.replace("سفید", "")
    delete_car = delete_white.replace('خودرو', '')
    final_filtered_name = delete_car.strip().lower()

    return final_filtered_name


# print(filter_unuseful_words('کوییک دنده‌ای r فروشی وقابل'))
# print(filter_unuseful_words('برلیانس اچ 230 دنده'))
# print(filter_unuseful_words('سمندlx ef 7 گازسوزکارخانه کارمندی'))
# print(filter_unuseful_words(' سمند ef 7 سورن پلاس با مانیتور'))
# print(filter_unuseful_words('پژو پارس عالی هزار تومن'))
# print(filter_unuseful_words('206 تیپ ۲'))
# print(filter_unuseful_words('خودرو فیدلیتی 7 نفره فوری'))
# print(filter_unuseful_words('  پژو پارس سال عروسک'))
# print(filter_unuseful_words('رانا پلاس تحویل کم'))
# print(filter_unuseful_words(' پژو ۴۰۵ لاکاغذی'))
# print(filter_unuseful_words(' پژو ۴۰۵ پرکلاغی'))
# print(filter_unuseful_words(' سوزوکی گراند ویتارا مونتاژ'))
# print(filter_unuseful_words('پژو 206 تیپ 2 فقط 1 کاپوت یخچال'))
# print(filter_unuseful_words('اس دی v 8 ۳۰ درصدنقدمابقی شرایط تا 4 ماه'))
# print(filter_unuseful_words('کوییک دنده‌ای rسفید'))
