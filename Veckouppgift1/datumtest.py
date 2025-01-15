from datetime import datetime,timedelta

# Hämta dagens datum utan tid
idag = datetime.now().date() + timedelta(days=5)

print(f"Dagens datum utan tid: {idag}")