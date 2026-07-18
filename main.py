import random
import flet as ft

def main(page: ft.Page):
    page.title = "Random Phrase Picker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Your aviation headings list extracted from the memory cards
    memos = [
    (
        "DC GEN 1+2 FAULT",
        "► PF: CAPT\n► DC GEN 1: RESET\n► DC GEN 2: RESET\n\n"
        "If one generator recovered:\n► DC GEN 1(2) FAULT procedure: APPLY\n\n"
        "If no generator recovered:\n► HYD GREEN PUMP: OFF\n► TRU: ON\n"
        "If no TRU arrow light -> MAX IMC FLIGHT TIME: 30 min / TRU OFF / LAND ASAP"
    ),
    (
        "SMOKE OR FUMES",
        "If smoke/fumes in the cockpit:\n► CREW OXY MASKS: DON\n"
        "► CREW OXY MASK MODE: 100% or EMERGENCY\n► GOGGLES: DON / ESTABLISH\n"
        "► CREW COMMUNICATIONS: ON\n► RECIRC FANS 1+2: OFF\n► AP: ON\n► LAND ASAP"
    ),
    (
        "EMERGENCY DESCENT",
        "► CREW OXY MASKS: AS RQRD\n► CREW COMMUNICATIONS: AS RQRD\n"
        "► GOGGLES: AS RQRD\n► DESCENT: INITIATE\n► PL 1+2: FI\n► CL 1+2: 100% OVRD"
    ),
    (
        "PED OVERHEATING",
        "► NOT AFFECTED SIDE: MOVE TO OBSERVER AREA\n\n"
        "If smoke or fumes:\n► CREW OXY MASKS: DON (100% or EMERGENCY)\n"
        "► GOGGLES: DON / ESTABLISH\n► CREW COMMUNICATIONS: ON\n► CABIN CREW: ADVISE FOR ACTION"
    ),
    (
        "PITCH CONTROL JAM AT TAKEOFF OR LANDING",
        "► MAX IAS: 180 kt\n► CONTROL COLUMNS: UNCOUPLE\n"
        "► FREE CONTROL COLUMN: PF IDENTIFY\n► FREE CONTROL COLUMN SIDE"
    ),
    (
        "ENG 1(2) FIRE AT TAKEOFF",
        "WHEN AIRBORNE:\n► LDG GEAR: UP\n\n"
        "AT ACCELERATION ALTITUDE:\n► PWR MGT: MCT\n\n"
        "AT VFTO:\n• If normal conditions -> FLAPS: 0\n"
        "• If icing conditions -> FLAPS: MAINTAIN 15°\n"
        "► PL (affected ENG): FI\n"
        "► CL (affected ENG): FTR THEN FUEL S.O.\n"
        "► FIRE HANDLE (affected ENG): PULL\n\n"
        "If fire persists after 10 s:\n► AGENT 1 (affected ENG): DISCH\n"
        "If fire persists 30 s after AGENT 1 DISCH:\n► AGENT 2 (affected ENG): DISCH\n\n"
        "Note: Captain may decide to shut down affected engine before reaching acceleration altitude, but not before 400 ft AGL."
    ),
    (
        "ENG 1(2) FIRE OR SEVERE MECHANICAL DAMAGE IN FLIGHT",
        "► PL (affected ENG): FI\n► CL (affected ENG): FTR THEN FUEL S.O.\n"
        "► FIRE HANDLE (affected ENG): PULL\n\n"
        "If fire persists after 10 s:\n► AGENT 1 (affected ENG): DISCH\n"
        "If fire persists 30 s after AGENT 1 DISCH:\n► AGENT 2 (affected ENG): DISCH"
    ),
    (
        "ENG 1+2 FLAME OUT",
        "► PF: CAPT\n► PL 1+2: FI\n\n"
        "If NH drops below 30%:\n► CL 1+2: FTR THEN FUEL S.O.\n"
        "► OPTIMUM SPEED: VmHB"
    ),
    (
        "ENG 1(2) FIRE OR SEVERE MECHANICAL DAMAGE ON GROUND",
        "► AIRCRAFT: STOP\n► BRAKE HANDLE: PARKING\n"
        "► CL 1+2: FTR THEN FUEL S.O.\n► FIRE HANDLE (affected ENG): PULL\n\n"
        "If fire persists:\n► AGENT 1 (affected ENG): DISCH\n"
        "If fire persists 30 s after AGENT 1 DISCH:\n► AGENT 2 (affected ENG): DISCH"
    ),
    (
        "ENG 1(2) FLAME OUT AT TAKEOFF",
        "► AUTOFEATHER: CHECK\n► UPTRIM: CHECK\n"
        "If no UPTRIM -> PL 1+2: ADVANCE TO THE RAMP\n"
        "• WHEN AIRBORNE -> LDG GEAR: UP\n"
        "If NO BLEEDS 1+2 FAULT -> BLEEDS 1+2: OFF\n\n"
        "AT ACCELERATION ALTITUDE:\n► ALT MODE: SET\n\n"
        "AT VFTO:\n► PL 1+2: IN THE NOTCH\n► PWR MGT: MCT\n"
        "• If normal conditions -> FLAPS: 0° / SPD TGT: CHECK VFTO\n"
        "• If icing conditions -> FLAPS: MAINTAIN 15° / SPD TGT: CHECK VFTO ICING FLAPS 15°\n"
        "► IAS MODE: SET\n► PL (affected eng): FI\n► CL (affected eng): FTR THEN FUEL S.O."
    ),
    (
        "SEVERE ICING",
        "► IAS: ICING BUG + 30 kt (or ICING BUG IF FLAPS 15 EXTENDED)\n"
        "► PWR MGT: MCT\n► PL 1+2: ADJUST\n► CL 1+2: 100% OVRD"
    ),
    (
        "STALL",
        "► CONTROL COLUMN: PUSH\n► ENG PWR: INCREASE\n"
        "If FLAPS 0 -> FLAPS: EXTEND TO 15\n► BANK: WINGS LEVEL"
    ),
    (
        "RNP LNAV GUIDANCE DISAGREE",
        "BOTH LATERAL DEVIATIONS\nDuring approach:\n► GO-AROUND: PERFORM\n► COMPARE"
    ),
    (
        "UNRELIABLE AIRSPEED INDICATION",
        "► AP/YD: OFF\n► FD: STBY\n► PITCH: MAINTAIN\n► TQ: MAINTAIN\n\n"
        "If at takeoff or GA below 1,500 ft:\n► PITCH: 8° IMMEDIATELY\n"
        "► ICING CONDITIONS / VOLCANIC ASHES CONDITIONS: ESCAPE\n\n"
        "CAUTION: Unreliable airspeed indication procedure has to be applied only when the three airspeed sources (both ADC and IESI) indications differ."
    ),
    (
        "FLAPS UNLK",
        "Before V1:\n► TAKEOFF: ABORT\n\n"
        "After V1:\n► VR & V2 SPEED BUGS AUTOMATICALLY INCREASED\n"
        "Not less than Vmin OPS\n\n"
        "If FLAPS UNLK during approach:\n► GO-AROUND: PERFORM\n► VGA"
    ),
    (
        "PITCH DISCONNECT",
        "► FREE CONTROL COLUMN(S): PF IDENTIFY\n"
        "► FREE CONTROL COLUMN SIDE\n► MAX IAS: 180 kt"
    ),
    (
        "PEC 1(2) FAULT",
        "If in short final approach (below 400 ft RA):\n► GO-AROUND: PERFORM"
    ),
    (
        "ENG 1(2) FLAME OUT IN FLIGHT",
        "► PL (affected ENG): FI\n\n"
        "If NH drops below 30% (no immediate relight):\n"
        "► CL (affected ENG): FTR THEN FUEL S.O."
    ),
    (
        "LO PITCH IN FLIGHT",
        "► PL (affected ENG): FI\n► CL (affected ENG): FTR THEN FUEL S.O."
    ),
    (
        "ABNORMAL PARAMETERS DURING START",
        "If ITT tends to exceed 900°C, or no ITT, or no NH:\n"
        "► CL (affected ENG): FUEL S.O.\n"
        "► ENG START selector: OFF & START ABORT"
    )
]

    remaining_memos = memos.copy()
    
    # -------------------------------------------------------------
    # 1. START SCREEN (Moved to the top so everything else can see it)
    # -------------------------------------------------------------
    def go_to_start_screen():
        remaining_memos.clear()
        remaining_memos.extend(memos)
        page.clean()
        page.add(
            ft.Text("ATR-72 Memo Items", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("Press start to pick a random card", size=16, color=ft.Colors.GREY_400),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("START", size=16, weight=ft.FontWeight.BOLD),
                on_click=go_to_active_screen,
                width=200,
                height=50,
            )
        )
        page.update()

    def go_to_answer_screen(x):
        page.clean()
        page.add(
            ft.Text("Answer Screen", size=32, weight=ft.FontWeight.BOLD),
            ft.Text(x, size=16, color=ft.Colors.BLACK),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("Next Item", size=16, weight=ft.FontWeight.BOLD),
                # Using lambda here prevents the "undefined" error!
                on_click=lambda _: go_to_active_screen(None),
                width=200,
                height=50,
            ),
            ft.Button(
                content=ft.Text("Back to Start", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: go_to_start_screen(),
                width=200,
                height=50,
            )
        )
        page.update()

    # -------------------------------------------------------------
    # 2. COMPLETION SCREEN (Middle - sees start_screen, visible to active_screen)
    # -------------------------------------------------------------
    def go_to_completion_screen():
        page.clean()
        page.add(
            ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=64),
            ft.Container(height=10),
            ft.Text("Congratulations!", size=32, weight=ft.FontWeight.BOLD),
            ft.Text("You have successfully completed your training.", size=16, color=ft.Colors.GREY_400),
            ft.Text("All memory items reviewed.", size=14, italic=True),
            ft.Container(height=30),
            ft.Button(
                content=ft.Text("Restart Training", size=16, weight=ft.FontWeight.BOLD),
                on_click=lambda _: go_to_start_screen(),
                width=220,
                height=50,
            )
        )
        page.update()

    # -------------------------------------------------------------
    # 3. ACTIVE SCREEN (Bottom - sees both screens safely)
    # -------------------------------------------------------------
    def go_to_active_screen(e):
        page.clean()
        
        # Check if we run out of cards
        if not remaining_memos:
            go_to_completion_screen()
            return
            
        # Pick a random emergency heading
        chosen_tuple = random.choice(remaining_memos)
        remaining_memos.remove(chosen_tuple)
        chosen_memo = chosen_tuple[0]  # Extract the memo string from the tuple
        chosen_answer = chosen_tuple[1]  # Extract the answer string from the tuple
        
        cards_left = len(remaining_memos)
        
        page.add(
            ft.Text(f"Remaining items: {cards_left}/20", size=12, color=ft.Colors.GREY_500),
            ft.Container(height=10),
            ft.Text("Your Random Selection:", size=16, color=ft.Colors.BLUE),
            ft.Container(height=10),
            ft.Text(chosen_memo, size=24, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER),
            ft.Container(height=40),
            ft.Button(
                content=ft.Text("Show Answer"), 
                # This safely carries your chosen answer string over to the answer screen
                on_click=lambda _: go_to_answer_screen(chosen_answer), 
                width=150
            ),
            ft.Container(height=10),
            ft.Button(
                content=ft.Text("Back to Home", color=ft.Colors.BLUE),
                on_click=lambda _: go_to_start_screen(),
                style=ft.ButtonStyle(bgcolor=ft.Colors.TRANSPARENT)
            )
        )
        page.update()

    # Initialize the app on the start screen
    go_to_start_screen()

# Modern Flet entry point
ft.run(main)
