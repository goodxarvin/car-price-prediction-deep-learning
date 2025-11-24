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
    'اقساط', 'اقساطی', 'نقد', 'و', 'آپشن', 'وترمز', 'ترمز', 'گانه', 'رینگ'
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
    final_filtered_name = delete_dot.strip().lower()

    return final_filtered_name


# print(filter_unuseful_words('**تیگو 7 پرو پرمیوم صفر*'))
# print(filter_unuseful_words('٪٪ریسپکت 2 پرایم صفرخشک '))
# print(filter_unuseful_words('%%تارا V 4 ال ایکس تیتانیوم'))
# print(filter_unuseful_words('&nbsp; هیوندای اکسنت'))
# print(filter_unuseful_words('تیگو 8 پروe+ . پلاگین هیبرید .'))
# print(filter_unuseful_words('کوییک GXR رینگ آلمینیومی گانه ترمزESC+آپشن'))