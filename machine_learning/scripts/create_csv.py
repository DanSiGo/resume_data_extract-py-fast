import os
import csv
from data_treatment import pdf_to_string

root_dir = '/home/daniel/Desktop/resume_data_extract-py-fast/machine_learning/data/data'
output_file = 'processed_resumes.csv'
resume_id_counter = 1


with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'field_id', 'field_name', 'resume'])

    field_ids = {}
    field_id_counter = 1

    for field_name in os.listdir(root_dir):
        field_dir = os.path.join(root_dir, field_name)

        if field_name not in field_ids:
            field_ids[field_name] = field_id_counter 
            field_id_counter += 1

        field_id = field_ids[field_name] 

        for pdf_file in os.listdir(field_dir):
            if pdf_file.endswith('.pdf'):
                pdf_file_path = os.path.join(field_dir, pdf_file)
                resume_id = resume_id_counter
                resume_id_counter += 1

                text_final = pdf_to_string(pdf_file_path)
                writer.writerow([resume_id, field_id, field_name, text_final])