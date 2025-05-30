from pathlib import Path

def generate_html(input_file, output_file):
    content = Path(input_file).read_text()
    html = f"""<html>
<head><title>Suggested Tests Report</title></head>
<body>
<h1>Suggested Automated Tests</h1>
<pre>{content}</pre>
</body>
</html>"""
    Path(output_file).write_text(html)

if __name__ == "__main__":
    generate_html("suggested_tests.txt", "report.html")
    print("HTML report generated as report.html")
