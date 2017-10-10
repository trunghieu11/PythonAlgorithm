problem_name = "ColorfulGarden"
root_path = "/home/hieunt6/Documents/Sinh code Topcoder/Problems/ColorfulGarden/"


def parse_input(data):
    data = data.replace("\"", "").replace(" ", "").split(",")
    return "\r".join(x for x in data)

def parse_output(data):
    return data


# ===================== parse data =====================
test_cases = []
empty_count = 0
while True:
    line = raw_input().split("\t")
    info = []
    for x in line:
        if x != "":
            info.append(x)

    if len(info) <= 0:
        empty_count += 1
        if empty_count >= 3:
            break
    else:
        empty_count = 0
        test_cases.append(info)


# ===================== write data =====================
def write_file(file_name, data):
    fo = open(file_name, "wb")
    fo.write(data)
    fo.close()

for i in range(len(test_cases)):
    file_name = str(i + 1)
    while len(file_name) < 3:
        file_name = "0" + file_name
    file_name = root_path + problem_name + file_name
    write_file(file_name + ".inp", parse_input(test_cases[i][0]))
    write_file(file_name + ".out", parse_output(test_cases[i][1]))
