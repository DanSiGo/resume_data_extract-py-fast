import csv
from data_treatment import pdf_to_string

resume_id_counter = 1
def add_resume(pdf_file_path, output_file, field_name, field_ids, field_id_counter):

    with open(output_file, 'a+') as file:
        reader = csv.reader(file)
        data = list(reader)

        if data:
            last_id = int(data[-1][0]) + 1
        else:
            last_id = 1

    text_final = pdf_to_string(pdf_file_path)

    if field_name not in field_ids:
        field_ids[field_name] = field_id_counter
        field_id_counter += 1

    field_id = field_ids[field_name]

    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([last_id, field_id, field_name, text_final])

    return field_id_counter



pdf_file_path = '/home/daniel/Desktop/resume_data_extract-py-fast/machine_learning/data/data/TEACHER/10504237.pdf'
output_file = '/home/daniel/Desktop/resume_data_extract-py-fast/test.csv'
field_name = 'TEACHER'
field_ids = {}
field_id_counter = 1
add_resume(pdf_file_path, output_file, field_name, field_ids, field_id_counter)


with open('output_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

    def find_field_id(data, field_name):
        for row in data:
            if row['field_name'] == field_name:
                return int(row['field_id'])            
        return None