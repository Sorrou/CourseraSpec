import argparse
import json


storage_path = ('D:\\Temp\\storage_data')

storage_path = 'D:\\Temp\\storage'
with open (storage_path, 'a') as s:
    s.read()




def get_data():
    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')

    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('None')
