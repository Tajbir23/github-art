import os
import datetime

# লেখার জন্য প্যাটার্ন (Hire me!)
pattern = [
    "  H   H  III  RRRR   EEEEE     M   M  EEEEE  ! ",
    "  H   H   I   R   R  E         MM MM  E      ! ",
    "  HHHHH   I   RRRR   EEEE      M M M  EEEE   ! ",
    "  H   H   I   R  R   E         M   M  E      ! ",
    "  H   H  III  R   R  EEEEE     M   M  EEEEE  ! ",
]

# স্টার্টিং তারিখ (কবে থেকে শুরু হবে)
start_date = datetime.date(2024, 1, 1)  # এটি পরিবর্তন করতে পারেন

# গিট সেটআপ
os.system("git config --global user.name 'Tajbir23'")
os.system("git config --global user.email 'studenttajbirislam@gmail.com'")

# প্রতিটি লাইনের জন্য লুপ চালান
for row, line in enumerate(pattern):
    for col, char in enumerate(line):
        if char != " ":
            # নির্দিষ্ট দিনের জন্য কমিট তৈরি করা
            commit_date = start_date + datetime.timedelta(days=col + row * 7)
            for _ in range(10):  # গাঢ় কালার আনতে একাধিক কমিট
                os.system(f"echo '{commit_date}' >> commits.txt")
                os.system(f"git add commits.txt")
                os.system(f'GIT_COMMITTER_DATE="{commit_date} 12:00:00" git commit --date="{commit_date} 12:00:00" -m "Commit for {commit_date}"')

# পরিবর্তনগুলো পুশ করা
os.system("git push origin main")
