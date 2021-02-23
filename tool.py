import os


def get_file_name(path, file_type=0):
    list_data = path.split('/')
    file_all_name = list_data[len(list_data)-1]
    file_name = file_all_name.split('.')
    if file_type == 1:
        return file_all_name
    else:
        return file_name[0]


def to_pcm_by_command(filename):
    name = filename
    file_name = get_file_name(filename)
    tmp = os.getcwd() + '/tmp/'
    command = './ffmpegg/bin/ffmpeg -y  -i ' + name + ' -acodec pcm_s16le -f s16le -ac 1 -ar 16000 '+tmp + file_name + '.pcm'
    result = os.system(command)
    return result
