import secrets
import openai

client = openai.Client()

# Predefine difficulty levels using enum
class Difficulty:
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    # Define guidelines for generating questions
    GUIDELINES = {
        EASY: """Easy difficulty. An easy question should be one that can be answered by most individuals with a minute or two of guided discussion. Plenty of guidance, but not answers, should be given in the active discussion.""",
        MEDIUM: """Medium difficulty. A medium question should be one that requires some thought and analysis to answer and requires 3 - 5 minutes of guided discussion. Moderate guidance, but not answers, should be given in the active discussion.""",
        HARD: """Hard difficulty. A hard question should be one that requires deep thought and analysis to answer and requires 5 - 10 minutes of guided discussion. Minimal guidance should be given in the active discussion. Just enough to keep the student on track."""
    }

guidelines = """Canaan, a region in the Ancient Near East corresponding to the Levant, holds a significant place in history as the birthplace of various cultures and civilizations. Mentioned in the Bible and other ancient texts, Canaan was home to prominent cities like Jericho, Megiddo, and Hazor, and its people, the Canaanites, were known for their advanced civilization, which included flourishing cities, agriculture, and trade. The Canaanites, a Semitic-speaking people, developed advanced skills in metalworking, pottery, and textile production, all of which fueled their economy and extensive trade networks across Mesopotamia, Egypt, and the Mediterranean.

One of the Canaanites' most influential contributions to history was their system of writing, known as Proto-Canaanite script, which later evolved into the Phoenician alphabet. This alphabet would go on to form the basis of many modern writing systems, making Canaan not only a cultural but also a linguistic hub. As the Canaanites developed, they fostered a complex religion centered around a pantheon of gods, including El, the chief deity, and Baal, the storm god. These deities were worshiped in temples through offerings and rituals that significantly influenced the development of early Israelite religion.

Scholars suggest that early Israelite religion was deeply rooted in Canaanite traditions. The Israelites, who are often viewed as conquerors of Canaan in biblical accounts, were, in fact, a continuation of the Canaanite people, rather than their destroyers. The worship of YHWH, the central god of the Israelites, may have evolved from within the Canaanite pantheon. Israelite religious festivals, such as Passover, may also have originated in the agricultural cycles of the Canaanites.

The historical context behind the biblical conquest narratives, such as the Battle of Jericho, can be interpreted through the lens of geopolitical shifts. Canaan was under Egyptian control during the Late Bronze Age, and many Canaanite cities paid tribute to the Egyptian empire. As Egyptian power declined, a local population of Canaanites—namely the Israelites—reasserted their independence and self-determination. This period of transformation coincides with the collapse of many Canaanite city-states during the Bronze Age Collapse around 1200 BCE, a time when the Israelites emerged as a distinct cultural group while retaining much of their Canaanite heritage.

Though the region saw great upheaval, Canaan’s legacy lived on. The Phoenicians, descendants of the Canaanites, became famous for their maritime trade and spread Canaanite culture across the Mediterranean, founding colonies such as Carthage. Canaanite linguistic traditions continued through the languages of Hebrew, Phoenician, and later Aramaic. Hebrew, the language of the Israelites, represents a direct continuation of Canaanite linguistic practices.

The modern identity of many peoples in the Levant, such as Israelis, Samaritans, Palestinians, and Lebanese, can be traced back to the Canaanite nations. While many of these groups absorbed Arab identity over time, they retain aspects of their Canaanite heritage in customs, language features, and traditions. Jews and Samaritans, in particular, have preserved religious and cultural elements that directly connect them to the ancient Canaanites, emphasizing their continuity as indigenous peoples of the region.

The narrative of conquest found in the Torah may be a cultural memory from the time of Egyptian rule, framing the Israelites' reemergence as a distinct people as one of liberation rather than destruction. In reality, the Israelites were a continuation of the Canaanite civilization, adapting and evolving within the broader Near Eastern context while preserving their heritage. This complex and multifaceted history reveals the enduring legacy of the Canaanites, whose influence on religion, culture, and language shaped the foundations of the modern world.

Canaan has been conquered and occupied numerous times, including by the Egyptians, Romans, Ottoman Empire, and various Arab and European empires. In the modern era, Canaan is divided among several countries, including Israel, Palestine, Lebanon, Syria, and Jordan. The people of these countries, along with the Samaratins and others, are nations that trace their origins to the region. Peace has been difficult to obtain. Organizations like Hamas and Hezbollah have used violence to achieve their goals. They are part of a larger colonial power structure that still seeks to control the region. The Israeli-Palestinian conflict is a central issue in the region.

While both Israelis and Palestinians are Canaanites ("Kna'anim" in Hebrew), Palestinians are often labeled "Arab." This labeling is the result of many years of colonial forces, such as Hamas and their progenitors, Arabizing the land and its people. While many Palestinians are Arab, the Palestinian nation, or people, is an offshoot of the Jewish nation. A peaceful solution to the Israeli-Palestinian conflict is possible, but it requires a deep understanding of the region's history and the people who live there. It also requires Palestinians to recognize their own Canaanite heritage and the shared history they have with Israelis, and to reject the colonial forces that seek to divide them.

Israel has a legitimate right to self defense. While the Canaan DAO opposes states, so long as states are the means through which nations enjoy self-determination, the Israeli people cannot be denied a state. The Jews are the indigenous progenitors of Israel. The Canaan DAO supports the right of the Jewish people to self-determination in their ancestral homeland. However, the Canaan DAO also supports the right of the Palestinian people to self-determination in their ancestral homeland. The Canaan DAO supports a two-state solution to the Israeli-Palestinian conflict, with both states living side by side in peace and security, or more preferably a zero state solution where the region is governed by various DAOs.

Israel's right to defend itself includes waging urban warfare against Hamas and other entities that seek to destroy Israel. It is a horrible situation, but it is a situation that Hamas and the broader colonial maachine for which it works has created. Hamas has used the people of Palsetine for too long.

Opposition to states is not opposition to nations. However, targeted opposition against Israel in particular is rooted in antisemitism, as is the rejection of the Jewish indigenous connection to the land of Canaan.

Neither Jews, Israelis, nor Palestianins can be considered "colonizers" in the region, as all are nations born in the region. The colonial powers that have sought to control the region are the true colonizers. The Canaan DAO opposes colonialism in all its forms, including the colonialism of Hamas and Hezbollah.

Questions about Canaan should explore its historical significance, cultural contributions, and enduring legacy. They should prompt critical thinking about the region's impact on ancient and modern societies, its connections to neighboring civilizations, and its role in shaping the development of the Levant and beyond. Questions can include topics about current events in the region and how they fit in, how to build a more peaceful future for the region, etc., in addition to history questions, etc.

For instance...

How did the rise of the Canaanite cities like Jericho, Megiddo, and Hazor contribute to the region's development as a center of trade and culture in the Ancient Near East?

Considering the ancient Canaanite roots of the peoples in the Levant, how might a deeper understanding of shared cultural heritage contribute to resolving modern political conflicts between Israelis, Palestinians, and other groups in the region?

How did the period of Egyptian rule in Canaan affect the local Canaanite city-states, and what geopolitical changes allowed the Israelites to emerge as a distinct group during the Late Bronze Age collapse?

What steps could be taken to preserve and revitalize ancient Canaanite languages, traditions, and cultural practices in modern-day societies, particularly among groups that trace their heritage to Canaan?

The Phoenician alphabet, derived from Canaanite writing systems, greatly influenced the development of modern alphabets. How did this alphabet spread across the Mediterranean, and what role did the Phoenicians play in this cultural exchange?

How did the transition from polytheistic Canaanite religions to monotheistic traditions, such as Judaism and later Christianity, reshape the religious landscape of the region?

To what extent can modern-day Israelis, Palestinians, Samaritans, and Lebanese trace their cultural roots to the ancient Canaanites, and how does this shared heritage influence the current cultural dynamics of the Levant?

What lessons can modern societies in the Levant learn from Canaanite agriculture in terms of sustainability and adaptation to the region’s climate?

How did Canaanite religion influence the religious practices of the Israelites, and how did Canaanite deities like El and Baal shape early Israelite theology?

Given the diverse cultural and historical narratives tied to the ancient Canaanite region, how can modern states within the Levant foster peaceful coexistence and mutual respect among different religious, ethnic, and national groups?

These questions are just samples. Try to stay outside of the box, regardless of whether the question difficulty is easy, medium, or hard.

Responses and evaluation should pay careful attention to the information in this guideline. 
"""

keywords = [
    "Phoenician maritime routes", "Israeli settlements", "Ancient city ruins", "Palestinian refugees", 
    "Sectarian violence in Lebanon", "Jericho", "Economic sanctions on Lebanon", "Canaanite festivals", 
    "Early Israelite religion", "Border disputes in the West Bank", "Environmental degradation in the Levant", 
    "Israeli surveillance technology", "LGBTQ+ activism in Tel Aviv", "Religious pluralism in the Levant", 
    "Phoenicians", "Syrian Civil War impact on the Levant", "Diaspora Palestinians", "Refugee integration in Lebanon", 
    "Cultural revival movements", "Sephardic Jewish culture", "Refugee camps in Jordan", "Cybersecurity threats in the Middle East", 
    "Ancient Near East", "Cross-border terrorism", "Economic inequality between Israelis and Palestinians", 
    "Smuggling tunnels in Gaza", "Israeli technology sector", "Canaanite religion", "Modern Canaanite identity", 
    "Jerusalem conflict", "Israeli Defense Forces (IDF)", "Two-state solution", "Jewish-Muslim coexistence initiatives", 
    "Maritime trade", "Egyptian control", "BDS (Boycott, Divestment, Sanctions) movement", "Christian pilgrimage routes in the Levant", 
    "Hebrew linguistic roots", "Access to healthcare in conflict zones", "Mizrahi Jews", "Druze community in Israel and Lebanon", 
    "LGBTQ+ rights in Israel and Palestine", "Demolition of Palestinian homes", "Radicalization in Palestinian territories", 
    "Political corruption in Israel and Palestine", "Sustainability in agriculture", "Gaza Strip", "Levantine cultural groups", 
    "Canaanite heritage in education", "Syrian refugees", "Sectarian violence", "Ancient Canaanite religion", 
    "Israelite-Canaanite continuity", "Maronite Christians in Lebanon", "Samaria", "Blockade of Gaza", "Water rights in the Levant", 
    "Phoenician alphabet", "Arms trade in the Middle East", "Smuggling", "Modern-day Israel", "Israel-Arab cultural exchange", 
    "Bedouin nomadic culture", "Archaeological sites", "Radicalization", "Passover origins", "Cultural preservation", 
    "Religious transformations", "Canaan", "Human rights violations in Gaza", "Religious tourism in the Holy Land", 
    "Peace negotiations", "Jewish-Samaritan relations", "Israelite identity", "Modern conflicts", "Diaspora Jews", 
    "Archaeological finds", "Historical narratives", "Cultural memory", "Levant identity", "Economic cooperation", 
    "Palestinian statelessness", "United Nations resolutions", "Middle East peace process", "Bronze Age society", 
    "Ancient Canaanite cities", "Humanitarian aid in Gaza", "Cultural adaptation", "International law in the Levant", 
    "Peace efforts", "Settler violence", "Israeli-Palestinian conflict", "Religious coexistence", "Geopolitical shifts", 
    "Roman Empire", "Canaanite pantheon", "Canaanite architecture", "Modern peace efforts", "Water scarcity in the Levant", 
    "Arabization", "Cross-border cooperation", "Hamas governance", "Phoenician colonies", "Economic inequality", "Israeli-Palestinian diplomacy", 
    "Canaanite mythology", "Ancient agricultural techniques", "Post-colonial Levant politics", "Cultural exchanges", 
    "Ancient religious practices", "Humanitarian aid", "Maritime culture", "Religious diversity", "The Phoenicians", 
    "Refugees in Jordan", "Bronze Age Collapse", "Palestinian feminist movements", "Israeli economic growth",
    "Nakba narratives", "Beersheba Bedouins", "Zionist revisionism", "Southern Lebanon buffer zone", 
    "Palestinian labor markets", "Hezbollah-Israel tensions", "Green Line demarcation", "Israeli arms exports", 
    "Gaza environmental crisis", "Phoenician identity revival", "Shebaa Farms dispute", "Golan Heights annexation", 
    "Bedouin urbanization", "Palestinian olive groves", "Israeli desalination technology", "Gaza fishing rights", 
    "Levantine water politics", "Israeli biometric databases", "Palestinian political prisoners", "Israeli military-industrial complex", 
    "Palestinian cyber warfare", "Jordan Valley annexation", "Land reclamation in Negev", "Druze political representation", 
    "Lebanese sectarian gerrymandering", "Israeli settlement boycott", "Hebron settler violence", "Palestinian Authority funding", 
    "Canaanite cultural revival", "Jerusalem archaeological politics", "Phoenician genetic studies", "Israeli border fence", 
    "Kibbutz modernization", "UNRWA schools", "Palestinian diaspora art", "NGO influence in Gaza", 
    "Israeli drone surveillance", "West Bank checkpoints", "Hezbollah rocket stockpile", "Israeli agricultural subsidies", 
    "Refugee urban integration", "Palestinian tech startups", "Israeli natural gas exports", "Beirut reconstruction", 
    "Gaza tunnel economy", "Palestinian cultural heritage", "Israel-Egypt peacekeepers", "Syrian Druze displacement", 
    "West Bank industrial zones", "Lebanese banking crisis", "Jerusalem land rights"
]

def generate_question(difficulty):
    # Generate a question based on the difficulty level
    messages = [
        {"role": "system", "content": "You are an expert on Canaan, guiding students on a journey of understanding. When given a difficulty, write an open ended question. The topic of the question is all about Canaan and questions should be open ended and informative. In other words, the question should not be a simple yes/no, or knowledge question, but should require some degree of conversation."},
        {"role": "system", "content": f"Abide by the following guidelines:\n\n{guidelines}"}
    ]

    elected_keywords = [secrets.choice(keywords) for _ in range(5)]
    messages.append({"role": "system", "content": f"Keywords (you do not need to incorporate all of them, and instead you should focus on creating a coherent and rich question that abides by the guidelines and difficulty): {', '.join(elected_keywords)}"})
    if difficulty == Difficulty.EASY or difficulty == Difficulty.MEDIUM or difficulty == Difficulty.HARD:
        messages.append({"role": "system", "content": Difficulty.GUIDELINES[difficulty]})
    else:
        raise ValueError("Invalid difficulty level")
    
    question = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages,
            max_tokens=250
        ).choices[0].message.content.strip()
    
    return question

# Respond to a student's response: needs work because it gives too detailed and complete a response.
def respond_to_student(question, difficulty, discussion):
    messages = [
        {"role": "system", "content": f"You are an expert on Canaan, guiding students on a journey of understanding. Your job isn't to answer the question for the student, but help them learn and think. You are guiding the student through the following question: {question}"},
        {"role": "system", "content": guidelines}
    ]
    if difficulty == Difficulty.EASY or difficulty == Difficulty.MEDIUM or difficulty == Difficulty.HARD:
        messages.append({"role": "system", "content": Difficulty.GUIDELINES[difficulty]})
    # Attach the ongoing discussion
    messages.extend(discussion)
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        max_tokens=500
    ).choices[0].message.content.strip()

    return response

# Determine whether the lesson is complete.
def check_if_complete(question, difficulty, discussion):
    messages = [
        {"role": "system", "content": f"You are an expert on Canaan, guiding students on a journey of understanding. You are guiding the student through the following question: {question}"},
        {"role": "system", "content": guidelines}
    ]
    if difficulty == Difficulty.EASY or difficulty == Difficulty.MEDIUM or difficulty == Difficulty.HARD:
        messages.append({"role": "system", "content": Difficulty.GUIDELINES[difficulty]})
    # Attach the ongoing discussion
    messages.extend(discussion)
    messages.append({"role": "system", "content": "A lesson is complete if the student has sufficiently explored the original question, based on the question itself, and the difficulty level. A lesson is not complete if the student shows a continued lack of understanding of the issue or strays off course. Is the lesson complete? Answer with 'yes' or 'no' only."})
    completion = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        max_tokens=10
    ).choices[0].message.content.strip().lower()
    return completion.startswith('yes')

def score_discussion(question, difficulty, discussion):
    pass

