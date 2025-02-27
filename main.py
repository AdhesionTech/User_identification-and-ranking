
# 主函数代码

from messages_from_gmail_api import list_gmail_api_messages
# from LLM_summary import llm_summary
from LLM_summary import llm_summary
from LLM_user_identification import llm_user_id
from LLM_priority_rank import llm_rank


mail_id = "zhuth@g.ecc.u-tokyo.ac.jp"   # 要查询的邮件
# mail_id = "me"   # 要查询的邮件
query = ""   # 邮件筛选标准
count = 30  # 最大返回邮件数

messages = list_gmail_api_messages(mail_id, query, count)

user_identity = llm_user_id(mail_id)

original_message = messages[20]["body"]
print("The original email content is:")
print(original_message)
print("\n")

summary_message = llm_summary(original_message)
print("The summarized email content is:")
print(summary_message)

print("\n")

rank = llm_rank(original_message, user_identity)
print("The ranking of this email is: ")
print(rank)