import os
import subprocess
import pandas as pd


def to_percentage(num):
    num = num * 100
    num = "{0:.2f}%".format(num)
    return num


def two_decimals(num):
    num = float("{0:.2f}".format(num))
    return num


def different_verbosities(row):
    count_verbosities = 0
    if row["Debug_Verbosity_Level_Usage"] > 0:
        count_verbosities += 1
    if row["Info_Verbosity_Level_Usage"] > 0:
        count_verbosities += 1
    if row["Warning_Verbosity_Level_Usage"] > 0:
        count_verbosities += 1
    if row["Error_Verbosity_Level_Usage"] > 0:
        count_verbosities += 1
    if row["Critical_Verbosity_LevelsUsage"] > 0:
        count_verbosities += 1
    return count_verbosities


if __name__ == "__main__":
    # read the inputs
    df = pd.read_csv(os.path.join("outputs", "output.csv"))

    # set language and verbosity data structures
    langs = ["Python", "JavaScript", "C#", "Java"]
    avg_log_lines_per_repo = {}
    avg_all_logs_divided_by_all_lines = {}
    avg_files_with_logs_divided_by_all_files = {}
    repos_with_50_use_of_no_verbosity = {}
    repos_with_no_debug_logs = {}
    use_of_4_verbosity_levels = {}
    use_of_mostly_debug_logs = {}

    # collect language and verbosity metrics
    for lang in ["General"] + langs:
        if lang == "General":
            lang_df = df
        else:
            lang_df = df.loc[df["Main_Language"] == lang]
        avg_log_lines_per_repo[lang] = two_decimals(lang_df["Total_Amount_of_Logs"].mean())
        avg_all_logs_divided_by_all_lines[lang] = to_percentage(lang_df["Total_Logs_Divided_by_Total_Lines"].mean())
        avg_files_with_logs_divided_by_all_files[lang] = to_percentage(
            lang_df["Files_with_Logs_Divided_by_Total_Files"].mean())

        no_verbosity_counter = 0
        no_debug_counter = 0
        vast_use_of_verbosities_counter = 0
        mostly_debug_counter = 0
        for index, row in lang_df.iterrows():
            if row["Total_Amount_of_Logs"] > 0 and (row["No_Logger_Logs"] / row["Total_Amount_of_Logs"] > 0.5):
                no_verbosity_counter += 1
            if row["Total_Amount_of_Logs"] > 0 and row["Debug_Verbosity_Level_Usage"] == 0:
                no_debug_counter += 1
            if different_verbosities(row) >= 4:
                vast_use_of_verbosities_counter += 1
            if row["Total_Amount_of_Logs"] > 0 and row["Debug_Verbosity_Level_Usage"] / row[
                "Total_Amount_of_Logs"] > 0.8:
                mostly_debug_counter = mostly_debug_counter + 1
        if lang_df.shape[0] == 0:
            repos_with_50_use_of_no_verbosity[lang], repos_with_no_debug_logs[lang], use_of_4_verbosity_levels[lang], use_of_mostly_debug_logs[lang] = [0, 0, 0, 0]
        else:
            repos_with_50_use_of_no_verbosity[lang] = to_percentage(no_verbosity_counter / lang_df.shape[0])
            repos_with_no_debug_logs[lang] = to_percentage(no_debug_counter / lang_df.shape[0])
            use_of_4_verbosity_levels[lang] = to_percentage(vast_use_of_verbosities_counter / lang_df.shape[0])
            use_of_mostly_debug_logs[lang] = to_percentage(mostly_debug_counter / lang_df.shape[0])

    # set metadata data structures
    metadata_divisions = {
        "Contributors": [5, 75, 300],
        "Stars": [500, 1000, 10000],
        "Forks": [100, 400, 1000],
        "Watchers": [10, 100, 800]
    }
    metadata_to_print = {
        "Contributors": "contributors",
        "Stars": "stars",
        "Forks": "forks",
        "Watchers": "watchers"
    }
    metadata_holder = {
        "Contributors": {},
        "Stars": {},
        "Forks": {},
        "Watchers": {}
    }

    # collect metadata metrics
    for metadata in metadata_divisions.keys():
        metadata_df = df.loc[df[metadata] < metadata_divisions[metadata][0]]
        metadata_holder[metadata][f"under {metadata_divisions[metadata][0]}"] = to_percentage(
            metadata_df["Total_Logs_Divided_by_Total_Lines"].mean())
        metadata_df = df.loc[
            (df[metadata] >= metadata_divisions[metadata][0]) & (df[metadata] < metadata_divisions[metadata][1])]
        metadata_holder[metadata][
            f"{metadata_divisions[metadata][0]} to {metadata_divisions[metadata][1] - 1}"] = to_percentage(
            metadata_df["Total_Logs_Divided_by_Total_Lines"].mean())
        metadata_df = df.loc[
            (df[metadata] >= metadata_divisions[metadata][1]) & (df[metadata] < metadata_divisions[metadata][2])]
        metadata_holder[metadata][
            f"{metadata_divisions[metadata][1]} to {metadata_divisions[metadata][2] - 1}"] = to_percentage(
            metadata_df["Total_Logs_Divided_by_Total_Lines"].mean())
        metadata_df = df.loc[df[metadata] >= metadata_divisions[metadata][2]]
        metadata_holder[metadata][f"{metadata_divisions[metadata][2]} or above"] = to_percentage(
            metadata_df["Total_Logs_Divided_by_Total_Lines"].mean())

    # set type data structures
    creator_types = ["User", "Organization"]
    per_creator_type = {}
    license_types = ["open source", "closed source"]
    per_license_type = {}

    # collect metadata metrics
    for i in range(2):
        type_df = df.loc[df["Organization_or_User"] == creator_types[i]]
        per_creator_type[creator_types[i]] = to_percentage(type_df["Total_Logs_Divided_by_Total_Lines"].mean())
        type_df = df.loc[df["License_Type"] == license_types[i]]
        per_license_type[license_types[i]] = to_percentage(type_df["Total_Logs_Divided_by_Total_Lines"].mean())

    # set Corporates data structures
    corporates = {
        "Amazon": ["amazon", "amzn" "aws", "aws-amplify", "aws-cloudformation", "aws-quickstart", "aws-samples",
                   "awslabs"],
        "Google": ["google", "google-ar", "googleads", "googleanalytics", "googleapis", "googlearchive",
                   "GoogleChromeLabs", "GoogleCloudPlatform", "GoogleContainerTools", "googlemaps", "googleprojectzero",
                   "googlesamples", "googleevr"],
        "Microsoft": ["microsoft", "MicrosoftDocs", "MicrosoftTranslator"],
        "Apple": ["apple"],
        "Facebook": ["facebook", "facebookresearch", "facebookincubator"]
    }
    per_corporate = {}

    # collect corporates metrics
    for corporate in corporates.keys():
        corp_df = df.loc[df["Creator"].isin(corporates[corporate])]
        if corp_df.shape[0] > 0:
            log_lines_per_repo = two_decimals(corp_df["Total_Amount_of_Logs"].mean())
            all_logs_divided_by_all_lines = to_percentage(corp_df["Total_Logs_Divided_by_Total_Lines"].mean())
            files_with_logs_divided_by_all_files = to_percentage(
                corp_df["Files_with_Logs_Divided_by_Total_Files"].mean())
            per_corporate[corporate] = [log_lines_per_repo, all_logs_divided_by_all_lines,
                                        files_with_logs_divided_by_all_files]
        else:
            per_corporate[corporate] = [0, 0, 0]

    # write to file
    with open(os.path.join('outputs', 'analysis', 'analysis.txt'), 'w') as file_content:
        file_content.write("Total Log Lines:\n")
        for lang in ["General"] + langs:
            file_content.write(f"In {lang}:\n")
            file_content.write(
                f"{lang} average all logs divided by all code lines - {avg_all_logs_divided_by_all_lines[lang]}\n")
            file_content.write(
                f"{lang} average files with logs divided by the total amount of files - {avg_files_with_logs_divided_by_all_files[lang]}\n")
            file_content.write(
                f"{lang} average of log lines per repository (non-relative) - {avg_log_lines_per_repo[lang]}\n")
            file_content.write("\n")
        file_content.write("\n")

        file_content.write("Use of Verbosity Levels:\n")
        for lang in ["General"] + langs:
            file_content.write(f"In {lang}:\n")
            file_content.write(
                f"Repositories with 50% or above use of no verbosity level logs - {repos_with_50_use_of_no_verbosity[lang]}\n")
            file_content.write(
                f"Repositories without use of debug verbosity level - {repos_with_no_debug_logs[lang]}\n")
            file_content.write(
                f"Repositories that use 4 or more different verbosity levels - {use_of_4_verbosity_levels[lang]}\n")
            file_content.write(
                f"Repositories that above 80% of its logs has debug verbosity level - {use_of_mostly_debug_logs[lang]}\n")
            file_content.write("\n")
        file_content.write("\n")

        file_content.write("MetaData:\n")
        for metadata in metadata_holder.keys():
            file_content.write(f"{metadata}:\n")
            for level in metadata_holder[metadata]:
                file_content.write(
                    f"Average all logs divided by all code lines in repositories with {level} {metadata_to_print[metadata]} - {metadata_holder[metadata][level]}\n")
            file_content.write("\n")
        file_content.write("\n")

        file_content.write("Repository Type:\n")
        file_content.write("Creator Type:\n")
        for creator_type in creator_types:
            file_content.write(
                f"Average all logs divided by all code lines in repositories made by {creator_type} - {per_creator_type[creator_type]}\n")
        file_content.write("\n")
        file_content.write("License Type:\n")
        for license_type in license_types:
            file_content.write(
                f"Average all logs divided by all code lines in {license_type} repositories - {per_license_type[license_type]}\n")
        file_content.write("\n")

        file_content.write("Corporates:\n")
        for corporate in per_corporate.keys():
            file_content.write(f"{corporate}:\n")
            file_content.write(
                f"{corporate} average all logs divided by all code lines - {per_corporate[corporate][1]}\n")
            file_content.write(
                f"{corporate} average files with logs divided by the total amount of files - {per_corporate[corporate][2]}\n")
            file_content.write(f"{corporate} average of log lines per repository - {per_corporate[corporate][0]}\n")
            file_content.write("\n")

    print("done")
    try:
        subprocess.call(["open", os.path.join('outputs', 'analysis', 'analysis.txt')])
    except:
        quit()
