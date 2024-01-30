# Acquiring-and-processing-information-on-world-s-largest-banks


I am creating an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

Particulars of the code to be made have been shared below.
|                                         |                                                                                                                                 |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code name                               | banks_project.py                                                                                                                |
| Data URL                                | https://en.wikipedia.org/wiki/List_of_largest_banks                                 |
| Exchange rate CSV path                  | https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv |
| Table Attributes (upon Extraction only) | Name, MC_USD_Billion                                                                                                            |
| Table Attributes (final)                | Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion                                                            |
| Output CSV Path                         | ./Largest_banks_data.csv                                                                                                        |
| Database name                           | Banks.db                                                                                                                        |
| Table name                              | Largest_banks                                                                                                                   |


while bank_project_utils.py contains functions like: **extract , transform , load_to_csv , load_to_db , log_progress , run_query**  
and **Banks.db**  are the resulted Database
