import difflib
import textwrap
import os

# removing empty lines from both files AND removing indetations

string_without_empty_lines=""
with open("Text compare\Files to compare\scheme.txt", encoding="utf-8") as scheme_website_evidence:
    for line in scheme_website_evidence:
        if not line.isspace():
            line = textwrap.dedent(line)
            string_without_empty_lines+=line


scheme_website_evidence = open("Text compare\Files to compare\scheme.txt","w", encoding="utf-8")
scheme_website_evidence.write(string_without_empty_lines)
scheme_website_evidence.close()

string_without_empty_lines=""
with open("Text compare\Files to compare\demo.txt", encoding="utf-8") as demo_website_evidence:
    for line in demo_website_evidence:
        if not line.isspace():
            line = textwrap.dedent(line)
            string_without_empty_lines+=line


demo_website_evidence = open("Text compare\Files to compare\demo.txt","w", encoding="utf-8")
demo_website_evidence.write(string_without_empty_lines)
demo_website_evidence.close()

# loading text from both files to program memory

scheme_website_evidence = open("Text compare\Files to compare\scheme.txt","r", encoding="utf-8")
demo_website_evidence = open("Text compare\Files to compare\demo.txt","r", encoding="utf-8")

scheme_wording = scheme_website_evidence.read()
demo_wording = demo_website_evidence.read()

scheme_website_evidence.close()
demo_website_evidence.close()

# creating evidence file with difference between the files

filename = "Text compare\Evidence\Difference.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

evidence_file_diff = open("Text compare\Evidence\Difference.txt","w", encoding="utf-8")
evidence_file_diff.close()
evidence_file_diff = open("Text compare\Evidence\Difference.txt","a", encoding="utf-8")
scheme_wording_list = scheme_wording.split("\n")
demo_wording_list = demo_wording.split("\n")
d = difflib.Differ()
diff = d.compare(scheme_wording_list, demo_wording_list)
evidence_file_diff.write('\n'.join(diff))
evidence_file_diff.close()

# info about generating evidence file

print("\n\033[1mEvidence file was successfully generated!\033[0m\n")