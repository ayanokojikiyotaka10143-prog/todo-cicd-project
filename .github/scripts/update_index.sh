#!/bin/bash
TODO_FILE=$1
TEST_FILE=$2
HTML_FILE="index.html"

TODO_TASKS=$(grep -A 100 "ToDo Tasks:" "$TODO_FILE" | sed -n '/ToDo Tasks:/,/Done Tasks:/p' | grep -v "Done Tasks:" | sed 's/^  //')
DONE_TASKS=$(grep -A 100 "Done Tasks:" "$TODO_FILE" | sed -n '/Done Tasks:/,$p' | sed 's/^  //')
TEST_RESULTS=$(cat "$TEST_FILE")

update_pre() {
    local id=$1
    local content=$2
    local file=$3
    perl -0777 -i -pe "s|(<pre id=\"$id\">)(.*?)(</pre>)|\$1\n$content\n\$3|s" "$file"
}

update_pre "todo" "$TODO_TASKS" "$HTML_FILE"
update_pre "done" "$DONE_TASKS" "$HTML_FILE"
update_pre "tests" "$TEST_RESULTS" "$HTML_FILE"
echo "index.html updated successfully"

git config user.email "${GITHUB_USER}@users.noreply.github.com"
git config user.name "${GITHUB_USER}"
git add "$HTML_FILE"
git commit -m "Update index.html with latest task data and test results" || echo "No changes to commit"
git push || echo "Push skipped"
