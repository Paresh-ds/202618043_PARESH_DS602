import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from scipy import stats
from statsmodels.stats.stattools import jarque_bera
from statsmodels.stats.outliers_influence import variance_inflation_factor

from model import df, model, FEATURES


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="California Housing Statistical Dashboard",
    layout="wide"
)


# ==========================================
# MAIN TITLE
# ==========================================

st.title("California Housing Statistical Dashboard")

st.write(
    "Interactive dashboard for California housing "
    "statistical analysis and prediction."
)


# ==========================================
# CREATE THREE TABS
# ==========================================

tab1, tab2, tab3 = st.tabs([
    "Data Exploration",
    "Hypothesis Testing Lab",
    "Live Prediction and Diagnostics"
])


# ==========================================
# TAB 1 - DATA EXPLORATION
# ==========================================

with tab1:

    st.header("Data Exploration")

    st.write(
        "Explore the California Housing dataset "
        "using interactive filters and visualizations."
    )


    # ======================================
    # SIDEBAR FILTERS
    # ======================================

    st.sidebar.header("Data Filters")

    min_income = float(df["MedInc"].min())
    max_income = float(df["MedInc"].max())

    income_range = st.sidebar.slider(
        "Median Income Range",
        min_value=min_income,
        max_value=max_income,
        value=(min_income, max_income)
    )


    income_groups = df["IncomeGroup"].unique()

    selected_groups = st.sidebar.multiselect(
        "Income Group",
        options=income_groups,
        default=list(income_groups)
    )


    min_age = int(df["HouseAge"].min())
    max_age = int(df["HouseAge"].max())

    age_range = st.sidebar.slider(
        "House Age Range",
        min_value=min_age,
        max_value=max_age,
        value=(min_age, max_age)
    )


    # ======================================
    # FILTER DATA
    # ======================================

    filtered_df = df[
        (df["MedInc"] >= income_range[0]) &
        (df["MedInc"] <= income_range[1]) &
        (df["HouseAge"] >= age_range[0]) &
        (df["HouseAge"] <= age_range[1]) &
        (df["IncomeGroup"].isin(selected_groups))
    ]


    # ======================================
    # DATASET OVERVIEW
    # ======================================

    st.subheader("Filtered Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Records",
        len(filtered_df)
    )

    col2.metric(
        "Variables",
        len(filtered_df.columns)
    )

    col3.metric(
        "Average House Value",
        f"{filtered_df['MedHouseVal'].mean():.3f}"
        if len(filtered_df) > 0
        else "N/A"
    )

    col4.metric(
        "Average Median Income",
        f"{filtered_df['MedInc'].mean():.3f}"
        if len(filtered_df) > 0
        else "N/A"
    )


    # ======================================
    # FILTERED DATASET
    # ======================================

    st.subheader("Filtered Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


    # ======================================
    # DESCRIPTIVE STATISTICS
    # ======================================

    st.subheader("Descriptive Statistics")

    numerical_columns = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude",
        "MedHouseVal"
    ]

    descriptive_stats = filtered_df[
        numerical_columns
    ].describe().T

    descriptive_stats["Median"] = (
        filtered_df[numerical_columns].median()
    )

    descriptive_stats["IQR"] = (
        filtered_df[numerical_columns].quantile(0.75)
        -
        filtered_df[numerical_columns].quantile(0.25)
    )

    descriptive_stats["Skewness"] = (
        filtered_df[numerical_columns].skew()
    )

    descriptive_stats["Kurtosis"] = (
        filtered_df[numerical_columns].kurtosis()
    )

    st.dataframe(
        descriptive_stats,
        use_container_width=True
    )


    # ======================================
    # SCATTER PLOT
    # ======================================

    st.subheader("Median Income vs House Value")

    if len(filtered_df) > 0:

        fig_scatter = px.scatter(
            filtered_df,
            x="MedInc",
            y="MedHouseVal",
            color="IncomeGroup",
            title="Median Income vs Median House Value",
            labels={
                "MedInc": "Median Income",
                "MedHouseVal": "Median House Value"
            }
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

    else:

        st.warning(
            "No records match the selected filters."
        )


    # ======================================
    # HISTOGRAM
    # ======================================

    st.subheader("Distribution of House Values")

    if len(filtered_df) > 0:

        fig_hist = px.histogram(
            filtered_df,
            x="MedHouseVal",
            color="IncomeGroup",
            nbins=40,
            title="Distribution of Median House Value",
            labels={
                "MedHouseVal": "Median House Value"
            }
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )


# ==========================================
# TAB 2 - HYPOTHESIS TESTING LAB
# ==========================================

with tab2:

    st.header("Hypothesis Testing Lab")

    st.write(
        "Select a categorical variable and a numerical "
        "variable to perform a statistical comparison "
        "between two groups."
    )


    # ======================================
    # VARIABLE SELECTION
    # ======================================

    categorical_variables = [
        "IncomeGroup"
    ]

    numerical_variables = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude",
        "MedHouseVal"
    ]


    category = st.selectbox(
        "Select Categorical Variable",
        categorical_variables
    )


    metric = st.selectbox(
        "Select Numerical Variable",
        numerical_variables
    )


    # ======================================
    # GROUP SELECTION
    # ======================================

    available_groups = (
        df[category]
        .dropna()
        .unique()
        .tolist()
    )


    selected_groups = st.multiselect(
        "Select Two Groups",
        options=available_groups,
        default=available_groups[:2]
    )


    if len(selected_groups) != 2:

        st.warning(
            "Please select exactly two groups."
        )

    else:

        group1_name = selected_groups[0]
        group2_name = selected_groups[1]


        group1 = df[
            df[category] == group1_name
        ][metric].dropna()


        group2 = df[
            df[category] == group2_name
        ][metric].dropna()


        # ==================================
        # GROUP SUMMARY
        # ==================================

        st.subheader("Group Summary")

        col1, col2 = st.columns(2)


        with col1:

            st.write(
                f"Group 1: {group1_name}"
            )

            st.write(
                f"Sample Size: {len(group1)}"
            )

            st.write(
                f"Mean: {group1.mean():.4f}"
            )

            st.write(
                f"Median: {group1.median():.4f}"
            )


        with col2:

            st.write(
                f"Group 2: {group2_name}"
            )

            st.write(
                f"Sample Size: {len(group2)}"
            )

            st.write(
                f"Mean: {group2.mean():.4f}"
            )

            st.write(
                f"Median: {group2.median():.4f}"
            )


        # ==================================
        # HYPOTHESES
        # ==================================

        st.subheader("Hypotheses")

        st.write(
            "H0: There is no significant difference "
            "between the two groups."
        )

        st.write(
            "H1: There is a significant difference "
            "between the two groups."
        )


        # ==================================
        # SHAPIRO-WILK TEST
        # ==================================

        st.subheader("Normality Test")

        group1_sample = group1.sample(
            n=min(len(group1), 5000),
            random_state=42
        )

        group2_sample = group2.sample(
            n=min(len(group2), 5000),
            random_state=42
        )


        shapiro1 = stats.shapiro(
            group1_sample
        )

        shapiro2 = stats.shapiro(
            group2_sample
        )


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                f"{group1_name} p-value",
                f"{shapiro1.pvalue:.6f}"
            )


        with col2:

            st.metric(
                f"{group2_name} p-value",
                f"{shapiro2.pvalue:.6f}"
            )


        # ==================================
        # LEVENE TEST
        # ==================================

        st.subheader("Equal Variance Test")

        levene_stat, levene_pvalue = stats.levene(
            group1,
            group2
        )


        st.metric(
            "Levene p-value",
            f"{levene_pvalue:.6f}"
        )


        normal_group1 = (
            shapiro1.pvalue > 0.05
        )

        normal_group2 = (
            shapiro2.pvalue > 0.05
        )


        both_normal = (
            normal_group1 and normal_group2
        )


        equal_variance = (
            levene_pvalue > 0.05
        )


        # ==================================
        # SELECT STATISTICAL TEST
        # ==================================

        st.subheader("Statistical Test")


        if both_normal:

            test_statistic, p_value = stats.ttest_ind(
                group1,
                group2,
                equal_var=equal_variance
            )

            if equal_variance:

                test_name = "Two-Sample t-test"

            else:

                test_name = "Welch's t-test"

        else:

            test_statistic, p_value = stats.mannwhitneyu(
                group1,
                group2,
                alternative="two-sided"
            )

            test_name = "Mann-Whitney U test"


        # ==================================
        # TEST RESULT
        # ==================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Selected Test",
                test_name
            )


        with col2:

            st.metric(
                "Test Statistic",
                f"{test_statistic:.4f}"
            )


        with col3:

            st.metric(
                "p-value",
                f"{p_value:.6f}"
            )


        # ==================================
        # DECISION
        # ==================================

        st.subheader("Decision at alpha = 0.05")


        if p_value < 0.05:

            st.error(
                "Reject H0: There is a statistically "
                "significant difference between the two groups."
            )

        else:

            st.success(
                "Fail to Reject H0: There is insufficient "
                "evidence of a statistically significant "
                "difference between the two groups."
            )


        # ==================================
        # TEST EXPLANATION
        # ==================================

        st.subheader("Test Selection Explanation")


        if both_normal:

            if equal_variance:

                st.write(
                    "Both groups passed the normality check "
                    "and Levene's test indicates equal variances. "
                    "Therefore, a standard two-sample t-test "
                    "was performed."
                )

            else:

                st.write(
                    "Both groups passed the normality check, "
                    "but Levene's test indicates unequal variances. "
                    "Therefore, Welch's t-test was performed."
                )

        else:

            st.write(
                "At least one group did not satisfy the "
                "normality condition. Therefore, the "
                "Mann-Whitney U test was performed."
            )


# ==========================================
# TAB 3 - LIVE PREDICTION AND DIAGNOSTICS
# ==========================================

with tab3:

    st.header("Live Prediction and Diagnostics")

    st.write(
        "Enter housing characteristics to generate "
        "a live prediction from the OLS regression model."
    )


    # ======================================
    # INPUT SECTION
    # ======================================

    st.subheader("Housing Characteristics")


    col1, col2 = st.columns(2)


    with col1:

        MedInc = st.number_input(
            "Median Income",
            min_value=float(df["MedInc"].min()),
            max_value=float(df["MedInc"].max()),
            value=float(df["MedInc"].median()),
            step=0.1
        )


        HouseAge = st.number_input(
            "House Age",
            min_value=float(df["HouseAge"].min()),
            max_value=float(df["HouseAge"].max()),
            value=float(df["HouseAge"].median()),
            step=1.0
        )


        AveRooms = st.number_input(
            "Average Rooms",
            min_value=float(df["AveRooms"].min()),
            max_value=float(df["AveRooms"].max()),
            value=float(df["AveRooms"].median()),
            step=0.1
        )


        AveBedrms = st.number_input(
            "Average Bedrooms",
            min_value=float(df["AveBedrms"].min()),
            max_value=float(df["AveBedrms"].max()),
            value=float(df["AveBedrms"].median()),
            step=0.1
        )


    with col2:

        Population = st.number_input(
            "Population",
            min_value=float(df["Population"].min()),
            max_value=float(df["Population"].max()),
            value=float(df["Population"].median()),
            step=10.0
        )


        AveOccup = st.number_input(
            "Average Occupancy",
            min_value=float(df["AveOccup"].min()),
            max_value=float(df["AveOccup"].max()),
            value=float(df["AveOccup"].median()),
            step=0.1
        )


        Latitude = st.number_input(
            "Latitude",
            min_value=float(df["Latitude"].min()),
            max_value=float(df["Latitude"].max()),
            value=float(df["Latitude"].median()),
            step=0.01
        )


        Longitude = st.number_input(
            "Longitude",
            min_value=float(df["Longitude"].min()),
            max_value=float(df["Longitude"].max()),
            value=float(df["Longitude"].median()),
            step=0.01
        )


    # ======================================
    # CREATE NEW OBSERVATION
    # ======================================

    new_house = pd.DataFrame({
        "MedInc": [MedInc],
        "HouseAge": [HouseAge],
        "AveRooms": [AveRooms],
        "AveBedrms": [AveBedrms],
        "Population": [Population],
        "AveOccup": [AveOccup],
        "Latitude": [Latitude],
        "Longitude": [Longitude]
    })


    # ======================================
    # ADD INTERCEPT
    # ======================================

    new_house = new_house[FEATURES]

    new_house = pd.concat(
        [
            pd.DataFrame({"const": [1]}),
            new_house
        ],
        axis=1
    )


    # ======================================
    # GENERATE MODEL PREDICTION
    # ======================================

    prediction_result = model.get_prediction(
        new_house
    )


    prediction_summary = (
        prediction_result.summary_frame(
            alpha=0.05
        )
    )


    predicted_value = (
        prediction_summary["mean"].iloc[0]
    )


    confidence_lower = (
        prediction_summary["mean_ci_lower"].iloc[0]
    )


    confidence_upper = (
        prediction_summary["mean_ci_upper"].iloc[0]
    )


    prediction_lower = (
        prediction_summary["obs_ci_lower"].iloc[0]
    )


    prediction_upper = (
        prediction_summary["obs_ci_upper"].iloc[0]
    )


    # ======================================
    # DISPLAY PREDICTION
    # ======================================

    st.subheader("Model Prediction")


    st.metric(
        "Predicted Median House Value",
        f"{predicted_value:.4f}"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.write("95% Confidence Interval")

        st.write(
            f"Lower: {confidence_lower:.4f}"
        )

        st.write(
            f"Upper: {confidence_upper:.4f}"
        )


    with col2:

        st.write("95% Prediction Interval")

        st.write(
            f"Lower: {prediction_lower:.4f}"
        )

        st.write(
            f"Upper: {prediction_upper:.4f}"
        )


    # ======================================
    # INTERVAL VISUALIZATION
    # ======================================

    interval_data = pd.DataFrame({
        "Type": [
            "Confidence Interval",
            "Prediction Interval"
        ],
        "Lower": [
            confidence_lower,
            prediction_lower
        ],
        "Upper": [
            confidence_upper,
            prediction_upper
        ]
    })


    fig_interval = go.Figure()


    for i in range(len(interval_data)):

        fig_interval.add_trace(
            go.Scatter(
                x=[
                    interval_data["Lower"].iloc[i],
                    interval_data["Upper"].iloc[i]
                ],
                y=[
                    interval_data["Type"].iloc[i],
                    interval_data["Type"].iloc[i]
                ],
                mode="lines+markers",
                name=interval_data["Type"].iloc[i]
            )
        )


    fig_interval.add_vline(
        x=predicted_value,
        line_dash="dash",
        annotation_text="Prediction"
    )


    fig_interval.update_layout(
        title="95% Confidence and Prediction Intervals",
        xaxis_title="House Value",
        yaxis_title="Interval Type"
    )


    st.plotly_chart(
        fig_interval,
        use_container_width=True
    )


    # ======================================
    # MODEL DIAGNOSTICS
    # ======================================

    st.subheader("Model Diagnostics")


    fitted_values = model.fittedvalues

    residuals = model.resid


    # ======================================
    # RESIDUALS VS FITTED
    # ======================================

    st.write("Residuals vs Fitted Values")


    residual_df = pd.DataFrame({
        "Fitted Values": fitted_values,
        "Residuals": residuals
    })


    fig_residual = px.scatter(
        residual_df,
        x="Fitted Values",
        y="Residuals",
        title="Residuals vs Fitted Values",
        opacity=0.35
    )


    fig_residual.add_hline(
        y=0,
        line_dash="dash"
    )


    st.plotly_chart(
        fig_residual,
        use_container_width=True
    )


    # ======================================
    # Q-Q PLOT
    # ======================================

    st.write("Normal Q-Q Plot")


    qq_result = stats.probplot(
        residuals,
        dist="norm"
    )


    theoretical_quantiles = (
        qq_result[0][0]
    )

    ordered_residuals = (
        qq_result[0][1]
    )

    slope = qq_result[1][0]
    intercept = qq_result[1][1]


    qq_df = pd.DataFrame({
        "Theoretical Quantiles":
            theoretical_quantiles,
        "Ordered Residuals":
            ordered_residuals
    })


    fig_qq = px.scatter(
        qq_df,
        x="Theoretical Quantiles",
        y="Ordered Residuals",
        title="Normal Q-Q Plot"
    )


    line_x = [
        theoretical_quantiles.min(),
        theoretical_quantiles.max()
    ]


    line_y = [
        intercept + slope * line_x[0],
        intercept + slope * line_x[1]
    ]


    fig_qq.add_trace(
        go.Scatter(
            x=line_x,
            y=line_y,
            mode="lines",
            name="Reference Line"
        )
    )


    st.plotly_chart(
        fig_qq,
        use_container_width=True
    )


    # ======================================
    # JARQUE-BERA TEST
    # ======================================

    st.subheader("Jarque-Bera Normality Test")


    jb_statistic, jb_pvalue, skewness, kurtosis = (
        jarque_bera(residuals)
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "JB Statistic",
            f"{jb_statistic:.3f}"
        )


    with col2:

        st.metric(
            "p-value",
            f"{jb_pvalue:.6f}"
        )


    with col3:

        st.metric(
            "Skewness",
            f"{skewness:.3f}"
        )


    with col4:

        st.metric(
            "Kurtosis",
            f"{kurtosis:.3f}"
        )


    if jb_pvalue < 0.05:

        st.error(
            "Reject H0: The residuals are not "
            "normally distributed."
        )

    else:

        st.success(
            "Fail to Reject H0: The residuals are "
            "approximately normally distributed."
        )


    # ======================================
    # VIF
    # ======================================

    st.subheader("Variance Inflation Factor")


    X_vif = df[FEATURES]


    vif_table = pd.DataFrame({
        "Variable": FEATURES,
        "VIF": [
            variance_inflation_factor(
                X_vif.values,
                i
            )
            for i in range(len(FEATURES))
        ]
    })


    st.dataframe(
        vif_table,
        use_container_width=True
    )


    # ======================================
    # MODEL SUMMARY
    # ======================================

    st.subheader("Regression Model Summary")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "R-squared",
            f"{model.rsquared:.4f}"
        )


    with col2:

        st.metric(
            "Adjusted R-squared",
            f"{model.rsquared_adj:.4f}"
        )


    with col3:

        st.metric(
            "Observations",
            f"{int(model.nobs)}"
        )


    with col4:

        st.metric(
            "F-statistic",
            f"{model.fvalue:.2f}"
        )