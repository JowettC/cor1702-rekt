IMPORTANT: readme

There is no difference between the m_packages... & s_packages EXCEPT the file name.
(i) s_packages are meant for Q1, and the file name contains W
(e.g. s_packages_170 --> W = 170). This value for W is read by q1_main.py
(ii) m_packages are meant for Q2 and the file name contains n and W
(e.g. m_packages_2_75 --> n = 2 and W = 75). These values for n and W are extracted by q2_main.py.

So, in order to use different n and W values for testing, you can:
(i) make a copy of the CSV file
(ii) rename it to indicate the new n and W values (e.g. m_packages_2_75.csv to m_packages_3_50.csv)
(iii) edit line 11 of q1_main or q2_main.py to use your new CSV file.

Besides those already provided, you should create your own CSV files to test your solution. Try CSV files with a small vs huge list of packages. Try CSV files with a huge n/W vs small n/W.