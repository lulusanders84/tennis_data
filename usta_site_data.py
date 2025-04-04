data = {
    "player_search": {
        "url": lambda player_name: f"https://www.usta.com/en/home/play/player-search.html#searchText={player_name}&page=1",
        "input_id": "gridsearch-5689e82879-input",
        "submit_class": "v-grid-search__search-icon"
    },
    "wtn_search": {
        "url": lambda uaid: f"https://www.usta.com/en/home/play/player-search/profile.html#uaid={uaid}&tab=tournaments",
        "class_name": "v-form-wtn-widget__section"
    }
}