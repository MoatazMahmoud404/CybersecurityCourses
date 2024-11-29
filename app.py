from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {
        "id": "1",
        "name": "Certified Junior Penetration Tester",
        "nickname": "eJPT",
        "description": "Learn the basics of penetration testing, network vulnerabilities, and exploitation techniques.",
        "price": "$200",
        "company": "INE/Offensive Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/eJPT.webp",
        "enroll_url": "https://security.ine.com/certifications/ejpt-certification/"
    },
    {
        "id": "2",
        "name": "Professional Penetration Tester",
        "nickname": "eCPPT",
        "description": "In-depth course covering advanced penetration testing techniques and methodologies.",
        "price": "$400",
        "company": "INE/Offensive Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/eCPPT.webp",
        "enroll_url": "https://security.ine.com/certifications/ecppt-certification/"
    },
    {
        "id": "3",
        "name": "Certified Expert Penetration Tester",
        "nickname": "eCPTX",
        "description": "Master level penetration testing course for those aiming to become expert penetration testers.",
        "price": "$600",
        "company": "INE/Offensive Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/eCPTX.webp",
        "enroll_url": "https://example.com/"
    },
    {
        "id": "4",
        "name": "Certified Threat Hunting Professional",
        "nickname": "eCTHP",
        "description": "Learn advanced threat hunting techniques to detect and respond to cyber threats.",
        "price": "$500",
        "company": "INE/Offensive Security",
        "classification": "Blue Teaming",
        "team": "Blue",
        "image": "images/eCTHP.webp",
        "enroll_url": "https://security.ine.com/certifications/ecthp-certification/"
    },
    {
        "id": "5",
        "name": "Web Application Penetration Tester",
        "nickname": "eWPT",
        "description": "Learn how to perform penetration tests on web applications to uncover vulnerabilities.",
        "price": "$350",
        "company": "INE/Offensive Security",
        "classification": "Web Application Security",
        "team": "Red",
        "image": "images/eWPT.webp",
        "enroll_url": "https://security.ine.com/certifications/ewpt-certification/"
    },
    {
        "id": "6",
        "name": "Adv Web Application Penetration Tester",
        "nickname": "eWPTX",
        "description": "Take your web application security skills to the next level with this advanced course.",
        "price": "$500",
        "company": "INE/Offensive Security",
        "classification": "Web Application Security",
        "team": "Red",
        "image": "images/eWPTX.webp",
        "enroll_url": "https://security.ine.com/certifications/ewptx-certification/"
    },
    {
        "id": "7",
        "name": "Offensive Security Certified Professional",
        "nickname": "OSCP",
        "description": "Advanced course focused on offensive security techniques for ethical hackers.",
        "price": "$1000",
        "company": "Offensive Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/OSCP.png",
        "enroll_url": "https://www.offsec.com/courses/pen-200/"
    },
    {
        "id": "8",
        "name": "Offensive Security Wireless Professional",
        "nickname": "OSWP",
        "description": "A course designed for those looking to specialize in wireless network penetration testing.",
        "price": "$800",
        "company": "Offensive Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/OSWP.png",
        "enroll_url": "https://www.offsec.com/courses/pen-210/"
    },
    {
        "id": "9",
        "name": "Offensive Security Web Application Assessor",
        "nickname": "OSWA",
        "description": "Learn how to assess web application security and find vulnerabilities in a controlled environment.",
        "price": "$600",
        "company": "Offensive Security",
        "classification": "Web Application Security",
        "team": "Red",
        "image": "images/OSWA.png",
        "enroll_url": "https://www.offsec.com/courses/web-200/"
    },
    {
        "id": "10",
        "name": "Practical Network Penetration Tester",
        "nickname": "PNPT",
        "description": "A practical, hands-on course in network penetration testing and vulnerability exploitation.",
        "price": "$450",
        "company": "TCM Security",
        "classification": "Networking",
        "team": "Red",
        "image": "images/PNPT.webp",
        "enroll_url": "https://certifications.tcm-sec.com/product/practical-network-penetration-tester-with-training/"
    },
    {
        "id": "11",
        "name": "Certified Red Team Professional",
        "nickname": "CRTP",
        "description": "Specialize in advanced red teaming techniques and adversary simulation.",
        "price": "$750",
        "company": "Pentester Academy/INE",
        "classification": "Red Teaming",
        "team": "Red",
        "image": "images/CRTP.png",
        "enroll_url": "https://www.alteredsecurity.com/post/certified-red-team-professional-crtp/"
    },
    {
        "id": "12",
        "name": "Certified Red Team Expert",
        "nickname": "CRTE",
        "description": "An expert-level course on red teaming and advanced adversary simulation.",
        "price": "$900",
        "company": "Pentester Academy/INE",
        "classification": "Red Teaming",
        "team": "Red",
        "image": "images/CRTE.png",
        "enroll_url": "https://www.alteredsecurity.com/redteamlab"
    },

    {
        "id": "13",
        "name": "GIAC Web Application Penetration Tester",
        "nickname": "GWAPT",
        "description": "Learn advanced web app testing techniques and prepare for GIAC certification.",
        "price": "$700",
        "company": "SANS",
        "classification": "Web Application Security",
        "team": "Red",
        "image": "images/GWAPT.png",
        "enroll_url": "https://www.giac.org/certifications/web-application-penetration-tester-gwapt/"
    },
    {
        "id": "14",
        "name": "GIAC Certified Intrusion Analyst",
        "nickname": "GCIA",
        "description": "Learn to identify and respond to intrusions within a network and protect critical infrastructure.",
        "price": "$800",
        "company": "SANS",
        "classification": "Blue Teaming",
        "team": "Blue",
        "image": "images/GCIA.png",
        "enroll_url": "https://www.giac.org/certifications/certified-intrusion-analyst-gcia/"
    },
    {
        "id": "15",
        "name": "GIAC Certified Incident Handler",
        "nickname": "GCIH",
        "description": "Prepare for incident handling and response with hands-on training in cybersecurity incidents.",
        "price": "$700",
        "company": "SANS",
        "classification": "Blue Teaming",
        "team": "Blue",
        "image": "images/GCIH.png",
        "enroll_url": "https://www.giac.org/certifications/certified-incident-handler-gcih/"
    },
    {
        "id": "16",
        "name": "GIAC Certified Forensic Examiner",
        "nickname": "GCFE",
        "description": "Specialize in conducting digital forensic examinations and incident response.",
        "price": "$900",
        "company": "SANS",
        "classification": "Forensics and Incident Response",
        "team": "Blue",
        "image": "images/GCFE.png",
        "enroll_url": "https://www.giac.org/certifications/certified-forensic-examiner-gcfe/"
    },
    {
        "id": "17",
        "name": "Certified Red Team Operator",
        "nickname": "CRTO",
        "description": "Master the skills required for red team operations and adversary simulation.",
        "price": "$1200",
        "company": "Zero Point Security",
        "classification": "Red Teaming",
        "team": "Red",
        "image": "images/CRTO.png",
        "enroll_url": "https://training.zeropointsecurity.co.uk/courses/red-team-ops"
    },
]


@app.route('/')
def index():
    return render_template('index.html', courses=courses)


@app.route('/course_detail/<int:course_id>')
def course_detail(course_id):
    course = next((c for c in courses if c['id'] == str(course_id)), None)
    if not course:
        return "Course not found", 404
    return render_template('course_detail.html', course=course)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
