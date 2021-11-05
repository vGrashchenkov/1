from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class All_breeds(BaseModel):
    affenpinscher: List[Optional[str]]
    african: List[Optional[str]]
    airedale: List[Optional[str]]
    akita: List[Optional[str]]
    appenzeller: List[Optional[str]]
    australian: List[Optional[str]]
    basenji: List[Optional[str]]
    beagle: List[Optional[str]]
    bluetick: List[Optional[str]]
    borzoi: List[Optional[str]]
    bouvier: List[Optional[str]]
    boxer: List[Optional[str]]
    brabancon: List[Optional[str]]
    briard: List[Optional[str]]
    buhund: List[str]
    bulldog: List[str]
    bullterrier: List[str]
    cattledog: List[str]
    chihuahua: List[Optional[str]]
    chow: List[Optional[str]]
    clumber: List[Optional[str]]
    cockapoo: List[Optional[str]]
    collie: List[str]
    coonhound: List[Optional[str]]
    corgi: List[str]
    cotondetulear: List[Optional[str]]
    dachshund: List[Optional[str]]
    dalmatian: List[Optional[str]]
    dane: List[str]
    deerhound: List[str]
    dhole: List[Optional[str]]
    dingo: List[Optional[str]]
    doberman: List[Optional[str]]
    elkhound: List[str]
    entlebucher: List[Optional[str]]
    eskimo: List[Optional[str]]
    finnish: List[str]
    frise: List[str]
    germanshepherd: List[Optional[str]]
    greyhound: List[str]
    groenendael: List[Optional[str]]
    havanese: List[Optional[str]]
    hound: List[str]
    husky: List[Optional[str]]
    keeshond: List[Optional[str]]
    kelpie: List[Optional[str]]
    komondor: List[Optional[str]]
    kuvasz: List[Optional[str]]
    labradoodle: List[Optional[str]]
    labrador: List[Optional[str]]
    leonberg: List[Optional[str]]
    lhasa: List[Optional[str]]
    malamute: List[Optional[str]]
    malinois: List[Optional[str]]
    maltese: List[Optional[str]]
    mastiff: List[str]
    mexicanhairless: List[Optional[str]]
    mix: List[Optional[str]]
    mountain: List[str]
    newfoundland: List[Optional[str]]
    otterhound: List[Optional[str]]
    ovcharka: List[str]
    papillon: List[Optional[str]]
    pekinese: List[Optional[str]]
    pembroke: List[Optional[str]]
    pinscher: List[str]
    pitbull: List[Optional[str]]
    pointer: List[str]
    pomeranian: List[Optional[str]]
    poodle: List[str]
    pug: List[Optional[str]]
    puggle: List[Optional[str]]
    pyrenees: List[Optional[str]]
    redbone: List[Optional[str]]
    retriever: List[str]
    ridgeback: List[str]
    rottweiler: List[Optional[str]]
    saluki: List[Optional[str]]
    samoyed: List[Optional[str]]
    schipperke: List[Optional[str]]
    schnauzer: List[str]
    setter: List[str]
    sheepdog: List[str]
    shiba: List[Optional[str]]
    shihtzu: List[Optional[str]]
    spaniel: List[str]
    springer: List[str]
    stbernard: List[Optional[str]]
    terrier: List[str]
    tervuren: List[Optional[str]]
    vizsla: List[Optional[str]]
    waterdog: List[str]
    weimaraner: List[Optional[str]]
    whippet: List[Optional[str]]
    wolfhound: List[str]


class Model_all_breeds(BaseModel):
    message: All_breeds
    status: str


class Model_breed_list(BaseModel):
    message: List[str]
    status: str


class Model_single_image(BaseModel):
    message: HttpUrl
    status: str


class Model_multiple_image(BaseModel):
    message: List[HttpUrl]
    status: str
