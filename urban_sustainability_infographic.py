# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:50:08 2024

@author: Michael
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def extractUrbanPop_df(file_path):
    '''Function for reading, slicing and transposing specific \
        series code from the general dataframe'''
    # Read the CSV file into a DataFrame
    urban_pop = pd.read_csv(file_path)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name',
                       'Series Code'] + [str(year) for year in
                                         range(2000, 2020)]

    # Extract relevant columns
    urban_pop = urban_pop[urban_pop['Series Code']
                          == 'SP.URB.TOTL.IN.ZS'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    urban_pop = urban_pop[urban_pop['Country Code'].isin(countries)]

    # Select specific columns
    urban_pop = urban_pop.drop(
        ['Series Name', 'Series Code', 'Country Name'], axis=1)

    # Set 'Country Code' as the index
    urban_pop.set_index('Country Code', inplace=True)
    urban_pop = urban_pop.astype('float64')

    # Transpose the DataFrame
    urban_pop_T = urban_pop.transpose()

    return urban_pop, urban_pop_T


file_path = 'sdg df.csv'

# Call the function with the file path
urban_pop, urban_pop_T = extractUrbanPop_df(file_path)


def extractForestArea_df(file_path):
    '''Function for reading, slicing and transposing specific \
        series code from the general dataframe'''
    # Read the CSV file into a DataFrame
    forest_df = pd.read_csv(file_path)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name',
                       'Series Code'] + [str(year) for year in
                                         range(2000, 2021)]

    # Extract relevant columns
    forest_df = forest_df[forest_df['Series Code']
                          == 'AG.LND.FRST.ZS'][columns_extract]

    # Define countries to filter
    countries = ['CEB', 'EAS', 'ECS', 'LCN', 'MEA', 'NAC', 'SAS', 'SSF']

    # Filter rows based on countries
    forest_df = forest_df[forest_df['Country Code'].isin(countries)]

    # Select specific columns
    forest_df = forest_df.drop(
        ['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    forest_df.set_index('Country Name', inplace=True)
    forest_df = forest_df.astype('float64')

    # Transpose the DataFrame
    forest_df_T = forest_df.transpose()

    return forest_df, forest_df_T


file_path = 'sdg df.csv'

# Call the function with the file path
forest_df, forest_df_T = extractForestArea_df(file_path)


def extractRenewableCountries_df(file_path):
    '''Function for reading, slicing and transposing specific \
        series code from the general dataframe'''
    # Read the CSV file into a DataFrame
    renew_energy_city_df = pd.read_csv(file_path)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name',
                       'Series Code'] + [str(year) for year in
                                         range(2000, 2016)]

    # Extract relevant columns
    renew_energy_city_df =\
        renew_energy_city_df[renew_energy_city_df['Series Code']
                             == 'EG.ELC.RNEW.ZS'][columns_extract]

    # Define countries to filter
    countries = ['BRA', 'CAN', 'CHL', 'COL', 'FRA', 'DEU', 'MEX', 'USA', 'GBR']

    # Filter rows based on countries
    renew_energy_city_df =\
        renew_energy_city_df[renew_energy_city_df['Country Code'].isin(
            countries)]

    # Select specific columns
    renew_energy_city_df = renew_energy_city_df.drop(
        ['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    renew_energy_city_df.set_index('Country Name', inplace=True)
    renew_energy_city_df = renew_energy_city_df.astype('float64')

    # Transpose the DataFrame
    renew_energy_city_df_T = renew_energy_city_df.transpose()

    return renew_energy_city_df, renew_energy_city_df_T


file_path = 'sdg df.csv'

# Call the function with the file path
renew_energy_city_df, renew_energy_city_df_T = extractRenewableCountries_df(
    file_path)


def extractCo2Countries_df(file_path):
    '''Function for reading, slicing and transposing specific \
        series code from the general dataframe'''
    # Read the CSV file into a DataFrame
    co2_emission_df = pd.read_csv(file_path)

    # Define columns to extract
    columns_extract = ['Country Name', 'Country Code', 'Series Name',
                       'Series Code'] + [str(year) for year in
                                         range(2000, 2020)]

    # Extract relevant columns
    co2_emission_df = co2_emission_df[co2_emission_df['Series Code']
                                      == 'EN.ATM.CO2E.PC'][columns_extract]

    # Define countries to filter
    countries = ['BRA', 'CAN', 'CHL', 'COL', 'FRA', 'DEU', 'MEX', 'USA', 'GBR']

    # Filter rows based on countries
    co2_emission_df = co2_emission_df[co2_emission_df['Country Code'].isin(
        countries)]

    # Select specific columns
    co2_emission_df = co2_emission_df.drop(
        ['Series Name', 'Series Code', 'Country Code'], axis=1)

    # Set 'Country Name' as the index
    co2_emission_df.set_index('Country Name', inplace=True)
    co2_emission_df = co2_emission_df.astype('float64')

    # Transpose the DataFrame
    co2_emission_df_T = co2_emission_df.transpose()

    return co2_emission_df, co2_emission_df_T


file_path = 'sdg df.csv'

# Call the function with the file path
co2_emission_df, co2_emission_df_T = extractCo2Countries_df(file_path)



# Set the style for Seaborn Subplot
sns.set(style="whitegrid")

# Create a figure and gridspec
fig = plt.figure(figsize=(24, 22))
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1], height_ratios=[1.2, 1.2, 0.8])


# Plotting the bar chart with Seaborn - Urban Population Growth
ax0 = plt.subplot(gs[0, 0])
urban_pop_mean = urban_pop_T.mean()
sns.barplot(x=urban_pop.index, y=urban_pop_mean, palette='viridis', ax=ax0)
ax0.set(title='Urban Population Growth over 20 Years',
        xlabel='Regions', ylabel='Percentage of Urban Population')
ax0.grid(True)


# Plotting the line graph with Seaborn - CO2 Emission
ax1 = plt.subplot(gs[0, 1])
sns.lineplot(data=co2_emission_df_T, dashes=False, ax=ax1, linewidth=2.5)
ax1.set(title='CO2 Emission',
        ylabel='CO2 Emission(Metric Tons per Capita)')
ax1.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
ax1.grid(True)

# Plotting the bar chart with Seaborn - Forest Area Growth
ax2 = plt.subplot(gs[1, 0])
forestarea_mean = forest_df_T.mean()
sns.barplot(x=forestarea_mean, y=forest_df.index, palette='viridis', ax=ax2)
ax2.set(xlim=(0, 100), title='Forest Area Over 20 Years',
        xlabel='Percentage of Forest Area', ylabel='Regions')
ax2.grid(True)

# Plotting the line graph with Seaborn - Renewable Energy Output
ax3 = plt.subplot(gs[1, 1])
sns.lineplot(data=renew_energy_city_df_T, dashes=False, ax=ax3, linewidth=2.5)
ax3.set(title='Renewable Energy Output',
        ylabel='Renewable electricity output (% of total electricity output)')
ax3.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
ax3.grid(True)


fig.text(0.5, 0.92, 'Impact of Urban Population on Sustainable Development\
 Goals \n Michael Obiala \n Student ID: 22078603',
         fontsize=26, ha='center', va='center')

# Create a grid for the text at the bottom
ax_text = plt.subplot(gs[2, :])
ax_text.axis('off')  # Turn off the axis for the text grid


# Description text at the bottom
fig.text(0.05, 0.5, """This plot shows the impact of Urban growth on the \
sustainable development goals. As shown above Regions with high \
Urban population \n have maintained sustainablility regardless of high \
Urbanization. Top countries in the these regions with the highest \
Urbanization are \n focused in reducing CO2 emissions while maintaining a\
good forest area and that is supported by the focus on increasing renewable \
energy output. \n We can see that countries in Latin America and Carribean \
Regions have the high renewable energy output and even as Brazil and Colombia\
\n have been dropping we can relate that to the economic challenges these \
countries have been facing in the last decade. Viewing the top regions\n with \
high urban population, their forestry area hasn't reduced significantly after \
20 years and countries in these region maintain high renewable \n energy \
output as they gradually reduce their CO2 emissions.\n This shows that \
Highly urbanized regions are more likely to meet the UN Sustainable \
Development Goals.""",
         fontsize=20, ha='left', va='center', transform=ax_text.transAxes,
         linespacing=1.5)

# Show Infographic
plt.show()

