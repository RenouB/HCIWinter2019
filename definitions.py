import os
import json
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

constants = \
{
"PROJECT_DIR" : PROJECT_DIR,
"MPIIEMO_ANNOS_DIR" : os.path.join(PROJECT_DIR, "MPIIEmo/annotations"),
"MPIIEMO_ANNOS_WEBSITE" : os.path.join(PROJECT_DIR, "MPIIEmo/annos_website"),
"GOLD_STANDARD_PATH": os.path.join(PROJECT_DIR, "MPIIEmo/annotations/aggregate_emotion_labels.csv"),
"TEN_FPS_VIEWS_DIR" : os.path.join(PROJECT_DIR, "MPIIEmo/views/10fps_views"),
"SVM_DATA_PATH": os.path.join(PROJECT_DIR, "models//emotion_classification/data/svm_data.pkl"),
"MODELS_DIR": os.path.join(PROJECT_DIR, 'models'),
"MANUALLY_SELECTED_IMAGES_DIR": os.path.join(PROJECT_DIR, "MPIIEmo/views/manually_selected_images"),
"ACTOR_REFERENCE_IMAGES_DIR": os.path.join(PROJECT_DIR, "MPIIEmo/annos_website/actor_ids/"),
"RAW_BODY_FEATS_DIR" : os.path.join(PROJECT_DIR, "MPIIEmo/features/body_features/raw"),
"PROCESSED_BODY_FEATS_DIR" : os.path.join(PROJECT_DIR, "MPIIEmo/features/body_features/processed"),
"VERIFICATION_IMAGES_DIR": os.path.join(PROJECT_DIR, "MPIIEmo/prepare_data/verification_images"),
"HISTOGRAMS_DATA_DIR": os.path.join(PROJECT_DIR, 'models/visual_pose_alignment/data'),
"KEYPOINTS_FOR_SCALING" : (9, 15),
"SVM_ANGLES": [ [ (6,5), (2,5) ],
				[ (3,2), (5,2) ],
				[ (4,3), (2,3) ],
				[ (7,6), (5,6) ],
				[ (10,9), (12,9) ],
				[ (13,12), (9,12) ],
				[ (0,1), (5,1) ],
				[ (0,1), (2,1) ],
				[ (0,1), (12,1) ],
				[ (0,1), (9,1)] ],
"STABLE_BODY_PART_INDICES" : [0, 1, 2, 5, 8, 9, 12, 15, 10, 17, 18],
"WAIST_UP_BODY_PART_INDICES": [0, 1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18],
"WAIST_UP_FILTER_RATIO": 1/2,
"TOO_CLOSE_THRESHOLD":70,
"BODY_CENTER" : 8,
"NECK": 1,
"FULL-HH":[2,3,1,5,6,7],
"FULL-HEAD":[2,3,4,5,6,7,1],
"HANDS":[4,7],
"HEAD":[17,15,16,18,0],
"ACTOR_PAIRS": ['0102','0304','0506','0708','0910','1112','1314','1516']
}
