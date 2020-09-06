from imageai.Detection import ObjectDetection
import os


def init_detector():
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    return detector


def detect_objects(fname_in, fname_out, detector, verbose=False):
    detections = detector.detectObjectsFromImage(input_image=fname_in, output_image_path=fname_out, thread_safe=True)

    if verbose:
        for eachObject in detections:
            print(eachObject["name"], " : ", eachObject["percentage_probability"])

    return detections



if __name__ == '__main__':
    detector = init_detector()

    detect_objects("img.jpeg", "imagenew.jpeg", detector)
