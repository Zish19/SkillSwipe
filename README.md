SkillSwipe: A "Tinder-for-Engineers" Project

SkillSwipe is a web application I built to solve a common problem for students and developers: finding the right teammates for a project. It replaces the slow, random search for partners with a fast, skill-based, mutual-interest matching system.

You don't just find a teammate; you find a React Developer or UI/UX Designer who is also actively looking for a team with your skills.

Key Features:
Simple Swipe Interface: Uses a familiar and intuitive "swipe" (click) model.
Skill-Based Matching: Users are defined by their skills, not just their name.
Mutual Interest: A "match" only happens when both users swipe right on each other.
Real-Time Match Logic: The "IT'S A MATCH!" screen appears instantly when a mutual swipe is detected.
Lightweight & Fast: Built with a minimal, efficient stack.

🚀 Core Functionality

Here is the app's core matching logic, demonstrated with two demo users, "Priya" and "Rohan".
1. Two Users Log In:
Priya (a 'Project Leader') logs in. She sees Rohan's card.
Rohan (a 'React Dev') logs in on another browser. He sees Priya's card.
2. Both Users Swipe Right:
Priya clicks the "YES" side of Rohan's card. Her swipe is saved to the database.
Rohan clicks the "YES" side of Priya's card. The backend receives his swipe, and...
3. IT'S A MATCH!
...the backend instantly checks for Priya's swipe, finds it, and sends a "Match: True" response.
The "IT'S A MATCH!" screen appears, and a new team is formed.

