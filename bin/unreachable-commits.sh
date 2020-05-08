
# git fsck --unreachable 获取结果存储到commits.txt文件里

cat commits.txt | while read line
do
        echo ----------------------------------------
        commit=`echo ${line} | cut -d " " -f3`
        echo $commit
        git cat-file -p $commit
done

