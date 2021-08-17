aws lambda list-functions | jq -r '.Functions | .[] | .FunctionName' |
while read uname1; do
echo "Deleting $uname1";
aws lambda delete-function --function-name $uname1;
done