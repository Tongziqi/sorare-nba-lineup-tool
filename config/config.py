# tournaments
# target 可以根据奖池目标进行设置，如果目标太高，会倾向于选表现更不稳定的球员
from types_ import Tournaments, CardRarity, NBAConference


common_champion: Tournaments = {
    "name": "common_champion",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": None,
    "allowedRarities": [CardRarity.common],
    "minRarity": None,
    "target": 265,
}

common_contender: Tournaments = {
    "name": "common_contender",
    "tenGameAverageTotalLimit": 110,
    "allowMVP": False,
    "allowedConference": None,
    "allowedRarities": [CardRarity.common],
    "minRarity": None,
    "target": 220,
}

common_western_conference: Tournaments = {
    "name": "common_western_conference",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": NBAConference.west,
    "allowedRarities": [CardRarity.common],
    "minRarity": None,
    "target": 260,
}

common_eastern_conference: Tournaments = {
    "name": "common_eastern_conference",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": NBAConference.east,
    "allowedRarities": [CardRarity.common],
    "minRarity": None,
    "target": 260,
}

common_underdog: Tournaments = {
    "name": "common_underdog",
    "tenGameAverageTotalLimit": 60,
    "allowMVP": False,
    "allowedConference": None,
    "allowedRarities": [CardRarity.common],
    "minRarity": None,
    "target": 100,
}

rare_champion: Tournaments = {
    "name": "rare_champion",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": None,
    "allowedRarities": [CardRarity.limited, CardRarity.rare],
    "minRarity": {
        "minCount": 3,
        "rarity": CardRarity.rare,
    },
    "target": 250,
}

rare_contender: Tournaments = {
    "name": "rare_contender",
    "tenGameAverageTotalLimit": 110,
    "allowMVP": False,
    "allowedConference": None,
    "allowedRarities": [CardRarity.limited, CardRarity.rare],
    "minRarity": {
        "minCount": 3,
        "rarity": CardRarity.rare,
    },
    "target": 185,
}

super_rare_contender: Tournaments = {
    "name": "super_rare_contender",
    "tenGameAverageTotalLimit": 110,
    "allowMVP": False,
    "allowedConference": None,
    "allowedRarities": [CardRarity.rare, CardRarity.super_rare],
    "minRarity": {
        "minCount": 3,
        "rarity": CardRarity.super_rare,
    },
    "target": 180,
}

super_rare_champion: Tournaments = {
    "name": "super_rare_champion",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": None,
    "allowedRarities": [CardRarity.rare, CardRarity.super_rare],
    "minRarity": {
        "minCount": 3,
        "rarity": CardRarity.super_rare,
    },
    "target": 255,
}

limited_champion: Tournaments = {
    "name": "limited_champion",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": None,
    "allowedRarities": [CardRarity.limited],
    "minRarity": {
        "minCount": 5,
        "rarity": CardRarity.limited,
    },
    "target": 230,
}

limited_contender: Tournaments = {
    "name": "limited_contender",
    "tenGameAverageTotalLimit": 110,
    "allowMVP": False,
    "allowedConference": None,
    "allowedRarities": [CardRarity.limited],
    "minRarity": {
        "minCount": 5,
        "rarity": CardRarity.limited,
    },
    "target": 170,
}

limited_western_conference: Tournaments = {
    "name": "limited_western_conference",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": NBAConference.west,
    "allowedRarities": [CardRarity.limited],
    "minRarity": {
        "minCount": 5,
        "rarity": CardRarity.limited,
    },
    "target": 200,
}

limited_eastern_conference: Tournaments = {
    "name": "limited_eastern_conference",
    "tenGameAverageTotalLimit": 120,
    "allowMVP": True,
    "allowedConference": NBAConference.east,
    "allowedRarities": [CardRarity.limited],
    "minRarity": {
        "minCount": 5,
        "rarity": CardRarity.limited,
    },
    "target": 200,
}


# 球员表现和评分差异服从正态分布，mu是该分布的均值，例如球员评分30，mu=0.1，则表现的期望均值是33
# 下面设置的mu加成（或削减）都是经验值，不保证100%准确，可以自己微调
compute_by_recent_n_weeks_games: int = 10  # 计算最近n周比赛的表现变化率
mu_of_game_decision: float = -0.1  # 伤病报告里面game_decision的可能会打也可能不打，表现变化率均值的加该负值
mu_of_max_rank_team_bonus_ratio: float = 0.2  # 如果对手是攻防最弱球队，表现变化率均值的最大加成，反之打强队削减
mu_of_home_bonus: float = 0.04  # 表现变化率均值的主场加成
mu_of_home_b2b: float = -0.01  # 主场打背靠背表现变化率均值的扣减
mu_of_away_b2b: float = -0.02  # 客场打背靠背表现变化率均值的扣减
mu_of_single_game_bonus: float = -0.2  # 只打单场表现变化率均值的扣减
mu_of_multiple_games_bonus: float = 0.15  # 打3场及以上的比赛的表现变化率均值的加成
suggestion_count: int = 10
probability_reach_target: float = 0.05  # 从有该概率达到目标分数的结果中排序

all_tournaments: list[Tournaments] = [
    common_champion,
    common_contender,
    # common_underdog,
    # common_western_conference,
    # common_eastern_conference,
    # super_rare_contender,
    # rare_contender,
    # limited_contender,
    # rare_champion,
    # super_rare_champion,
    # limited_champion,
    # limited_western_conference,
    # limited_eastern_conference,
]  # 更改联赛优先级，越前的会优先选卡
# TODO 添加无上限的联赛

blacklist_players: dict[str, list[str]] = {
    "common_champion": [],
    "common_contender": [],
    "common_underdog": [],
    "common_western_conference": [],
    "common_eastern_conference": [],
    "super_rare_contender": [
        # "dbb7d8a8-4a7d-4097-b8b7-77f4faed2350",  # Sam Hauser
        # "839244ed-a59c-4b46-b13b-b124b49a8038",  # Kevin Huerter
        # "aa34b029-d04c-43de-8b3f-9f5ea58814dd",  # Kevin Huerter
        # "9754710e-0cea-4372-8d41-743781ca3ffb",  # Kevin Huerter
        # "aa3a4968-2d2d-419b-8e5b-85f3fbaae634",  # Brandon Ingram
        # "a6cca7ff-4832-4a1e-887d-35216e2c310e",  # Paul Reed
    ],
    "rare_contender": [],
    "limited_contender": [],
    "super_rare_champion": [],
    "rare_champion": [],
    "limited_champion": [],
    "limited_western_conference": [],
    "limited_eastern_conference": [],
}  # 设置不会被选中的id，重复卡建议设置

suggest_players: dict[str, list[str]] = {
    "common_champion": [],
    "common_contender": [],
    "common_underdog": [],
    "common_western_conference": [],
    "common_eastern_conference": [],
    "super_rare_contender": [
        # "da82a46b-3265-4861-958f-5d13da220269",  # Bruce Brown
    ],
    "rare_contender": [],
    "limited_contender": [
        # "6cf4ed29-a5fc-4f4c-a935-79978daa5a16",  # Wendell Moore Jr.
    ],
    "super_rare_champion": [],
    "rare_champion": [],
    "limited_champion": [],
    "limited_western_conference": [],
    "limited_eastern_conference": [],
}  # 设置会被优先选中的id
