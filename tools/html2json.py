#/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re
from bs4 import BeautifulSoup

def html2json(html):
    """
    summary = [course_number, half_or_full_semester, season_of_course, GIGA_or_not,
        course_period, course_language]
    """
    html_doc = html.read()
    soup = BeautifulSoup(html_doc, 'lxml')

    # course name and course number
    course_name_list = []
    course_number_list = []
    course_class = soup.find(attrs={"class": "clist"})
    for course in course_class.find_all("a"):
        course_number_list.append(course.get_text()[0:5])
        course_name_list.append(course.get_text()[6:])
    num_name_dict = dict(zip(course_number_list, course_name_list))

    course_title_number_list = []
    giga_verified_list = []
    half_verified_list = []
    season_list = []
    for course_title in soup.find_all(attrs={"class": "course_title"}):
        course_title_number_list.append(course_title.get_text()[0:5])
        if u"GIGA/GG/GI" in course_title.get_text():
            giga_verified_list.append(True)
        else:
            giga_verified_list.append(False)
        if u"学期前半" in course_title.get_text():
            half_verified_list.append(True)
        else:
            half_verified_list.append(False)
        if u"Fall" in course_title.get_text():
            season_list.append("Fall")
        if u"Spring" in course_title.get_text():
            season_list.append("Spring")
    course_name_info_list = []
    for item in course_title_number_list:
        course_name_info_list.append(num_name_dict[item])

    # faculty_in_charge
    teacher_list = []
    for faculty_in_charge in soup.find_all(attrs={"class": "tag"}, text=re.compile(r'Faculty-in-charge')):
        for teacher in faculty_in_charge.next_siblings:
            teacher_list.append(teacher.get_text().split(u"・"))

    # Semester, Day and Period
    period_info_list = []
    for period in soup.find_all(attrs={"class": "tag"}, text=re.compile(r'Semester, Day and Period')):
        for period_info in period.next_siblings:
            time_list = period_info.get_text().split(",")
            period_info_list.append(time_list)

    # Language used in the class
    language_info_list = []
    for language in soup.find_all(attrs={"class": "tag"}, text=re.compile(r'Language used in the class')):
        for language_info in language.next_siblings:
            language_info_list.append(language_info.get_text())

    summary = zip(course_title_number_list, course_name_info_list, half_verified_list, season_list, giga_verified_list, period_info_list, language_info_list)
    
    with open("data.json", "w+") as data:
        data.write(json.dumps(summary))
    return

if __name__ == "__main__":
    with open("test.html", "r") as html:
        html2json(html)
