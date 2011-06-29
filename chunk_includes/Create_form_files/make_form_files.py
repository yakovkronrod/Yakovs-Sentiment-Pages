import sys
#import nltk
import glob
import os,re

loc_path = sys.path[0]
os.chdir(loc_path)
cwd = os.getcwd()

#Go through the sentences file
file_sents = "orig_sentences.txt"
file_sents_full = os.path.abspath(file_sents)
f_in_sents = open(file_sents_full,'r')

file_debug = "debug.txt"
file_debug_full = os.path.abspath(file_debug)
f_out_debug = open(file_debug_full, 'w')

end_of_block = False
sent_eng = sent_arab  = block = q1_eng = q2_eng = q3_eng = q4_eng = q5_eng = q6_eng = q7_eng = q8_eng = q9_eng = q10_eng = q11_eng = q12_eng = q13_eng= q1_arab = q2_arab = q3_arab = q4_arab = q5_arab = q6_arab = q7_arab = q8_arab = q9_arab = q10_arab = q11_arab = q12_arab = q13_arab = ""
next_line = ""
for line in f_in_sents:
    #remove whitespace from line and split by tabs
    line = line.strip()
    entries = line.split("\t")
    #if line.startswith("block"):
    #    print "Line starts with block:", line
    #f_out_debug.write(",".join(entries) + "\n")
    
    #print "entries[0]:", entries[0]

    #If already on the arabic version then record it and clear the next line
    if next_line == "sent_arab":
        sent_arab = entries[0]
        next_line = ""
    elif next_line == "q1_arab":
        q1_arab = entries[0]
        next_line = ""
    elif next_line == "q2_arab":
        q2_arab = entries[0]
        next_line = ""
    elif next_line == "q3_arab":
        q3_arab = entries[0]
        next_line = ""
    elif next_line == "q4_arab":
        q4_arab = entries[0]
        next_line = ""
    elif next_line == "q5_arab":
        q5_arab = entries[0]
        next_line = ""
    elif next_line == "q6_arab":
        q6_arab = entries[0]
        next_line = ""
    elif next_line == "q7_arab":
        q7_arab = entries[0]
        next_line = ""
    elif next_line == "q8_arab":
        q8_arab = entries[0]
        next_line = ""
    elif next_line == "q9_arab":
        q9_arab = entries[0]
        next_line = ""
    elif next_line == "q10_arab":
        q10_arab = entries[0]
        next_line = ""
    elif next_line == "q11_arab":
        q11_arab = entries[0]
        next_line = ""
    elif next_line == "q12_arab":
        q12_arab = entries[0]
        next_line = ""
    elif next_line == "q13_arab":
        q13_arab = entries[0]
        next_line = ""
        end_of_block = True

    #For encountering first lines, record them and set next_line value to arabic version
    if "block\t" in line: #entries[0] == "block":
        block = entries[1]
    elif entries[0] == "sent":
        sent_eng = entries[1]
        next_line = "sent_arab"
    elif entries[0] == "q1":
        q1_eng = entries[1]
        next_line = "q1_arab"
    elif entries[0] == "q2":
        q2_eng = entries[1]
        next_line = "q2_arab"
    elif entries[0] == "q3":
        q3_eng = entries[1]
        next_line = "q3_arab"
    elif entries[0] == "q4":
        q4_eng = entries[1]
        next_line = "q4_arab"
    elif entries[0] == "q5":
        q5_eng = entries[1]
        next_line = "q5_arab"
    elif entries[0] == "q6":
        q6_eng = entries[1]
        next_line = "q6_arab"
    elif entries[0] == "q7":
        q7_eng = entries[1]
        next_line = "q7_arab"
    elif entries[0] == "q8":
        q8_eng = entries[1]
        next_line = "q8_arab"
    elif entries[0] == "q9":
        q9_eng = entries[1]
        next_line = "q9_arab"
    elif entries[0] == "q10":
        q10_eng = entries[1]
        next_line = "q10_arab"
    elif entries[0] == "q11":
        q11_eng = entries[1]
        next_line = "q11_arab"
    elif entries[0] == "q12":
        q12_eng = entries[1]
        next_line = "q12_arab"
    elif entries[0] == "q13":
        q13_eng = entries[1]
        next_line = "q13_arab"
    
    if end_of_block:
        #Process the block
        #print "In end of block with block=", block
        #open a new file called arabic_<block>.html
        file_arab = "arabic_" + block + ".html"
        file_arab_full = os.path.abspath(file_arab)
        f_out_html = open(file_arab_full, 'w')

        #Open the template file
        file_template = "arabic_form_template.html"
        file_template_full = os.path.abspath(file_template)
        f_in_template = open(file_template_full,'r')

        #Go through the template file and replace all the necessary locations with the following switches
        for line in f_in_template:
            line = line.strip()
            #ENGLISH_SENTENCE   :   sent_eng
            #SENTENCE_CODE      :   block
            #SENT_ID            :   block
            #ARABIC_SENTENCE    :   sent_arab
            if line == "SENTENCE_CODE" or line == "SENT_ID":
                f_out_html.write(block+"\n")
            elif line == "ENGLISH_SENTENCE":
                f_out_html.write(sent_eng + "\n")
            elif line == "ARABIC_SENTENCE":
                f_out_html.write(sent_arab + "\n")
            elif line == "ENGLISH_QUESTION_1":
                f_out_html.write(q1_eng + "\n")
            elif line == "ARABIC_QUESTION_1":
                f_out_html.write(q1_arab + "\n")
            elif line == "ENGLISH_QUESTION_2":
                f_out_html.write(q2_eng + "\n")
            elif line == "ARABIC_QUESTION_2":
                f_out_html.write(q2_arab + "\n")
            elif line == "ENGLISH_QUESTION_3":
                f_out_html.write(q3_eng + "\n")
            elif line == "ARABIC_QUESTION_3":
                f_out_html.write(q3_arab + "\n")
            elif line == "ENGLISH_QUESTION_4":
                f_out_html.write(q4_eng + "\n")
            elif line == "ARABIC_QUESTION_4":
                f_out_html.write(q4_arab + "\n")
            elif line == "ENGLISH_QUESTION_5":
                f_out_html.write(q5_eng + "\n")
            elif line == "ARABIC_QUESTION_5":
                f_out_html.write(q5_arab + "\n")
            elif line == "ENGLISH_QUESTION_6":
                f_out_html.write(q6_eng + "\n")
            elif line == "ARABIC_QUESTION_6":
                f_out_html.write(q6_arab + "\n")
            elif line == "ENGLISH_QUESTION_7":
                f_out_html.write(q7_eng + "\n")
            elif line == "ARABIC_QUESTION_7":
                f_out_html.write(q7_arab + "\n")
            elif line == "ENGLISH_QUESTION_8":
                f_out_html.write(q8_eng + "\n")
            elif line == "ARABIC_QUESTION_8":
                f_out_html.write(q8_arab + "\n")
            elif line == "ENGLISH_QUESTION_9":
                f_out_html.write(q9_eng + "\n")
            elif line == "ARABIC_QUESTION_9":
                f_out_html.write(q9_arab + "\n")
            elif line == "ENGLISH_QUESTION_10":
                f_out_html.write(q10_eng + "\n")
            elif line == "ARABIC_QUESTION_10":
                f_out_html.write(q10_arab + "\n")
            elif line == "ENGLISH_QUESTION_11":
                f_out_html.write(q11_eng + "\n")
            elif line == "ARABIC_QUESTION_11":
                f_out_html.write(q11_arab + "\n")
            elif line == "ENGLISH_QUESTION_12":
                f_out_html.write(q12_eng + "\n")
            elif line == "ARABIC_QUESTION_12":
                f_out_html.write(q12_arab + "\n")
            elif line == "ENGLISH_QUESTION_13":
                f_out_html.write(q13_eng + "\n")
            elif line == "ARABIC_QUESTION_13":
                f_out_html.write(q13_arab + "\n")
            #ENGLISH_QUESTION_1 :   q1_eng
            #ARABIC_QUESTION_1  :   q1_arab
            #...
            else:
                f_out_html.write(line+"\n")
        #Close file, reset variables, and keep reading the sentences file
        f_out_html.close()
        f_in_template.close()
        end_of_block = False
        sent_eng = sent_arab  = block = q1_eng = q2_eng = q3_eng = q4_eng = q5_eng = q6_eng = q7_eng = q8_eng = q9_eng = q10_eng = q11_eng = q12_eng = q13_eng= q1_arab = q2_arab = q3_arab = q4_arab = q5_arab = q6_arab = q7_arab = q8_arab = q9_arab = q10_arab = q11_arab = q12_arab = q13_arab = ""

f_in_sents.close()
f_out_debug.close()
