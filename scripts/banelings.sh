#pysc2_play --map Simple64
cd ~/github/dauntless/agents
python -m pysc2.bin.agent \
--map DefeatBanelings_updated \
--agent defeat_banelings_scripted_agent.Agent \
--agent_race T \
--max_agent_steps 100000 \
--step_mul 1 \
--save_replay true \
--norender




