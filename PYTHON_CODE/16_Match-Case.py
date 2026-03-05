country = "Poland"

match country:
    case "USA" | "United States":
        "US"
    case "Poland":
        print("PL")
    case "India":
        print("IN")
    case _:
        print("Unknown Country")
