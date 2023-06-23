from django.core.management.base import BaseCommand
import pandas as pd
from core.models import *


class Command(BaseCommand):
    help = "import booms"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('udefrika_data_instructor.csv', sep=";")
        for idi, url, title, img, job_title in zip(df.id, df.url, df.title, df.image_100x100, df.job_title):
            models_instructor = Vendor(id=idi, title=title, image=img, url=url, job_title=job_title, user_id=1, cover_image='user_1/vendor-header-bg_v5YKnjd.png')
            try:
                models_instructor.save()
            except:
                pass
            print(idi, " ",url, " ",title," ",img," ",job_title)

        dfc = pd.read_csv('udefrika_data_course.csv', sep=";")
        i = 1
        for idc, url, avg_rating, price, user, category, image, language, description, gift_url, headline, vendor, instructional_level in zip(dfc.id_udemy, dfc.url, dfc.avg_rating, dfc.price, dfc.user, dfc.category, dfc.image, dfc.language, dfc.description, dfc.gift_url, dfc.headline, dfc.vendor, dfc.instructional_level):
            sku = "sku0"+str(i)
            models_course = Product(id=idc, title=(url.replace("https://www.udemy.com/course/","").replace("/","").replace("-"," ")).upper(), image=image, url=url, vendor_id=vendor, user_id=1, language=language, category_id=category, gift_url=gift_url, instructional_level=instructional_level, avg_rating=avg_rating, headline=headline, price=price, old_price=price, date="2023-06-23 04:38:39.038153", sku=sku, description=description)

            try:
                models_course.save()
            except:
                pass

            i+=1

            print(idc, " ",url, " "," ",image," ",language)
