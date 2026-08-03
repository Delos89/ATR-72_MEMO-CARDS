import random
import flet as ft

def main(page: ft.Page):
    page.title = "ATR 72 Trainer - Limitations & Memos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # ==========================================
    # 1. MEMOS DATASET
    # ==========================================
    memos = [
        (
                "DC GEN 1+2 FAULT",
                "► PF: CAPT\n"
                "► DC GEN 1: RESET\n"
                "► DC GEN 2: RESET\n\n"
                "If one generator recovered:\n"
                "► DC GEN 1(2) FAULT procedure (A24.15): APPLY\n\n"
                "If no generator recovered:\n"
                "► HYD GREEN PUMP: OFF\n"
                "► TRU: ON\n\n"
                "If no TRU arrow light:\n"
                "► MAX IMC FLIGHT TIME: 30 min\n"
                "► TRU: OFF\n"
                "► LAND ASAP"
            ),
            (
                "SMOKE OR FUMES",
                "If smoke/fumes in the cockpit:\n"
                "► CREW OXY MASKS: DON\n"
                "► CREW OXY MASK MODE: 100% or EMERGENCY\n"
                "► GOGGLES: DON\n"
                "► CREW COMMUNICATIONS: ESTABLISH\n"
                "► RECIRC FANS 1+2: OFF\n"
                "► AP: ON\n"
                "► LAND ASAP"
            ),
            (
                "EMERGENCY DESCENT",
                "► CREW OXY MASKS: AS RQRD\n"
                "► CREW COMMUNICATIONS: AS RQRD\n"
                "► GOGGLES: AS RQRD\n"
                "► DESCENT: INITIATE\n"
                "► PL 1+2: FI\n"
                "► CL 1+2: 100% OVRD"
            ),
            (
                "PED OVERHEATING",
                "► PF : NOT AFFECTED SIDE\n"
                "► PM : MOVE TO OBSERVER AREA\n\n"
                "If smoke or fumes:\n"
                "► CREW OXY MASKS: DON\n"
                "► CREW OXY MASK MODE: 100% or EMERGENCY\n"
                "► GOGGLES: DON\n"
                "► CREW COMMUNICATIONS: ESTABLISH\n"
                "► AP : ON\n"
                "► CABIN CREW: ADVISE FOR ACTION"
            ),
            (
                "PITCH CONTROL JAM AT TAKEOFF OR LANDING",
                "► MAX IAS: 180 kt\n"
                "► CONTROL COLUMNS: UNCOUPLE\n"
                "► FREE CONTROL COLUMN: IDENTIFY\n"
                "► PF: FREE CONTROL COLUMN SIDE"
            ),
            (
                "ENG 1(2) FIRE AT TAKEOFF",
                "WHEN AIRBORNE:\n"
                "► LDG GEAR: UP\n\n"
                "AT ACCELERATION ALTITUDE:\n"
                "► PWR MGT: MCT\n\n"
                "AT VFTO:\n"
                "• If normal conditions -> FLAPS: 0°\n"
                "• If icing conditions -> FLAPS: MAINTAIN 15°\n"
                "► PL (affected ENG): FI\n"
                "► CL (affected ENG): FTR THEN FUEL S.O.\n"
                "► FIRE HANDLE (affected ENG): PULL\n"
                "If fire persists after 10 s:\n"
                "► AGENT 1 (affected ENG): DISCH\n\n"
                "If fire persists 30 s after AGENT 1 DISCH:\n"
                "► AGENT 2 (affected ENG): DISCH\n"
                "Note: Captain may decide to shut down affected engine before reaching acceleration altitude, but not before 400 ft AGL."
            ),
            (
                "ENG 1(2) FIRE OR SEVERE MECHANICAL DAMAGE IN FLIGHT",
                "► PL (affected ENG): FI\n"
                "► CL (affected ENG): FTR THEN FUEL S.O.\n"
                "► FIRE HANDLE (affected ENG): PULL\n\n"
                "If fire persists after 10 s:\n"
                "► AGENT 1 (affected ENG): DISCH\n\n"
                "If fire persists 30 s after AGENT 1 DISCH:\n"
                "► AGENT 2 (affected ENG): DISCH"
            ),
            (
                "ENG 1+2 FLAME OUT",
                "► PF: CAPT\n"
                "► PL 1+2: FI\n\n"
                "If NH drops below 30%:\n"
                "► CL 1+2: FTR THEN FUEL S.O.\n"
                "► OPTIMUM SPEED: VmHB"
            ),
            (
                "ENG 1(2) FIRE OR SEVERE MECHANICAL DAMAGE ON GROUND",
                "► AIRCRAFT: STOP\n"
                "► BRAKE HANDLE: PARKING\n"
                "► CL 1+2: FTR THEN FUEL S.O.\n"
                "► FIRE HANDLE (affected ENG): PULL\n\n"
                "If fire persists:\n"
                "► AGENT 1 (affected ENG): DISCH\n\n"
                "If fire persists 30 s after AGENT 1 DISCH:\n"
                "► AGENT 2 (affected ENG): DISCH"
            ),
            (
                "ENG 1(2) FLAME OUT AT TAKEOFF",
                "► AUTOFEATHER: CHECK\n"
                "► UPTRIM: CHECK\n"
                "If no UPTRIM:\n"
                "► PL 1+2: ADVANCE TO THE RAMP\n"
                "WHEN AIRBORNE:\n"
                "► LDG GEAR: UP\n"
                "If NO BLEEDS 1+2 FAULT:\n"
                "► BLEEDS 1+2: OFF\n"
                "AT ACCELERATION ALTITUDE:\n"
                "► ALT MODE: SET\n"
                "AT VFTO:\n"
                "► PL 1+2: IN THE NOTCH\n"
                "► PWR MGT: MCT\n"
                "• If normal conditions -> FLAPS: 0° \n SPD TGT: CHECK VFTO\n"
                "• If icing conditions -> FLAPS: MAINTAIN 15° \n SPD TGT: CHECK VFTO ICING FLAPS 15°\n"
                "► IAS MODE: SET\n"
                "► PL (affected eng): FI\n"
                "► CL (affected eng): FTR THEN FUEL S.O."
            ),
            (
                "SEVERE ICING",
                "► IAS: ICING BUG + 30 kt (or ICING BUG IF FLAPS 15 EXTENDED)\n"
                "► PWR MGT: MCT\n"
                "► PL 1+2: ADJUST\n"
                "► CL 1+2: 100% OVRD"
            ),
            (
                "STALL",
                "► CONTROL COLUMN: PUSH\n"
                "► ENG PWR: INCREASE\n"
                "If FLAPS 0:\n"
                "► FLAPS: EXTEND TO 15\n"
                "► BANK: WINGS LEVEL"
            ),
            (
                "RNP LNAV GUIDANCE DISAGREE",
                "► BOTH LATERAL DEVIATIONS: COMPARE\n"
                "During approach:\n"
                "► GO-AROUND: PERFORM"
            ),
            (
                "UNRELIABLE AIRSPEED INDICATION",
                "► AP/YD: OFF\n"
                "► FD: STBY\n"
                "► PITCH: MAINTAIN\n"
                "► TQ: MAINTAIN\n"
                "If at takeoff or GA below 1,500 ft:\n"
                "► PITCH: 8° IMMEDIATELY\n"
                "► ICING CONDITIONS: ESCAPE\n"
                "► VOLCANIC ASHES CONDITIONS: ESCAPE\n"
                "CAUTION: Unreliable airspeed indication procedure has to be applied only when the three airspeed sources (both ADC and IESI) indications differ."
            ),
            (
                "INCREASE SPEED",
                "► IAS: ICING BUG + 30 kt"
            ),
            (
                "FLAPS UNLK",
                "Before V1:\n"
                "► TAKEOFF: ABORT\n"
                "After V1:\n"
                "► VR & V2 SPEED BUGS AUTOMATICALLY INCREASED\n"
                "If FLAPS UNLK during approach:\n"
                "► GO-AROUND: PERFORM\n"
                "► VGA: NOT LESS THAN Vmin OPS"
            ),
            (
                "PITCH DISCONNECT",
                "► FREE CONTROL COLUMN(S): IDENTIFY\n"
                "► PF: FREE CONTROL COLUMN SIDE\n"
                "► MAX IAS: 180 kt"
            ),
            (
                "PEC 1(2) FAULT",
                "If in short final approach (below 400 ft RA):\n"
                "► GO-AROUND: PERFORM"
            ),
            (
                "ENG 1(2) FLAME OUT IN FLIGHT",
                "► PL (affected ENG): FI\n"
                "If NH drops below 30% (no immediate relight):\n"
                "► CL (affected ENG): FTR THEN FUEL S.O."
            ),
            (
                "LO PITCH IN FLIGHT",
                "► PL (affected ENG): FI\n"
                "► CL (affected ENG): FTR THEN FUEL S.O."
            ),
            (
                "ABNORMAL PARAMETERS DURING START",
                "If ITT tends to exceed 900°C, or no ITT, or no NH:\n"
                "► CL (affected ENG): FUEL S.O.\n"
                "► ENG START selector: OFF & START ABORT"
            )
    ]

    # ==========================================
    # 2. LIMITATIONS DATASET
    # ==========================================
    limitations = [
        ("OPERATING ALTITUDE", "25,000 ft"),
        ("Gear and flaps retracted","+2,5 g to -1.0 g"),
        ("Gear and/or flaps extended","+2.0 g to 0.0 g"),
        ("MAXIMUM NUMBER OF SEATS","74"),
        #RUNWAY
        ("Slope","± 2% \n Approval required for runaway slopes beyond ± 2%"),
        #ICING CONDITIONS
        ("Ground Icing Conditions","OAT ≤ 5°C, and water contaminants on ramp, taxiways or runways"),
        ("Atmospheric Icing Conditions","OAT ≤ 5°C in ground and for takeoff.\n TAT ≤ 7°C in flight.\n Visible moisture in any form."),
        ("All icing detection lights must :", "be operative before a night flight \n The ice detector must be operative"),
        #ELECTRICAL SYSTEMS
        ("DC GEN MAX LOAD + TIME LIMIT","400A...NONE\n 600A...2 MINUTES\n 800A...8 SECONDS"),
        ("INV MAX LOAD + TIME LIMIT","500VA...NONE\n 575VA...30 MINUTES\n 750VA...5 SECONDS"),
        ("ACW GEN MAX LOAD + TIME LIMIT","20 KVA...NONE\n 30 KVA...5 MINUTES\n 40 KVA...5 SECONDS"),
        ("TRU MAX LOAD + TIME LIMIT","60A...NONE\n 90A...5 MINUTES"),
        #AIRSPEEDS
        ("VMO (Maximum Operating Speed)", "250 kt"),
        ("MMO (Maximum Operating Mach)", "Mach 0.55"),
        ("VA (Maneuvering Speed)", "175 kt"),
        ("VRA (Rough Air Speed)", "180 kt"),
        ("VFE Flaps 15°", "185 kt"),
        ("VFE Flaps 30°", "150 kt"),
        ("VLE (Max Speed Gear Extended)", "185 kt"),
        ("VLO Extension", "170 kt"),
        ("VLO Retraction", "160 kt"),
        ("VMCL (Flaps 15° & 30°)", "98 kt"),
        ("VWO(wipers ops)","160kt"),
        ("VTS(tire speed)","165 kt GS"),
        ("Conservative flaps 0°","180 kt"),
        ("Conservative flaps 15°","150 kt"),
        ("Conservative flaps 30°","135 kt"),
        #WEIGHT
        ("Max Ramp Weight", "23,170 kg"),
        ("Max Takeoff Weight (MTOW)", "23,000 kg"),
        ("Max Landing Weight (MLW)", "22,350 kg"),
        ("Max Zero Fuel Weight (MZFW)", "21,000 kg"),
        ("Min Takeoff Weight", "13,500 kg"),
        ("Min. Flight weight","13,000 kg"),
        #WIND LIMITATION
        ("Tailwind Limit", "15 kt max"),
        ("Crosswind Takeoff", "35 kt"),
        ("Cross wind landing","35 kt(F30°)"),
        #SINGLE DC GEN OPERATION
        ("Single DC GEN Operation in flight if OAT exceeds ISA +25", "flight level must be limited to FL200"),
        #FLIGHT CONTROL
        ("Holding with any flaps extended","is prohibited in icing conditions(except for single engine operations)"),
        #AIR CONDITIONING
        ("Max Positive Δ Pressure", "+6.35 PSI"),
        ("Max Negative Δ Pressure", "-0.5 PSI"),
        ("Max Δ Pressure for Landing", "0.35 PSI"),
        ("Max Δ for OVDB Valve full open","1 PSI"),
        ("Maximum altitude with one (1) bleed off","20,000 ft(FL200)"),
        #AUTO FLIGHT
        ("AUTO FLIGHTMin Height for AP engagement after TO", "100 ft"),
        ("AUTO FLIGHT Except during takeoff or approach","1,000 ft"),
        ("AUTO FLIGHT VS or IAS mode during approach","160 ft"),
        ("AUTO FLIGHT V-FP APP mode(LNAV/VNAV approach)","160 ft"),
        ("AUTO FLIGHT L-GS APP mode (LPV approach)","160 ft"),
        ("AUTO FLIGHT CAT I APP mode", "160 ft"),
        #OVERTORQUE LIMIT
        ("Overtorque Range 0% - 106.3%","10 minutes \n Operation up to 106.3% torque is unlimited when NP is below 94%"),
        ("Overtorque Range 106.3% - 120%", "20 seconds"),
        #ITT LIMITATION ENGINE OPERATING
        ("ITT ENGINE OPERATING0-800°C","No Limit"),
        ("ITT ENGINE OPERATING 800-840°C","20 seconds"),
        ("ITT ENGINE OPERATING >840°C", "Report to maintenance"),
        #OVERTEMPERATURE LIMIT FOR STARTING
        ("ITT STARTING(0-800°C)","No Limit"),
        ("ITT STARTING(800-840°C)","20 seconds"),
        ("ITT Starting (840°C - 950°C)", "5 seconds"),
        ("ITT Starting (> 950°C)", "Report to maintenance"),
        #FUEL SYSTEM
        ("Refuelling Pressure","50 PSI(3.5 bar)"),
        ("Total Usable Fuel", "5,000 kg (2,500 kg each tank)"),
        ("Max Fuel Imbalance", "730 kg"),
        #ENGINE PARAMETERS
        ("PWR SETTING RTO, TIME + TQ + ITT","10 MINUTES...100%...800°C"),
        ("PWR SETTING TO, TIME + TQ + ITT","5 MINUTES...90%...REFER TO TABLE"),
        ("PWR SETTING MCT, TIME + TQ + ITT","No limit...90.9%...800°C"),
        ("PWR SETTING Hotel Mode, TIME + TQ + ITT","N/A...N/A...715°C"),
        #STARTER
        ("STARTER, MAXIMUM CUMULATIVE RUNNING TIME, TIME PERIOD BEFORE REUSE","Three successive starter uses, with a maximum cumulative starter running time of 1 min 30 s. Then, respect a 4 min period before using starter again"),
        #DOORS
        ("CARGO DOOR OPERATION", "Do not operate cargo door with lateral wind component of more than 45 kt"),
        #RESET POLICY
        ("For the following systems the flight crew should strictly follow the abnormal procedure and RESET only when it is called by the abnormal procedure:"," ECU/EEC \n PEC.\n CAB PRESS MODE SEL.\n BAT CHG (EMER & MAIN), in FLIGHT only. \n NOTE: In the case of EMER(MAIN) BAT CHG FAULT on ground, only one reset is permitted provided that TRU and both DC GEN are operative."),
        ("In case of BLEED LEAK,HYD OVHT or BUS FAULT alerts, do not reset the associated systems :","BLEED VALVE pb, associated HYD PUMP or GEN pb"),
        ("Circuit Breaker (C/B) Reset", "CAUTION: Circuit Breaker (C/B) must not be RESET by the flight crew unless otherwise specified in the operational documentation by ATR. \n NOTE: Flight crew may REENGAGE a tripped circuit breaker ONLY IF HE/SHE JUDGES IT IS NECESSARY FOR A SAFE CONTINUATION OF THE FLIGHT.\n In this case only ONE reengagement should be attempted.\n         WARNING \n DO NOT REENGAGE THE C/B OF THE FUEL PUMP(S).")
        ]

    active_deck = []
    total_cards = 0
    mode_title = ""

    # -------------------------------------------------------------
    # NAVIGATION HANDLERS
    # -------------------------------------------------------------
    def go_to_start_screen():
        page.clean()
        page.add(
            ft.Text("ATR-72 Flight Deck Trainer", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Select a category to start your randomized study session", size=16, color=ft.Colors.GREY_400),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("LIMITATIONS", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: start_deck(limitations, "ATR-72 Limitations"),
                width=240,
                height=50,
            ),
            ft.Container(height=10),
            ft.Button(
                content=ft.Text("MEMO ITEMS", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: start_deck(memos, "ATR-72 Memos"),
                width=240,
                height=50,
            )
        )
        page.update()

    def start_deck(selected_dataset, title_name):
        nonlocal active_deck, total_cards, mode_title
        active_deck = selected_dataset.copy()
        total_cards = len(active_deck)
        mode_title = title_name
        go_to_active_screen(None)

    def go_to_answer_screen(answer_text):
        page.clean()
        page.add(
            ft.Text(mode_title, size=20, color=ft.Colors.BLUE_200, weight=ft.FontWeight.BOLD),
            ft.Text("Answer / Action:", size=16, color=ft.Colors.GREY_400),
            ft.Container(height=10),
            ft.Text(answer_text, size=18, color=ft.Colors.WHITE, weight=ft.FontWeight.W_500),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("Next Item", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: go_to_active_screen(None),
                width=200,
                height=50,
            ),
            ft.Container(height=5),
            ft.Button(
                content=ft.Text("Back to Menu", size=14),
                on_click=lambda _: go_to_start_screen(),
                width=200,
                height=40,
            )
        )
        page.update()

    def go_to_completion_screen():
        page.clean()
        page.add(
            ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=64),
            ft.Container(height=10),
            ft.Text("Session Complete!", size=32, weight=ft.FontWeight.BOLD),
            ft.Text(f"You reviewed all {total_cards} cards in {mode_title}.", size=16, color=ft.Colors.GREY_400),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("Return to Menu", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: go_to_start_screen(),
                width=220,
                height=50,
            )
        )
        page.update()

    def go_to_active_screen(e):
        page.clean()
        
        if not active_deck:
            go_to_completion_screen()
            return
            
        chosen_tuple = random.choice(active_deck)
        active_deck.remove(chosen_tuple)
        chosen_memo = chosen_tuple[0]
        chosen_answer = chosen_tuple[1]
        
        cards_left = len(active_deck)
        
        page.add(
            ft.Text(f"Category: {mode_title}", size=14, color=ft.Colors.BLUE_400, weight=ft.FontWeight.BOLD),
            ft.Text(f"Remaining: {cards_left} / {total_cards}", size=12, color=ft.Colors.GREY_500),
            ft.Container(height=20),
            ft.Text(chosen_memo, size=22, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Container(height=40),
            ft.Button(
                content=ft.Text("Show Answer"), 
                on_click=lambda _: go_to_answer_screen(chosen_answer), 
                width=160,
                height=45
            ),
            ft.Container(height=10),
            ft.Button(
                content=ft.Text("Back to Menu"),
                on_click=lambda _: go_to_start_screen(),
                style=ft.ButtonStyle(color=ft.Colors.GREY_400)
            )
        )
        page.update()

    # Initialize at startup
    go_to_start_screen()

# Modern Flet entry point
ft.run(main)
