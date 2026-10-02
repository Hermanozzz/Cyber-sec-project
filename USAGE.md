HOW TO USE

    #Prerequisites
Mac OS with python 3.9+
terminal Access

    #Setup
Run './setup.sh'
Activate environment: 'source .venv/bin/activate'

    #Training
Run 'python train.py'. The dataset will load followed by training of Random Forest model. The SQLite database will also be created.

    #Analysing Emails
Run 'python analyze.py "any email content"

    #Viewing statistics
Run 'python analyze.py --stats'

    #Database
Results are stored in 'phishing_analysis.db'.It can be inspected through: 'sqlite3 phishing_analysis.db "SELECT * FROM phising_attempts;'
