# importação das bibliotecas
import pandas as pd
from fuzzywuzzy import fuzz, process

# read csv
df = pd.read_csv('MailingTalento2018.csv')

# drop null values
df = df.dropna(subset=['NomeCompleto', 'Email', 'Curso'])

# remove duplicates
df = df.drop_duplicates(subset=['Email'], keep='first')

# string matching - courses
courses = 	['Administração', 
			'Análise de Sistemas', 
			'Arquitetura',
			'Artes Cênicas',
			'Artes Visuais',
			'Biologia',
			'Biomedicina',
			'Ciência da Computação',
			'Ciências Contábeis',
			'Ciências Econômicas',
			'Ciência Sociais',
			'Comunicação',
			'Dança',
			'Design',
			'Direito',
			'Economia',
			'Educação Física',
			'Enfermagem',
			'Engenharia Agrícola',
			'Engenharia Ambiental',
			'Engenharia Civil',
			'Engenharia da Computação',
			'Engenharia de Controle e Automação',
			'Engenharia de Manufatura',
			'Engenharia de Materiais',
			'Engenharia de Produção',
			'Engenharia de Software',
			'Engenharia Elétrica',
			'Engenharia Física',
			'Engenharia Mecânica',
			'Engenharia Química',
			'Estatística',
			'Farmácia',
			'Filosofia'
			'Física',
			'Fisioterapia',
			'Fonoaudiologia',
			'Geografia',
			'Geologia',
			'História',
			'Jornalismo',
			'Letras',
			'Linguística',
			'Logística',
			'Marketing',
			'Matemática',
			'Medicina',
			'Medicina Veterinária',
			'Midialogia',
			'Moda',
			'Música',
			'Nutrição',
			'Odontologia',
			'Pedagogia',
			'Psicologia',
			'Publicidade e Propaganda',
			'Química',
			'Relações Internacionais',
			'Relações Públicas',
			'Sistemas de Informação'
			]

for i in range(len(df['Curso'])):
	for course in courses:
		if (fuzz.token_set_ratio(course, df['Curso'][i]) > 90):
			df['Curso'][i] = course


# string matching - universities
universities =	['Unicamp',
				'USP',
				'Unesp',
				'Mackenzie',
				'PUCCAMP',
				'FACAMP',
				'ESAMC',
				'FATEC',
				'FGV',
				'ITA',
				'PUC',
				'UFSCAR',
				]

for i in range(len(df['Faculdade'])):
	for university in universities:
		if (fuzz.token_set_ratio(university, df['Faculdade'][i]) > 90):
			df['Faculdade'][i] = university


# string matching - cities
cities = ['Campinas',
		  'São Paulo',
		  'Limeira',
		  'São Carlos',
		  'Bauru',
		  'São José dos Campos',
		  'Piracicaba',
		  'Jundiaí',
		]

for i in range(len(df['Cidade'])):
	for city in cities:
		if (fuzz.token_set_ratio(city, df['Cidade'][i]) > 90):
			df['Cidade'][i] = city


# string matching - referrers
referrers = ['Facebook',
			 'Email',
			 'Amigos'
			 'Unicamp',
			 'Universidade'
		]

for i in range(len(df['Referência'])):
	for referrer in referrers:
		if (fuzz.token_set_ratio(referrer, df['Referência'][i]) > 90):
			df['Referência'][i] = referrer


# subscription data
total = len(df)
subscribed = len(df.loc[df['Idade'].notna() == True])
checkedin = len(df.loc[df['Status'] == 'checkedin'])

# Visitors data
# age
# remove weird values
age = df.loc[df['Idade'] < 75]
# get the average
age_avg = age.mean()['Idade']

# gender
male = len(df.loc[df['Gênero'] == 'M'])
female = len(df.loc[df['Gênero'] == 'F'])

# cities
cities = df.groupby('Cidade').size()
cities = cities.sort_values(ascending=False)
cities_top10 = cities[:10]

# first time as Talento's visitor
first_time = len(df.loc[df['Primeira Vez'] == 'True'])
not_first_time = total - first_time

# referrer
facebook = len(df.loc[df['Referência'] == 'Facebook'])
email = len(df.loc[df['Referência'] == 'Email'])
friends = len(df.loc[df['Referência'] == 'Amigos'])
others = total - (facebook + email + friends)

# main courses
courses = df.groupby('Curso').size()
courses = courses.sort_values(ascending=False)
courses_top10 = courses[:10]

# enroll year
enroll_year = df.groupby('AnoDeEntrada').size()
enroll_year = enroll_year.sort_values(ascending=False)
enroll_year_top5 = enroll_year[:5]

# universities
universities = df.groupby('Faculdade').size()
universities = universities.sort_values(ascending=False)
universities_top10 = universities[:10]

# english level
basic_english = len(df.loc[df['Inglês'] == 'basic'])
intermediate_english = len(df.loc[df['Inglês'] == 'intermediate'])
advanced_english = len(df.loc[df['Inglês'] == 'advanced'])

# excel level
basic_excel = len(df.loc[df['Excel'] == 'basic'])
intermediate_excel = len(df.loc[df['Excel'] == 'intermediate'])
advanced_excel = len(df.loc[df['Excel'] == 'advanced'])

# education
undergraduate = len(df.loc[df['Escolaridade'] == 'Graduação'])
masters = len(df.loc[df['Escolaridade'] == 'Mestrado'])
phd = len(df.loc[df['Escolaridade'] == 'Doutorado'])
high = len(df.loc[df['Escolaridade'] == 'Ensino Médio'])
elementary = len(df.loc[df['Escolaridade'] == 'Ensino Fundamental'])

# resumé
one_resume = len(df.loc[df['Currículo1'].notna() == True])
two_resume = len(df.loc[df['Currículo2'].notna() == True])
