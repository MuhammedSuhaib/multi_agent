Here I try to create the simplest agent for hands-on practice with the concepts.        
I do it in a modular form:      

1. The agent is in the `simple_agents` folder

        agents.py

2. The config required for the agent is in the `configs` folder

        config.py

3. The runner is in the main file

        main.py

Here I implement agent-level config, meaning configs are done in the Agent class so we can give agents different configs.   
I use `Runner.run`, which is async, so it requires extra code for `async/await` and `asyncio`.  

