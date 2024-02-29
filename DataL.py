import pandas as pd
title_basics_df = pd.read_csv("C:\\Users\\GAGAN\\OneDrive\\Desktop\\EDA-Project(IMDB)\\title.basics.tsv\\data.tsv", sep='\t', low_memory=False)
title_ratings_df = pd.read_csv("C:\\Users\\GAGAN\\OneDrive\\Desktop\\EDA-Project(IMDB)\\title.ratings.tsv\\data.tsv", sep='\t', low_memory=False)
title_name_df = pd.read_csv("C:\\Users\\GAGAN\\OneDrive\\Desktop\\EDA-Project(IMDB)\\name.basics.tsv\\data.tsv", sep='\t', low_memory=False)
title_basics_df.head(10)