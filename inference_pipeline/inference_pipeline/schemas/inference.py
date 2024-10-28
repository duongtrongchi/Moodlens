from pydantic import BaseModel
from typing import List

class SentimentAnalysisInput(BaseModel):
    prompt: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prompt": "Good work culture, and Environment, Seniors are Supportive and Management is transparent.",
                }
            ]
        }
    }

class TopicModelInput(BaseModel):
    docs: List[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "docs": [
                            "Great work culture and supportive seniors. Transparent management helps build trust.",
                            "Good learning experience with excellent support from senior managers.",
                            "High brand value, but work pressure is intense with limited work-life balance.",
                            "Enjoyed my time here. Strong support from team members, but room for improvement exists.",
                            "Customer-centric approach, but lacks structured career growth.",
                            "Supportive work environment, with an engaging company culture.",
                            "Effective teamwork, though promotion policies could improve.",
                            "Organizational culture encourages learning and skill development.",
                            "Supportive senior staff, but the company could provide clearer career paths.",
                            "Good salary and punctual payments. Teamwork and support are notable.",
                            "Good platform to learn, but workload has increased post-pandemic.",
                            "Supportive team, with a strong emphasis on job security.",
                            "Encouraging work environment, but high pressure affects work-life balance.",
                            "Punctual payments with moderate support for career development.",
                            "Team-oriented, but the promotion process lacks transparency.",
                            "Learning-oriented, though workload often spills into personal time.",
                            "Solid job security and clear, structured company policies.",
                            "Supportive company culture that focuses on team growth.",
                            "Timely salary and structured work environment.",
                            "Flexible work hours and learning opportunities make this a good place to grow.",
                            "Colleagues are supportive; IT issues, however, slow down productivity.",
                            "Company's work culture fosters a healthy learning environment.",
                            "Encouraging work environment with steady support from management.",
                            "Opportunities to develop skills, but promotion is slow.",
                            "Friendly work environment and timely payments.",
                            "Structured learning environment, with encouragement from senior staff.",
                            "Reliable company policies; however, the career growth system needs improvement.",
                            "Good work culture and team support; management could be more engaged.",
                            "Encouraging workplace with good employee welfare policies.",
                            "Comprehensive support from the team, with prompt assistance from senior staff.",
                            "The management team is approachable and open to feedback, which fosters transparency.",
                            "Flexible work hours allow for better work-life balance, though workload can vary greatly.",
                            "Great career development programs, but the promotion process is very competitive.",
                            "Supportive colleagues and a strong team spirit, but high turnover among new hires.",
                            "The company invests in training, but skills are often underutilized in day-to-day tasks.",
                            "Strong focus on employee well-being with health and wellness initiatives.",
                            "Office facilities are modern and comfortable, though remote work support could improve.",
                            "A dynamic environment with fast-paced projects, but deadlines are often tight.",
                            "Effective mentorship program, though it could benefit from more personalized guidance.",
                            "Opportunities for growth are available, but networking within the company is essential.",
                            "Management promotes open communication, although decisions are sometimes delayed.",
                            "Generous vacation policy, but taking extended leave can be challenging during peak times.",
                            "High-quality benefits package, including healthcare and retirement plans.",
                            "The company values diversity and inclusivity, but more initiatives are needed for women in leadership.",
                            "Innovative projects encourage learning, though processes can sometimes be rigid.",
                            "Employees have access to state-of-the-art tools and technology.",
                            "The onboarding process is thorough, but it could be more streamlined for new hires.",
                            "Open workspace layout encourages collaboration, though it can be noisy.",
                            "Management sets clear expectations, but there's limited flexibility in role assignments.",
                            "Team outings and social events create a fun work atmosphere.",
                            "The performance review process is fair, although it could be more frequent.",
                            "Good compensation and clear bonus structure, though raises are often performance-driven.",
                            "Emphasis on sustainability and environmental responsibility in business practices.",
                            "Collaborative cross-functional teams, though coordination can be challenging at times.",
                            "Encouraging work culture, but more opportunities for remote work are needed.",
                            "Company values creativity and innovation, though it can be difficult to implement new ideas.",
                            "The leadership team is inspiring, but there could be more clarity on long-term goals.",
                            "Strong emphasis on cybersecurity and data privacy, especially for customer data.",
                            "Structured workflows help maintain quality, but they can slow down creative processes.",
                            "Team feedback sessions are held regularly, fostering a sense of inclusion."
                        ]
                }
            ]
        }
    }


class SummarizationInput(BaseModel):
    docs: List[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "docs": [
                            "Great work culture and supportive seniors. Transparent management helps build trust.",
                            "Good learning experience with excellent support from senior managers.",
                            "High brand value, but work pressure is intense with limited work-life balance.",
                            "Enjoyed my time here. Strong support from team members, but room for improvement exists.",
                            "Customer-centric approach, but lacks structured career growth.",
                            "Supportive work environment, with an engaging company culture.",
                            "Effective teamwork, though promotion policies could improve.",
                            "Organizational culture encourages learning and skill development.",
                            "Supportive senior staff, but the company could provide clearer career paths.",
                            "Good salary and punctual payments. Teamwork and support are notable.",
                            "Good platform to learn, but workload has increased post-pandemic.",
                            "Supportive team, with a strong emphasis on job security.",
                            "Encouraging work environment, but high pressure affects work-life balance.",
                            "Punctual payments with moderate support for career development.",
                            "Team-oriented, but the promotion process lacks transparency.",
                            "Learning-oriented, though workload often spills into personal time.",
                            "Solid job security and clear, structured company policies.",
                            "Supportive company culture that focuses on team growth.",
                            "Timely salary and structured work environment.",
                            "Flexible work hours and learning opportunities make this a good place to grow.",
                            "Colleagues are supportive; IT issues, however, slow down productivity.",
                            "Company's work culture fosters a healthy learning environment.",
                            "Encouraging work environment with steady support from management.",
                            "Opportunities to develop skills, but promotion is slow.",
                            "Friendly work environment and timely payments.",
                            "Structured learning environment, with encouragement from senior staff.",
                            "Reliable company policies; however, the career growth system needs improvement.",
                            "Good work culture and team support; management could be more engaged.",
                            "Encouraging workplace with good employee welfare policies.",
                            "Comprehensive support from the team, with prompt assistance from senior staff.",
                            "The management team is approachable and open to feedback, which fosters transparency.",
                            "Flexible work hours allow for better work-life balance, though workload can vary greatly.",
                            "Great career development programs, but the promotion process is very competitive.",
                            "Supportive colleagues and a strong team spirit, but high turnover among new hires.",
                            "The company invests in training, but skills are often underutilized in day-to-day tasks.",
                            "Strong focus on employee well-being with health and wellness initiatives.",
                            "Office facilities are modern and comfortable, though remote work support could improve.",
                            "A dynamic environment with fast-paced projects, but deadlines are often tight.",
                            "Effective mentorship program, though it could benefit from more personalized guidance.",
                            "Opportunities for growth are available, but networking within the company is essential.",
                            "Management promotes open communication, although decisions are sometimes delayed.",
                            "Generous vacation policy, but taking extended leave can be challenging during peak times.",
                            "High-quality benefits package, including healthcare and retirement plans.",
                            "The company values diversity and inclusivity, but more initiatives are needed for women in leadership.",
                            "Innovative projects encourage learning, though processes can sometimes be rigid.",
                            "Employees have access to state-of-the-art tools and technology.",
                            "The onboarding process is thorough, but it could be more streamlined for new hires.",
                            "Open workspace layout encourages collaboration, though it can be noisy.",
                            "Management sets clear expectations, but there's limited flexibility in role assignments.",
                            "Team outings and social events create a fun work atmosphere.",
                            "The performance review process is fair, although it could be more frequent.",
                            "Good compensation and clear bonus structure, though raises are often performance-driven.",
                            "Emphasis on sustainability and environmental responsibility in business practices.",
                            "Collaborative cross-functional teams, though coordination can be challenging at times.",
                            "Encouraging work culture, but more opportunities for remote work are needed.",
                            "Company values creativity and innovation, though it can be difficult to implement new ideas.",
                            "The leadership team is inspiring, but there could be more clarity on long-term goals.",
                            "Strong emphasis on cybersecurity and data privacy, especially for customer data.",
                            "Structured workflows help maintain quality, but they can slow down creative processes.",
                            "Team feedback sessions are held regularly, fostering a sense of inclusion."
                        ]
                }
            ]
        }
    }