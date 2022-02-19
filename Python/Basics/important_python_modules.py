import datetime
import os
import sys
import time

from functions import foo


def work_with_time():
    print(f'time.altzone - {time.altzone}')
    print(f'time.asctime() - {time.asctime()}')
    print(f'The function time.clock() has been removed, after having been deprecated since Python 3.3:'
          f'\nuse {time.perf_counter()} or {time.process_time()}')
    print('time.ctime(secs) - преобразует время, выраженное в секундах с начала эпохи в строку вида '
          f'{time.ctime()}')
    print(f'{time.daylight} - не 0, если определено, зимнее время или летнее')
    print(f'time.gmtime() {time.gmtime()}')
    print(f'time.localtime() - {time.localtime()}')
    print(f'struct_time object - {time.struct_time((2022, 2, 17, 8, 0, 0, 0, 0, 0))}')
    print(f'time.mktime() - {time.mktime((2022, 2, 17, 8, 0, 0, 0, 0, 0))}')
    time.sleep(5)
    print(time.strftime('%a %A'))
    print(time.time())
    print(f'time.timezone - смещение местного часового пояса в секундах к западу от нулевого меридиана. '
          'Если часовой пояс находится восточнее, смещение отрицательно.')
    print(time.tzname)


def work_with_datetime():
    date = datetime.date(year=2022, month=2, day=18)
    time = datetime.time()
    now = datetime.datetime.now()
    print(f'{date} '
          '- стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.')
    print(f'{time}  datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)'
          '- стандартное время, не зависит от даты. '
          'Атрибуты: hour, minute, second, microsecond, tzinfo.')
    print(f'{now - datetime.timedelta(days=2)} - разница между двумя моментами времени, с точностью до микросекунд.')
    print(dir(datetime.datetime))

    d = datetime.datetime(year=2022, month=2, day=18)
    print(f'd.today() - {d.today()}')
    print(f'd.now() - {d.now()}')
    print(f'd.combine(date, time) - {d.combine(date, time)}')
    print(f'd.strptime("18/2/22 11:30", "%d/%m/%y %H:%M") - {d.strptime("18/2/22 11:30", "%d/%m/%y %H:%M")}')
    print(f'd.strftime("%d/%m/%y %H:%M") - {d.strftime("%d/%m/%y %H:%M")}')
    print(f'd.date() - {d.date()}')
    print(f'd.time() {d.time()}')
    print(f'd.replace() - {d.replace()}')
    print(f'd.timetuple() - {d.timetuple()}')
    print(f'd.toordinal() - {d.toordinal()}')
    print(f'd.timestamp() - {d.timestamp()}')
    print(f'd.weekday() - {d.weekday()}')
    print(f'd.isoweekday() - {d.isoweekday()}')
    print(f'd.isocalendar() - {d.isocalendar()}')
    print(f'd.isoformat() - {d.isoformat()}')
    print(f'd.ctime() - {d.ctime()}')


def work_with_os():
    print(os.name)
    print(os.environ)
    print(os.getlogin())
    print(os.getpid())
    print(os.uname())
    print(os.getcwd())
    print(os.listdir())
    print(os.sync())
    print(list(os.walk(os.getcwd(), topdown=True, onerror=None, followlinks=False)))
    os.system('date')


def work_with_sys():
    print(sys.argv)
    print(sys.byteorder)
    print(sys.builtin_module_names)
    print(sys.call_tracing(foo, (1, 2, 3, 4)))
    print(sys.copyright)
    print(sys.exc_info())
    print(sys.exec_prefix)
    print(sys.executable)
    print(sys.flags)
    print(sys.float_info)
    print(sys.float_repr_style)
    print(sys.getfilesystemencoding())
    print(sys.getdlopenflags())
    print(sys.getfilesystemencoding())
    print(sys.getrefcount(5))
    print(sys.getrecursionlimit())
    print(sys.getsizeof(int))
    print(sys.getswitchinterval())
    print(sys.hash_info)
    print(sys.hexversion)
    print(sys.implementation)
    print(sys.int_info)
    print(sys.intern('some str'))
    print(sys.modules)
    print(sys.path)
    print(sys.path_importer_cache)
    print(sys.platform)


if __name__ == '__main__':
    work_with_time()
    work_with_datetime()
    work_with_os()
    work_with_sys()
