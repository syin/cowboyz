#!/usr/bin/env python

import json


DATA_FILENAME = 'assets/coordinates.json'

EMOJI = {
    "faces": ["1f600", "1f603", "1f604", "1f601", "1f606", "1f605", "1f923", "1f602", "1f642", "1f643", "1f609", "1f60a", "1f607", "1f970", "1f60d", "1f929", "1f618", "1f617", "263a", "1f61a", "1f619", "1f60b", "1f61b", "1f61c", "1f92a", "1f61d", "1f911", "1f917", "1f92d", "1f92b", "1f914", "1f910", "1f928", "1f610", "1f611", "1f636", "1f60f", "1f612", "1f644", "1f62c", "1f925", "1f60c", "1f614", "1f62a", "1f924", "1f634", "1f637", "1f912", "1f915", "1f922", "1f92e", "1f927", "1f975", "1f976", "1f974", "1f635", "1f92f", "1f920", "1f973", "1f60e", "1f913", "1f9d0", "1f615", "1f61f", "1f641", "2639", "1f62e", "1f62f", "1f632", "1f633", "1f97a", "1f626", "1f627", "1f628", "1f630", "1f625", "1f622", "1f62d", "1f631", "1f616", "1f623", "1f61e", "1f613", "1f629", "1f62b", "1f624", "1f621", "1f620", "1f92c", "1f608", "1f47f", "1f480", "2620"]
}


def load_json():
    input_file = open(DATA_FILENAME, "r")
    data = json.load(input_file)
    input_file.close()
    return data


def write_emoji_faces(master_data):
    for emoji in EMOJI["faces"]:
        name, value = next((k, v) for (k, v) in master_data.items() if k.endswith(emoji))
        master_data[name]["size"] = [132, 132]
        master_data[name]["offset"] = [14, 19]

    # EXCEPTIONS
    # face screaming in fear
    # 1f631
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f631"))
    master_data[name]["offset"] = [14, 22]

    # face blowing kiss
    # 1f618
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f618"))
    master_data[name]["offset"] = [14, 19]

    # face with cold sweat
    # 1f613
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f613"))
    master_data[name]["offset"] = [14, 17]

    # cowboy hat
    # 1f920

    # face with finger covering closed lips
    # 1f92b
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f92b"))
    master_data[name]["offset"] = [14, 23]

    # face with look of triumph
    # 1f624
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f624"))
    master_data[name]["offset"] = [14, 22]

    # face with one eyebrow raised
    # 1f928
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f928"))
    master_data[name]["offset"] = [14, 22]

    # face with open mouth vomiting
    # 1f92e
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f92e"))
    master_data[name]["size"] = [148, 148]
    master_data[name]["offset"] = [2, 27]

    # face with stuck out tongue
    # 1f61b
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f61b"))
    master_data[name]["offset"] = [14, 22]

    # face with stuck out tongue and tightly closed eyes
    # 1f61d
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f61d"))
    master_data[name]["offset"] = [14, 22]

    # face with stuck out tongue and winking eye
    # 1f61c
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f61c"))
    master_data[name]["offset"] = [14, 22]

    # grinning face with one large and one small eye
    # 1f92a
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f92a"))
    master_data[name]["offset"] = [24, 22]
    master_data[name]["rotation"] = 15
    master_data[name]["hat_offset"] = [-10, -20]

    # grinning face with star eyes
    # 1f929
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f929"))
    master_data[name]["offset"] = [14, 22]

    # hugging face
    # 1f917
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f917"))
    master_data[name]["offset"] = [14, 22]

    # imp
    # 1f47f
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f47f"))
    master_data[name]["size"] = [134, 134]
    master_data[name]["offset"] = [12, 19]

    # money mouth face
    # 1f911
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f911"))
    master_data[name]["offset"] = [14, 22]

    # rolling on the floor laughing
    # 1f923
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f923"))
    master_data[name]["offset"] = [27, 23]
    master_data[name]["rotation"] = 30
    master_data[name]["hat_offset"] = [-20, -26]

    # shocked face with exploding head
    # 1f92f
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f92f"))
    master_data[name]["size"] = [120, 120]
    master_data[name]["offset"] = [20, 40]

    # skull
    # 1f480
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f480"))
    master_data[name]["size"] = [128, 128]
    master_data[name]["offset"] = [20, 26]
    master_data[name]["hat_size"] = [138, 138]
    master_data[name]["hat_offset"] = [15, 0]

    # skull and crossbones
    # 2620
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("2620"))
    master_data[name]["size"] = [144, 144]
    master_data[name]["offset"] = [12, 12]
    master_data[name]["hat_size"] = [138, 138]
    master_data[name]["hat_offset"] = [15, 0]

    # smiling face with halo
    # 1f607
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f607"))
    master_data[name]["size"] = [126, 126]
    master_data[name]["offset"] = [19, 33]
    master_data[name]["hat_size"] = [140, 140]
    master_data[name]["hat_offset"] = [12, 0]

    # smiling face with horns
    # 1f608
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f608"))
    master_data[name]["size"] = [134, 134]
    master_data[name]["offset"] = [12, 19]

    # smiling face with smiling eyes and hand covering mouth
    # 1f92d
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f92d"))
    master_data[name]["offset"] = [14, 22]

    # thinking face
    # 1f914
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f914"))
    master_data[name]["offset"] = [14, 22]

    # upside down face
    # 1f643
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f643"))
    master_data[name]["rotation"] = 180
    master_data[name]["offset"] = [14, 4]
    master_data[name]["hat_offset"] = [0, -4]

    # zipper mouth face
    # 1f910
    name, value = next((k, v) for (k, v) in master_data.items() if k.endswith("1f910"))
    master_data[name]["offset"] = [16, 19]

    return master_data


def write_output(master_data):
    output_file = open(DATA_FILENAME, "w")
    json.dump(master_data, output_file, indent=4)


def main():

    master_data = load_json()
    master_data = write_emoji_faces(master_data)
    write_output(master_data)


if __name__ == '__main__':
    main()
