from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


POLYGON_INPUTS = {


    "c-E": [
        (103.8631892,1.2398037,0),
        (103.8922921,1.2498086,0),
        (103.866783,1.2874469,0),
        (103.8651347,1.2971969,0),
        (103.866044,1.2992778,0),
        (103.8695792,1.3025814,0),
        (103.8655235,1.3120205,0),
        (103.8756319,1.3200279,0),
        (103.8703692,1.3266562,0),
        (103.868335,1.328144,0),
        (103.8623396,1.3303719,0),
        (103.8624056,1.3292929,0),
        (103.8618726,1.3276919,0),
        (103.8606196,1.3259159,0),
        (103.8583366,1.3238389,0),
        (103.8564946,1.3216589,0),
        (103.8585286,1.3200269,0),
        (103.8581816,1.3196379,0),
        (103.8585776,1.3193139,0),
        (103.8580666,1.3185519,0),
        (103.8585946,1.3182239,0),
        (103.8575996,1.3168459,0),
        (103.8563476,1.3154529,0),
        (103.8544306,1.3136839,0),
        (103.8531356,1.3121079,0),
        (103.8526276,1.3108379,0),
        (103.8493136,1.3061859,0),
        (103.8507986,1.3049349,0),
        (103.8480886,1.3034859,0),
        (103.8460426,1.3048379,0),
        (103.8453276,1.3030589,0),
        (103.8437896,1.2997779,0),
        (103.8453046,1.2972709,0),
        (103.8436986,1.2930859,0),
        (103.8421156,1.2941139,0),
        (103.8410366,1.2924779,0),
        (103.840257,1.291692,0),
        (103.840602,1.290598,0),
        (103.842377,1.290667,0),
        (103.841096,1.288139,0),
        (103.840688,1.287624,0),
        (103.837813,1.28579,0),
        (103.8369008,1.2843098,0),
        (103.83601,1.28328,0),
        (103.831472,1.281414,0),
        (103.8297286,1.279912,0),
        (103.8283633,1.2781527,0),
        (103.827788,1.27767,0),
        (103.8269766,1.2773803,0),
        (103.8258179,1.2775323,0),
        (103.823436,1.278714,0),
        (103.82174,1.278884,0),
        (103.822221,1.277335,0),
        (103.8227695,1.2748749,0),
        (103.82293,1.272288,0),
        (103.822372,1.272246,0),
        (103.821835,1.271742,0),
        (103.823101,1.267828,0),
        (103.823205,1.265751,0),
        (103.823801,1.265844,0),
        (103.823833,1.261527,0),
        (103.832309,1.265496,0),
        (103.857436,1.253976,0),
        (103.8631892,1.2398037,0),
    ],

    "c-W": [
        (103.843508,1.2330761,0),
        (103.8631892,1.2398037,0),
        (103.857436,1.253976,0),
        (103.832309,1.265496,0),
        (103.823833,1.261527,0),
        (103.823801,1.265844,0),
        (103.823205,1.265751,0),
        (103.823101,1.267828,0),
        (103.821835,1.271742,0),
        (103.822372,1.272246,0),
        (103.82293,1.272288,0),
        (103.822814,1.274731,0),
        (103.822221,1.277335,0),
        (103.82174,1.278884,0),
        (103.823436,1.278714,0),
        (103.8258179,1.2775323,0),
        (103.8269766,1.2773803,0),
        (103.827788,1.27767,0),
        (103.8283633,1.2781527,0),
        (103.8297286,1.279912,0),
        (103.831472,1.281414,0),
        (103.83601,1.28328,0),
        (103.8369008,1.2843098,0),
        (103.837813,1.28579,0),
        (103.840688,1.287624,0),
        (103.841096,1.288139,0),
        (103.842377,1.290667,0),
        (103.840602,1.290598,0),
        (103.840257,1.291692,0),
        (103.841036,1.29248,0),
        (103.838874,1.293987,0),
        (103.837618,1.292105,0),
        (103.836942,1.293232,0),
        (103.835606,1.292963,0),
        (103.835638,1.292416,0),
        (103.835193,1.29254,0),
        (103.83368,1.292411,0),
        (103.832183,1.29217,0),
        (103.830923,1.2921,0),
        (103.828669,1.292699,0),
        (103.823924,1.291991,0),
        (103.8242,1.295029,0),
        (103.818616,1.295657,0),
        (103.822532,1.305686,0),
        (103.806097,1.313818,0),
        (103.805047,1.31146,0),
        (103.802947,1.312236,0),
        (103.7982665,1.305944,0),
        (103.7996503,1.3050179,0),
        (103.8007871,1.3015783,0),
        (103.8015158,1.2972733,0),
        (103.8053565,1.2923871,0),
        (103.8085749,1.2915338,0),
        (103.8048793,1.287084,0),
        (103.7999376,1.2890824,0),
        (103.7951247,1.2875841,0),
        (103.7924876,1.2850826,0),
        (103.7980688,1.2773037,0),
        (103.8015923,1.2758617,0),
        (103.8017728,1.2731492,0),
        (103.7985327,1.264654,0),
        (103.8122656,1.243888,0),
        (103.843508,1.2330761,0),
    ],

    "c-NE": [
        (103.8596304,1.3457445,0),
        (103.8604051,1.3436704,0),
        (103.8609276,1.3421359,0),
        (103.8621276,1.3375139,0),
        (103.8623396,1.3303719,0),
        (103.868335,1.328144,0),
        (103.868885,1.330474,0),
        (103.869958,1.330216,0),
        (103.870332,1.331674,0),
        (103.872855,1.332523,0),
        (103.87296,1.333371,0),
        (103.8751902,1.3419192,0),
        (103.8729265,1.341828,0),
        (103.8726475,1.344177,0),
        (103.8706735,1.3441556,0),
        (103.8657997,1.346394,0),
        (103.8596304,1.3457445,0),
    ],

    "c-N": [
        (103.802947,1.312236,0),
        (103.805047,1.31146,0),
        (103.806097,1.313818,0),
        (103.822532,1.305686,0),
        (103.818616,1.295657,0),
        (103.8242,1.295029,0),
        (103.823924,1.291991,0),
        (103.828669,1.292699,0),
        (103.830923,1.2921,0),
        (103.8317918,1.2921492,0),
        (103.83368,1.292411,0),
        (103.835193,1.29254,0),
        (103.835638,1.292416,0),
        (103.835606,1.292963,0),
        (103.836942,1.293232,0),
        (103.837618,1.292105,0),
        (103.838874,1.293987,0),
        (103.841036,1.29248,0),
        (103.8421156,1.2941139,0),
        (103.8436986,1.2930859,0),
        (103.8453046,1.2972709,0),
        (103.8437896,1.2997779,0),
        (103.8453276,1.3030589,0),
        (103.8460426,1.3048379,0),
        (103.8480886,1.3034859,0),
        (103.8507986,1.3049349,0),
        (103.8493136,1.3061859,0),
        (103.8526276,1.3108379,0),
        (103.8531356,1.3121079,0),
        (103.8544306,1.3136839,0),
        (103.8563476,1.3154529,0),
        (103.8575996,1.3168459,0),
        (103.8585946,1.3182239,0),
        (103.8580666,1.3185519,0),
        (103.8585776,1.3193139,0),
        (103.8581816,1.3196379,0),
        (103.8585286,1.3200269,0),
        (103.8564946,1.3216589,0),
        (103.8583366,1.3238389,0),
        (103.8606196,1.3259159,0),
        (103.8618726,1.3276919,0),
        (103.8624056,1.3292929,0),
        (103.8621276,1.3375139,0),
        (103.8609276,1.3421359,0),
        (103.8604051,1.3436704,0),
        (103.8534999,1.3435192,0),
        (103.8493627,1.3441403,0),
        (103.8464527,1.344224,0),
        (103.8467267,1.3461076,0),
        (103.8409331,1.3462149,0),
        (103.8371565,1.3446275,0),
        (103.8189656,1.3439403,0),
        (103.812061,1.334324,0),
        (103.810242,1.330516,0),
        (103.811739,1.328361,0),
        (103.812675,1.32339,0),
        (103.810755,1.321232,0),
        (103.809891,1.32203,0),
        (103.806828,1.318677,0),
        (103.803652,1.322032,0),
        (103.801936,1.317493,0),
        (103.802267,1.316448,0),
        (103.801566,1.314932,0),
        (103.802947,1.312236,0),
    ],

    "NE-2": [
        (103.8562456,1.399428,0),
        (103.8583862,1.4003255,0),
        (103.8605427,1.4008189,0),
        (103.8745653,1.401205,0),
        (103.8828265,1.4013766,0),
        (103.8859379,1.4012801,0),
        (103.8905727,1.4007331,0),
        (103.8959908,1.3999823,0),
        (103.8983404,1.3994138,0),
        (103.9010548,1.3983305,0),
        (103.9035761,1.3969469,0),
        (103.9068913,1.3944371,0),
        (103.9094769,1.3915519,0),
        (103.9160322,1.3838509,0),
        (103.9184784,1.3813732,0),
        (103.91874,1.382023,0),
        (103.925894,1.391504,0),
        (103.936341,1.401028,0),
        (103.903675,1.4302,0),
        (103.871267,1.438779,0),
        (103.849561,1.408769,0),
        (103.856007,1.400038,0),
        (103.8562456,1.399428,0),
    ],

    "NE-1": [
        (103.8729265,1.341828,0),
        (103.8751902,1.3419192,0),
        (103.87296,1.333371,0),
        (103.874974,1.333516,0),
        (103.875367,1.333495,0),
        (103.875722,1.333586,0),
        (103.876304,1.331779,0),
        (103.878671,1.332528,0),
        (103.879618,1.332811,0),
        (103.880406,1.332968,0),
        (103.880238,1.334241,0),
        (103.880466,1.334606,0),
        (103.880743,1.334526,0),
        (103.88102,1.335174,0),
        (103.880782,1.33548,0),
        (103.881441,1.335845,0),
        (103.881994,1.336404,0),
        (103.882176,1.33722,0),
        (103.883409,1.335516,0),
        (103.884128,1.335828,0),
        (103.88491,1.337373,0),
        (103.885055,1.337534,0),
        (103.886447,1.3346,0),
        (103.888146,1.33507,0),
        (103.888676,1.333448,0),
        (103.892195,1.33466,0),
        (103.901292,1.340966,0),
        (103.9184784,1.3813732,0),
        (103.9160322,1.3838509,0),
        (103.9094769,1.3915519,0),
        (103.9068913,1.3944371,0),
        (103.9035761,1.3969469,0),
        (103.9010548,1.3983305,0),
        (103.8983404,1.3994138,0),
        (103.8959908,1.3999823,0),
        (103.8859379,1.4012801,0),
        (103.8828265,1.4013766,0),
        (103.8745653,1.401205,0),
        (103.8605427,1.4008189,0),
        (103.8583862,1.4003255,0),
        (103.8562456,1.399428,0),
        (103.857554,1.39609,0),
        (103.858243,1.391242,0),
        (103.858334,1.384292,0),
        (103.858257,1.379058,0),
        (103.858471,1.376773,0),
        (103.858814,1.375175,0),
        (103.860594,1.37082,0),
        (103.860978,1.369362,0),
        (103.860931,1.368203,0),
        (103.86058,1.366916,0),
        (103.85713,1.357092,0),
        (103.856841,1.355247,0),
        (103.857034,1.353189,0),
        (103.857679,1.35096,0),
        (103.8596013,1.3457412,0),
        (103.8657997,1.346394,0),
        (103.8706735,1.3441556,0),
        (103.8726475,1.344177,0),
        (103.8729265,1.341828,0),
    ],

    "N-3": [
        (103.763091,1.4490684,0),
        (103.74125,1.446686,0),
        (103.739105,1.422726,0),
        (103.741787,1.415132,0),
        (103.742237,1.413373,0),
        (103.741594,1.409898,0),
        (103.741894,1.408289,0),
        (103.74346,1.406401,0),
        (103.745928,1.405436,0),
        (103.748675,1.405329,0),
        (103.751271,1.404943,0),
        (103.752322,1.404256,0),
        (103.75288,1.403055,0),
        (103.752022,1.399666,0),
        (103.756292,1.398507,0),
        (103.764296,1.40061,0),
        (103.7716776,1.4099059,0),
        (103.7711793,1.4238974,0),
        (103.770793,1.4260855,0),
        (103.7688846,1.43135,0),
        (103.768155,1.4430193,0),
        (103.763091,1.4490684,0),
    ],

    "N-2": [
        (103.7711793,1.4238974,0),
        (103.7712839,1.4214798,0),
        (103.77417,1.423818,0),
        (103.7750068,1.4243757,0),
        (103.7763801,1.4251372,0),
        (103.7783757,1.4258987,0),
        (103.7801245,1.4263063,0),
        (103.7821951,1.4265852,0),
        (103.7841263,1.4265744,0),
        (103.7859395,1.4264135,0),
        (103.7877741,1.4260381,0),
        (103.7900165,1.4252337,0),
        (103.7924841,1.4239574,0),
        (103.7951878,1.4224558,0),
        (103.7981489,1.4208684,0),
        (103.8001445,1.4195385,0),
        (103.8049617,1.415452,0),
        (103.8058522,1.4142079,0),
        (103.8068071,1.4120413,0),
        (103.8080087,1.4086413,0),
        (103.8091245,1.4063353,0),
        (103.8102296,1.4048123,0),
        (103.8115707,1.4031283,0),
        (103.8129547,1.4004684,0),
        (103.8135448,1.3989024,0),
        (103.8141563,1.3972292,0),
        (103.8149395,1.3961781,0),
        (103.8159802,1.3954059,0),
        (103.8166562,1.3949983,0),
        (103.8219347,1.3934216,0),
        (103.823351,1.393132,0),
        (103.8257757,1.3929175,0),
        (103.8279214,1.3930033,0),
        (103.8295522,1.3932286,0),
        (103.841708,1.3962639,0),
        (103.8434675,1.3965213,0),
        (103.8451198,1.3966501,0),
        (103.8484672,1.3965428,0),
        (103.8501409,1.3965213,0),
        (103.8513747,1.3967573,0),
        (103.8540891,1.3979854,0),
        (103.8562456,1.399428,0),
        (103.856007,1.400038,0),
        (103.849561,1.408769,0),
        (103.871267,1.438779,0),
        (103.8636896,1.4504759,0),
        (103.8351076,1.4719269,0),
        (103.8075136,1.4733859,0),
        (103.7979856,1.4690949,0),
        (103.7734386,1.4530069,0),
        (103.763091,1.4490684,0),
        (103.768155,1.4430193,0),
        (103.7688846,1.43135,0),
        (103.770793,1.4260855,0),
        (103.7711793,1.4238974,0),
    ],

    "N-1": [
        (103.8604051,1.3436704,0),
        (103.857679,1.35096,0),
        (103.857034,1.353189,0),
        (103.856841,1.355247,0),
        (103.85713,1.357092,0),
        (103.8589322,1.3622266,0),
        (103.8596904,1.3643822,0),
        (103.86058,1.366916,0),
        (103.860931,1.368203,0),
        (103.860978,1.369362,0),
        (103.860594,1.37082,0),
        (103.858814,1.375175,0),
        (103.858471,1.376773,0),
        (103.858257,1.379058,0),
        (103.8583412,1.3843348,0),
        (103.858243,1.391242,0),
        (103.857554,1.39609,0),
        (103.8562456,1.399428,0),
        (103.8540891,1.3979854,0),
        (103.8513747,1.3967573,0),
        (103.8501409,1.3965213,0),
        (103.8451198,1.3966501,0),
        (103.8434675,1.3965213,0),
        (103.841708,1.3962639,0),
        (103.8295522,1.3932286,0),
        (103.8279214,1.3930033,0),
        (103.8257757,1.3929175,0),
        (103.823351,1.393132,0),
        (103.8218919,1.3934216,0),
        (103.8166562,1.3949983,0),
        (103.8149395,1.3961781,0),
        (103.8141563,1.3972292,0),
        (103.8129547,1.4004684,0),
        (103.8115707,1.4031283,0),
        (103.8102296,1.4048123,0),
        (103.8091245,1.4063353,0),
        (103.8080087,1.4086413,0),
        (103.8068071,1.4120413,0),
        (103.8058522,1.4142079,0),
        (103.8049617,1.415452,0),
        (103.8001445,1.4195385,0),
        (103.7981489,1.4208684,0),
        (103.7900165,1.4252337,0),
        (103.7877741,1.4260381,0),
        (103.7859395,1.4264135,0),
        (103.7841263,1.4265744,0),
        (103.7821951,1.4265852,0),
        (103.7801245,1.4263063,0),
        (103.7783757,1.4258987,0),
        (103.7763801,1.4251372,0),
        (103.7750068,1.4243757,0),
        (103.77417,1.423818,0),
        (103.7712839,1.4214798,0),
        (103.7716776,1.4099059,0),
        (103.7733936,1.4025699,0),
        (103.7738236,1.3990299,0),
        (103.7739516,1.3953409,0),
        (103.7755286,1.3829309,0),
        (103.7759046,1.3805609,0),
        (103.7789946,1.3691919,0),
        (103.77966,1.3653,0),
        (103.7804966,1.3613829,0),
        (103.7813976,1.3594949,0),
        (103.7826636,1.3575859,0),
        (103.7844656,1.3556769,0),
        (103.7892726,1.3523519,0),
        (103.7902386,1.3512149,0),
        (103.7915256,1.3491989,0),
        (103.7940146,1.3493059,0),
        (103.7955816,1.3490479,0),
        (103.7965896,1.3485759,0),
        (103.7973836,1.3480829,0),
        (103.7998296,1.3457659,0),
        (103.8023516,1.3432029,0),
        (103.8050016,1.3405109,0),
        (103.8090996,1.3368639,0),
        (103.8113316,1.3347829,0),
        (103.8120606,1.3343109,0),
        (103.8189656,1.3439403,0),
        (103.8371565,1.3446275,0),
        (103.8409331,1.3462149,0),
        (103.8467267,1.3461076,0),
        (103.8464527,1.344224,0),
        (103.8493627,1.3441403,0),
        (103.8534999,1.3435192,0),
        (103.8604051,1.3436704,0),
    ],

    "E-3": [
        (103.936341,1.401028,0),
        (103.925894,1.391504,0),
        (103.91874,1.382023,0),
        (103.9184784,1.3813732,0),
        (103.9201607,1.3799803,0),
        (103.9219031,1.3791766,0),
        (103.9240402,1.3783458,0),
        (103.9276408,1.3774691,0),
        (103.9287438,1.3771273,0),
        (103.9349,1.374383,0),
        (103.9400101,1.37166,0),
        (103.9411159,1.3709579,0),
        (103.9438361,1.3684402,0),
        (103.9463334,1.3671599,0),
        (103.9521781,1.3658367,0),
        (103.9554454,1.3647991,0),
        (103.9575111,1.3637186,0),
        (103.9596412,1.3619303,0),
        (103.9611275,1.3601419,0),
        (103.962789,1.3572458,0),
        (103.9643034,1.3515288,0),
        (103.9639785,1.3496946,0),
        (103.9646008,1.3493628,0),
        (103.9661458,1.3481454,0),
        (103.9699384,1.3424017,0),
        (103.9708933,1.3411897,0),
        (103.9721271,1.3402673,0),
        (103.9901085,1.3322917,0),
        (103.9751739,1.2979255,0),
        (104.0266724,1.3017011,0),
        (104.05019,1.3588489,0),
        (103.9904518,1.4007222,0),
        (103.936341,1.401028,0),
    ],

    "E-2": [
        (103.8655238,1.312015,0),
        (103.8695792,1.3025814,0),
        (103.866044,1.2992778,0),
        (103.865135,1.2971914,0),
        (103.8667833,1.2874414,0),
        (103.8922923,1.2498031,0),
        (103.9751742,1.29792,0),
        (103.9901088,1.3322862,0),
        (103.9721274,1.3402618,0),
        (103.9708936,1.3411842,0),
        (103.9699386,1.3423962,0),
        (103.966146,1.3481399,0),
        (103.964601,1.3493573,0),
        (103.9639788,1.3496891,0),
        (103.9614973,1.3505159,0),
        (103.9597574,1.3505862,0),
        (103.9577157,1.3501278,0),
        (103.9559732,1.3491586,0),
        (103.9400365,1.3357687,0),
        (103.9390766,1.3351676,0),
        (103.9379744,1.3350065,0),
        (103.9299452,1.3355373,0),
        (103.9278492,1.3354246,0),
        (103.9250732,1.3348294,0),
        (103.9223976,1.3337596,0),
        (103.9112322,1.3284624,0),
        (103.9085786,1.3270043,0),
        (103.9036799,1.3255516,0),
        (103.8922404,1.3232366,0),
        (103.8909541,1.3229801,0),
        (103.8892048,1.3225095,0),
        (103.8874102,1.3222685,0),
        (103.8850149,1.3221669,0),
        (103.8792935,1.3199899,0),
        (103.8774842,1.3198023,0),
        (103.8756321,1.3200224,0),
        (103.8655238,1.312015,0),
    ],

    "E-1": [
        (103.8703692,1.3266562,0),
        (103.8756319,1.3200279,0),
        (103.877484,1.3198078,0),
        (103.8792933,1.3199954,0),
        (103.8850146,1.3221724,0),
        (103.8874099,1.322274,0),
        (103.8892045,1.322515,0),
        (103.8909539,1.3229856,0),
        (103.9036796,1.3255571,0),
        (103.9057315,1.3261953,0),
        (103.9085783,1.3270098,0),
        (103.911232,1.3284679,0),
        (103.9223973,1.3337651,0),
        (103.9250729,1.3348349,0),
        (103.927849,1.3354301,0),
        (103.929945,1.3355428,0),
        (103.9379741,1.335012,0),
        (103.9390763,1.3351731,0),
        (103.9400362,1.3357742,0),
        (103.9559729,1.3491641,0),
        (103.9577154,1.3501333,0),
        (103.9597413,1.3505916,0),
        (103.961497,1.3505214,0),
        (103.9639785,1.3496946,0),
        (103.9643034,1.3515288,0),
        (103.9638558,1.35332,0),
        (103.962789,1.3572458,0),
        (103.9611275,1.3601419,0),
        (103.9596412,1.3619303,0),
        (103.9575111,1.3637186,0),
        (103.9554454,1.3647991,0),
        (103.9521781,1.3658367,0),
        (103.9463334,1.3671599,0),
        (103.9438361,1.3684402,0),
        (103.9411159,1.3709579,0),
        (103.9400101,1.37166,0),
        (103.9349,1.374383,0),
        (103.9287438,1.3771273,0),
        (103.9276408,1.3774691,0),
        (103.9240402,1.3783458,0),
        (103.9219031,1.3791766,0),
        (103.9201607,1.3799803,0),
        (103.9184784,1.3813732,0),
        (103.901292,1.340966,0),
        (103.892195,1.33466,0),
        (103.888676,1.333448,0),
        (103.888146,1.33507,0),
        (103.886447,1.3346,0),
        (103.885055,1.337534,0),
        (103.88491,1.337373,0),
        (103.884128,1.335828,0),
        (103.883409,1.335516,0),
        (103.882176,1.33722,0),
        (103.881994,1.336404,0),
        (103.881441,1.335845,0),
        (103.880782,1.33548,0),
        (103.88102,1.335174,0),
        (103.880743,1.334526,0),
        (103.880466,1.334606,0),
        (103.880238,1.334241,0),
        (103.880406,1.332968,0),
        (103.879579,1.332807,0),
        (103.876304,1.331779,0),
        (103.875722,1.333586,0),
        (103.875367,1.333495,0),
        (103.874974,1.333516,0),
        (103.87296,1.333371,0),
        (103.872855,1.332523,0),
        (103.870422,1.331738,0),
        (103.870332,1.331674,0),
        (103.869958,1.330216,0),
        (103.869617,1.330289,0),
        (103.868885,1.330474,0),
        (103.868335,1.328144,0),
        (103.8703692,1.3266562,0),
    ],


    "W-2": [
        (103.74125,1.446686,0),
        (103.723976,1.456425,0),
        (103.705093,1.451362,0),
        (103.7038548,1.3674654,0),
        (103.7064552,1.3644784,0),
        (103.7087405,1.3660766,0),
        (103.7107575,1.3670633,0),
        (103.7209499,1.3700344,0),
        (103.7224626,1.3706994,0),
        (103.7242973,1.3717934,0),
        (103.7430964,1.3878535,0),
        (103.7439762,1.3885399,0),
        (103.745328,1.3892264,0),
        (103.7463902,1.3895374,0),
        (103.7471626,1.3896983,0),
        (103.7484501,1.3898055,0),
        (103.7497161,1.3896554,0),
        (103.751186,1.389398,0),
        (103.7528167,1.3890118,0),
        (103.7538145,1.3888402,0),
        (103.7556277,1.3886686,0),
        (103.7579022,1.3888724,0),
        (103.7594042,1.3892264,0),
        (103.7625156,1.3901702,0),
        (103.7645219,1.3904813,0),
        (103.7660347,1.3905563,0),
        (103.7745829,1.3903096,0),
        (103.7739516,1.3953409,0),
        (103.7738236,1.3990299,0),
        (103.7733936,1.4025699,0),
        (103.7716776,1.4099059,0),
        (103.764296,1.40061,0),
        (103.756292,1.398507,0),
        (103.752022,1.399666,0),
        (103.75288,1.403055,0),
        (103.752322,1.404256,0),
        (103.751271,1.404943,0),
        (103.748675,1.405329,0),
        (103.745928,1.405436,0),
        (103.74346,1.406401,0),
        (103.741894,1.408289,0),
        (103.741594,1.409898,0),
        (103.742237,1.413373,0),
        (103.741787,1.415132,0),
        (103.739105,1.422726,0),
        (103.74125,1.446686,0),
    ],

    "W-1": [
        (103.8015923,1.2758617,0),
        (103.7980688,1.2773037,0),
        (103.7924876,1.2850826,0),
        (103.7951247,1.2875841,0),
        (103.7999376,1.2890824,0),
        (103.8048793,1.287084,0),
        (103.8085749,1.2915338,0),
        (103.8053565,1.2923871,0),
        (103.8015158,1.2972733,0),
        (103.8007871,1.3015783,0),
        (103.7996503,1.3050179,0),
        (103.7982665,1.305944,0),
        (103.802947,1.312236,0),
        (103.801566,1.314932,0),
        (103.802267,1.316448,0),
        (103.801936,1.317493,0),
        (103.803652,1.322032,0),
        (103.806828,1.318677,0),
        (103.809891,1.32203,0),
        (103.810755,1.321232,0),
        (103.812675,1.32339,0),
        (103.811739,1.328361,0),
        (103.810242,1.330516,0),
        (103.812061,1.334324,0),
        (103.811331,1.334796,0),
        (103.808263,1.337649,0),
        (103.805001,1.340524,0),
        (103.79983,1.34578,0),
        (103.797384,1.348096,0),
        (103.79659,1.34859,0),
        (103.795581,1.349062,0),
        (103.793864,1.349319,0),
        (103.791526,1.349212,0),
        (103.790238,1.351228,0),
        (103.789273,1.352365,0),
        (103.786633,1.354232,0),
        (103.784466,1.35569,0),
        (103.782664,1.357599,0),
        (103.781398,1.359509,0),
        (103.780496,1.361396,0),
        (103.77966,1.3653,0),
        (103.778994,1.369205,0),
        (103.777278,1.375447,0),
        (103.775904,1.380574,0),
        (103.775497,1.383019,0),
        (103.7745829,1.3903096,0),
        (103.7660347,1.3905563,0),
        (103.7645219,1.3904813,0),
        (103.7625156,1.3901702,0),
        (103.7594042,1.3892264,0),
        (103.7579022,1.3888724,0),
        (103.7556277,1.3886686,0),
        (103.7538145,1.3888402,0),
        (103.7528167,1.3890118,0),
        (103.751186,1.389398,0),
        (103.7497161,1.3896554,0),
        (103.7484501,1.3898055,0),
        (103.7471626,1.3896983,0),
        (103.745328,1.3892264,0),
        (103.7439762,1.3885399,0),
        (103.7242973,1.3717934,0),
        (103.7224626,1.3706994,0),
        (103.7209499,1.3700344,0),
        (103.7107575,1.3670633,0),
        (103.7087405,1.3660766,0),
        (103.7064552,1.3644784,0),
        (103.7038548,1.3674654,0),
        (103.705093,1.451362,0),
        (103.689729,1.436518,0),
        (103.680202,1.43506,0),
        (103.671619,1.425536,0),
        (103.667414,1.414381,0),
        (103.656599,1.404084,0),
        (103.643123,1.371221,0),
        (103.615057,1.318192,0),
        (103.591882,1.211102,0),
        (103.6538524,1.2029494,0),
        (103.7266366,1.2461982,0),
        (103.8122656,1.243888,0),
        (103.7985327,1.264654,0),
        (103.8017728,1.2731492,0),
        (103.8015923,1.2758617,0),
    ]
}


def make_polygon(polygon_input):
    """
    Given a LIST with polygon points, format
    [(LNG, LAT, Z), ... ]
    return a polygon
    """
    tmp_plygn = []
    for pt in polygon_input:
        tmp_plygn.append((pt[1], pt[0]))
    return Polygon(tmp_plygn)



POLYGON_DICT = {}

for k,v in POLYGON_INPUTS.iteritems():
    POLYGON_DICT[k] = make_polygon(v)
