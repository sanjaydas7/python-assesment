import json
import unittest

from app import app

app.testing = True


class TestApi(unittest.TestCase):

    def test_hello_world(self):
        with app.test_client() as client:
            sent = {}
            result = client.get('/', data=sent)
            a = result.data.decode()
            self.assertEqual(a, "hello flask is running")

    def test_player_birth_year(self):
        with app.test_client() as client:
            sent = '{"Year": "1995"}'
            response = client.get('/players_birth_year', data=sent)
            result = json.loads(response.data.decode())
            a = {
                "Percentage of player born above 1995": "1.06%",
                "Percentage of player with no date of birth": "16.78%"
            }
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(result, a)

    def test_average_ages(self):
        with app.test_client() as client:
            sent = '{"Country" : "India"}'
            response = client.get('/average_age', data=sent)
            result = json.loads(response.data.decode())
            a = {
                "India team average age": "35.42%"
            }
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(result, a)

    def test_batsmen_position(self):
        with app.test_client() as client:
            sent = {}
            response = client.get('/batsmen_position_left', data=sent)
            result = json.loads(response.data.decode())
            a = {
                "The country with maximum left hand batsmen is": "Pakistan"
            }
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(result, a)

    def test_no_country(self):
        with app.test_client() as client:
            sent = {}
            response = client.get('/no_country', data=sent)
            result = json.loads(response.data.decode())
            a = {
                "Player with no country defined": "['A Choudhary', 'A Dananjaya', 'A Hales', 'A Joseph', 'A Roy', 'A Turner', 'AJ Tye', 'Ankit Soni', 'AR Bawne', 'AS Yadav', 'Avesh Khan', 'B Stanlake', 'BA Stokes', 'Basil Thampi', 'C de Grandhomme', 'C Ingram', 'CR Woakes', 'D Shorey', 'D Short', 'D Willey', 'DM Bravo', 'E Lewis', 'H Brar', 'H Gurney', 'H Klaasen', 'H Vihari', 'H Viljoen', 'Harmeet Singh (2)', 'I Sodhi', 'J Archer', 'J Bairstow', 'J Behrendorff', 'J Dala', 'J Denly', 'J Searles', 'JJ Roy', 'K Ahmed', 'K Gowtham', 'K Khejroliya', 'K Paul', 'K Rabada', 'KM Asif', 'L Ferguson', 'L Livingstone', 'L Ngidi', 'L Plunkett', 'LH Ferguson', 'M Ali', 'M Lomror', 'M Markande', 'M Santner', 'M Ur Rahman', 'M Wood', 'MJ Henry', 'Mohammad Nabi', 'Mohammed Siraj', 'N Naik', 'N Pooran', 'NB Singh', 'Niraj Patel', 'O Thomas', 'P Chopra', 'P Krishna', 'P R Barman', 'P Raj', 'P Shaw', 'R Bhui', 'R Parag', 'R Salam', 'R Singh', 'RA Tripathi', 'Rashid Khan', 'RD Chahar', 'S Curran', 'S Dube', 'S Gill', 'S Hetmyer', 'S Kuggeleijn', 'S Lamichhane', 'S Mavi', 'S Midhun', 'S Rutherford', 'S Sharma', 'S Singh', 'S Warrier', 'SD Lad', 'SP Jackson', 'SS Agarwal', 'T Curran', 'T Natarajan', 'Tejas Baroka', 'TS Mills', 'V Chakravarthy', 'Vishnu Vinod', 'Washington Sundar']"
            }
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(result, a)

    def test_country_player(self):
        with app.test_client() as client:
            sent = '{"Country" : "India"}'
            response = client.get('/player_country', data=sent)
            result = json.loads(response.data.decode())
            a = {
                "Players of India": "['A Ashish Reddy', 'A Chandila', 'A Chopra', 'A Kumble', 'A Mishra', 'A Mithun', 'A Mukund', 'A Nehra', 'A Singh', 'A Uniyal', 'AA Bilakhia', 'AA Chavan', 'AA Jhunjhunwala', 'AA Kazi', 'AB Agarkar', 'AB Barath', 'AB Dinda', 'AD Nath', 'AG Murtaza', 'AG Paunikar', 'AL Menaria', 'AM Nayar', 'AM Rahane', 'AM Salvi', 'AN Ahmed', 'AN Ghosh', 'Anand Rajan', 'Anirudh Singh', 'Ankit Sharma', 'Anureet Singh', 'AP Dole', 'AP Majumdar', 'AP Tare', 'AR Patel', 'AS Rajpoot', 'AS Raut', 'AT Rayudu', 'AUK Pathan', 'AV Wankhade', 'B Akhil', 'B Aparajith', 'B Chipli', 'B Kumar', 'B Sumanth', 'BA Bhatt', 'BB Samantray', 'BB Sran', 'Bipul Sharma', 'C Ganapathy', 'C Madan', 'C Nanda', 'CA Pujara', 'CM Gautam', 'D Kalyankrishna', 'D Salunkhe', 'DB Das', 'DB Ravi Teja', 'DH Yagnik', 'DJ Hooda', 'DJ Muthuswami', 'DL Chahar', 'DP Vijaykumar', 'DS Kulkarni', 'DT Patil', 'ER Dwivedi', 'FY Fazal', 'G Gambhir', 'Gagandeep Singh', 'GH Vihari', 'Gurkeerat Singh', 'H Das', 'Harbhajan Singh', 'Harmeet Singh', 'Harpreet Singh', 'HH Pandya', 'HV Patel', 'I Malhotra', 'I Sharma', 'IC Pandey', 'IK Pathan', 'Imran Tahir', 'Iqbal Abdulla', 'IR Jaggi', 'Ishan Kishan', 'J Arunkumar', 'J Suchith', 'J Syed Mohammad', 'J Yadav', 'Jaskaran Singh', 'JD Unadkat', 'JJ Bumrah', 'Joginder Sharma', 'K Goel', 'K Upadhyay', 'Kamran Khan', 'Karanveer Singh', 'KB Arun Karthik', 'KC Cariappa', 'KD Karthik', 'KH Devdhar', 'KH Pandya', 'KK Nair', 'KL Rahul', 'KM Jadhav', 'KP Appanna', 'Kuldeep Yadav', 'KV Sharma', 'L Ablish', 'L Balaji', 'LR Shukla', 'M Ashwin', 'M Kaif', 'M Kartik', 'M Manhas', 'M Rawat', 'M Vijay', 'M Vohra', 'MA Agarwal', 'MA Khote', 'Mandeep Singh', 'MB Parmar', 'MC Juneja', 'MD Mishra', 'MF Maharoof', 'MK Pandey', 'MK Tiwary', 'MM Patel', 'MM Sharma', 'Mohammed Shami', 'MS Bisla', 'MS Dhoni', 'MS Gony', 'N Rana', 'N Saini', 'ND Doshi', 'NK Patel', 'NS Naik', 'NV Ojha', 'P Amarnath', 'P Awana', 'P Dharmani', 'P Dogra', 'P Kumar', 'P Negi', 'P Parameswaran', 'P Prasanth', 'P Sahu', 'P Suyal', 'PA Patel', 'PA Reddy', 'Pankaj Singh', 'Parvez Rasool', 'PC Valthaty', 'PJ Sangwan', 'PM Sarvesh Kumar', 'PP Chawla', 'PP Ojha', 'PR Shah', 'PV Tambe', 'R Ashwin', 'R Bhatia', 'R Bishnoi', 'R Dhawan', 'R Dravid', 'R Ninan', 'R Sathish', 'R Sharma', 'R Shukla', 'R Tewatia', 'R Vinay Kumar', 'RA Jadeja', 'RA Shaikh', 'RG More', 'RG Sharma', 'RP Singh', 'RR Bhatkal', 'RR Bose', 'RR Pant', 'RR Powar', 'RR Raje', 'RS Gavaskar', 'RS Sodhi', 'RV Gomez', 'RV Pawar', 'RV Uthappa', 'S Anirudha', 'S Aravind', 'S Badrinath', 'S Dhawan', 'S Gopal', 'S Kaul', 'S Kaushik', 'S Ladda', 'S Nadeem', 'S Narwal', 'S Rana', 'S Sohal', 'S Sreesanth', 'S Sriram', 'S Tyagi', 'S Vidyut', 'SA Asnodkar', 'SA Yadav', 'Sachin Baby', 'Sandeep Sharma', 'SB Bangar', 'SB Jakati', 'SB Joshi', 'SB Wagh', 'SC Ganguly', 'SD Chitnis', 'Shivam Sharma', 'SJ Srivastava', 'SK Raina', 'SK Trivedi', 'SN Khan', 'SN Thakur', 'SP Goswami', 'SPD Smith', 'SR Tendulkar', 'SS Iyer', 'SS Mundhe', 'SS Sarkar', 'SS Shaikh', 'SS Tiwary', 'STR Binny', 'Sunny Gupta', 'Sunny Singh', 'SV Samson', 'Swapnil Singh', 'T Kohli', 'T Mishra', 'TL Suman', 'TM Srivastava', 'TP Sudhindra', 'U Kaul', 'UA Birla', 'UBT Chand', 'UT Yadav', 'V Kohli', 'V Pratap Singh', 'V Sehwag', 'V Shankar', 'VH Zol', 'VR Aaron', 'VRV Singh', 'VS Malik', 'VS Yeligati', 'VVS Laxman', 'VY Mahesh', 'W Jaffer', 'WA Mota', 'WP Saha', 'X Thalaivan Sargunam', 'Y Gnaneswara Rao', 'Y Nagar', 'Y Venugopal Rao', 'YA Abdulla', 'Yashpal Singh', 'YK Pathan', 'YS Chahal', 'Yuvraj Singh', 'YV Takawale', 'Z Khan']"
            }
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(result, a)



