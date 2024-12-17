import json

# 입력 파일과 출력 파일 경로 설정
input_file = input("filepath : ") 
output_file = 'output.jsonl'  

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:

    lines = ""

    for line in infile:
        if(line == "}\n" or line == "}") :
            lines += line.strip()
            outfile.write(lines + '\n') 
            lines = ""

        lines += line.strip()
