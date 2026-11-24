"""Records collected from the public DarGlobal and Wasalt websites (Nov 2026).

These are the fallback knowledge base: `scrape.py` refreshes / extends them
live when the sites are reachable, and merges by URL.
"""

DG = "https://darglobal.co.uk"
WS = "https://wasalt.sa/en"

DARGLOBAL = [
    dict(title="DarGlobal - company overview", type="company", city="Dubai", country="UAE",
         url=f"{DG}/partners/trump",
         text="DarGlobal (Dar Global PLC) is a London-listed luxury international real estate developer, "
              "the international arm of Saudi developer Dar Al Arkan. Founded 2017, listed on the Main Market of the "
              "London Stock Exchange on 28 February 2023. CEO: Ziad El Chaar. Projects in the UAE, Saudi Arabia, Oman, "
              "Qatar, Spain and the UK. Brand partners include the Trump Organization, Aston Martin, Automobili Lamborghini, "
              "Fendi Casa, ELIE SAAB, Marriott Residences, Missoni, Mouawad, Pagani Automobili and W Hotels. Sales offices in "
              "New York, London, Marbella, Athens, Dubai, Jeddah, Riyadh, Muscat and Doha. The projects page lists 38 projects."),
    dict(title="Trump International Hotel & Tower Dubai", type="project", city="Dubai", country="UAE", brand="Trump",
         status="Under construction, completion expected Q4 2031", property_types="Apartments, 1-4 bedrooms, penthouses",
         price="From about AED 3.4M-4M (launch, per brokers); 4-bed penthouses from AED 70M",
         url=f"{DG}/trump-international-hotel-and-tower-dubai",
         text="80-floor tower on Sheikh Zayed Road at the entrance of Downtown Dubai, developed with The Trump Organization. "
              "Residential floors 18-80, 1 to 4 bedroom apartments from about 1,173 sq ft. Introduced April 2025. Podium "
              "construction contract awarded to Gulf Asia Contracting. About 15 minutes to Dubai International Airport."),
    dict(title="D-Villas at Jumeirah Golf Estates", type="project", city="Dubai", country="UAE",
         property_types="Villas", url=f"{DG}/d-villas-at-jge",
         text="Villa community by DarGlobal at Jumeirah Golf Estates, Dubai."),
    dict(title="The Astera, Interiors by Aston Martin", type="project", city="Al Marjan Island, Ras Al Khaimah", country="UAE",
         brand="Aston Martin", status="Under development, handover December 2028",
         property_types="1-3 bedroom beach residences and 3-bedroom beach villas", size="61-265 sqm (FAQ)",
         price="Launch from about AED 1.8M-1.87M (brokers)", url=f"{DG}/the-astera",
         text="Beachfront residences on Al Marjan Island with interiors by Aston Martin's design team, direct beach access, "
              "about 5 minutes from the planned Wynn Resort and 60 minutes from Dubai International Airport. Amenities: infinity "
              "pool, spa, sauna, pool bar, fitness centre, indoor cinema, yoga lawn, multipurpose hall, kids' play area, 24/7 "
              "security. 10-year UAE Golden Visa for investments of AED 2M+. RERA registration and escrow."),
    dict(title="DG1", type="project", city="Business Bay, Dubai", country="UAE", status="Under development (delivery Q4 2026 per brokers)",
         property_types="Studios, 1, 2 and 3 bedrooms", size="452-2,476 sq ft", price="From about AED 1.46M-1.7M (brokers)",
         url=f"{DG}/dg1",
         text="DarGlobal's first self-branded tower on the Dubai Canal in Business Bay, designed by Gensler. City views, close "
              "to The Dubai Mall and Burj Khalifa. Amenities: gym, infinity pool, landscaped podium, 24-hour reception, sky "
              "garden, yoga studio."),
    dict(title="DaVinci Tower, Interiors by Pagani", type="project", city="Business Bay, Dubai", country="UAE", brand="Pagani",
         status="Completed", property_types="2, 3 and 4 bedroom residences", size="800-14,768 sq ft",
         price="Launch from about AED 5M (brokers)", url=f"{DG}/davinci-tower-by-pagani",
         text="Branded residential tower on the Dubai Canal near Marasi Business Bay; the first residences in the world by "
              "Pagani Automobili. 19 floors plus three basements. Interiors with premium leather, Italian marble, carbon "
              "fibre accents; smart home control, 24/7 concierge, rooftop pool, gym, sauna and steam rooms, private elevators. "
              "About 9 minutes to The Dubai Mall."),
    dict(title="Urban Oasis by Missoni", type="project", city="Business Bay, Dubai", country="UAE", brand="Missoni",
         status="Completed (Q3 2023), sold out", property_types="Studio to 4 bedrooms",
         url=f"{DG}/urban-oasis-by-missoni",
         text="Dubai Canal-front tower in Business Bay with Missoni interiors and a Miami-inspired lifestyle. Launched 2017 as "
              "'I Love Florence', rebranded June 2021. Gym, infinity pool, 24/7 concierge."),
    dict(title="W Residences Dubai - Downtown", type="project", city="Downtown Dubai", country="UAE", brand="W Hotels",
         status="Completed and sold out (resale only)", property_types="1, 2 and 3 bedroom apartments", size="701-7,627 sq ft",
         price="Launch from about AED 1.67M (brokers)", url=f"{DG}/w-residences",
         text="Branded tower with W Hotels (Marriott Bonvoy) by Business Bay. Burj Khalifa 5 min, Dubai Fountain 4 min, Dubai "
              "Mall 6 min. Amenities: infinity pool, clubhouse, fitness centre, private cinema, game room, co-working, guest "
              "suites, W Lounge."),
    dict(title="The Pagani Penthouse", type="project", city="Dubai", country="UAE", brand="Pagani",
         url=f"{DG}/one-of-one/project-pagani", text="Ultra-exclusive '1 of 1' collection penthouse by Pagani in Dubai."),
    dict(title="Top of the Astera", type="project", city="Al Marjan Island, Ras Al Khaimah", country="UAE",
         url=f"{DG}/one-of-one/top-of-the-astera", text="'1 of 1' collection penthouse at The Astera."),
    dict(title="Tierra Viva, Design inspired by Automobili Lamborghini", type="project", city="Benahavis, Costa del Sol", country="Spain",
         brand="Lamborghini", status="Under development, completion June 2028", property_types="Gated luxury villas",
         size="680-1,515 sqm", url=f"{DG}/tierra-viva",
         text="Limited collection of 53 hillside villas in Los Jaralillos, Benahavis, 15 minutes from Marbella, near Puerto "
              "Banus and Sotogrande. Private pool in each villa; select Painite villas have an in-villa car lift. Gated, 24/7 "
              "security, residents' clubhouse, sauna and steam room. Construction began December 2023."),
    dict(title="Painite Villas, Design inspired by Automobili Lamborghini", type="project", city="Benahavis", country="Spain",
         brand="Lamborghini", url=f"{DG}/one-of-one/painite-villas-design-inspired-by-Automobili-Lamborghini",
         text="'1 of 1' villas within Tierra Viva with in-villa car lift."),
    dict(title="Marea, Interiors by Missoni", type="project", city="Cortesin, Costa del Sol", country="Spain", brand="Missoni",
         url=f"{DG}/marea", text="Residential project in Cortesin on Spain's Costa del Sol with interiors by Missoni."),
    dict(title="Les Vagues by Elie Saab", type="project", city="Qetaifan Island North, Doha", country="Qatar", brand="ELIE SAAB",
         status="Under development, completion December 2027", property_types="1, 2 and 3 bedroom residences",
         size="84-383 sqm", url=f"{DG}/les-vagues",
         text="Seafront branded residences on Qetaifan Island North, a 1.3 million sqm man-made island: 7 km of beach, marina, "
              "18-hole golf course, Qatar's largest theme park nearby, 30 minutes from Hamad International Airport. Infinity "
              "pool, fitness centre, 24-hour reception, luxury retail, parking for all units."),
    dict(title="Trump International Simaisma", type="project", city="Simaisma", country="Qatar", brand="Trump",
         url=f"{DG}/lp/trump-international-qatar",
         text="Trump-branded development with Trump International Golf Club in Simaisma, Qatar."),
    dict(title="AIDA, Muscat", type="project", city="Muscat", country="Oman", brand="Trump, Marriott",
         property_types="Villas, apartments, hotel rooms and hotel residences", url=f"{DG}/landing-page/aida",
         text="Gated hilltop golfing community 130 m above sea level near Muscat, master planned by DarGlobal with OMRAN, about "
              "25 minutes from Muscat International Airport. 18-hole Trump championship golf course, Trump International Hotel, "
              "Trump club, Marriott Residences, AIDA Beach, residence club, trails. Villa collections: Trump Golf, Trump Cliff, "
              "Fairway, Azure Oceanfront (Fendi Casa), Coastal Investment, Sunrise Haven, Amour Sans Detour 1 and 2, The Great "
              "Escape. 100% freehold for all nationalities in designated zones; payment plans linked to construction milestones; "
              "short-term rental permitted on approved properties. Sales launched March 2023."),
    dict(title="Trump International Hotel, Oman", type="project", city="Muscat (AIDA)", country="Oman", brand="Trump",
         url=f"{DG}/aida-trump-international-hotel", text="USD 500 million luxury hotel at AIDA, launched June 2024."),
    dict(title="Trump Cliff Villas", type="project", city="Muscat (AIDA)", country="Oman", brand="Trump", property_types="Villas",
         url=f"{DG}/aida-trump-international-cliff-villas", text="Trump-branded cliff villas at AIDA."),
    dict(title="Trump Golf Villas", type="project", city="Muscat (AIDA)", country="Oman", brand="Trump", property_types="Villas",
         url=f"{DG}/aida-trump-villas", text="Trump-branded golf villas at AIDA."),
    dict(title="Fairway Villas", type="project", city="AIDA, Muscat", country="Oman", property_types="Villas",
         url=f"{DG}/fairway-villas-aida-oman", text="Fairway-facing villas at AIDA."),
    dict(title="Azure Oceanfront Villas, Interiors by Fendi Casa", type="project", city="AIDA, Muscat", country="Oman",
         brand="Fendi Casa", property_types="Villas", url=f"{DG}/one-of-one/fendi-casa-azure-oceanfront-villas",
         text="Oceanfront villas at AIDA with Fendi Casa interiors."),
    dict(title="Marriott Residences AIDA", type="project", city="AIDA, Muscat", country="Oman", brand="Marriott",
         url=f"{DG}/marriott-residences-aida-oman", text="Marriott-branded residences at AIDA."),
    dict(title="Other AIDA collections", type="project", city="AIDA, Muscat", country="Oman",
         url=f"{DG}/projects",
         text="Amour Sans Detour, Amour Sans Detour 2, The Great Escape, The Great Escape 2, Coastal Investment Villas, Sunrise "
              "Haven, and Nickelodeon Hotels & Resorts are further DarGlobal projects at AIDA, Muscat."),
    dict(title="The Mulliner, 149 Old Park Lane", type="project", city="London", country="UK", status="Completed and sold out",
         property_types="5-bedroom apartment", size="485.22 sqm", url=f"{DG}/the-mulliner",
         text="Mayfair residence in a century-old building with classical and Art Nouveau features. Concierge, 24-hour porterage, "
              "underfloor heating, Loxone, Lutron, Sonos, Gaggenau and Miele kitchen, 24-hour security."),
    dict(title="7&8 Albert Hall Mansions", type="project", city="London", country="UK",
         url=f"{DG}/one-of-one/THE-ALBERT-HALL-MANSION", text="'1 of 1' residence overlooking Hyde Park, London."),
    dict(title="Trump Tower Jeddah", type="project", city="Jeddah", country="Saudi Arabia", brand="Trump",
         status="Under development, completion December 2029", property_types="1-4 bedroom apartments, 3-4 bedroom penthouses",
         size="70-365 sqm", price="SAR 2 billion project (USD 531M); unit prices on request", url=f"{DG}/trump-tower-jeddah",
         text="47-floor seafront tower on the Jeddah Corniche with Red Sea views, near the marina, F1 street circuit and King Fahd "
              "Fountain. Hosts the Kingdom's first members-only Trump Club. Amenities: concierge, cigar lounge, fine dining, pool, "
              "kids' pool, jacuzzi, gym, yoga. Ground broken February 2025 (SIFCO enabling works); main contract to Arabian "
              "Construction Company."),
    dict(title="Trump Plaza Jeddah (Amaya)", type="project", city="Jeddah", country="Saudi Arabia", brand="Trump",
         url=f"{DG}/trump-plaza/park-residences",
         text="About USD 1bn mixed-use project in Amaya, Jeddah with Trump Park Residences and Trump Executive Residences, offices "
              "and a Central Park-inspired design on a 28,800 sqm plot."),
    dict(title="Amaya plots and Padel Living Residences", type="project", city="Jeddah", country="Saudi Arabia",
         property_types="Luxury plots, residences", url=f"{DG}/amaya/amaya-plots",
         text="Amaya in Jeddah offers luxury plots and the Padel Living Residences."),
    dict(title="Neptune, Interiors by Mouawad", type="project", city="Riyadh", country="Saudi Arabia", brand="Mouawad",
         status="Under development, completion December 2027", property_types="Five-bedroom villas", size="300-448 sqm",
         url=f"{DG}/neptune",
         text="Limited branded villa collection in northern Riyadh near the Expo 2030 site, interiors by Mouawad. Freehold for "
              "foreign investors; residency eligibility for investment of SAR 4M+."),
    dict(title="Trump Mansions and DarGlobal Mansions (Rayana, Wadi Safar)", type="project", city="Riyadh", country="Saudi Arabia",
         brand="Trump, Fendi Casa", url=f"{DG}/rayana/trump-mansions",
         text="Trump Mansions and DarGlobal Mansions with Fendi Casa interiors at Rayana in Wadi Safar, Riyadh, part of the Trump "
              "Organization collaboration in Riyadh launched December 2024."),
]

WASALT = [
    dict(title="Wasalt - platform overview", type="company", city="Riyadh", country="Saudi Arabia", url=f"{WS}",
         text="Wasalt is an AI-powered real estate platform in Saudi Arabia for verified (REGA) residential and commercial "
              "properties: buy, rent, projects, daily rentals and auctions. It is a joint venture between Dar Al Arkan and Quara "
              "Holding. About 17,900 properties for sale and 2,500 for rent listed. Property types: apartment, villa, land, floor, "
              "building, rest house, farm, palace, duplex, chalet, studio. Features AI price valuation, 5-year ROI predictions, "
              "mortgage calculator and 'Rent now, pay later' monthly instalments. Wasalt Business app serves brokers."),
    dict(title="Wasalt rental guide", type="guide", country="Saudi Arabia", url=f"{WS}/properties-for-rent-in-saudi-arabia",
         text="Expats with a valid Iqama can rent; leases are registered on the Ejar platform. Indicative annual rents: SAR "
              "25,000-40,000 for apartments in central Riyadh or Jeddah, SAR 70,000-200,000 for upscale villas. 1-bed suits "
              "professionals, 2-bed small families, 3-bed larger families; furnished, semi-furnished and unfurnished options. "
              "Popular cities: Riyadh, Jeddah, Dammam, Makkah, Madinah, Khobar, Al Qassim (cheapest)."),
    dict(title="Wasalt buying guide", type="guide", country="Saudi Arabia", url=f"{WS}/properties-for-sale-in-saudi-arabia",
         text="Riyadh, Jeddah, Dammam and Al Khobar are top cities for property investment due to economic growth, population "
              "increase and infrastructure. Wasalt Projects lets users reserve units in residential projects in Jeddah and Riyadh; "
              "Wasalt Masterplans covers land investment."),
    # rentals
    dict(type="listing", purpose="rent", title="Furnished Apartment with 2 Bedrooms", city="Riyadh", country="Saudi Arabia",
         price="SAR 100,000 / year", bedrooms=2, bathrooms=3, area="129 sqm", url=f"{WS}/property/rent/furnished-apartment-with-2-bedrooms-5809890",
         text="Furnished, built 2025, terrace, indoor and underground parking, fitted kitchen, split AC, elevator."),
    dict(type="listing", purpose="rent", title="Furnished Family Apartment, Al Rimal", city="Riyadh", district="Al Rimal",
         country="Saudi Arabia", price="SAR 96,000 / year", bedrooms=3, bathrooms=3, area="128.89 sqm",
         url=f"{WS}/property/rent/3-bedrooms-apartment-rent-249025",
         text="Built 2024, rooftop, storage, yard, walk-in closet, marble flooring, smart home, elevator, 1 parking."),
    dict(type="listing", purpose="rent", title="Semi-Furnished Family Apartment, Al-Malqa", city="Riyadh", district="Al-Malqa",
         country="Saudi Arabia", price="SAR 100,000 / year (about SAR 9,417/month via AQSAT)", bedrooms=3, area="206.41 sqm",
         url=f"{WS}/property/rent/3-bedrooms-apartment-rent-5832276",
         text="Ground floor, basement, underground parking, laundry room, 30 m street."),
    dict(type="listing", purpose="rent", title="Furnished Apartment 575 sqm with Studio, Namar", city="Riyadh", district="Namar",
         country="Saudi Arabia", price="SAR 66,000 / year", area="575 sqm",
         url=f"{WS}/property/rent/furnished-apartment-575-sqm-with-studio-229867",
         text="Built 2024, 2 guest rooms, two separate entrances, smart home, CCTV."),
    dict(type="listing", purpose="rent", title="Apartment 136 sqm with 3 Bedrooms, Al Arid", city="Riyadh", district="Al Arid",
         country="Saudi Arabia", price="SAR 60,000 / year", bedrooms=3, bathrooms=3, area="136 sqm",
         url=f"{WS}/property/undefined/apartment-136-sqm-with-3-bedrooms-5756520", text="Built 2025, basement, security system."),
    dict(type="listing", purpose="rent", title="Semi-Furnished Apartment 125 sqm with 3 Bedrooms", city="Riyadh", country="Saudi Arabia",
         price="SAR 90,000 / year", bedrooms=3, area="125 sqm",
         url=f"{WS}/property/rent/semi-furnished-apartment-125-sqm-with-3-bedrooms-225438",
         text="Built 2023, indoor pool, sauna, maid's room, smart home, CCTV."),
    dict(type="listing", purpose="rent", title="Elegant Apartment, Garden Residence, Hittin", city="Riyadh", district="Hittin",
         country="Saudi Arabia", price="SAR 95,000 / year", bedrooms=3, url=f"{WS}/property/rent/apartment-with-3-bedrooms-5758264",
         text="About 5 min to Riyadh Boulevard, 7 min to King Saud University, 10 min to Diriyah Gate, 15 min to KAFD."),
    dict(type="listing", purpose="rent", title="Un-Furnished Family Apartment, An-Narjis", city="Riyadh", district="An-Narjis",
         country="Saudi Arabia", bedrooms=3, area="138.76 sqm", url=f"{WS}/property/rent/3-bedrooms-apartment-rent-5812451",
         text="First floor, 30 m street."),
    dict(type="listing", purpose="rent", title="2 Bedroom Apartment 63.84 sqm", city="Riyadh", country="Saudi Arabia",
         price="SAR 58,000 / year", bedrooms=2, bathrooms=2, area="63.84 sqm",
         url=f"{WS}/property/rent/2-bedrooms-apartment-rent-5741010", text="Second floor, two streets, CCTV, 1 parking."),
    dict(type="listing", purpose="rent", title="Semi-Furnished Family Apartment 180 sqm, Al Arid", city="Riyadh", district="Al Arid",
         country="Saudi Arabia", price="SAR 85,000 / year", bedrooms=3, bathrooms=3, area="180 sqm",
         url=f"{WS}/property/rent/semi-furnished-apartment-180-sqm-with-3-bedrooms-183115",
         text="Built 2023, maid's room, smart home, elevator."),
    dict(type="listing", purpose="rent", title="Apartment for Rent, Jareer", city="Riyadh", district="Jareer", country="Saudi Arabia",
         price="SAR 20,000 / year", bathrooms=1, url=f"{WS}/property/rent/apartment-5831947", text="Under 1 year old, 3 streets."),
    dict(type="listing", purpose="rent", title="2 Bedroom Apartment, Al-Jarradiyah", city="Riyadh", district="Al-Jarradiyah",
         country="Saudi Arabia", price="SAR 25,000 / year", bedrooms=2, bathrooms=1, area="278.25 sqm",
         url=f"{WS}/property/rent/2-bedrooms-apartment-rent-5803669", text="Central Riyadh, third floor, built 2014."),
    dict(type="listing", purpose="rent", title="Un-Furnished Family Apartment with 4 Bedrooms, Qurtubah", city="Riyadh",
         district="Qurtubah", country="Saudi Arabia", price="SAR 65,000 / year", bedrooms=4,
         url=f"{WS}/property/rent/apartment-with-4-bedrooms-5745785", text="Fitted kitchen, split AC, elevator."),
    dict(type="listing", purpose="rent", title="Semi-Furnished Apartment 1017 sqm with 4 Bedrooms, Al Malqa", city="Riyadh",
         district="Al Malqa", country="Saudi Arabia", bedrooms=4, bathrooms=5, area="1017 sqm",
         url=f"{WS}/property/rent/semi-furnished-apartment-1017-sqm-with-4-bedrooms-226572", text="North Riyadh, floor 2."),
    # sales
    dict(type="listing", purpose="sale", title="Villa 150 sqm, Al Suwaidi", city="Riyadh", district="Al Suwaidi", country="Saudi Arabia",
         price="SAR 950,000", bedrooms=5, area="150 sqm", url=f"{WS}/property/Saudi Arabia/villa-150-sqm-facing-west-on-15m-width-street-5753989",
         text="West Riyadh, west facing, 15 m street. AI valuation range for similar listings SAR 677K-748K."),
    dict(type="listing", purpose="sale", title="Villa 307 sqm, Al Manarat", city="Jeddah", district="Al Manarat", country="Saudi Arabia",
         bedrooms=9, url=f"{WS}/property/Saudi Arabia/villa-307-sqm-facing-east-on-15m-width-street-5756534",
         text="North Jeddah, unfurnished, 9 bedrooms, 9+ bathrooms, east facing."),
    dict(type="listing", purpose="sale", title="Villa 435 sqm with 3 Apartments", city="Jeddah", district="As Salhiyah", country="Saudi Arabia",
         price="SAR 2,050,000 (SAR 4,713/sqm)", area="435 sqm", url=f"{WS}/property/sale/فيلا-435-متر-مربع-مع-3-شقق-واجهة-شمالية-5808910",
         text="New, north facing, 15 m street, 3 living rooms, 3 guest rooms."),
    dict(type="listing", purpose="sale", title="Villa 481 sqm, east facing on 20 m street", city="Jeddah", country="Saudi Arabia",
         price="SAR 2,600,000 (SAR 5,405/sqm)", bedrooms=8, bathrooms=6, area="481 sqm land, 550 sqm built",
         url=f"{WS}/property/sale/فيلا-481-متر-مربع-شرقية-على-شارع-20م-5859413",
         text="Built 2026, maid's room, rooftop, indoor parking, yard."),
    dict(type="listing", purpose="sale", title="Villa 345 sqm, east facing", city="Saudi Arabia", country="Saudi Arabia",
         price="SAR 3,500,000 (SAR 10,145/sqm)", bedrooms=6, area="345 sqm",
         url=f"{WS}/property/sale/villa-345-sqm-facing-east-on-15m-width-street-5804978",
         text="8 years old; AI valuation range SAR 2.5M-2.8M."),
    dict(type="listing", purpose="sale", title="Villa 450 sqm, west facing on 18 m street", city="Saudi Arabia", country="Saudi Arabia",
         price="SAR 700,000 (SAR 1,556/sqm)", area="450 sqm", url=f"{WS}/property/sale/villa-450-sqm-facing-west-on-18m-width-street-252445",
         text="Built 2025, garden, storage, laundry, security system, elevator."),
    dict(type="listing", purpose="sale", title="Villa 300 sqm, east facing on 15 m street", city="Saudi Arabia", country="Saudi Arabia",
         price="SAR 1,300,000 (SAR 4,333/sqm)", area="300 sqm", url=f"{WS}/property/sale/فيلا-300-متر-مربع-شرقية-على-شارع-15م-5859825",
         text="Built 2026, rooftop, two separate entrances, electric garage door, elevator."),
    dict(type="listing", purpose="sale", title="Villa 375 sqm with 3 Apartments, Al Bashaer", city="Jeddah", district="Al Bashaer",
         country="Saudi Arabia", area="375 sqm", url=f"{WS}/property/Saudi Arabia/villa-375-sqm-with-3-apartments-facing-north-232765",
         text="New, north facing, 20 m street."),
    dict(type="listing", purpose="sale", title="Apartment 126.2 sqm, Abruq Ar Rughamah", city="Jeddah", district="Abruq Ar Rughamah",
         country="Saudi Arabia", price="SAR 450,000", area="126.2 sqm", url=f"{WS}/apartments-for-sale-in-saudi-arabia?page=76",
         text="New, East Jeddah. Predicted 5-year ROI 25% (Wasalt AI)."),
    dict(type="listing", purpose="sale", title="Apartment 123.79 sqm, As Swaryee", city="Jeddah", district="As Swaryee",
         country="Saudi Arabia", price="SAR 570,000", area="123.79 sqm", url=f"{WS}/apartments-for-sale-in-saudi-arabia?page=76",
         text="1 year old, North Jeddah. Predicted 5-year ROI 26.3%."),
    dict(type="listing", purpose="sale", title="Apartment 98.86 sqm, Al Wahah", city="Jeddah", district="Al Wahah",
         country="Saudi Arabia", price="SAR 350,000", area="98.86 sqm", url=f"{WS}/apartments-for-sale-in-saudi-arabia?page=76",
         text="11 years old, East Jeddah. Predicted 5-year ROI 23.4%."),
    dict(type="listing", purpose="sale", title="Apartment 102.62 sqm, As Salamah", city="Jeddah", district="As Salamah",
         country="Saudi Arabia", price="SAR 520,000", area="102.62 sqm", url=f"{WS}/apartments-for-sale-in-saudi-arabia?page=76",
         text="New, North Jeddah. Predicted 5-year ROI 51.2%."),
    dict(type="listing", purpose="sale", title="Apartment with 3 Bedrooms, Az Zahra", city="Jeddah", district="Az Zahra",
         country="Saudi Arabia", price="SAR 650,000", bedrooms=3, url=f"{WS}/property/Saudi Arabia/apartment-with-3-bedrooms-5750023",
         text="North Jeddah, built 2025."),
    dict(type="listing", purpose="sale", title="Apartment with 3 Bedrooms, Al Wahah", city="Jeddah", district="Al Wahah",
         country="Saudi Arabia", price="SAR 339,000", bedrooms=3, url=f"{WS}/property/Saudi%20Arabia/apartment-with-3-bedrooms-5755396",
         text="East Jeddah, built 2025, est. repayment SAR 2,121/month."),
    dict(type="listing", purpose="sale", title="Apartment with 4 Bedrooms, As Saif", city="Dammam", district="As Saif",
         country="Saudi Arabia", price="SAR 780,000", bedrooms=4, bathrooms=4, area="200 sqm",
         url=f"{WS}/property/sale/apartment-with-4-bedrooms-5747728", text="Built 2025, maid's room, est. repayment SAR 4,881/month."),
    dict(type="listing", purpose="sale", title="Apartment 233.82 sqm with 8 Bedrooms, Al Qusur", city="Dammam", district="Al Qusur",
         country="Saudi Arabia", price="SAR 1,300,000", bedrooms=8, area="233.82 sqm",
         url=f"{WS}/property/sale/apartment-23382-sqm-with-8-bedrooms-251598", text="Built 2016."),
    dict(type="listing", purpose="sale", title="Apartment 216 sqm with 6 Bedrooms, Ash Shati Al Gharbi", city="Dammam",
         district="Ash Shati Al Gharbi", country="Saudi Arabia", bedrooms=6, bathrooms=4, area="216 sqm",
         url=f"{WS}/property/sale/apartment-216-sqm-with-6-bedrooms-231093", text="Unfurnished."),
    dict(type="listing", purpose="sale", title="Apartment 177 sqm, Al Khuzama", city="Al Khobar", district="Al Khuzama",
         country="Saudi Arabia", price="SAR 720,000", area="177 sqm", url=f"{WS}/apartments-for-sale-in-khobar?page=2",
         text="New. Predicted 5-year ROI 26.8%."),
    dict(type="listing", purpose="sale", title="Apartment, Al Hamra", city="Al Khobar", district="Al Hamra", country="Saudi Arabia",
         price="SAR 590,000", url=f"{WS}/apartments-for-sale-in-khobar?page=2", text="1 year old. Predicted 5-year ROI 16.5%."),
]

for r in DARGLOBAL:
    r["source"] = "DarGlobal"
for r in WASALT:
    r["source"] = "Wasalt"

SEED = DARGLOBAL + WASALT
