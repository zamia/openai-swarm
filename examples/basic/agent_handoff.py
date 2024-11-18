from swarm import Swarm, Agent
import litellm

client = Swarm(use_litellm=True)
litellm.modify_params = True

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
    model="claude-3-5-sonnet-20241022",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
    model="claude-3-5-sonnet-20241022",
)


def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent


english_agent.functions.append(transfer_to_spanish_agent)

messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = client.run(agent=english_agent, messages=messages)

print(response)
print(f"-----\n{response.messages[-1]['content']}\n-----")
# print(response.messages[-1]["content"])
