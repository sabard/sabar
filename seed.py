from sabar_me.models import db, create_project

projects = [
    # tools
    {
        "category": "tool", # TODO should be enum?
        "subcategory": "Acquisition",
        "title": "esp32-peripheral",
        "text": """
        <p>The <a href="https://github.com/sabard/esp32-peripheral">ESP32 Peripheral Library</a> makes it easy to use sensors and transducers with minimal hardware/firmware experience.</p>
        <p>The generic firmware exposes an API that accepts msgpack'ed Python dicts over UDP in order to control GPIO pins and other peripherals.</p>
        <p>The library is built on top of Espressif's <a href="https://esp-idf-lib.readthedocs.io/en/latest/">ESP-IDF framework</a>.</p>
        """,
        "image_link": "/static/images/esp32.png"
    },
    {
        "category": "tool",
        "subcategory": "Application",
        "title": "LiCoRICE",
        "text": """
        <p><a href="http://github.com/sabard/licorice">LiCoRICE</a> (<a href="https://docs.licorice.su.domains/">documentation</a>) is an open source realtime computational engine that makes it easy to run realtime applications with empirically derived timing guarantees using high-level programming languages.</p>
        <p>It runs on POSIX-compliant hardware including MacOS and is able to log data, output to a display, and incorporate inputs from various peripherals (including USB) all while maintaining a 1ms clock cycle.</p>
        <p>LiCoRICE was developed in the <a href="https://bil.stanford.edu/licorice">Brain Interfacing Lab</a> to conduct closed-loop experiments.</p>
        """,
        "image_link": "https://openclipart.org/download/210617/spice-licorice.svg"
    },
    {
        "category": "tool",
        "subcategory": "Analysis",
        "title": "provision-it",
        "text": """
        <p><a href="https://github.com/sabard/provision-it"><code>provision-it</code></a> is a wrapper on top of a number of <a href="https://en.wikipedia.org/wiki/Infrastructure_as_code">infrastructure-as-code (IaC)</a> tools that helps you set up and manage computer.</p>
        <p><code>provision-it</code> is a generic tool and may be used in a number of different ways, but it is currently being used to validate timing guarantees for <a href="/project/licorice">realtime systems</a> and manage setup of self-hosted clusters.</P>
        <p>provision-it consists of four main components:
        <ul>
        <li>Netboot HTTP Server</li>
        <li>CDK8s config</li>
        <li>Autoinstall config</li>
        <li>Salt config</li>
        </ul>
        """,
        "image_link": "/static/images/cloud.png"
    },

    # builds
    {
        "category": "build", # TODO should be enum?
        "subcategory": None,
        "title": "Sliding Door",
        "text": "DIY sliding door",
        "image_link": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Upvc_Patio_doors.JPG"
    },
    {
        "category": "build",
        "subcategory": None,
        "title": "Lights",
        "text": "DIY lights controller",
        "image_link": "https://live.staticflickr.com/5489/11844980226_16be8dba96_w.jpg"
    },
    {
        "category": "build",
        "subcategory": None,
        "title": "Trailer sauna",
        "text": "Trailer sauna",
        "image_link": "https://openclipart.org/image/800px/336583"
    },
    {
        "category": "build",
        "subcategory": None,
        "title": "3D Printer",
        "text": "Reprap Prusa Mendel i3",
        "image_link": "https://reprap.org/mediawiki/images/5/55/Prusai3-metalframe.jpg"
    }
]


created_projects = []
for project in projects:
    created_projects.append(create_project(project, commit=False))

db.session.commit()

print(created_projects)
