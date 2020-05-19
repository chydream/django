
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """ 回收订单 """

    def add_arguments(self, parser):
        """
        argparse

        :param parser:
        :return:
        添加命令参数
        python manage.py update --all()
        python manage.py update --one 20001
        """
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='回收所有超时未支付订单'
        )

        parser.add_argument(
            '--one',
            action='store',
            dest='one',
            default=False,
            help='指定回收订单'
        )

    def handle(self, *args, **options):
        if options['all']:
            self.stdout.write('开始回收订单')
            self.stdout.write('-----------')
            self.stdout.write('处理完成')
        elif options['one']:
            self.stdout.write('指定回收订单{}'.format(options['one']))
            self.stdout.write('-----------')
            self.stdout.write('处理完成')
        else:
            self.stderr.write('指令异常')