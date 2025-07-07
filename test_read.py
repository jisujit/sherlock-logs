with open('sample_logs/ansible_sample.log', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for line in lines[:5]:
        print(f"Sample line: {line}")
