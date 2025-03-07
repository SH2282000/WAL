
import pandas as pd



def remove_outliers_per_column(df:pd.DataFrame, column:str) -> pd.DataFrame:
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    print(lower_bound, upper_bound)
    # Filter the DataFrame based on the specific column
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df


def remove_outliers_based_on_IQR(df:pd.DataFrame) -> pd.DataFrame:
    df = remove_outliers_per_column(df, "Grade Summer (AVG)")
    print("after removing grade summer outliers", len(df))
    df = remove_outliers_per_column(df, "Grade Winter (AVG)")
    print("after removing grade winter outliers", len(df))
    df = remove_outliers_per_column(df, "ECTS Summer")
    print("after removing ects summer outliers", len(df))
    df = remove_outliers_per_column(df, "ECTS Winter")
    print("after removing ects winter outliers", len(df))
    return df


def prepare_DF(df:pd.DataFrame) -> pd.DataFrame:
    # Drop rows with missing values
    df = df.dropna()
    # remove outliers
    df = remove_outliers_based_on_IQR(df)
    # Reset the index so it is continuous
    df = df.reset_index(drop=True)
    return df