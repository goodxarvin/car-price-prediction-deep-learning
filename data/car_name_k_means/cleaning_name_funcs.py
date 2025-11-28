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
    'اقساط', 'اقساطی', 'نقد', 'آپشن', 'وترمز', 'ترمز', 'گانه', 'رینگ', 'کارخانه', 'خودرو', 'سوز', 'تومن', 'تومان', 'هزار', 'عالی',
    'رین', 'فوری', 'عروسک', 'سال', 'تحویل', 'کم', 'نمایندگی', 'با', 'مانیتور', 'پایین', 'قالپاق', 'گازوئیل', 'کارمندی', 'کارمند',
    'گازسوزکارخانه', 'قابل', 'وقابل', 'فروشی', 'صفرخشک', 'پایدار', 'پایداری', 'ثالث', 'شخص', 'بدنه', 'دارد', 'تمام', 'بدون‌رنگ', 'فنی',
    'پر', 'کلاغی', 'پرکلاغی', 'تک', 'لاکاغذی', 'سواری', 'مونتاژ', 'وارداتی', 'واردات', 'یخچال', 'کاپوت', 'فقط', 'شرایط', 'تا', 'درصدنقدمابقی',
    'ماه', 'پارسال', 'فوق', 'سلامت', 'اخر', 'ها', 'آخر', 'اراک', 'ساده', 'سالم', 'دارم', 'روز', 'ارتقاء', 'سود', 'شما', 'برج', 'برای', 'بسیار',
    'یی', 'ایربگ', 'گازسوز', 'دور', 'روزه', 'یکپارچه', 'سامانه', 'همان', 'ثانیه', 'تکسوز', 'لازرورقی', 'بسیارسالم', 'میکنم', 'یا', 'ابشنال',
    'خیلی', 'دیلایت', 'دار', 'خوش', 'روخ', 'رخ', 'شاسی', 'سرحال', 'مدیران', 'موتوری', 'لحظه', 'پلمب', 'استیشن', 'تصادف', 'معمولی', 'آفتاب'
    'افتاب', 'سوختگی', 'دست', 'درجه', 'یک', 'اسپرت', 'لکه', 'یه', 'فرانسه', 'بارنخورده', 'واقعاسالمه', 'ماشین', 'کاملا', 'ثبت', 'نام',
    'سایر', 'لاستیک', 'باتری', 'باطری', 'کمپرسی', 'هفت', 'نفره', 'دریچه', 'cc', 'دگانه', 'داشبورد', 'خط', 'خش', 'پلمپ', 'کار', 'مرتب',
    'ملی', 'بیرنگ', 'شرکت', 'دوگانه‌شرکت‌بیرنگ', 'وسط', 'اتاق', 'نیمه', 'کلکسیونی', 'باز', 'درگاه', 'نقد', 'اقساط', 'نقدو', 'بشرط', 'به',
    'شرط', 'تخفیف', 'پای', 'معامله', 'یخچالدار', 'شرایطی', 'بهمن', 'فورش', 'کره', 'نقدی', 'گردشی', 'ضربه', 'کرد', 'کار', 'الها',
    'ژاپن', 'قصر', 'ژاپنی', 'بعدی', 'کف', 'پا', 'حواله‌', 'صدا', 'سقف', 'کارخونه', 'بزرگ', 'زیر', 'مناسب', 'قیمت', 'پرشتاب', 'شتاب',
    'پر', 'قسطی', 'ترو'
]
colors = [
    'سفید', 'مشکی', 'طوسی', 'نقره‌ای', 'خاکستری', 'آبی', 'قرمز', 'زرشکی', 'سبز', 'بژ',
    'زرد', 'نارنجی', 'قهوه‌ای', 'طلایی', 'موکا', 'یخی', 'نوک‌مدادی', 'دلفینی', 'سیمی', 'مدادی', 'نوک',
    'white', 'black', 'gray', 'grey', 'blue', 'red', 'green', 'silver', 'gold', 'orange', 'brown'
]
years = [y for y in range(1370, 1406)] + [y for y in range(1990, 2026)] + \
    [y for y in range(50, 100)] + [y for y in range(400, 404)
                                   ] + [y for y in range(300, 400)]

models = [y for y in range(400)]


unuseful_words = adjectives + docs_words + colors + years


def filter_unuseful_words(name):
    token = word_tokenize(name)
    for word in token.copy():
        try:
            int_word = int(word)
            if int_word in years or int_word == 1:
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
    rep_jade = delete_dot.replace("یشمی", "")
    delete_silver = rep_jade.replace("نقره ای", "")
    delete_es = delete_silver.replace("اص", "")
    delete_white = delete_es.replace("سفید", "")
    delete_car = delete_white.replace('خودرو', '')
    delete_12 = delete_car.replace("12", "")
    delete_same = delete_12.replace('همان', "")
    delete_cng = delete_same.replace("سی ان جی", "")
    delete_leather_seat = delete_cng.replace("صندلی چرم", "")
    delete_10 = delete_leather_seat.replace("10", "")
    delete_bar = delete_10.replace("بار", "")
    delete_user = delete_bar.replace("مصرف کننده", "")
    delete_yee = delete_user.replace("یی", "")
    delete_polomb = delete_yee.replace("پلمب", "")
    rep_2 = delete_polomb.replace(" دو ", "2")
    rep_3 = rep_2.replace(" سه ", "3")
    rep_4 = rep_3.replace(" چهار ", "4")
    rep_4_alt = rep_4.replace(" چار ", "4")
    rep_5 = rep_4_alt.replace(" پنج ", "5")
    rep_6 = rep_5.replace(" شش ", "6")
    rep_6_alt = rep_6.replace(" شیش ", "6")
    delete_models = rep_6_alt.replace("مدل‌های", "")
    delete_company = delete_models.replace("شرکت", "")
    delete_installments = delete_company.replace("نقدواقساط", "")
    delete_discount = delete_installments.replace("تخفیف پای معامله", "")
    delete_noise = delete_discount.replace("صدا  سیستم برقی فعال", "")
    delete_noice_2 = delete_noise.replace("توربوشارژاتومات اردیبهشت", "")

    final_filtered_name = delete_noice_2.strip().lower()

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
# print(filter_unuseful_words('      رنو تندر e 2 پارس یی'))
# print(filter_unuseful_words(' 207 صفرکیلومتر تحویل همان ثانیه'))
# print(filter_unuseful_words('       پژو 206 تیپ 2 دور'))
# print(filter_unuseful_words('         سمند سورن پلاس تحویلی 12  17'))
# print(filter_unuseful_words(' سمند ای اف‌ سون 1 397'))
