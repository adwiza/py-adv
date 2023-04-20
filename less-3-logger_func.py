import gzip
import io
import logging
import os.path


def setup_logger(log_path):
    log_dir = os.path.split(log_path)[0]
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format='[%(asctime)s] %(levelname).1s %(message)s', datefmt='%Y.%m.%d %H:%M:%S' )


def get_log_records(log_path, errors_limit=None):
    open_fn = gzip.open if is_gzip_file(log_path) else io.open
    errors = 0
    records = 0
    with open_fn(log_path, mode='rb') as log_file:
        for line in log_file:
            records += 1
            line = line.decode('utf8')
            record = parse_log_record(line)
            if not record:
                errors += 1
                continue
            yield record


def is_gzip_file(file_path):
    return file_path.split('.')[-1] == 'gz'


def parse_log_record(log_line):
    match = LOG_RECORD_RE.match(log_line)
    if not match:
        logging.error('Unable to parse line: "{}"'.format(log_line.rstrip()))
        return None

    href = match.groupdict()['href']
    request_time = float(match.groupdict()['time'])

    return href, request_time
