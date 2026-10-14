from wfrp.data.careers.academics import ACADEMIC_CLASS
from wfrp.data.careers.burghers import BURGHERS_CLASS
from wfrp.data.careers.courtiers import COURTIERS_CLASS
from wfrp.data.careers.peasants import PEASANTS_CLASS
from wfrp.data.careers.rangers import RANGERS_CLASS
from wfrp.data.careers.riverfolk import RIVERFOLK_CLASS
from wfrp.data.careers.rogues import ROGUES_CLASS
from wfrp.data.careers.warriors import WARRIORS_CLASS

CAREER_DATA = (
    ACADEMIC_CLASS
    | BURGHERS_CLASS
    | COURTIERS_CLASS
    | PEASANTS_CLASS
    | RANGERS_CLASS
    | RIVERFOLK_CLASS
    | ROGUES_CLASS
    | WARRIORS_CLASS
)

CAREER_BY_CLASS = (
    {career: "Academics" for career in ACADEMIC_CLASS}
    | {career: "Burghers" for career in BURGHERS_CLASS}
    | {career: "Courtiers" for career in COURTIERS_CLASS}
    | {career: "Peasants" for career in PEASANTS_CLASS}
    | {career: "Rangers" for career in RANGERS_CLASS}
    | {career: "Riverfolk" for career in RIVERFOLK_CLASS}
    | {career: "Rogues" for career in ROGUES_CLASS}
    | {career: "Warriors" for career in WARRIORS_CLASS}
)
