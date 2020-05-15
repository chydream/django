import os
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse

from djangoDemo import settings


class VerifyCode(object):
    def __init__(self, dj_request):
        self.dj_request = dj_request
        self.img_width = 100
        self.img_height = 30
        self.code_len = 4
        self.session_key = 'verify_code'

    def gen_code(self):
        code = self.__get_vcode()
        self.dj_request.session[self.session_key] = code
        font_color = ['black', 'brown', 'red', 'brown', 'green', 'blue']
        bg_color = (random.randrange(230, 255), random.randrange(230, 255), random.randrange(230, 255))
        font_path = os.path.join(settings.BASE_DIR, 'static/fonts/timesbi.ttf')
        # print(font_path)
        im = Image.new('RGB', (self.img_width, self.img_height), bg_color)
        draw = ImageDraw.Draw(im)
        for i in range(random.randrange(1, int(self.code_len/2)+1)):
            line_color = random.choice(font_color)
            point = (
                random.randrange(0,self.img_width*0.2),
                random.randrange(0, self.img_height),
                random.randrange(self.img_width-self.img_width*0.2, self.img_width),
                random.randrange(0, self.img_height),
            )
            width = random.randrange(1, 4)
            draw.line(point, fill=line_color, width=width)

        for index, char in enumerate(code):
            code_color = random.choice(font_color)
            font_size = random.randrange(15,25)
            font = ImageFont.truetype(font_path, font_size)
            point = (
                index*self.img_width/self.code_len,
                random.randrange(0, self.img_height/3)
            )
            draw.text(point, char, font=font, fill=code_color)

        buf = BytesIO()
        im.save(buf, 'gif')
        return HttpResponse(buf.getvalue(), 'image/gif')

    def __get_vcode(self):
        random_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz23456789'
        code = random.sample(list(random_str), self.code_len)
        code = ''.join(code)
        return code

    def validate_code(self, code):
        code = str(code).lower()
        vcode = self.dj_request.session.get(self.session_key, '')
        return vcode.lower() == code
