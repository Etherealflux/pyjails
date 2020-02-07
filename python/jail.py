LEVEL = """
                               _                _ 
                              | | _____   _____| |
                              | |/ _ \ \ / / _ \ |
                              | |  __/\ V /  __/ |
                              |_|\___| \_/ \___|_|
"""

LEVELS = [

r"""                                
                               _______ _ __ ___  
                              |_  / _ \ '__/ _ \ 
                               / /  __/ | | (_) |
                              /___\___|_|  \___/ 
""",
r"""                         
                                 ___  _ __   ___ 
                                / _ \| '_ \ / _ \
                               | (_) | | | |  __/
                                \___/|_| |_|\___|
""",
r"""
                               _                 
                              | |___      _____  
                              | __\ \ /\ / / _ \ 
                              | |_ \ V  V / (_) |
                               \__| \_/\_/ \___/ 
""",
r"""
                            _   _                   
                           | |_| |__  _ __ ___  ___ 
                           | __| '_ \| '__/ _ \/ _ \
                           | |_| | | | | |  __/  __/
                            \__|_| |_|_|  \___|\___|
""",
r"""
                               __                  
                              / _| ___  _   _ _ __ 
                             | |_ / _ \| | | | '__|
                             |  _| (_) | |_| | |   
                             |_|  \___/ \__,_|_|   
""",
r"""
                                 __ _           
                                / _(_)_   _____ 
                               | |_| \ \ / / _ \
                               |  _| |\ V /  __/
                               |_| |_| \_/ \___|
""",
r"""
                                       _      
                                   ___(_)_  __
                                  / __| \ \/ /
                                  \__ \ |>  < 
                                  |___/_/_/\_\
""",
r"""                 
                            ___  _____   _____ _ __  
                           / __|/ _ \ \ / / _ \ '_ \ 
                           \__ \  __/\ V /  __/ | | |
                           |___/\___| \_/ \___|_| |_|
""",
r"""
                                  _       _     _   
                              ___(_) __ _| |__ | |_ 
                             / _ \ |/ _` | '_ \| __|
                            |  __/ | (_| | | | | |_ 
                             \___|_|\__, |_| |_|\__|
                                    |___/           
"""
]

DOOM = r"""
                              _                       
                           __| | ___   ___  _ __ ___  
                          / _` |/ _ \ / _ \| '_ ` _ \ 
                         | (_| | (_) | (_) | | | | | |
                          \__,_|\___/ \___/|_| |_| |_|
"""
def intro(level):
    if level == 666:
        return LEVEL + "\n" + DOOM
    else:
        return LEVEL + "\n" + LEVELS[level]