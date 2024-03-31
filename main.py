from Agent import Agent
import KimiToken as kt

# AI回复较慢
agent1 = Agent(token=kt.new_token('agent1.txt')[0])
agent2 = Agent(token=kt.new_token('agent2.txt')[0])
agent1_say = None
agent2_say = None

context1 = "我扮演一个蓝队安全专家，你扮演一个红队安全专家，现在我要和你讨论有关蓝队安全的问题，你将会解释你的回答，并且以反问的方式提出你将如何攻破我的系统，除此之外不用说任何的总结。"
context2 = "我扮演一个红队安全专家，你扮演一个蓝队安全专家，现在我要和你讨论有关红队安全的问题，你将会解释你的回答，并且以反问的方式提出你将如何防止我的进攻，除此之外不用说任何的总结。"

for i in range(5):
    if agent2_say is None:
        agent1_say = agent1.chat(context1 + "我有一部苹果手机。")
    else:
        agent1_say = agent1.chat(context1 + agent2_say)
    print('Agent1:', agent1_say)
    agent2_say = agent2.chat(context2 + agent1_say)
    print('Agent2:', agent2_say)