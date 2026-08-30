import pandas as pd
import json
from pathlib import Path

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from (videos.csv and category_id.json) and answer the questions.
"""


def _path(name: str) -> str:
    # grader: /data/... ; local: ./...
    grader = Path("/data") / name
    return str(grader if grader.exists() else Path(name))


def Q1():
    """
        1. How many rows are there in the videos.csv after removing duplications?
        - To access 'videos.csv', use the path '/data/videos.csv'.
    """
    vdo_df = pd.read_csv(_path("videos.csv"))
    vdo_df.drop_duplicates(inplace=True)
    return len(vdo_df)


def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    return vdo_df.loc[vdo_df["dislikes"] > vdo_df["likes"], "title"].nunique()


def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    mask = (vdo_df["trending_date"] == "18.22.01") & (vdo_df["comment_count"] > 10000)
    return int(mask.sum())


def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    return vdo_df.groupby("trending_date")["comment_count"].mean().idxmin()


def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - videos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'category_id.json' into memory before executing any operations.
            - To access 'category_id.json', use the path '/data/category_id.json'.
    '''
    with open(_path("category_id.json")) as fd:
        cat_json = json.load(fd)

    cat_list = [(int(d["id"]), d["snippet"]["title"]) for d in cat_json["items"]]
    cat_df = pd.DataFrame(cat_list, columns=["id", "category"])

    merged = vdo_df.merge(cat_df, left_on="category_id", right_on="id")
    daily = merged.groupby(["trending_date", "category"])["views"].sum().unstack(fill_value=0)
    return int((daily["Sports"] > daily["Comedy"]).sum())
