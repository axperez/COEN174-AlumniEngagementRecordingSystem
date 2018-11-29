# COEN174-AERS
The Santa Clara University Alumni Office is requesting help in creating a system that can record activities of alumni in events that have been created by the Alumni Officeor spontaneously by one or more alumni. Alumni Office staff can enter formal university-sponsored events(e.g., SCU athletic events, classroom speaking opportunities, etc.) and alumni participants can check in to record their participation. Alumni-organized events (e.g., informal class reunions) can be created by alumni, but must be approved byan Alumni Office manager before they will appear to the whole alumni community. Reports must be provided to detail events, locations, number of participants, etc.

# Wep Application Link
http://axperez.pythonanywhere.com

# Installation Guide
1. Set-up a virtual environment with python 3.6 or greater (virtualenv --python=<path_to_python> <directory_for_virtualenv>).
2. Git init in the location you would like to have the project.
3. Git clone: git clone 
3. In terminal, pip install the requirements.txt file (pip3 install -r requirements.txt)
3. Within the project folder inside terminal. Run 'python3 manage.py makemigrations'. Then run
'python manage.py migrate'. Then run 'python manage.py runserver'.
4. To create a superuser, run 'python3 manage.py createsuperuser' in terminal. Follow the
instructions to create an Admin account to gain access to admin controls.
