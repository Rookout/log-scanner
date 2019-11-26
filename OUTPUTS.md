<p align="center">
    <a href="https://www.rookout.com/" target="_blank">
        <img src="https://github.com/Rookout/docs/blob/master/website/static/img/logos/rookout_logo_horizontal.svg" alt="Rookout logo" width="460" height="100">
    </a>
</p>

<h1 align="center">Rookout Log Scanner</h1>
<p align="center">
    The Rookout Log Scanner project enables easy and straight-forward log lines scanning of Github public repositories.
</p>

## Metrics and Metadata

The following list will specify all metrics and metadata contained in the Rookout Log Scanner main output file - `outputs/output.csv` :

* ***Repository_URL*** - The original URL of the repository, as supplied in [inputs/repositories.txt file](https://github.com/Rookout/log-scanner/tree/master/inputs/repositories.txt).
* ***Project_Name*** - The name of the repository, extracted from the URL. htt<span>ps://github</span>.com/Rookout/**log-scanner**
* ***Creator*** - The creator of the repository, extracted from the URL. htt<span>ps://github</span>.com/**Rookout**/log-scanner
* ***Organization_or_User*** - The type of the repository creator, either **Organization** or private **User**
* ***Contributors_Count*** - The numeric amount of the repository's contributors.
* ***License_Type*** - Is the project either open-source licensed or closed-source.
* ***Main_Language*** - The main programming language used in the repository, as specified in Github.
* ***Used_Languages*** - A JSON structured string which holds every known programming language used in the repository, with its percentage from the total files.
* ***Total_Amount_of_Logs*** - A numeric value which represents the count of any log line of any kind which was found in the repository.
* ***No_Logger_Logs*** - A numeric value which represents the count of any log line which didn't include use of verbosity level. (That number is also included in Info_Verbosity_Level_Usage)
* ***Debug_Verbosity_Level_Usage*** - A numeric value that represents the count of any log line which used **Debug** verbosity level. Debug also includes: **trace**, **verbose**, **silly**, **fine/er/est**, **spam**.
* ***Info_Verbosity_Level_Usage*** - A numeric value that represents the count of any log line which used **Info** verbosity level. Info also includes: **notice**, **message**, **success**, **normal**, **medium**, as well as logs without any verbosity level.
* ***Warning_Verbosity_Level_Usage*** - A numeric value that represents the count of any log line which used **Warning** verbosity level. Debug also includes: **high**.
* ***Error_Verbosity_Level_Usage*** - A numeric value that represents the count of any log line which used **Error** verbosity level. Debug also includes: **exception**, **fail**, **monitorable**.
* ***Critical_Verbosity_LevelsUsage*** - A numeric value that represents the count of any log line which used **Critical** verbosity level. Debug also includes: **alert**, **emergency**, **fatal**, **severe**, **unexpected**.
* ***Amount_of_Files_Which_Contains_Logs*** - A numeric value that represents the amount of files in the repository which are coded in one of the supported languages(*) and contains one or more log lines.
* ***Amount_of_Files_in_Supported_Languages*** - A numeric value that represents the amount of files in the repository which are coded in one of the supported languages(*).
* ***Files_with_Logs_Divided_by_Total_Files*** - The quotient of Amount_of_Files_Which_Contains_Logs divided by Amount_of_Files_in_Supported_Languages.
* ***Amount_of_Lines_in_Supported_Languages*** - A numeric value that represents the amount of lines in the repository which are coded in one of the supported languages(*).
* ***Total_Logs_Divided_by_Total_Lines*** - The quotient of Total_Amount_of_Logs divided by Amount_of_Lines_in_Supported_Languages.
* ***Forks*** - The amount of forks the repository has.
* ***Stars*** - The amount of stars the repository has.
* ***Watchers*** - The amount of watchers the repository has.

#### Notice
You can automatically quick analyse the output you received by running the following script:
```bash
python3 outputs/analysis/analysis.py
```
and view the results in a generated text file `output/analysis/analysis.txt`.  
This script requires [pandas](https://pandas.pydata.org/), so if you do not have it installed, before running the script you'll need to run:
```bash
pip install -r outputs/analysis/requirements.txt
```

## Histograms

The output file `outputs/logs_strings_line_histogram.csv` contains a histogram sorted in a descending order which holds the **most popular values of logs** in all of the supplied repositories together.
The output file `outputs/logs_strings_word_histogram.csv` contains a histogram sorted in a descending order which holds the **most popular words in values of logs** in all of the supplied repositories together.

The values of logs are defined as the actual data which was passed by the log lines and was written between quotation marks. Before entering the histogram, punctuation marks, numbers, single-character words, and words with above 15 characters were dropped from the data, and it was refactored to lowercase. In both histograms, values/words that had 5 appearances or less, didn't enter the final output.

## Logs Records

The output directory `outputs/all_logs_record` conatains text files, a file for each supplied repository (named with a repository's full name, with the slash changed to double hyphen `rookout--log-scanner`). Each file contains a record of all the log lines the scanner detected.

<p style="font-size:x-small;">(*) The supported languages are currently: Python, Java, JavaScripts, C#.</p>
