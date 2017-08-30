# 1b. discover companies (startups)

### Introduction

- Pain: There are so many startups. It's quite difficult to tell which one to join.
- Data sources: TechCrunch, CrunchBase, AngelList, Linkedin, (CISION PR NEWSWIRE, Bloomberg, Facebook, Twitter)
** - Challenge: categorize a company into a specific industry, how to collect valuable insights (competitive advantage, competitor)**
** - Challenge: CrunchBase seems to monetize its db service and thus does not allow me to scrape.
- Output: matching recommendations, 
** - Features: B2B, B2C, Location, **
- Skill: web scraping, database storoage, data preprocessing, exploratory data analysis, data visualization, machine learning, natural language processing (potentially)
** - Usecase: put some variable information such as industry, company size, location, etc. the app returns company recommendations.**

### Step 1. Data Collection and Preprocessing

**From Techcrunch**
- Input: search keywords
- Output: a list of startups with some info.

- Get a list of startup companies with a key word "raises C round" at Techcrunch. For each company, we also collect a link to each article that mention about a company and a short exerpt from the article. Now we have a title, a link, and an exerpt column.
- Extract a funding round, money raised for the round, and when the article was published at from existing three columns.

- Extract a company name from the title column.

#### - First set of scenarios
company_name + space + key verbs
company_name + ","... + "," + space + key verbs such as raise, land, get

- str1 = "Indian online lending platform Capital Float raises $45M Series C"
- str2 = "Carwow, a UK startup that helps you buy a new car, raises $39M Series C"
- str3 = "Stash raises $40 million Series C to make investing more approachable"

regex = re.compile(r"(\w*\s*\w+.{0,1})(,.+,)*\s(raise|land|grab|step|receive|get|collect|close|secure|take|tap|score|snare|snag|nab|win)", re.IGNORECASE)

#### - Second set of scenarios
keyword such as marketplace, firm, startup, company + space + company_name

-str1 = 
regex2 = re.compile(r"(marketplace|firm|startup|company|competitor|platform|developer|retailer)\s(\w+\s*\w*)", re.IGNORECASE)

#### - Third set of scenarios

company_name + verbs
regex4 = re.compile(r"(\w+|\w+\s\w+),\s", re.IGNORECASE)


** Challenge: error handling. 

**From Google**
- Input: Company name
- Output: A link to the linkedin Website for the company

**From Linkedin**
- Input: A link to the linkedin Website for the company
- Output: Profile information for each company

### Step 2. Exploratory Data Analysis
- Geo
- Industry Mix
- 

### Step 3. Recommendation Engine


