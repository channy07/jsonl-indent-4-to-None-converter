import json

# 입력 파일과 출력 파일 경로 설정
input_file = input("filepath : ")  # 원본 JSONL 파일 경로
output_file = 'output.jsonl'  # 변경된 JSONL 파일 경로

# JSONL 파일을 읽고, 재포맷하여 출력 파일에 쓰기
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:

    lines = ""

    for line in infile:
        if(line == "}\n") :
            lines += line.strip()
            outfile.write(lines + '\n')  # 한 줄로 작성하여 출력
            lines = ""

        lines += line.strip()