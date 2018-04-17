#pysc2_play --map Simple64
python -m pysc2.bin.agent \
--map Simple64 \
--agent refined_agent.SparseAgent \
--agent_race T \
--max_agent_steps 0 \
--norender



