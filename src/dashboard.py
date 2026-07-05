#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import kagglehub
# path = kagglehub.dataset_download("mrnize/pharmacy-transaction")


# In[2]:


# from pathlib import Path
# files = [i for i in Path(path).rglob('*.csv')]
# files


# In[76]:


# Prepare Data
import pandas as pd

# Visualize Data
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.rcParams['axes.formatter.use_mathtext'] = True
plt.style.use('seaborn-v0_8-whitegrid')


# In[77]:


def wrangle(filepath):
    # Read csv file into DataFrame
    df = pd.read_csv(filepath, parse_dates=['Transaction_Date'], index_col='Transaction_ID')

    # Drop high null column
    df.drop(columns=['Strength_mg'], inplace=True)

    # Rename Medicine Name to Brand Name
    df.rename(columns={'Medicine_Name': 'Brand_Name'}, inplace=True)

    # Return DataFrame
    return df


# In[78]:


import os

relative_path = 'Pharmacy_OLTP_SLStyle_18Months.csv'

# Get the path to the folder where THIS script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Point to the data folder (going up one level from 'src' into 'data')
data_path = os.path.join(current_dir, '..', 'data', relative_path)

df = wrangle(data_path)


# In[80]:


# import itables
# itables.show(df.head())


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


# Number of branches
def get_branch_count(df):
    return str(df['Branch_ID'].nunique())
get_branch_count(df)


# In[10]:


# Best performing Branch (ID)
def get_best_branch(df, column='Branch_ID'):
    return df.groupby(column)['Line_Total_LKR'].sum().idxmax()
get_best_branch(df)


# In[11]:


# Best performing Branch (Name)
get_best_branch(df, column='Branch_Name')


# In[12]:


# Worst performing Branch (ID)
def get_worst_branch(df, column='Branch_ID'):
    return df.groupby(column)['Line_Total_LKR'].sum().idxmin()
get_worst_branch(df)


# In[13]:


# Worst performing Branch (Name)
get_worst_branch(df, column='Branch_Name')


# In[14]:


# Difference in performance between best and worst branches
def get_branch_perf_diff(df, column='Branch_ID'):
    branch_perf = df.groupby(column)['Line_Total_LKR'].sum().reset_index()
    return f'''{round(branch_perf['Line_Total_LKR'].max() - branch_perf['Line_Total_LKR'].min(), 2)} LKR'''
get_branch_perf_diff(df)


# In[15]:


# Percentage of performance difference to best performance
def get_branch_perf_diff_perc(df, column='Branch_ID'):
    branch_perf = df.groupby(column)['Line_Total_LKR'].sum().reset_index()
    return f'''{round((branch_perf['Line_Total_LKR'].max() - branch_perf['Line_Total_LKR'].min()) / branch_perf['Line_Total_LKR'].max() * 100, 2)}%'''
get_branch_perf_diff_perc(df)


# In[16]:


# Most common payment method
def get_most_common_payment(df):
    return df['Payment_Method'].value_counts().head(1).keys()[0]
get_most_common_payment(df[df['Branch_ID'] == 7])


# In[17]:


# Rarest payment method
def get_rarest_payment(df):
    return df['Payment_Method'].value_counts().tail(1).keys()[0]
get_rarest_payment(df[df['Branch_ID'] == 7])


# In[18]:


# Proportion of customers by gender
# df_branch = df[df['Branch_ID'] == 5]
def get_gender_prop(df):
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        (
            round(df['Customer_Gender']
                .value_counts(normalize=True)
                .mul(100), 2)),
        labels=['Female', 'Male'],
        autopct='%1.1f%%'
    )
    ax.set_title('Percentage Proportion of Customer Gender')
    plt.close()
    return fig
get_gender_prop(df)


# In[19]:


# Most Popular Product amongst Females (Generic)
def get_most_popular_product(df, column='Generic_Name', gender='Female'):
    return df[df['Customer_Gender'] == gender][column].value_counts().head(1).keys()[0]
get_most_popular_product(df)


# In[20]:


# Most Popular Product amongst Females (Brand)
# def get_most_popular_brand_female(df, column='Brand_Name'):
#     return df[df['Customer_Gender'] == 'Female'][column].value_counts().head(1).keys()[0]
get_most_popular_product(df, column='Brand_Name')


# In[21]:


# Most Popular Product amongst Males (Generic)
# def get_most_popular_male(df, column='Generic_Name'):
#     return df[df['Customer_Gender'] == 'Male'][column].value_counts().head(1).keys()[0]
get_most_popular_product(df, gender='Male')


# In[22]:


# Most Popular Product amongst Males (Brand)
# def get_most_popular_brand_male(df, column='Brand_Name'):
#     return df[df['Customer_Gender'] == 'Male'][column].value_counts().head(1).keys()[0]
get_most_popular_product(df, column='Brand_Name', gender='Male')


# In[23]:


# Least Popular Product amongst Females (Generic)
def get_least_popular_product(df, column='Generic_Name', gender='Female'):
    return df[df['Customer_Gender'] == gender][column].value_counts().tail(1).keys()[0]
get_least_popular_product(df)


# In[24]:


# Least Popular Product amongst Females (Brand)
# def get_least_popular_brand_female(df, column='Brand_Name'):
#     return df[df['Customer_Gender'] == 'Female'][column].value_counts().tail(1).keys()[0]
get_least_popular_product(df, column='Brand_Name')


# In[25]:


# Least Popular Product amongst Males (Generic)
# def get_least_popular_male(df, column='Generic_Name'):
#     return df[df['Customer_Gender'] == 'Male'][column].value_counts().tail(1).keys()[0]
get_least_popular_product(df, gender='Male')


# In[26]:


# Least Popular Product amongst Males (Brand)
# def get_least_popular_brand_male(df, column='Brand_Name'):
#     return df[df['Customer_Gender'] == 'Male'][column].value_counts().tail(1).keys()[0]
get_least_popular_product(df, column='Brand_Name', gender='Male')


# In[27]:


# Age Range of Customers
def get_age_range(df, column='Customer_Age'):
    return f'''Customer Age ranges from "{df[column].min()}" to "{df[column].max()}" years old.'''
get_age_range(df)


# In[28]:


# Most Popular Product per Age (Generic)
def get_most_popular_age(df, column='Generic_Name'):
    return (df.groupby('Customer_Age')[column]
        .value_counts()
        .reset_index(name='count')
        .sort_values('count', ascending=False)
        .groupby('Customer_Age')
        .head(1)[['Customer_Age', column]]
        .sort_values('Customer_Age')
        )
get_most_popular_age(df)


# In[29]:


# Least Popular Drugs by Age of Customer (Generic)
def get_least_popular_age(df, column='Generic_Name'):
    return (df.groupby('Customer_Age')[column]
        .value_counts()
        .reset_index(name='count')
        .sort_values('count', ascending=False)
        .groupby('Customer_Age')
        .tail(1)[['Customer_Age', column]]
        .sort_values('Customer_Age')
           )
get_least_popular_age(df)


# In[30]:


# Best performing drugs (Generic)
def get_best_drugs(df, column='Generic_Name'):
    fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
    sns.barplot(
        (df.groupby(column)['Line_Total_LKR']
        .sum()
        .sort_values(ascending=False)
        .head(5)
           ),
                orient='h', 
                ax=ax)
    ax.set_ylabel(' '.join(column.split('_')))
    ax.set_xlabel('Total Sales (LKR)')
    ax.set_title(f'''Best Five (5) Performing Drugs in Sales ({column.split('_')[0]})''')
    plt.close()
    return fig
get_best_drugs(df)


# In[31]:


# Worst performing drugs (Generic)
def get_worst_drugs(df, column='Generic_Name'):
    fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
    sns.barplot(
        (df.groupby(column)['Line_Total_LKR']
        .sum()
        .sort_values(ascending=False)
        .tail(5)
           ),
                orient='h', 
                ax=ax)
    ax.set_ylabel(' '.join(column.split('_')))
    ax.set_xlabel('Total Sales (LKR)')
    ax.set_title(f'''Worst Five (5) Performing Drugs in Sales ({column.split('_')[0]})''')
    plt.close()
    return fig
get_worst_drugs(df)


# In[32]:


# Best performing drugs (Brand)
# def get_best_drugs_brand(df, column='Brand_Name'):
#     return df.groupby(column)['Line_Total_LKR'].sum().sort_values(ascending=False).head(5)
get_best_drugs(df, column='Brand_Name')


# In[33]:


# Worst performing drugs (Brand)
# def get_worst_drugs_brand(df, column='Brand_Name'):
#     return df.groupby(column)['Line_Total_LKR'].sum().sort_values(ascending=False).tail(5)
get_worst_drugs(df, column='Brand_Name')


# In[34]:


df.groupby('Dosage_Form')['Quantity'].sum().index.tolist()


# In[35]:


df['Dosage_Form'].value_counts().index.tolist()


# In[36]:


# Ranking of Dosage forms
def get_dosage_form_rank(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        (df.groupby('Dosage_Form')['Quantity']
            .sum()
            .sort_values(ascending=False)
        ),
        orient='h', 
        ax=ax
    )
    ax.set_ylabel('Dosage Form')
    ax.set_xlabel('Count')
    ax.set_title('Ranking Of Dosage Form By Popularity')
    plt.close()
    return fig
get_dosage_form_rank(df)


# In[37]:


# Most Popular Dosage Form
def get_most_popular_dosage_form(df):
    return df.groupby('Dosage_Form')['Quantity'].sum().sort_values().tail(1).index[0]
get_most_popular_dosage_form(df)


# In[38]:


# Least Popular Dosage Form
def get_least_popular_dosage_form(df):
    return df.groupby('Dosage_Form')['Quantity'].sum().sort_values().head(1).index[0]
get_least_popular_dosage_form(df)


# In[39]:


# List the Suppliers
def get_supplier_list(df):
    return pd.DataFrame({'Supplier List': df['Supplier_Name'].unique()})
get_supplier_list(df)


# In[40]:


# Supplier for most drugs
def get_most_popular_supplier(df):
    return df.groupby('Supplier_Name')['Supplier_Name'].count().sort_values(ascending=False).head(1).index[0]
get_most_popular_supplier(df)


# In[41]:


# Supplier for least drugs
def get_least_popular_supplier(df):
    return df.groupby('Supplier_Name')['Supplier_Name'].count().sort_values(ascending=False).tail(1).index[0]
get_least_popular_supplier(df)


# In[42]:


# # Best Discount (Generic)
# df.groupby('Generic_Name')['Discount_Rate'].max().sort_values(ascending=False).head(2)


# In[43]:


# Best Discount
def get_best_discount(df, column='Discount_Rate'):
    return f'{df[column].max() * (100)}%'
get_best_discount(df)


# In[44]:


# The List of Available Discount Rates
def get_discount_rate_list(df, column='Discount_Rate'):
    return df[column].unique().tolist()
get_discount_rate_list(df)


# In[45]:


# This is irrelavant since discount given is not tied to the specific drug.
# Number of Drugs with Best Discount (Generic)
mask = df['Discount_Rate'] == df['Discount_Rate'].max()
df[mask]['Generic_Name'].nunique()


# In[46]:


df[mask].head()


# In[47]:


df.columns


# In[48]:


# Worst Discount
def get_worst_discount(df, column='Discount_Rate'):
    return f'{df[column].min()}%'
get_worst_discount(df)


# In[49]:


yearly = df.set_index('Transaction_Date').resample('YE')['Line_Total_LKR'].sum()
yearly


# In[65]:


# Resample the dataframe by year And Calculate the total Drug Sales
def get_yearly_sales(df):
    yearly_df = yearly = df.set_index('Transaction_Date').resample('YE')['Line_Total_LKR'].sum()
    yearly_df.index = yearly_df.index.year
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        yearly_df,
        orient='h',
        ax=ax
    )
    ax.set_xlabel('Total Sales (LKR)')
    ax.set_ylabel('Year')
    ax.set_title('Total Sales Per Year')
    plt.close()
    return fig
get_yearly_sales(df)


# In[70]:


# Resample the dataframe by month And Calculate the total Drug Sales
def get_monthly_sales(df):
    monthly_df = df.set_index('Transaction_Date').sort_index().resample('ME')['Line_Total_LKR'].sum()
    monthly_df.index = [f"{i.month_name()}, {i.year}" for i in monthly_df.index]
    fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
    sns.barplot(
        monthly_df,
        orient='h',
        ax=ax
    )
    ax.set_xlabel('Total Sales (LKR)')
    ax.set_ylabel('Month')
    ax.set_title('Total Sales Per Month')
    plt.close()
    return fig
get_monthly_sales(df)


# In[52]:


# Most Expensive Drug
def get_most_expensive_drug(df, column='Generic_Name'):
    return df.groupby(column)['Unit_Price_LKR'].max().sort_values().tail(1).index[0]
get_most_expensive_drug(df)


# In[53]:


# Looking at specified column to confirm
df.loc[df['Unit_Price_LKR'].idxmax()]


# In[54]:


# Since Acyclovir is the best performing product in Sales, I have to confirm the Price
df[df['Generic_Name'] == 'Acyclovir'].head()


# In[55]:


# Least Expensive Drug
def get_least_expensive_drug(df, column='Generic_Name'):
    return df.groupby(column)['Unit_Price_LKR'].min().sort_values(ascending=False).tail(1).index[0]
get_least_expensive_drug(df)
# df['Generic_Name'][df['Unit_Price_LKR'] == df['Unit_Price_LKR'].min()]


# In[56]:


# Confirming
df.loc[df['Unit_Price_LKR'].idxmin()]


# In[67]:


# Single Most Expensive Transaction
def get_most_expensive_transaction(df):
    return df.loc[[df['Line_Total_LKR'].idxmax()]]
get_most_expensive_transaction(df)


# In[68]:


# Least Expensive Transaction
def get_least_expensive_transaction(df):
    return df.loc[[df['Line_Total_LKR'].idxmin()]]
get_least_expensive_transaction(df)


# In[59]:


# df2 = df.copy()


# In[60]:


# def refresh_content(branch_name):
#     if branch_name != 'None':
#         mask = df2['Branch_Name'] == branch_name
#         df2 = df2[mask]
#     else:
#         df2 = df.copy()


# In[61]:


df['Branch_Name'].unique().tolist()


# In[62]:


# Instantiating df2
df2 = df.copy()


# In[82]:


import panel as pn

# Necessary for Panel to render Matplotlib Plots, including Seaborn
matplotlib.use('Agg')

# Creating a list of Branch options to be used to mask DataFrame
branch_options = [
    'None',
    'Pharmacy - Negombo',
    'Pharmacy - Kandy City',
    'Pharmacy - Ratnapura',
    'Pharmacy - Kurunegala',
    'Pharmacy - Colombo Fort',
    'Pharmacy - Galle',
    'Pharmacy - Jaffna'
]

# Branch Select Drop down for Masking df2
branch_select = pn.widgets.Select(
    options=branch_options
)


# Instantiating The Panel Elements 
# Note: The variable names are self-explanatory
refresh_button = pn.widgets.Button(name='Refresh', button_type='primary')
df2_pane = pn.pane.DataFrame(df2.head(), sizing_mode='stretch_width')
branch_count = pn.pane.Markdown(str(df2['Branch_Name'].nunique()))
best_branch_name = pn.pane.Markdown(f'''Branch Name: {get_best_branch(df2, column='Branch_Name')}''')
best_branch_id = pn.pane.Markdown(f'''Branch ID: {get_best_branch(df2, column='Branch_ID')}''')
worst_branch_name = pn.pane.Markdown(f'''Branch Name: {get_worst_branch(df2, column='Branch_Name')}''')
worst_branch_id = pn.pane.Markdown(f'''Branch ID: {get_worst_branch(df2, column='Branch_ID')}''')
performance_difference = pn.pane.Markdown(get_branch_perf_diff(df2))
performance_difference_percentage = pn.pane.Markdown(get_branch_perf_diff_perc(df2))
most_common_payment = pn.pane.Markdown(get_most_common_payment(df2))
rarest_payment = pn.pane.Markdown(get_rarest_payment(df2))
gender_proportion = pn.pane.Matplotlib(get_gender_prop(df2))
most_popular_generic_male = pn.pane.Markdown(f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Male')}''')
most_popular_brand_male = pn.pane.Markdown(f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Male')}''')
least_pop_brand_male = pn.pane.Markdown(f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Male')}''')
least_pop_generic_male = pn.pane.Markdown(f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Male')}''')
most_popular_generic_female = pn.pane.Markdown(f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Female')}''')
most_popular_brand_female = pn.pane.Markdown(f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Female')}''')
least_pop_brand_female = pn.pane.Markdown(f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Female')}''')
least_pop_generic_female = pn.pane.Markdown(f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Female')}''')
age_range = pn.pane.Markdown(get_age_range(df2))
most_popular_by_age_generic = pn.pane.DataFrame(get_most_popular_age(df2), height=200, index=False)
least_popular_by_age_generic = pn.pane.DataFrame(get_least_popular_age(df2), height=200, index=False)
most_popular_by_age_brand = pn.pane.DataFrame(get_most_popular_age(df2, column='Brand_Name'), height=200, index=False)
least_popular_by_age_brand = pn.pane.DataFrame(get_least_popular_age(df2, column='Brand_Name'), height=200, index=False)
best_drugs_generic = pn.pane.Matplotlib(get_best_drugs(df2))
worst_drugs_generic = pn.pane.Matplotlib(get_worst_drugs(df2))
best_drugs_brand = pn.pane.Matplotlib(get_best_drugs(df2, column='Brand_Name'))
worst_drugs_brand = pn.pane.Matplotlib(get_worst_drugs(df2, column='Brand_Name'))
rank_dosage_form = pn.pane.Matplotlib(get_dosage_form_rank(df2))
most_popular_dosage_form = pn.pane.Markdown(get_most_popular_dosage_form(df2))
least_popular_dosage_form = pn.pane.Markdown(get_least_popular_dosage_form(df2))
supplier_list = pn.pane.DataFrame(get_supplier_list(df2), index=False, height=200)
most_popular_supplier = pn.pane.Markdown(get_most_popular_supplier(df2))
least_popular_supplier = pn.pane.Markdown(get_least_popular_supplier(df2))
best_discount = pn.pane.Markdown(get_best_discount(df2))
worst_discount = pn.pane.Markdown(get_worst_discount(df2))
yearly_sales = pn.pane.Matplotlib(get_yearly_sales(df2))
monthly_sales = pn.pane.Matplotlib(get_monthly_sales(df2))
most_expensive_drug = pn.pane.Markdown(get_most_expensive_drug(df2))
least_expensive_drug = pn.pane.Markdown(get_least_expensive_drug(df2))
most_expensive_transaction = pn.pane.DataFrame(get_most_expensive_transaction(df2))
least_expensive_transaction = pn.pane.DataFrame(get_least_expensive_transaction(df2))


def mask_df(event):
    # Masking df2 based on the value from branch_select Drop down
    mask = branch_select.value
    if mask == 'None':
        df2 = df.copy()
    else:
        branch_mask = df['Branch_Name'] ==  mask
        df2 = df[branch_mask]

    # Reassigning the objects of the Panel elements
    df2_pane.object = df2.head()
    branch_count.object = str(df2['Branch_Name'].nunique())
    best_branch_name.object = f'''Branch Name: {get_best_branch(df2, column='Branch_Name')}'''
    best_branch_id.object = f'''Branch ID: {get_best_branch(df2, column='Branch_ID')}'''
    worst_branch_name.object = f'''Branch Name: {get_worst_branch(df2, column='Branch_Name')}'''
    worst_branch_id.object = f'''Branch ID: {get_worst_branch(df2, column='Branch_ID')}'''
    performance_difference.object = get_branch_perf_diff(df2)
    performance_difference_percentage.object = get_branch_perf_diff_perc(df2)
    most_common_payment.object = get_most_common_payment(df2)
    rarest_payment.object = get_rarest_payment(df2)
    gender_proportion.object = get_gender_prop(df2)
    most_popular_generic_male.object = f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Male')}'''
    most_popular_brand_male.object = f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Male')}'''
    least_pop_generic_male.object = f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Male')}'''
    least_pop_brand_male.object = f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Male')}'''
    most_popular_generic_female.object = f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Female')}'''
    most_popular_brand_female.object = f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Female')}'''
    least_pop_generic_female.object = f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Female')}'''
    least_pop_brand_female.object = f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Female')}'''
    age_range.object = get_age_range(df2)
    most_popular_by_age_generic.object = get_most_popular_age(df2)
    least_popular_by_age_generic.object = get_least_popular_age(df2)
    most_popular_by_age_brand.object = get_most_popular_age(df2, column='Brand_Name')
    least_popular_by_age_brand.object = get_least_popular_age(df2, column='Brand_Name')
    best_drugs_generic.object = get_best_drugs(df2)
    worst_drugs_generic.object = get_worst_drugs(df2)
    best_drugs_brand.object = get_best_drugs(df2, column='Brand_Name')
    worst_drugs_brand.object = get_worst_drugs(df2, column='Brand_Name')
    rank_dosage_form.object = get_dosage_form_rank(df2)
    most_popular_dosage_form.object = get_most_popular_dosage_form(df2)
    least_popular_dosage_form.object = get_least_popular_dosage_form(df2)
    supplier_list.object = get_supplier_list(df2)
    most_popular_supplier.object = get_most_popular_supplier(df2)
    least_popular_supplier.object = get_least_popular_supplier(df2)
    best_discount.object = get_best_discount(df2)
    worst_discount.object = get_worst_discount(df2)
    yearly_sales.object = get_yearly_sales(df2)
    monthly_sales.object = get_monthly_sales(df2)
    most_expensive_drug.object = get_most_expensive_drug(df2)
    least_expensive_drug.object = get_least_expensive_drug(df2)
    most_expensive_transaction.object = get_most_expensive_transaction(df2)
    least_expensive_transaction.object = get_least_expensive_transaction(df2)

    
    # Put the elements into a Column Layout
    return  pn.Column(
        pn.pane.Markdown('## Select The Pharmacy Branch'),
        branch_select,
        pn.pane.Markdown('## Click to Reload the Page'),
        refresh_button,
        pn.pane.Markdown('## A Snapshot Of The Data'),
        df2_pane,
        pn.pane.Markdown('## Number of Pharmacy Branches'),
        branch_count,
        pn.pane.Markdown('## Best Pharmacy Branch By Sales'),
        best_branch_name,
        best_branch_id,
        pn.pane.Markdown('## Worst Pharmacy Branch By Sales'),
        worst_branch_name,
        worst_branch_id,
        pn.pane.Markdown('## Difference in Sales'),
        performance_difference,
        pn.pane.Markdown('## Difference in Sales (%)'),
        performance_difference_percentage,
        pn.pane.Markdown('## Most Used Mode of Payment'),
        most_common_payment,
        pn.pane.Markdown('## Least Used Mode of Payment'),
        rarest_payment,
        pn.pane.Markdown('## Proportion of Customer Gender'),
        gender_proportion,
        pn.pane.Markdown('## Most Popular Products Amongst Males'),
        most_popular_generic_male,
        most_popular_brand_male,
        pn.pane.Markdown('## Least Popular Products Amongst Males'),
        least_pop_generic_male,
        least_pop_brand_male,
        pn.pane.Markdown('## Most Popular Products Amongst Females'),
        most_popular_generic_female,
        most_popular_brand_female,
        pn.pane.Markdown('## Least Popular Products Amongst Females'),
        least_pop_generic_female,
        least_pop_brand_female,
        pn.pane.Markdown('## Age Range of Customers'),
        age_range,
        pn.pane.Markdown('## Most Popular Generic Product Per Age'),
        most_popular_by_age_generic,
        pn.pane.Markdown('## Least Popular Generic Product Per Age'),
        least_popular_by_age_generic,
        pn.pane.Markdown('## Most Popular Brand Product Per Age'),
        most_popular_by_age_brand,
        pn.pane.Markdown('## Least Popular Brand Product Per Age'),
        least_popular_by_age_brand,
        pn.pane.Markdown('## Best Generic Product In Total Sales'),
        best_drugs_generic,
        pn.pane.Markdown('## Worst Generic Product In Total Sales'),
        worst_drugs_generic,
        pn.pane.Markdown('## Best Brand Product In Total Sales'),
        best_drugs_brand,
        pn.pane.Markdown('## Worst Brand Product In Total Sales'),
        worst_drugs_brand,
        pn.pane.Markdown('## Ranking Of Dosage Forms By Popularity'),
        rank_dosage_form,
        pn.pane.Markdown('## Most Popular Dosage Form'),
        most_popular_dosage_form,
        pn.pane.Markdown('## Least Popular Dosage Form'),
        least_popular_dosage_form,
        pn.pane.Markdown('## List of Drug Wholesalers'),
        supplier_list,
        pn.pane.Markdown('## Wholesaler For Most Drugs'),
        most_popular_supplier,
        pn.pane.Markdown('## Wholesaler for Least Drugs'),
        least_popular_supplier,
        pn.pane.Markdown('## Best Discount Rate'),
        best_discount,
        pn.pane.Markdown('## Worst Discount Rate'),
        worst_discount,
        pn.pane.Markdown('## Yearly Total Sales'),
        yearly_sales,
        pn.pane.Markdown('## Monthly Total Sales'),
        monthly_sales,
        pn.pane.Markdown('## Most Expensive Drug'),
        most_expensive_drug,
        pn.pane.Markdown('## Least Expensive Drug'),
        least_expensive_drug,
        pn.pane.Markdown('## Most Expensive Transaction'),
        most_expensive_transaction,
        pn.pane.Markdown('## Least Expensive Transaction'),
        least_expensive_transaction,
        name='Dashboard'
    )

refresh_button.on_click(mask_df)

pn.template.FastListTemplate(
    main = [
        pn.Tabs(
            mask_df(refresh_button.clicks),
            pn.Column(
                '## This is the fourth app made in my series of deliverables. You can try it.',
                '## Contact me at:',
                '### Emails: owykenneth@gmail.com, drkennethowusuboakye@gmail.com',
                '### LinkedIn: https://www.linkedin.com/in/kenneth-owusu-boakye/',
                '### Phone Number: +233501326199',
                '### WhatsApp: +233501326199',
                name='About',
    )
        )],
    title = "Pharmacy Transactions Version 3"
).servable().show()import panel as pn

# Necessary for Panel to render Matplotlib Plots, including Seaborn
matplotlib.use('Agg')

# Creating a list of Branch options to be used to mask DataFrame
branch_options = [
    'None',
    'Pharmacy - Negombo',
    'Pharmacy - Kandy City',
    'Pharmacy - Ratnapura',
    'Pharmacy - Kurunegala',
    'Pharmacy - Colombo Fort',
    'Pharmacy - Galle',
    'Pharmacy - Jaffna'
]

# Branch Select Drop down for Masking df2
branch_select = pn.widgets.Select(
    options=branch_options
)


# Instantiating The Panel Elements 
# Note: The variable names are self-explanatory
refresh_button = pn.widgets.Button(name='Refresh', button_type='primary')
df2_pane = pn.pane.DataFrame(df2.head(), sizing_mode='stretch_width')
branch_count = pn.pane.Markdown(str(df2['Branch_Name'].nunique()))
best_branch_name = pn.pane.Markdown(f'''Branch Name: {get_best_branch(df2, column='Branch_Name')}''')
best_branch_id = pn.pane.Markdown(f'''Branch ID: {get_best_branch(df2, column='Branch_ID')}''')
worst_branch_name = pn.pane.Markdown(f'''Branch Name: {get_worst_branch(df2, column='Branch_Name')}''')
worst_branch_id = pn.pane.Markdown(f'''Branch ID: {get_worst_branch(df2, column='Branch_ID')}''')
performance_difference = pn.pane.Markdown(get_branch_perf_diff(df2))
performance_difference_percentage = pn.pane.Markdown(get_branch_perf_diff_perc(df2))
most_common_payment = pn.pane.Markdown(get_most_common_payment(df2))
rarest_payment = pn.pane.Markdown(get_rarest_payment(df2))
gender_proportion = pn.pane.Matplotlib(get_gender_prop(df2))
most_popular_generic_male = pn.pane.Markdown(f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Male')}''')
most_popular_brand_male = pn.pane.Markdown(f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Male')}''')
least_pop_brand_male = pn.pane.Markdown(f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Male')}''')
least_pop_generic_male = pn.pane.Markdown(f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Male')}''')
most_popular_generic_female = pn.pane.Markdown(f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Female')}''')
most_popular_brand_female = pn.pane.Markdown(f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Female')}''')
least_pop_brand_female = pn.pane.Markdown(f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Female')}''')
least_pop_generic_female = pn.pane.Markdown(f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Female')}''')
age_range = pn.pane.Markdown(get_age_range(df2))
most_popular_by_age_generic = pn.pane.DataFrame(get_most_popular_age(df2), height=200, index=False)
least_popular_by_age_generic = pn.pane.DataFrame(get_least_popular_age(df2), height=200, index=False)
most_popular_by_age_brand = pn.pane.DataFrame(get_most_popular_age(df2, column='Brand_Name'), height=200, index=False)
least_popular_by_age_brand = pn.pane.DataFrame(get_least_popular_age(df2, column='Brand_Name'), height=200, index=False)
best_drugs_generic = pn.pane.Matplotlib(get_best_drugs(df2))
worst_drugs_generic = pn.pane.Matplotlib(get_worst_drugs(df2))
best_drugs_brand = pn.pane.Matplotlib(get_best_drugs(df2, column='Brand_Name'))
worst_drugs_brand = pn.pane.Matplotlib(get_worst_drugs(df2, column='Brand_Name'))
rank_dosage_form = pn.pane.Matplotlib(get_dosage_form_rank(df2))
most_popular_dosage_form = pn.pane.Markdown(get_most_popular_dosage_form(df2))
least_popular_dosage_form = pn.pane.Markdown(get_least_popular_dosage_form(df2))
supplier_list = pn.pane.DataFrame(get_supplier_list(df2), index=False, height=200)
most_popular_supplier = pn.pane.Markdown(get_most_popular_supplier(df2))
least_popular_supplier = pn.pane.Markdown(get_least_popular_supplier(df2))
best_discount = pn.pane.Markdown(get_best_discount(df2))
worst_discount = pn.pane.Markdown(get_worst_discount(df2))
yearly_sales = pn.pane.Matplotlib(get_yearly_sales(df2))
monthly_sales = pn.pane.Matplotlib(get_monthly_sales(df2))
most_expensive_drug = pn.pane.Markdown(get_most_expensive_drug(df2))
least_expensive_drug = pn.pane.Markdown(get_least_expensive_drug(df2))
most_expensive_transaction = pn.pane.DataFrame(get_most_expensive_transaction(df2))
least_expensive_transaction = pn.pane.DataFrame(get_least_expensive_transaction(df2))


def mask_df(event):
    # Masking df2 based on the value from branch_select Drop down
    mask = branch_select.value
    if mask == 'None':
        df2 = df.copy()
    else:
        branch_mask = df['Branch_Name'] ==  mask
        df2 = df[branch_mask]

    # Reassigning the objects of the Panel elements
    df2_pane.object = df2.head()
    branch_count.object = str(df2['Branch_Name'].nunique())
    best_branch_name.object = f'''Branch Name: {get_best_branch(df2, column='Branch_Name')}'''
    best_branch_id.object = f'''Branch ID: {get_best_branch(df2, column='Branch_ID')}'''
    worst_branch_name.object = f'''Branch Name: {get_worst_branch(df2, column='Branch_Name')}'''
    worst_branch_id.object = f'''Branch ID: {get_worst_branch(df2, column='Branch_ID')}'''
    performance_difference.object = get_branch_perf_diff(df2)
    performance_difference_percentage.object = get_branch_perf_diff_perc(df2)
    most_common_payment.object = get_most_common_payment(df2)
    rarest_payment.object = get_rarest_payment(df2)
    gender_proportion.object = get_gender_prop(df2)
    most_popular_generic_male.object = f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Male')}'''
    most_popular_brand_male.object = f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Male')}'''
    least_pop_generic_male.object = f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Male')}'''
    least_pop_brand_male.object = f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Male')}'''
    most_popular_generic_female.object = f'''Generic Product: {get_most_popular_product(df2, column='Generic_Name', gender='Female')}'''
    most_popular_brand_female.object = f'''Brand Product: {get_most_popular_product(df2, column='Brand_Name', gender='Female')}'''
    least_pop_generic_female.object = f'''Generic Product: {get_least_popular_product(df2, column='Generic_Name', gender='Female')}'''
    least_pop_brand_female.object = f'''Brand Product: {get_least_popular_product(df2, column='Brand_Name', gender='Female')}'''
    age_range.object = get_age_range(df2)
    most_popular_by_age_generic.object = get_most_popular_age(df2)
    least_popular_by_age_generic.object = get_least_popular_age(df2)
    most_popular_by_age_brand.object = get_most_popular_age(df2, column='Brand_Name')
    least_popular_by_age_brand.object = get_least_popular_age(df2, column='Brand_Name')
    best_drugs_generic.object = get_best_drugs(df2)
    worst_drugs_generic.object = get_worst_drugs(df2)
    best_drugs_brand.object = get_best_drugs(df2, column='Brand_Name')
    worst_drugs_brand.object = get_worst_drugs(df2, column='Brand_Name')
    rank_dosage_form.object = get_dosage_form_rank(df2)
    most_popular_dosage_form.object = get_most_popular_dosage_form(df2)
    least_popular_dosage_form.object = get_least_popular_dosage_form(df2)
    supplier_list.object = get_supplier_list(df2)
    most_popular_supplier.object = get_most_popular_supplier(df2)
    least_popular_supplier.object = get_least_popular_supplier(df2)
    best_discount.object = get_best_discount(df2)
    worst_discount.object = get_worst_discount(df2)
    yearly_sales.object = get_yearly_sales(df2)
    monthly_sales.object = get_monthly_sales(df2)
    most_expensive_drug.object = get_most_expensive_drug(df2)
    least_expensive_drug.object = get_least_expensive_drug(df2)
    most_expensive_transaction.object = get_most_expensive_transaction(df2)
    least_expensive_transaction.object = get_least_expensive_transaction(df2)

    
    # Put the elements into a Column Layout
    return  pn.Column(
        pn.pane.Markdown('## Select The Pharmacy Branch'),
        branch_select,
        pn.pane.Markdown('## Click to Reload the Page'),
        refresh_button,
        pn.pane.Markdown('## A Snapshot Of The Data'),
        df2_pane,
        pn.pane.Markdown('## Number of Pharmacy Branches'),
        branch_count,
        pn.pane.Markdown('## Best Pharmacy Branch By Sales'),
        best_branch_name,
        best_branch_id,
        pn.pane.Markdown('## Worst Pharmacy Branch By Sales'),
        worst_branch_name,
        worst_branch_id,
        pn.pane.Markdown('## Difference in Sales'),
        performance_difference,
        pn.pane.Markdown('## Difference in Sales (%)'),
        performance_difference_percentage,
        pn.pane.Markdown('## Most Used Mode of Payment'),
        most_common_payment,
        pn.pane.Markdown('## Least Used Mode of Payment'),
        rarest_payment,
        pn.pane.Markdown('## Proportion of Customer Gender'),
        gender_proportion,
        pn.pane.Markdown('## Most Popular Products Amongst Males'),
        most_popular_generic_male,
        most_popular_brand_male,
        pn.pane.Markdown('## Least Popular Products Amongst Males'),
        least_pop_generic_male,
        least_pop_brand_male,
        pn.pane.Markdown('## Most Popular Products Amongst Females'),
        most_popular_generic_female,
        most_popular_brand_female,
        pn.pane.Markdown('## Least Popular Products Amongst Females'),
        least_pop_generic_female,
        least_pop_brand_female,
        pn.pane.Markdown('## Age Range of Customers'),
        age_range,
        pn.pane.Markdown('## Most Popular Generic Product Per Age'),
        most_popular_by_age_generic,
        pn.pane.Markdown('## Least Popular Generic Product Per Age'),
        least_popular_by_age_generic,
        pn.pane.Markdown('## Most Popular Brand Product Per Age'),
        most_popular_by_age_brand,
        pn.pane.Markdown('## Least Popular Brand Product Per Age'),
        least_popular_by_age_brand,
        pn.pane.Markdown('## Best Generic Product In Total Sales'),
        best_drugs_generic,
        pn.pane.Markdown('## Worst Generic Product In Total Sales'),
        worst_drugs_generic,
        pn.pane.Markdown('## Best Brand Product In Total Sales'),
        best_drugs_brand,
        pn.pane.Markdown('## Worst Brand Product In Total Sales'),
        worst_drugs_brand,
        pn.pane.Markdown('## Ranking Of Dosage Forms By Popularity'),
        rank_dosage_form,
        pn.pane.Markdown('## Most Popular Dosage Form'),
        most_popular_dosage_form,
        pn.pane.Markdown('## Least Popular Dosage Form'),
        least_popular_dosage_form,
        pn.pane.Markdown('## List of Drug Wholesalers'),
        supplier_list,
        pn.pane.Markdown('## Wholesaler For Most Drugs'),
        most_popular_supplier,
        pn.pane.Markdown('## Wholesaler for Least Drugs'),
        least_popular_supplier,
        pn.pane.Markdown('## Best Discount Rate'),
        best_discount,
        pn.pane.Markdown('## Worst Discount Rate'),
        worst_discount,
        pn.pane.Markdown('## Yearly Total Sales'),
        yearly_sales,
        pn.pane.Markdown('## Monthly Total Sales'),
        monthly_sales,
        pn.pane.Markdown('## Most Expensive Drug'),
        most_expensive_drug,
        pn.pane.Markdown('## Least Expensive Drug'),
        least_expensive_drug,
        pn.pane.Markdown('## Most Expensive Transaction'),
        most_expensive_transaction,
        pn.pane.Markdown('## Least Expensive Transaction'),
        least_expensive_transaction,
        name='Dashboard'
    )

refresh_button.on_click(mask_df)

pn.template.FastListTemplate(
    main = [
        pn.Tabs(
            mask_df(refresh_button.clicks),
            pn.Column(
                '## This is the fourth app made in my series of deliverables. You can try it.',
                '## Contact me at:',
                '### Emails: owykenneth@gmail.com, drkennethowusuboakye@gmail.com',
                '### LinkedIn: https://www.linkedin.com/in/kenneth-owusu-boakye/',
                '### Phone Number: +233501326199',
                '### WhatsApp: +233501326199',
                name='About',
    )
        )],
    title = "Pharmacy Transactions Version 3"
).servable().show()


# In[ ]:




