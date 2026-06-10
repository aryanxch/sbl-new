"""Specification tables + image galleries per product."""

SPECS = {
    # ============================================================
    # INDUSTRIAL / MINING EXPLOSIVES
    # ============================================================
    'slurry-explosives': {
        'spec_table': {
            'caption': 'Slurry Cartridge Explosives — Shipping Class/Div: 1.1 D, UN No: 241. REE relative to ANFO at 0.85 g/cc; VOD shown is unconfined.',
            'headers': ['Product', 'PESO Brand ID', 'Diameter (mm)', 'Weight (g)', 'Cartridges / Box', 'Nominal Density (g/cc)', 'VOD (m/s)', 'Relative Weight Strength', 'Relative Bulk Strength'],
            'rows': [
                {'group': 'CAP SENSITIVE — Booster / Primer Charges'},
                ['NEO PRIME SPECIAL', '625', '83',  '1,000',  '25', '1.18 ± 0.05', '4,000 ± 400', '90%', '124%'],
                ['NEO PRIME SPECIAL', '625', '83',  '2,780',  '9',  '1.18 ± 0.05', '4,000 ± 400', '90%', '124%'],
                ['NEO PRIME SPECIAL', '625', '125', '6,250',  '4',  '1.18 ± 0.05', '4,000 ± 400', '90%', '124%'],
                ['NEO PRIME SPECIAL', '625', '200', '12,500', '2',  '1.18 ± 0.05', '4,000 ± 400', '90%', '124%'],
                ['NEO BLAST SPECIAL', '627', '83',  '2,780',  '9',  '1.15 ± 0.05', '3,800 ± 400', '88%', '120%'],
                ['NEO BLAST SPECIAL', '627', '125', '6,250',  '4',  '1.15 ± 0.05', '3,800 ± 400', '88%', '120%'],
                ['NEO BLAST SPECIAL', '627', '200', '12,500', '2',  '1.15 ± 0.05', '3,800 ± 400', '88%', '120%'],
                {'group': 'NON-CAP SENSITIVE — Column Charges'},
                ['NEO BASE — SPECIAL', '629', '83',  '2,780',  '9',  '1.18 ± 0.05', '4,000 ± 400', '75%', '105%'],
                ['NEO BASE — SPECIAL', '629', '125', '6,250',  '4',  '1.18 ± 0.05', '4,000 ± 400', '75%', '105%'],
                ['NEO BASE — SPECIAL', '629', '200', '12,500', '2',  '1.18 ± 0.05', '4,000 ± 400', '75%', '105%'],
                ['NEO COL (SPECIAL)',  '623', '83',  '2,780',  '9',  '1.15 ± 0.05', '3,800 ± 400', '73%', '100%'],
                ['NEO COL (SPECIAL)',  '623', '125', '6,250',  '4',  '1.15 ± 0.05', '3,800 ± 400', '73%', '100%'],
                ['NEO COL (SPECIAL)',  '623', '200', '12,500', '2',  '1.15 ± 0.05', '3,800 ± 400', '73%', '100%'],
            ],
        },
        'application_groups': {
            'title': 'How Slurry Explosives are used',
            'intro': 'Different sub-classes of slurry cartridge explosives serve different roles in a blast hole. Each sub-class below has its own application profile, initiation method and packaging.',
            'groups': [
                {
                    'label': 'CAP SENSITIVE',
                    'name': 'Booster / Primer Charges',
                    'products': 'NEO PRIME SPECIAL · NEO BLAST SPECIAL',
                    'application': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying, hill cutting — good fragmentation (Excellent Water Resistance). Can also be used for plaster shooting / secondary blasting.',
                    'how_to_use': 'Initiation with Detonator of No. 8 Strength and Detonating Cord. Air-gap sensitivity 2 centimetres.',
                    'packaging': 'Cartridges are packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes.',
                },
                {
                    'label': 'NON-CAP SENSITIVE',
                    'name': 'Column Charges',
                    'products': 'NEO BASE — SPECIAL · NEO COL (SPECIAL)',
                    'application': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying, hill cutting — used as a Column Charge with Excellent Water Resistance.',
                    'how_to_use': 'Non-Cap Sensitive / non-aluminized explosive — has to be used with a Cap-Sensitive explosive / Booster Charge. Air-gap sensitivity 2 centimetres minimum (unconfined).',
                    'packaging': 'Cartridges are packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes.',
                },
            ],
        },
        'gallery': [],
    },

    'emulsion-explosives': {
        'spec_table': {
            'caption': 'Emulsion Cartridge Explosives — Shipping Class/Div: 1.1 D, UN No: 241. REE relative to ANFO at 0.85 g/cc; VOD shown is unconfined.',
            'headers': ['Product', 'PESO Brand ID', 'Diameter (mm)', 'Weight (g)', 'Cartridges / Box', 'Nominal Density (g/cc)', 'VOD (m/s)', 'Relative Weight Strength', 'Relative Bulk Strength'],
            'rows': [
                {'group': 'CAP SENSITIVE — Large Diameter (Booster / Primer Charges)'},
                ['NEO PRIME', '620', '65',  '1,250',  '25', '1.20 ± 0.05', '4,200 ± 200', '118%', '164%'],
                ['NEO PRIME', '620', '83',  '1,000',  '25', '1.20 ± 0.05', '4,200 ± 200', '118%', '164%'],
                ['NEO PRIME', '620', '83',  '2,780',  '9',  '1.20 ± 0.05', '4,200 ± 200', '118%', '164%'],
                ['NEO PRIME', '620', '125', '6,250',  '4',  '1.20 ± 0.05', '4,200 ± 200', '118%', '164%'],
                ['NEO PRIME', '620', '200', '12,500', '2',  '1.20 ± 0.05', '4,200 ± 200', '118%', '164%'],
                ['NEO BLAST', '622', '83',  '2,780',  '9',  '1.20 ± 0.05', '4,200 ± 300', '120%', '169%'],
                ['NEO BLAST', '622', '125', '6,250',  '4',  '1.20 ± 0.05', '4,200 ± 300', '120%', '169%'],
                ['NEO BLAST', '622', '200', '12,500', '2',  '1.20 ± 0.05', '4,200 ± 300', '120%', '169%'],
                {'group': 'BOOSTER SENSITIVE — Large Diameter (Column Charges)'},
                ['NEO COLUMN', '621', '83',  '2,780',  '9',  '1.20 ± 0.05', '3,900 ± 300', '78%',  '110%'],
                ['NEO COLUMN', '621', '125', '6,250',  '4',  '1.20 ± 0.05', '3,900 ± 300', '78%',  '110%'],
                ['NEO COLUMN', '621', '200', '12,500', '2',  '1.20 ± 0.05', '3,900 ± 300', '78%',  '110%'],
                ['NEO BASE',   '628', '83',  '2,780',  '9',  '1.20 ± 0.05', '4,000 ± 300', '80%',  '115%'],
                ['NEO BASE',   '628', '125', '6,250',  '4',  '1.20 ± 0.05', '4,000 ± 300', '80%',  '115%'],
                ['NEO BASE',   '628', '200', '12,500', '2',  '1.20 ± 0.05', '4,000 ± 300', '80%',  '115%'],
                {'group': 'CAP SENSITIVE — Small Diameter Cartridge Explosives'},
                ['NEO GEL 90',  '918', '25',  '125',  '200', '1.20 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 90',  '918', '32',  '200',  '125', '1.20 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 90',  '918', '40',  '400',  '62',  '1.20 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 90',  '918', '50',  '625',  '50',  '1.20 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 901', '919', '25',  '125',  '200', '1.15 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 901', '919', '32',  '200',  '125', '1.15 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 901', '919', '40',  '400',  '62',  '1.15 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO GEL 901', '919', '50',  '625',  '50',  '1.15 ± 0.05', '4,400 ± 300', '119%', '165%'],
                ['NEO DYNE',    '922', '25',  '125',  '200', '1.15 ± 0.05', '4,300 ± 300', '110%', '155%'],
                ['NEO DYNE',    '922', '32',  '200',  '125', '1.15 ± 0.05', '4,300 ± 300', '110%', '155%'],
                ['NEO DYNE',    '922', '40',  '400',  '62',  '1.15 ± 0.05', '4,300 ± 300', '110%', '155%'],
                ['NEO DYNE',    '922', '50',  '625',  '50',  '1.15 ± 0.05', '4,300 ± 300', '110%', '155%'],
            ],
        },
        'application_groups': {
            'title': 'How Emulsion Explosives are used',
            'intro': 'SBL Energy\'s emulsion explosives are offered in three distinct sub-classes — each with its own application, initiation method and packaging profile.',
            'groups': [
                {
                    'label': 'CAP SENSITIVE — LARGE DIAMETER',
                    'name': 'Booster / Primer Charges',
                    'products': 'NEO PRIME · NEO BLAST',
                    'application': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying, hill cutting — good fragmentation (Excellent Water Resistance). Can also be used for plaster shooting / secondary blasting.',
                    'how_to_use': 'Initiation with Detonator of No. 8 Strength and Detonating Cord. Air-gap sensitivity 2 centimetres.',
                    'packaging': 'Cartridges are packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes.',
                },
                {
                    'label': 'BOOSTER SENSITIVE — LARGE DIAMETER',
                    'name': 'Column Charges',
                    'products': 'NEO COLUMN · NEO BASE',
                    'application': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying, hill cutting — used as a Column Charge (Excellent Water Resistance).',
                    'how_to_use': 'Non-Cap Sensitive / non-aluminized explosive — has to be used with a Cap-Sensitive explosive / Booster Charge. Air-gap sensitivity 2 centimetres minimum (unconfined).',
                    'packaging': 'Cartridges are packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes.',
                },
                {
                    'label': 'CAP SENSITIVE — SMALL DIAMETER',
                    'name': 'Underground Metal Mines &amp; Tunneling',
                    'products': 'NEO GEL 90 · NEO GEL 901 · NEO DYNE',
                    'application': 'For use in opencast as well as underground metal mines, quarrying, well-sinking, shaft-sinking and tunneling work (Excellent Water Resistance). Can also be used for plaster shooting / secondary blasting.',
                    'how_to_use': 'Products are High Strength, Non-Permitted Emulsion explosives. High density explosive — works well in watery conditions.',
                    'packaging': 'Cartridges are packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes.',
                },
            ],
        },
        'gallery': [],
    },

    'bulk-explosives': {
        'spec_table': {
            'caption': 'NEO BULK — Bulk Emulsion technical specifications',
            'headers': ['Property', 'Specification'],
            'rows': [
                ['Product Name', 'NEO BULK'],
                ['Category', 'Emulsion'],
                ['Viscosity', 'More than 40,000 cps (Brookfield)'],
                ['Sleeping Time', 'More than 10 days'],
                ['Sensitivity', 'Can be initiated by 0.2% of Cast Booster'],
                ['Water Resistance', 'Excellent'],
                ['Air Gap Sensitivity', 'As per specifications'],
                ['Application', 'Bulk Emulsion explosive sensitised by chemical gassing agents and stabilisers. NEO Bulk-901 is ideally suitable for Shovel as well as Dragline bench Blasting.'],
            ],
        },
        'gallery': [],
    },

    'low-column-charge': {
        'spec_table': {
            'caption': 'OPTIGEL — Non Cap Sensitive Class II Explosives. Shipping Class/Div: 1.1 D, UN No: 241. REE relative to ANFO at 0.85 g/cc; VOD shown is unconfined.',
            'headers': ['Product', 'PESO Brand ID', 'Diameter (mm)', 'Weight (g)', 'Cartridges / Box', 'Nominal Density (g/cc)', 'VOD (m/s)', 'Relative Weight Strength', 'Relative Bulk Strength'],
            'rows': [
                ['OPTIGEL', '1140', '83',  '2,080',  '2',  '0.86', '3,500 ± 500', '95%', '95%'],
                ['OPTIGEL', '1140', '125', '6,250',  '4',  '0.86', '3,500 ± 500', '95%', '95%'],
                ['OPTIGEL', '1140', '200', '12,500', '12', '0.86', '3,500 ± 500', '95%', '95%'],
            ],
        },
        'extra_sections': [
            {
                'tag': 'APPLICATION',
                'title': 'How OPTIGEL is used',
                'desc': 'Suitable for Deep / Long-hole Blasting in Opencast mines, quarrying and hill cutting — used as Column Charge in dry holes.',
                'items': [
                    'Non Cap Sensitive / non-aluminized explosive — has to be used with a Cap-Sensitive explosive / Booster Charge',
                    'Recommended for large-dia blast holes of 100 mm and above',
                    'Heave energy equivalent to ANFO with the benefits of an emulsion-based formulation',
                    'Cartridges packed in HDPE/LDPE film and further packed in 25 kg corrugated boxes',
                ],
            },
        ],
        'gallery': [],
    },

    'seismic-explosives': {
        'spec_table': {
            'caption': 'NEO GEL-90 CPT — Seismic Emulsion Explosive. Shipping Class/Div: 1.1 D, UN No: 241.',
            'headers': ['Product', 'PESO Brand ID', 'Diameter (mm)', 'Weight (g)', 'Cartridges / Box', 'Nominal Density (g/cc)', 'VOD (m/s)', 'Hydrostatic Head'],
            'rows': [
                ['NEO GEL - 90 CPT', '915', '50', '500',   '50', '1.20 ± 0.05', '5,000', '58'],
                ['NEO GEL - 90 CPT', '915', '50', '1,000', '25', '1.20 ± 0.05', '5,000', '58'],
                ['NEO GEL - 90 CPT', '915', '63', '500',   '50', '1.20 ± 0.05', '5,000', '58'],
                ['NEO GEL - 90 CPT', '915', '63', '1,000', '25', '1.20 ± 0.05', '5,000', '58'],
                ['NEO GEL - 90 CPT', '915', '76', '1,000', '25', '1.20 ± 0.05', '5,000', '58'],
                ['NEO GEL - 90 CPT', '915', '76', '2,500', '10', '1.20 ± 0.05', '5,000', '58'],
            ],
        },
        'extra_sections': [
            {
                'tag': 'APPLICATION',
                'title': 'How Seismic Explosives are used',
                'desc': 'Seismic explosive is used for seismic exploration. The product density is designed in a way that the cartridge sinks in water — ideal for sub-surface and water-filled borehole seismic surveys.',
                'items': [
                    'Initiation is done by No. 8 strength Seismic detonator',
                    'Sleeping time is approximately 8 weeks',
                    'Packed in couplable tube format for easy field deployment',
                    'Hydrostatic head of 58 metres — excellent water resistance',
                ],
            },
        ],
        'gallery': [],
    },

    # ============================================================
    # ACCESSORIES
    # ============================================================
    'ordinary-detonator': {
        'spec_table': {
            'caption': 'NEO OD — Packaging specification. 100 detonators packed in a cardboard box which is further packed in wooden cases containing 1,000 detonators.',
            'headers': ['Product', 'PESO Brand ID', 'Category', 'PESO Size Code', 'Detonators / Bunch (Inner Box)', 'Bunches / Inner Box', 'Total Detonators / Box'],
            'rows': [
                ['NEO OD', '1106', 'Ordinary Detonator', 'DFQ', '100', '100', '10,000'],
            ],
        },
        'extra_sections': [
            {
                'tag': 'PRODUCT DIMENSIONS',
                'title': 'Physical specifications',
                'desc': 'NEO OD is an Aluminium Plain Ordinary Detonator of No. 8 Strength, non-electric in nature, commonly used with Safety fuse.',
                'items': [
                    'Strength: No. 8',
                    'Length: 37 mm',
                    'Shell Diameter: 3.7 mm',
                    'Shell Material: Aluminium',
                    'Nature: Non-electric — initiated with Safety fuse',
                    'PESO Brand ID: 1106',
                ],
            },
        ],
        'gallery': [],
    },

    'electric-detonator': {
        'spec_table': {
            'caption': 'NEO ED (Instantaneous) and MSDD (Delay) Electric Detonators — packaging matrix. Aluminium shell, ASA primary + PETN secondary charge.',
            'headers': ['Product', 'PESO Brand ID', 'Category', 'PESO Size Code', 'Detonators / Bunch (Inner Box)', 'Bunches / Inner Box', 'Total Detonators / Box'],
            'rows': [
                ['NEO ED', '630', 'Instantaneous Electric Detonator', 'DBC', '25', '20', '500'],
                ['NEO ED', '630', 'Instantaneous Electric Detonator', 'DBF', '25', '30', '750'],
                ['NEO ED', '630', 'Instantaneous Electric Detonator', 'DBI', '25', '40', '1,000'],
                ['NEO ED', '630', 'Instantaneous Electric Detonator', 'DBL', '25', '60', '1,500'],
                ['MSDD',   '631', 'Delay Electric Detonator',         'DBC', '25', '20', '500'],
                ['MSDD',   '631', 'Delay Electric Detonator',         'DBF', '25', '30', '750'],
                ['MSDD',   '631', 'Delay Electric Detonator',         'DBI', '25', '40', '1,000'],
                ['MSDD',   '631', 'Delay Electric Detonator',         'DBL', '25', '60', '1,500'],
            ],
        },
        'gallery': [],
    },

    'non-electric-detonator': {
        'spec_table': {
            'caption': 'NEO DET / NEO DTS / NEO STL — Non-Electric Detonator packaging matrix',
            'headers': ['Product', 'PESO Brand ID', 'Category', 'PESO Size Code', 'Detonators / Bunch (Inner Box)', 'Bunches / Inner Box', 'Total Detonators / Box'],
            'rows': [
                {'group': 'NEO DET — Twin Det (DTHD + STLD)'},
                ['NEO DET', '632', 'Non Electric Detonator', 'DEF', '20', '20', '400'],
                ['NEO DET', '632', 'Non Electric Detonator', 'DFB', '05', '20', '100'],
                ['NEO DET', '632', 'Non Electric Detonator', 'DJD', '25', '60', '1,500'],
                {'group': 'NEO DTS — Down-the-Hole Delay Detonator'},
                ['NEO DTS', '635', 'Non Electric Detonator', 'DDG', '10', '16', '160'],
                ['NEO DTS', '635', 'Non Electric Detonator', 'DDI', '10', '20', '200'],
                ['NEO DTS', '635', 'Non Electric Detonator', 'DDL', '10', '25', '250'],
                ['NEO DTS', '635', 'Non Electric Detonator', 'DEV', '05', '10', '50'],
                ['NEO DTS', '635', 'Non Electric Detonator', 'DFB', '05', '20', '100'],
                ['NEO DTS', '635', 'Non Electric Detonator', 'DFE', '05', '24', '120'],
                {'group': 'NEO STL — Surface Trunk Line Delay Detonator'},
                ['NEO STL', '636', 'Non Electric Detonator', 'DDI', '10', '20', '200'],
                ['NEO STL', '636', 'Non Electric Detonator', 'DDL', '10', '25', '250'],
                ['NEO STL', '636', 'Non Electric Detonator', 'DDO', '10', '30', '300'],
                ['NEO STL', '636', 'Non Electric Detonator', 'DEF', '10', '20', '400'],
                ['NEO STL', '636', 'Non Electric Detonator', 'DFB', '05', '20', '100'],
            ],
        },
        'extra_sections': [
            {
                'tag': 'DELAY TIMINGS',
                'title': 'NEO DTS &amp; NEO STL delay periods',
                'desc': 'NEO DET provides unlimited delay periods and sequences to conduct large-scale blasts. The delay timings of NEO DET are combinations of the following:',
                'items': [
                    'NEO DTS (down-the-hole) delay times (ms): 125, 150, 175, 200, 225, 300, 350, 400, 450, 500',
                    'NEO STL (surface) delay times (ms): 0, 17, 25, 42, 65, 85, 100',
                    'Packing: NEO DET is first packed in a paper bag and the bags are then kept in a card-board box',
                    '25 to 200 nos. of NEO DET are packed into a box depending on the length of the shock tube',
                    'Available as per customer requirement — shock-tube lengths up to 50 metres',
                ],
            },
        ],
        'gallery': [],
    },

    'copper-delay-detonator': {
        'spec_table': {
            'caption': 'NEO CDD &amp; NEO CED — Copper Delay &amp; Instantaneous Detonator packaging matrix',
            'headers': ['Product', 'PESO Brand ID', 'Category', 'PESO Size Code', 'Detonators / Bunch (Inner Box)', 'Bunches / Inner Box', 'Total Detonators / Box'],
            'rows': [
                {'group': 'NEO CDD — Permitted Copper Delay Detonator'},
                ['NEO CDD', '634', 'Permitted Copper Delay Detonator',         'DBD', '25', '24', '600'],
                ['NEO CDD', '634', 'Permitted Copper Delay Detonator',         'DBF', '25', '30', '750'],
                {'group': 'NEO CED — Permitted Copper Instantaneous Detonator'},
                ['NEO CED', '633', 'Permitted Copper Instantaneous Detonator', 'DBF', '25', '30', '750'],
                ['NEO CED', '633', 'Permitted Copper Instantaneous Detonator', 'DBI', '25', '40', '1,000'],
                ['NEO CED', '633', 'Permitted Copper Instantaneous Detonator', 'DBL', '25', '60', '1,500'],
            ],
        },
        'gallery': [],
    },

    'electronic-detonator': {
        'spec_table': {
            'caption': 'NEO E-DET — Electronic Detonator Blasting System',
            'headers': ['Parameter', 'Specification'],
            'rows': [
                ['Product Name', 'NEO E-DET'],
                ['Communication', 'Fully testable 2-way digital'],
                ['Timing', 'Programmable, re-programmable, pre-programmable'],
                ['Traceability', 'Unique ID number per detonator'],
                ['Maximum Time Delay', '15,000 ms'],
                ['Minimum Increment', '1 ms'],
                ['Delay Accuracy', '0.1% ± 0.5 ms'],
                ['Operating Temperature', '−20 °C to +80 °C'],
                ['ESD Immunity', '30 kV &amp; 2500 PF'],
                ['Anti AC/DC', 'AC 220 V no damage, DC 48 V no damage'],
                ['ESD Resistance Standard', 'Compliant to EN 13763-13'],
                ['Maximum Modules (Master-Slave Mode)', '3,000+'],
                ['Shell Material', 'Copper'],
                ['Components', 'Capacitor + logic &amp; timing circuit + explosives'],
                ['Firing Equipment', 'Specialist proprietary firing system'],
            ],
        },
        'gallery': [],
    },

    'detonating-fuse': {
        'spec_table': {
            'caption': 'NEO CORD — Detonating Fuse range. Shipping Name: CORD DETONATING, FLEXIBLE. Class/Div: 1.1 D. UN No: 0065.',
            'headers': ['Product', 'PESO Brand ID', 'PETN (g/m)', 'DF / Spool (m)', 'Spools / Box', 'DF / Box (m)', 'Diameter (mm)', 'Tensile (Kgs)'],
            'rows': [
                ['NEO CORD',    '1031', '10', '250', '4', '1,000', '5.0 ± 0.1', '65'],
                ['NEO CORD',    '1031', '10', '375', '4', '1,500', '5.0 ± 0.1', '65'],
                ['NEO CORD 8',  '1153', '08', '375', '4', '1,500', '4.7 ± 0.1', '65'],
                ['NEO CORD 12', '1154', '12', '250', '4', '1,000', '5.2 ± 0.1', '70'],
                ['NEO CORD 12', '1154', '12', '375', '4', '1,500', '5.2 ± 0.1', '70'],
                ['NEO CORD 20', '1155', '20', '125', '4', '500',   '6.2 ± 0.1', '70'],
            ],
        },
        'extra_sections': [
            {
                'tag': 'APPLICATION',
                'title': 'How Detonating Fuse is used',
                'desc': 'The product is used for trunkline and downline for initiating explosive. Suitable for opencast mines, quarries, trenching and tunneling work.',
                'items': [
                    'Initiation by Number 6 Detonator',
                    'Provides a path for initiation of non-electric detonators',
                    'Different colour codings make field identification fast and unambiguous',
                ],
            },
        ],
        'gallery': [],
    },

    'cast-booster': {
        'spec_table': {
            'caption': 'NEO BOOST — Cast Booster product specifications',
            'headers': ['Product Name', 'NEO BOOST'],
            'rows': [
                ['Classification', 'Class - 3, Div. - 2'],
                ['Appearance', 'Yellowish Hard Solid Mass'],
                ['Density', '1.55 ± 0.05 gm/cc'],
                ['VOD', '6500 ± 500 m/sec'],
                ['Sensitivity', 'Cap Sensitive. Sensitive to No. 6 Detonator &amp; Detonating Fuse'],
                ['Water Resistance', 'Excellent'],
                ['Weight per Cartridge', '25 gm / 100 gm / 250 gm / 500 gm'],
                ['Package', '25 Kgs per box'],
                ['Shelf Life', 'More than 24 month'],
                ['Applications', 'Initiation of non-cap sensitive charges in a bore hole, at any fixed point in a column of explosives charge. Used with ANFO, cartridges and bulk explosives to prime the boreholes.'],
            ],
        },
        'gallery': [],
    },
}
