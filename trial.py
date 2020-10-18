import re
import raw_unparsed

labels_unparsed = raw_unparsed.events
labels = re.findall('[A-z]+', labels_unparsed)

data_label = []
for label in labels:
    if label == 'event':
        pass
    else:
        data_label.append(label)
values_unparsed = raw_unparsed.examples
values = values_unparsed.split('\n')

data_values = []
for value in values:
    data_value = []
    value = value.split('\t')
    if value[0] == 'timeStamp':
        for item in value:
            if len(item) > 0:
                data_value.append(item)
        data_values.append((data_value))

data_object = dict()
data_objects = []
for i in range(len(data_label)):
    if i <= 3:
        x = data_object[data_label[i]] = data_values[0]
    if i == 4:
        x = data_object[data_label[i]] = data_values[1]
    if i == 5 and i == 6:
        x = data_object[data_label[i]] = data_values[2]
    if i == 7 and i == 8:
        x = data_object[data_label[i]] = data_values[3]
    if i == 9:
        x = data_object[data_label[i]] = data_values[4]
    if i == 10 and i == 11:
        x = data_object[data_label[i]] = data_values[5]
    if i == 12:
        x = data_object[data_label[i]] = data_values[6]
    if i == 13:
        x = data_object[data_label[i]] = data_values[7]
    if i == 14:
        x = data_object[data_label[i]] = data_values[8]
    if i >= 15 and i <= 17:
        x = data_object[data_label[i]] = data_values[9]
    if i == 18:
        x = data_object[data_label[i]] = data_values[10]
    if i >= 19 and i <= 22:
        x = data_object[data_label[i]] = data_values[11]
    if i == 23:
        x = data_object[data_label[i]] = data_values[12]
    if i >= 24 and i <= 29:
        x = data_object[data_label[i]] = data_values[13]
    if i == 30:
        x = data_object[data_label[i]] = data_values[14]
    if i >= 31 and i <= 35:
        x = data_object[data_label[i]] = data_values[15]
    if i == 36 and i == 37:
        x = data_object[data_label[i]] = data_values[16]
    if i >= 38 and i <= 40:
        x = data_object[data_label[i]] = data_values[17]
    if i == 41:
        x = data_object[data_label[i]] = data_values[18]
    if i == 42:
        x = data_object[data_label[i]] = data_values[19]
data_objects.append(data_object)

print(data_objects)
