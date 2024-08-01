import pandas as pd

def analyze_bar_graph(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Bar Graph Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column2]):
        analysis.append(f"<h2>Basic statistics for {column2}:</h2>")
        analysis.append(f"<h3>Mean:</h3> {df[column2].mean():.2f}")
        analysis.append(f"<h3>Median:</h3> {df[column2].median():.2f}")
        analysis.append(f"<h3>Standard Deviation:</h3> {df[column2].std():.2f}")
        analysis.append(f"<h3>Minimum:</h3> {df[column2].min():.2f}")
        analysis.append(f"<h3>Maximum:</h3> {df[column2].max():.2f}")
    else:
        top_categories = df[column2].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column2}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_scatter_plot(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Scatter Plot Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column1]) and pd.api.types.is_numeric_dtype(df[column2]):
        correlation = df[column1].corr(df[column2])
        analysis.append(f"<h2>Correlation between {column1} and {column2}:</h2>")
        analysis.append(f"<h3>Correlation Coefficient:</h3> {correlation:.2f}")
    else:
        analysis.append("<h2>Correlation analysis requires numeric columns.</h2>")

    return "<br>".join(analysis)

def analyze_area_plot(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Area Plot Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column1]) and pd.api.types.is_numeric_dtype(df[column2]):
        analysis.append(f"<h2>Basic statistics for {column1}:</h2>")
        analysis.append(f"<h3>Mean:</h3> {df[column1].mean():.2f}")
        analysis.append(f"<h3>Median:</h3> {df[column1].median():.2f}")
        analysis.append(f"<h3>Standard Deviation:</h3> {df[column1].std():.2f}")
        analysis.append(f"<h3>Minimum:</h3> {df[column1].min():.2f}")
        analysis.append(f"<h3>Maximum:</h3> {df[column1].max():.2f}")
    else:
        top_categories = df[column1].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column1}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_scatter_3d_plot(df: pd.DataFrame, column1: str, column2: str, column3: str) -> str:
    analysis = []
    analysis.append(f"<h2>3D Scatter Plot Analysis of {column1}, {column2}, and {column3}:</h2>")

    for col in [column1, column2, column3]:
        if pd.api.types.is_numeric_dtype(df[col]):
            analysis.append(f"<h2>Basic statistics for {col}:</h2>")
            analysis.append(f"<h3>Mean:</h3> {df[col].mean():.2f}")
            analysis.append(f"<h3>Median:</h3> {df[col].median():.2f}")
            analysis.append(f"<h3>Standard Deviation:</h3> {df[col].std():.2f}")
            analysis.append(f"<h3>Minimum:</h3> {df[col].min():.2f}")
            analysis.append(f"<h3>Maximum:</h3> {df[col].max():.2f}")
        else:
            top_categories = df[col].value_counts().nlargest(5)
            analysis.append(f"<h2>Top 5 most frequent values in {col}:</h2>")
            for category, value in top_categories.items():
                analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)


def analyze_line_plot(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Line Plot Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column2]):
        analysis.append(f"<h2>Basic statistics for {column2}:</h2>")
        analysis.append(f"<h3>Mean:</h3> {df[column2].mean():.2f}")
        analysis.append(f"<h3>Median:</h3> {df[column2].median():.2f}")
        analysis.append(f"<h3>Standard Deviation:</h3> {df[column2].std():.2f}")
        analysis.append(f"<h3>Minimum:</h3> {df[column2].min():.2f}")
        analysis.append(f"<h3>Maximum:</h3> {df[column2].max():.2f}")
    else:
        top_categories = df[column2].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column2}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_histogram(df: pd.DataFrame, column: str) -> str:
    analysis = []
    analysis.append(f"<h2>Histogram Analysis of {column}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column]):
        analysis.append(f"<h2>Basic statistics for {column}:</h2>")
        analysis.append(f"<h3>Mean:</h3> {df[column].mean():.2f}")
        analysis.append(f"<h3>Median:</h3> {df[column].median():.2f}")
        analysis.append(f"<h3>Standard Deviation:</h3> {df[column].std():.2f}")
        analysis.append(f"<h3>Minimum:</h3> {df[column].min():.2f}")
        analysis.append(f"<h3>Maximum:</h3> {df[column].max():.2f}")

        analysis.append(f"<h2>Value ranges:</h2>")
        bins = pd.cut(df[column], bins=10)
        bin_counts = bins.value_counts().sort_index()
        for interval, count in bin_counts.items():
            analysis.append(f"<h3>{interval}:</h3> {count}")
    else:
        top_categories = df[column].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_box_plot(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Box Plot Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column2]):
        analysis.append(f"<h2>Basic statistics for {column2}:</h2>")
        analysis.append(f"<h3>Mean:</h3> {df[column2].mean():.2f}")
        analysis.append(f"<h3>Median:</h3> {df[column2].median():.2f}")
        analysis.append(f"<h3>Standard Deviation:</h3> {df[column2].std():.2f}")
        analysis.append(f"<h3>Minimum:</h3> {df[column2].min():.2f}")
        analysis.append(f"<h3>Maximum:</h3> {df[column2].max():.2f}")

        analysis.append(f"<h2>Box plot summary:</h2>")
        q1 = df[column2].quantile(0.25)
        q3 = df[column2].quantile(0.75)
        iqr = q3 - q1
        analysis.append(f"<h3>Q1 (25th percentile):</h3> {q1:.2f}")
        analysis.append(f"<h3>Q3 (75th percentile):</h3> {q3:.2f}")
        analysis.append(f"<h3>IQR (Interquartile Range):</h3> {iqr:.2f}")
        analysis.append(f"<h3>Lower Whisker:</h3> {max(df[column2].min(), q1 - 1.5 * iqr):.2f}")
        analysis.append(f"<h3>Upper Whisker:</h3> {min(df[column2].max(), q3 + 1.5 * iqr):.2f}")
    else:
        top_categories = df[column2].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column2}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_pie_chart(df: pd.DataFrame, column1: str, column2: str) -> str:
    analysis = []
    analysis.append(f"<h2>Pie Chart Analysis of {column1} vs {column2}:</h2>")

    if pd.api.types.is_numeric_dtype(df[column2]):
        top_categories = df.groupby(column1)[column2].sum().nlargest(5)
        analysis.append(f"<h2>Top 5 categories in {column1} by {column2}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value:.2f}")
    else:
        top_categories = df[column1].value_counts().nlargest(5)
        analysis.append(f"<h2>Top 5 most frequent values in {column1}:</h2>")
        for category, value in top_categories.items():
            analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_line_3d_plot(df: pd.DataFrame, column1: str, column2: str, column3: str) -> str:
    analysis = []
    analysis.append(f"<h2>3D Line Plot Analysis of {column1}, {column2}, and {column3}:</h2>")

    for col in [column1, column2, column3]:
        if pd.api.types.is_numeric_dtype(df[col]):
            analysis.append(f"<h2>Basic statistics for {col}:</h2>")
            analysis.append(f"<h3>Mean:</h3> {df[col].mean():.2f}")
            analysis.append(f"<h3>Median:</h3> {df[col].median():.2f}")
            analysis.append(f"<h3>Standard Deviation:</h3> {df[col].std():.2f}")
            analysis.append(f"<h3>Minimum:</h3> {df[col].min():.2f}")
            analysis.append(f"<h3>Maximum:</h3> {df[col].max():.2f}")
        else:
            top_categories = df[col].value_counts().nlargest(5)
            analysis.append(f"<h2>Top 5 most frequent values in {col}:</h2>")
            for category, value in top_categories.items():
                analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def analyze_surface_3d_plot(df: pd.DataFrame, column1: str, column2: str, column3: str) -> str:
    analysis = []
    analysis.append(f"<h2>3D Surface Plot Analysis of {column1}, {column2}, and {column3}:</h2>")

    for col in [column1, column2, column3]:
        if pd.api.types.is_numeric_dtype(df[col]):
            analysis.append(f"<h2>Basic statistics for {col}:</h2>")
            analysis.append(f"<h3>Mean:</h3> {df[col].mean():.2f}")
            analysis.append(f"<h3>Median:</h3> {df[col].median():.2f}")
            analysis.append(f"<h3>Standard Deviation:</h3> {df[col].std():.2f}")
            analysis.append(f"<h3>Minimum:</h3> {df[col].min():.2f}")
            analysis.append(f"<h3>Maximum:</h3> {df[col].max():.2f}")
        else:
            top_categories = df[col].value_counts().nlargest(5)
            analysis.append(f"<h2>Top 5 most frequent values in {col}:</h2>")
            for category, value in top_categories.items():
                analysis.append(f"<h3>{category}:</h3> {value}")

    return "<br>".join(analysis)

def is_numeric(series):
    try:
        pd.to_numeric(series)
        return True
    except ValueError:
        return False
